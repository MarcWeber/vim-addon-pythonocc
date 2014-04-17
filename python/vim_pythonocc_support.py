#!/usr/bin/env python
import os

class VimPythonOCCDisplay:

  def __init__(self, display_driver):
    self.display_driver = display_driver
    self.modules = {}
    self.display_list = None

  def add_or_update_module(self, module_or_path):
    """
    m can be a module or a path to a .py file
    """
    if type(module_or_path) == type(""):
      module_name = os.path.basename(module_or_path)
      import imp
      module_path = module_or_path
      module = imp.load_source(module_name, module_or_path)
    else:
      module_path = module_or_path.__path__
      module = module_or_path

    self.modules[module_path] = module
    self.update_display()

  def update_display(self):
    if self.display_list == None:
      # returns: display, start_display, add_menu, add_function_to_menu
      from OCC.Display.SimpleGui import init_display
      self.display_list = init_display(self.display_driver)

    # ask all modules to add shapes to display
    display = self.display_list[0]
    display.EraseAll()
    for m in self.modules:
      self.modules[m].add_shapes(display = display)

class VimPythonOCC:
  def __init__(self):
    self.display_by_name = {}

  def display_module(self, display_driver, module_or_path, display_name = None):
    """
    1) creates display if it doesn't exist yet
    2) loads module
    3) asks module to add shapes to display
    """

    if not display_name in self.display_by_name:
      self.display_by_name[display_name] = VimPythonOCCDisplay(display_driver)

    self.display_by_name[display_name].add_or_update_module(module_or_path)

if not 'vim_python_occ' in globals():
  vim_python_occ = VimPythonOCC()

# trace_file = "trace.txt"
# if display_name == None:
#   display_name = module_name
# display = display_by_name(module_name)

# try:
#   tmp_module = imp.load_source(module_name, path)
#   display.EraseAll()
#   tmp_module.display(display)
# except Exception, e:
#   if os.path.isfile(trace_file):
#     os.remove(trace_file)
#     import traceback
#     file = open(trace_file, 'w')
#     traceback.print_exc(None, file)
#     file.close()
#     ex = e

