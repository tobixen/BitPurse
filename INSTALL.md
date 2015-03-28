Those are some notes of all the whoopla I'm currently going through, attempting to install this on my Jolla ...

* Installed https://github.com/khertan/PyPackager
  * ran "python make.py" followed by "devel-su python ./setup.py install"
* Installed PyQt5, ref https://wiki.merproject.org/wiki/Sailfish/Python_Development
  * I had to install zypper and install PyQt5 through zypper, since one dependency was not possible to fulfill.  Zypper allows me to bypass this error, though now the whole PyQt5-installation may be broken anyway :-(
* Installed pycrypto from https://github.com/dlitz/pycrypto ... plain "devel-su python ./setup.py install"
  * had to install gcc and python-devel to be able to install pycrypto.
* Installed BitPurse
  * had to run "python ./make.py" followed by "devel-su python ./setup.py install" ...
  * had to do a `chmod a+x /opt/bitpurse/__init__.py`

Still it breaks ...

Mar 29 00:00:20 Jolla lipstick[20075]: [D] MLocalThemeDaemonClient::readImage:176 - Unknown theme image: "bitpurse" 
Mar 29 00:00:20 Jolla lipstick[20075]: [W] unknown:272 - file:///usr/share/lipstick-jolla-home-qt5/switcher/Switcher.qml:272:17: QML LauncherIcon: Failed to get image from provider: image://theme/bitpurse
Mar 29 00:00:20 Jolla lipstick[20075]: [W] unknown:278 - file:///usr/share/lipstick-jolla-home-qt5/switcher/Switcher.qml:278:35: Unable to assign [undefined] to QQmlComponent*
Mar 29 00:00:20 Jolla invoker[27644]: error: Failed to initiate connect on the socket.
Mar 29 00:00:21 Jolla python[27608]: [D] QWaylandEglClientBufferIntegration::QWaylandEglClientBufferIntegration:62 - Using Wayland-EGL 
Mar 29 00:00:21 Jolla lipstick[20075]: Traceback (most recent call last):
Mar 29 00:00:21 Jolla lipstick[20075]: File "/opt/bitpurse/__init__.py", line 133, in <module>
Mar 29 00:00:21 Jolla lipstick[20075]: sys.exit(BitPurse().exec_())
Mar 29 00:00:21 Jolla lipstick[20075]: File "/opt/bitpurse/__init__.py", line 86, in __init__
Mar 29 00:00:21 Jolla lipstick[20075]: self.walletController = WalletController()
Mar 29 00:00:21 Jolla lipstick[20075]: File "/opt/bitpurse/walletcontroller.py", line 65, in __init__
Mar 29 00:00:21 Jolla lipstick[20075]: self.addressesModel = AddressesModel()
Mar 29 00:00:21 Jolla lipstick[20075]: File "/opt/bitpurse/address.py", line 111, in __init__
Mar 29 00:00:21 Jolla lipstick[20075]: self.setRoleNames(dict(enumerate(AddressesModel.COLUMNS)))
Mar 29 00:00:21 Jolla lipstick[20075]: AttributeError: 'AddressesModel' object has no attribute 'setRoleNames'
Mar 29 00:00:21 Jolla mapplauncherd[925]: Boosted process (pid=27608) exited with status 1
Mar 29 00:00:21 Jolla lipstick[20075]: invoker: Invoking execution: '/opt/bitpurse/__init__.py'
Mar 29 00:00:21 Jolla lipstick[20075]: invoker: error: Failed to initiate connect on the socket.
Mar 29 00:00:21 Jolla lipstick[20075]: invoker: warning: Booster e is not available. Falling back to generic.


