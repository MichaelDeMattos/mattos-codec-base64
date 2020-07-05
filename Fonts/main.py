#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
import os
import time
import zlib
import base64

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

ui = Gtk.Builder()
jn_b64_decode = base64.b64decode(b'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')
jn_decompress = zlib.decompress(jn_b64_decode)
ui.add_from_string(jn_decompress.decode("utf-8"))

"""
Copyright (C) 
Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.

Author: Michael de Mattos
"""

class Handler(object):
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> Window
        self.main_window = ui.get_object("main_window")
     
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	# --> toolbar
        self.bt_convert = ui.get_object("bt_convert")
        self.bt_exit = ui.get_object("bt_exit")
        
    # --> Label
        self.lb_result = ui.get_object("lb_result")
    
    # --> Entry text
        self.archive = ui.get_object("archive")
        self.name_project = ui.get_object("name_project")
        self.path_destiny = ui.get_object("path_destiny")
    
    # --> Gtk dialog
        self.dialog = ui.get_object("dialog")
        self.var_global = ""
        
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> Functions
    
    #Function ends program execution    
    def on_bt_exit_clicked(self, *args):
        Gtk.main_quit()
    
    #Function ends program execution
    def on_main_window_destroy(self, *args):
        Gtk.main_quit()
    
    #Function converts and compresses
    #the file generated by the glade
    def on_bt_convert_clicked(self, *args):
        print("convert")
        
        #Function that initiates conversion
        #And compression to base 64
        def run_codec_base64():
            try:
                archive = self.archive.get_filename()
                name_project = self.name_project.get_text()
                path = self.path_destiny.get_filename()
                
                with open(str(archive), "rb") as file:
                    data = file.read()
                    compress = zlib.compress(data)
                    codec_base64 = base64.b64encode(compress)
                    
                    path_archive = open(str(path) + "/" + name_project, 'w')
                    path_archive.write(str(codec_base64))
                    path_archive.close()
                    
                    self.lb_result.set_text("Sucess!!!")
                    self.var_global = (str(path))
                    
                    self.dialog.set_transient_for(self.main_window)
                    self.dialog.set_modal(True)
                    self.dialog.set_destroy_with_parent(True)
                    self.dialog.show_all()
                    
                print("archive: " + archive)
                print("name_project: " + name_project)
            
            except Exception as ex:
                print("Erro")
                msg_add = ("You can also send the error log to the email: chelmto2000@gmail.com\n"
                           "Error log is in the directory: /tmp/mattos-codec-base64.txt")
                           
                self.lb_result.set_text("Error!!!\n"
                                        "checks the path "
                                        "of the reported files\n + {}".format(msg_add))
                                        
                date = time.ctime()
                log_error = open('/tmp/log_mattos-codec-base64.txt', 'w')
                log_error.write(str(date) + " " +  str(ex))
                log_error.close()
                
        run_codec_base64()
    #Function showing the system's user manual
    def on_bt_manual_clicked(self, *args):
        print("manual")
        os.system("firefox https://youtu.be/-VpNc9ZRi_Y")
    
    #Function that takes the
    #user to the donate page
    def on_bt_donate_activate(self, *args):
        print("donate")
        os.system("firefox https://www.paypal.com/myaccount/transfer/homepage/buy/preview")
        self.lb_result.set_text("your result")
        
    #Function close dialog
    def on_bt_close_clicked(self, *args):
        self.lb_result.set_text("your result")
        try:
            os.system("caja {}".format(self.var_global))
        except Exception as ex:
            print(str(ex))
            os.system("nautilus {}".format(self.var_global))
        Gtk.main_quit()
        
ui.connect_signals(Handler())
window = ui.get_object("main_window")
window.show_all()

if __name__ == '__main__':
    Gtk.main()
