if !exists('g:vim_addon_pythonocc') | let g:vim_addon_pythonocc = {} | endif | let s:c = g:vim_addon_pythonocc
let s:c.display_driver = get(s:c, 'display_driver', 'wx')

let s:c.plugin_top_level_path = expand("<sfile>:h:h")

" usage: call vim_addon_pythonocc#DisplayModule(expand('%:p'))
fun! vim_addon_pythonocc#DisplayModule(path)
python << EOF

import vim

if not 'VimPythonOCCDisplay' in globals():
  vim.command('pyfile %s/python/vim_pythonocc_support.py' % vim.eval('g:vim_addon_pythonocc.plugin_top_level_path'))
vim_python_occ.display_module(vim.eval('g:vim_addon_pythonocc.display_driver'), vim.eval('a:path'))

EOF
" TODO: catch exceptions
endf
