#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
import os
import base64
import zlib

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

ui = Gtk.Builder()

ui.add_from_file("/home/michael/mattos-codec-base64/Install/font/instalacao.ui")

class Handler(object):

    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> carrega estilo da aplicação
        self.style_application()
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> Carrega a stack da aplicação
        self.Stack: Gtk.Stack = ui.get_object('stack')
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> imagens e icones
        self.img_logo = ui.get_object("img_logo")
        self.img_logo.set_from_file("/home/michael/mattos-codec-base64/Icons/logo.png")
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # --> Funções
    def style_application(self, *args):
        style = "/home/michael/iq-option/style/class.css"
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(style)
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen.get_default(),
                                              css_provider,
                                              Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    
    def ao_clicar_em_proximo(self, *args):
        print("clicou em proximo", args)
        self.Stack.set_visible_child_name("page1")
    
    def ao_clicar_em_sair(self, *args):
        print("clicou em sair", args)
        Gtk.main_quit()
    
    def ao_clicar_em_instalar(self, *args):
        print("clicou em instalar", args)
    
    def ao_cliclar_em_voltar(self, *args):
        print("Clicou em voltar",  args)
        self.Stack.set_visible_child_name("page0")
        
ui.connect_signals(Handler())
window = ui.get_object("main_window")
window.show_all()

if __name__ == '__main__':
    Gtk.main()
