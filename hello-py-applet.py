#!/bin/env python

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('MatePanelApplet', '4.0') 

from gi.repository import  GObject, Gtk
from gi.repository import MatePanelApplet

class HelloPyApplet(MatePanelApplet.Applet):
  __gtype_name__ = "HelloPyApplet"

  def init(self):
    self.build_interface()

  def build_interface(self):
    self.label = Gtk.Label("Hello Python :)")

    self.add(self.label)

    self.show_all()

def factory_callback(applet, iid, data):
  if iid != "HelloPyApplet":
    return False

  applet.init()
  return True

MatePanelApplet.Applet.factory_main("HelloPyAppletFactory", True, HelloPyApplet.__gtype__, factory_callback, None)
