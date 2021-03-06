#!/usr/bin/env python3
#
# Discontinued. Use KeepassXC instead,
from __future__ import print_function
import sys
import os  # basics
try:
    import gi
    gi.require_version('Gtk', '3.0')  # inform the PC that we need GTK+ 3.
    from gi.repository import Gtk  # this is the GNOME depends
except ImportError as imper:
    print("Importing GObject failed!")
    print("Install GObject bindings.")
    print(imper)
    sys.exit(1)


def gload():
    global builder
    builder = Gtk.Builder()
    builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) +
                          "/gentore.ui")
    window = builder.get_object('gentore')  # main window
    window.show_all()


gload()
sptext = builder.get_object('sptext')
try:
    with open('gentore.psst', 'r') as psst:
        sptext.get_buffer().set_text(psst.read())
except:
    os.touch('gentore.psst')
    with open('gentore.psst', 'r') as psst:
        sptext.get_buffer().set_text(psst.read())
import secrets
import string
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class main():
    def on_window_destroy(self, rerun):
        Gtk.main_quit()

    def on_genpass_clicked(self, genpass):
        pss = builder.get_object('pass')
        pss.set_text(self.passgen())

    def on_setpass_clicked(self, setpass):
        mpass = builder.get_object('masterpass2')
        saltext = builder.get_object('salt')
        password = mpass.get_text().encode()
        salt = saltext.get_text().encode()
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=salt,
                         iterations=100000,
                         backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        startiter = sptext.get_buffer().get_start_iter()
        lastiter = sptext.get_buffer().get_end_iter()
        tosave = f.encrypt(sptext.get_buffer().get_text(startiter, lastiter,
                                                        'false').encode())
        tosave = tosave + b"\n[encrypted]"
        with open('gentore.psst', 'w') as psst:
            psst.write(tosave.decode())

    def on_showpass_clicked(self, showpass):
        startiter = sptext.get_buffer().get_start_iter()
        lastiter = sptext.get_buffer().get_end_iter()
        read = sptext.get_buffer().get_text(startiter, lastiter, 'false')
        if "\n[encrypted]" in read:
            read = read.replace("\n[encrypted]", '')
            mpass = builder.get_object('masterpass')
            saltext = builder.get_object('salt1')
            password = mpass.get_text().encode()
            salt = saltext.get_text().encode()
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                             length=32,
                             salt=salt,
                             iterations=100000,
                             backend=default_backend())
            key = base64.urlsafe_b64encode(kdf.derive(password))
            f = Fernet(key)
            toread = f.decrypt(read.encode()).decode()
            sptext.get_buffer().set_text(toread)

    def passgen(self, length=32):
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password) and
                    any(c.isupper() for c in password) and
                    sum(c.isdigit() for c in password) >= 3):
                break
        return password


builder.connect_signals(main())
Gtk.main()
# LICENSING:
# The MIT License (MIT)
# Copyright (c) 2017 Mufeed Ali
# This file is part of Gentore
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# Author: Mufeed Ali
