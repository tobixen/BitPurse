#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Benoit HERVIER <khertan@khertan.net>
# Licenced under GPLv3

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; version 3 only.
##
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QObject
from PyQt5 import QtQuick
from PyQt5.QtOpenGL import QGLWidget, QGLFormat
from walletcontroller import WalletController
import sys
import os
import os.path

__author__ = 'Benoit HERVIER (Khertan)'
__email__ = 'khertan@khertan.net'
__version__ = '2.1.1'
__build__ = '1'
__upgrade__ = '''0.9.0: First beta release
0.9.1: Second beta release, add missing python-crypto dependancy
0.9.2: Second beta release, add missing python-crypto dependancy for deb
0.9.3: Fix error due to API changes of BlockChain.info
1.5.0: Rewrite to be independant of BlockChain.info my wallet service, but
       still use BlockChain.info API to get blockchain informations
1.6.0: add an unEncrypted view of wallet address and private key
       Fix new address creation with double encrypted key
       Fix for clearing second password after successfully
       emitting a transaction
1.7.0: Fix a bug in blockchain.info mywallet import, add bitcoin://
       url scheme support
1.8.0: Add watch only address (addr without priv key)
1.9.0: Better splash screen and icon
2.0.0: Improve password dialog
       Add request btc feature
       Add fiat convertion
2.0.1: Fix a bug preventing openning wallet when there is no network
       Improve placeholder name in settings
       Improve edit label dialog
       Improve double password dialog
       Update wallet balance after sending a transaction
       Remove transaction without confirmation older than 7 days
       Add a copy address item menu in address page menu
2.0.2: Fix issue #4, avoid putting a change address with a null value
2.0.3: Workarround to try to fix tracker index for shareui
2.1.0: Fix a bug in storage of old transactions
       Add event notification on new transaction
2.1.1: Fix security issue SSLv3 (CVE-2014-3566)
       Lower minimal fee to 0.0001'''


class BitPurse(QApplication):

    ''' Application class '''

    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.setOrganizationName("Khertan Software")
        self.setOrganizationDomain("khertan.net")
        self.setApplicationName("BitPurse")

        self.view = QtQuick.QQuickView()
        # Are we on mer ? So don't use opengl
        # As it didn't works on all devices
        if os.path.exists('/etc/mer-release'):
            fullscreen = True
        elif os.path.exists('/etc/aegis'):
            fullscreen = True
            self.glformat = QGLFormat().defaultFormat()
            self.glformat.setSampleBuffers(False)
            self.glw = QGLWidget(self.glformat)
            self.glw.setAutoFillBackground(False)
            self.view.setViewport(self.glw)
        else:
            fullscreen = False

        self.walletController = WalletController()
        self.rootContext = self.view.rootContext()
        self.rootContext.setContextProperty("argv", sys.argv)
        self.rootContext.setContextProperty("__version__", __version__)
        self.rootContext.setContextProperty("__upgrade__", __upgrade__
                                            .replace('\n', '<br />'))
        self.rootContext.setContextProperty('WalletController',
                                            self.walletController)
        self.rootContext.setContextProperty('AddressesModel',
                                            self.walletController
                                            .addressesModel)
        self.rootContext.setContextProperty('TransactionsModel',
                                            self.walletController
                                            .transactionsModel)
        self.rootContext.setContextProperty('Settings',
                                            self.walletController
                                            .settings)

        self.view.setSource(QUrl.fromLocalFile(
            os.path.join(os.path.dirname(__file__),
                         'qml', 'main.qml')))

        self.rootObject = self.view.rootObject()
        if fullscreen:
            self.view.showFullScreen()
        else:
            self.view.show()
        self.sendPage = self.rootObject.findChild(QObject, "sendPage")
        self.aboutPage = self.rootObject.findChild(QObject, "aboutPage")
        self.walletController.onError.connect(self.rootObject.onError)
        self.walletController.onTxSent.connect(self.sendPage.onTxSent)
        if len(sys.argv) >= 2:
            if sys.argv[1].startswith('bitcoin:'):
                params = sys.argv[1][8:].split('?')
                addr = params[0].strip('/')
                amount = 0
                if params > 1:
                    for param in params:
                        if param.startswith('amount='):
                            if len(param.split('=')) > 1:
                                amount = param.split('=')[1]
                self.rootObject.sendTo(addr, amount)
        if self.walletController.settings.numberOfLaunch == 25:
            self.rootObject.showDonation()
        self.walletController.settings.numberOfLaunch += 1

if __name__ == '__main__':
    sys.exit(BitPurse().exec_())
