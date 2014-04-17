#!/usr/bin/env python

def add_shapes(display):
  from OCC.BRepPrimAPI import BRepPrimAPI_MakeCylinder
  s = BRepPrimAPI_MakeCylinder(60., 200.)
  display.DisplayShape(s.Shape(), update=True)
