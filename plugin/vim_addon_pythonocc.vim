if !exists('g:vim_addon_pythonocc') | let g:vim_addon_pythonocc = {} | endif | let s:c = g:vim_addon_pythonocc
let s:c.display_driver = get(s:c, 'display_driver', 'wx')
let s:c.support_vim_addon_actions = get(s:c, 'support_vim_addon_actions', 1)

if s:c.support_vim_addon_actions
  call actions#AddAction('pythonocc-display', {'action': funcref#Function("return [\"call vim_addon_pythonocc#DisplayModule(\".string(expand('%:p')).\") \"]")})
endif
