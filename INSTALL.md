Those are some notes of all the whoopla I'm currently going through, attempting to install this on my Jolla ...

* Installed https://github.com/khertan/PyPackager
  * ran "python make.py" followed by "devel-su python ./setup.py install"
* Installed PyQt5, ref https://wiki.merproject.org/wiki/Sailfish/Python_Development
  * I had to install zypper and install PyQt5 through zypper, since one dependency was not possible to fulfill.  Zypper allows me to bypass this error, though now the whole PyQt5-installation may be broken anyway :-(
* Installed pycrypto from https://github.com/dlitz/pycrypto ... plain "devel-su python ./setup.py install"
  * had to install gcc and python-devel to be able to install pycrypto.
* Installed BitPurse
  * had to run "python ./make.py" followed by "devel-su python ./setup.py install" ... and still it breaks ... :-(

error: can't copy 'net.khertan.bitpurse.service': doesn't exist or not a regular file

