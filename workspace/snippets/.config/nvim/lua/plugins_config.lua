require('packer').startup(function(use)
  use 'wbthomason/packer.nvim' -- Packer manages itself.
  use 'neovim/nvim-lspconfig' -- Collection of configurations for built-in LSP client.
  use 'hrsh7th/nvim-cmp' -- Autocompletion plugin.
  use 'hrsh7th/cmp-nvim-lsp' -- LSP source for nvim-cmp.
  use 'saadparwaiz1/cmp_luasnip' -- Snippets source for nvim-cmp (needed for suggestion confirm).
  use 'L3MON4D3/LuaSnip' -- Snippets plugin (needed for suggestion confirm).
  use 'doums/darcula' -- Color scheme like clion.
  use 'ntpeters/vim-better-whitespace' -- Trailing whitespace highlight.
  use 'ctrlpvim/ctrlp.vim' -- Fuzzy finder.
  use { 'puremourning/vimspector', run = ':VimspectorInstall vscode-cpptools debugpy' } -- Debugger.
  use 'karb94/neoscroll.nvim' -- Smooth scrolling.
  use 'vim-airline/vim-airline' -- Bottom line showing some context.
end)

