vim.g.mapleader = ' '
vim.api.nvim_set_keymap('n', '<Leader>dd', ':call vimspector#Launch()<CR>', {noremap = true})
vim.api.nvim_set_keymap('n', '<Leader>de', ':call vimspector#Reset()<CR>', {noremap = true})

vim.api.nvim_set_keymap('n', '<Leader>dbp', '<Plug>VimspectorToggleBreakpoint', {})
vim.api.nvim_set_keymap('n', '<Leader>dcbp', '<Plug>VimspectorToggleConditionalBreakpoint', {})

vim.api.nvim_set_keymap('n', '<Leader>dsi', '<Plug>VimspectorStepInto', {})
vim.api.nvim_set_keymap('n', '<Leader>ds', '<Plug>VimspectorStepOver', {})
vim.api.nvim_set_keymap('n', '<Leader>dso', '<Plug>VimspectorStepOut', {})
vim.api.nvim_set_keymap('n', '<Leader>dr', '<Plug>VimspectorRestart', {})
vim.api.nvim_set_keymap('n', '<Leader>dc', ':call vimspector#Continue()<CR>', {noremap = true})
vim.api.nvim_set_keymap('', '<C-l>', ':pyf /usr/share/vim/addons/syntax/clang-format.py<cr>', {})
vim.api.nvim_set_keymap('i', '<C-l>', '<c-o>:pyf /usr/share/vim/addons/syntax/clang-format.py<cr>', {})
