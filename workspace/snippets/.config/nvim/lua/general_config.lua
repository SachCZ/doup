vim.o.number = true	-- Show line numbers
vim.o.relativenumber = true -- Show relative line numbers.
vim.o.wrap = false	-- Wrap lines
vim.o.textwidth=100	-- Line wrap (number of cols)
vim.o.showmatch = true	-- Highlight matching brace
vim.o.spell = false	-- Enable spell-checking
vim.o.visualbell = true	-- Use visual bell (no beeping)
vim.o.hlsearch = true	-- Highlight all search results
vim.o.smartcase = true	-- Enable smart-case search
vim.o.ignorecase = true	-- Always case-insensitive
vim.o.incsearch = true	-- Searches for strings incrementally
vim.o.autoindent = false	-- Auto-indent new lines
vim.o.cindent = true	-- Use 'C' style program indenting
vim.o.expandtab = true	-- Use spaces instead of tabs
vim.o.shiftwidth = 4	-- Number of auto-indent spaces
vim.o.smartindent = true	-- Enable smart-indent
vim.o.smarttab = true	-- Enable smart-tabs
vim.o.softtabstop=4	-- Number of spaces per Tab
vim.o.ruler = true	-- Show row and column ruler information
vim.o.undolevels=1000	-- Number of undo levels
vim.o.backspace="indent,eol,start"	-- Backspace behaviour
vim.o.undodir="/tmp/.vim/undodir" -- Set undodir location
vim.o.undofile = true -- Persist undos
vim.o.cursorline = true -- Highlight line where the cursor is.

vim.cmd('colorscheme darcula')
vim.cmd('hi CursorLine cterm=NONE guifg=NONE')
vim.o.termguicolors = true

require('neoscroll').setup()
