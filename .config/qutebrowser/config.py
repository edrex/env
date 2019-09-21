# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'}

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = True


# Enable JavaScript.
# Type: Bool

# https://www.reddit.com/r/qutebrowser/comments/8iwdpw/how_do_i_disable_javascript_globally_then/
config.set('content.javascript.enabled', False)
config.bind('xs', 'config-cycle --print --pattern *://*.{url:host}/* content.javascript.enabled ;; reload')
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Number of commands to save in the command history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.cmd_history_max_items = -1

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined: * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['i3-sensible-terminal', '-e', 'i3-sensible-editor {file}']

# Hide the statusbar unless a message is shown.
# Type: Bool
c.statusbar.hide = False

# Position of the status bar.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.statusbar.position = 'top'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Open a new window for every tab.
# Type: Bool
c.tabs.tabs_are_windows = True

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://google.com/search?q={}', 'd': 'https://duckduckgo.com/?q={}', 'yt': 'http://www.youtube.com/results?search_query={}', 'wp': 'https://en.wikipedia.org/w/index.php?search={}&title=Special:Search', 'dict': 'https://wordnik.com/words/{}'}

# Hide the window decoration.  This setting requires a restart on
# Wayland.
# Type: Bool
c.window.hide_decoration = True

# Default zoom level.
# Type: Perc
c.zoom.default = '100%'

# Bindings for normal mode
config.bind(',p', 'spawn --userscript password_fill {url}')
config.bind(',v', 'spawn mpv {url}')
#config.unbind('ctrl+v')
