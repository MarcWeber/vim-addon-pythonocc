some python code and a vim function which allows you to update a model in
pythonocc

Give it a try this way:
  :e example/test1.py
  :call vim_addon_pythonocc#DisplayModule(expand('%:p'))
