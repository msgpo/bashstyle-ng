#coding=utf-8
#########################################################
# 							#
# This is BashStyle-NG  				#
#							#
# Licensed under GNU GENERAL PUBLIC LICENSE v3		#
#							#
# Copyright 2007 - 2016 Christopher Bratusek		#
#							#
#########################################################

color_styles = {
		 0 : "normal",
		 1 : "bright",
		 2 : "dimmed",
		 3 : "inverted",
		 4 : "underlined",
		}

less_foreground_colors = {
		   0 : "$lfblack",
		   1 : "$lfred",
		   2 : "$lfgreen",
		   3 : "$lfyellow",
		   4 : "$lfblue",
		   5 : "$lfmagenta",
		   6 : "$lfcyan",
		   7 : "$lfgrey",
		   8 : "$lfwhite",
		   9 : "$lfcoldblue",
		  10 : "$lfsmoothblue",
		  11 : "$lficeblue",
		  12 : "$lfturqoise",
		  13 : "$lfsmoothgreen",
		  14 : "$lfwinered",
		  15 : "$lfbrown",
		  16 : "$lfsilver",
		  17 : "$lfocher",
		  18 : "$lforange",
		  19 : "$lfpurple",
		  20 : "$lfpink",
		  21 : "$lfcream",
		}

less_background_colors = {
		   0 : "$lbblack",
		   1 : "$lbred",
		   2 : "$lbgreen",
		   3 : "$lbyellow",
		   4 : "$lbblue",
		   5 : "$lbmagenta",
		   6 : "$lbcyan",
		   7 : "$lbgrey",
		   8 : "$lbwhite",
}

grep_colors = {
		0 : "01;38;5;0",
		1 : "01;38;5;1",
		2 : "01;38;5;2",
		3 : "01;38;5;3",
		4 : "01;38;5;4",
		5 : "01;38;5;5",
		6 : "01;38;5;6",
		7 : "01;38;5;7",
		8 : "01;38;5;97",
		9 : "01;38;5;33",
	       10 : "01;38;5;111",
	       11 : "01;38;5;45",
	       12 : "01;38;5;60",
	       13 : "01;38;5;42",
	       14 : "01;38;5;637",
	       15 : "01;38;5;684",
	       16 : "01;38;5;761",
	       17 : "01;38;5;690",
	       18 : "01;38;5;714",
	       19 : "01;38;5;604",
	       20 : "01;38;5;213",
	       21 : "01;38;5;5344",
	      }

colors = {
	   0 : "$black",
	   1 : "$red",
	   2 : "$green",
	   3 : "$yellow",
	   4 : "$blue",
	   5 : "$magenta",
	   6 : "$cyan",
	   7 : "$grey",
	   8 : "$white",
	   9 : "$coldblue",
	  10 : "$smoothblue",
	  11 : "$iceblue",
	  12 : "$turqoise",
	  13 : "$smoothgreen",
	  14 : "$winered",
	  15 : "$brown",
	  16 : "$silver",
	  17 : "$ocher",
	  18 : "$orange",
	  19 : "$purple",
	  20 : "$pink",
	  21 : "$cream",
	 }

prompt_styles = {
		  0 : "separator",
		  1 : "vector",
		  2 : "clock",
		  3 : "equinox",
		  4 : "elite",
		  5 : "poweruser",
		  6 : "dirks",
		  7 : "dot_prompt",
		  8 : "sepa_ng",
		  9 : "quirk",
		 10 : "sputnik",
		 11 : "ayoli",
		}

history_types = {
		 0 : "erasedups",
		 1 : "ignoredups",
		 2 : "ignorespace",
		 3 : "ignoreboth",
		}

bell_styles = {
		0 : "audible",
		1 : "visible",
		2 : "none",
	      }

edit_modes = {
	      0 : "emacs",
	      1 : "vi",
	     }

memory_types = {
		0 : "free",
		1 : "used",
		2 : "both",
		3 : "none",
	       }

vim_colors = {
	       0 : "default",
	       1 : "adaryn",
	       2 : "advantage",
	       3 : "desert",
	       4 : "gobo",
	       5 : "impact",
	       6 : "nightshade",
	       7 : "nightwish",
	       8 : "wombat",
	       9 : "asu1dark",
	      10 : "candycode",
	      11 : "dw_orange",
	      12 : "fruit",
	      13 : "relaxedgreen",
	      14 : "tango",
	      15 : "molokai",
	      16 : "vividchalk",
	      17 : "meta5",
	      18 : "woju",
	      19 : "lightning",
	      20 : "papercolor",
	      21 : "solarized",
	     }

vim_foldmethods = {
	       0 : "indent",
	       1 : "marker",
	       2 : "manual",
	       3 : "expr",
	       4 : "syntax",
	       5 : "diff",
	}

nano_colors = {
              0 : "white",
              1 : "black",
              2 : "red",
              3 : "blue",
              4 : "green",
              5 : "yellow",
              6 : "magenta",
              7 : "cyan",
}

ls_colors = {
	      0 : "$lblack",
	      1 : "$lred",
	      2 : "$lgreen",
	      3 : "$lyellow",
	      4 : "$lblue",
	      5 : "$lmagenta",
	      6 : "$lcyan",
	      7 : "$lgrey",
	      8 : "$lwhite",
	      9 : "$lcoldblue",
	     10 : "$lsmoothblue",
	     11 : "$liceblue",
	     12 : "$lturqoise",
	     13 : "$lsmoothgreen",
	     14 : "$lwinered",
	     15 : "$lbrown",
	     16 : "$lsilver",
	     17 : "$locher",
	     18 : "$lorange",
	     19 : "$lpurple",
	     20 : "$lpink",
	     21 : "$lcream",
	    }


##### Keybindings #####

keybindings = {
	"undo",
	"upcase_word",
	"capitalize_word",
	"downcase_word",
	"transpose_words",
	"transpose_chars",
	"unix_word_rubout",
	"kill_word",
	"possible_filename_completions",
	"possible_hostname_completions",
	"possible_username_completions",
	"possible_variable_completions",
	"kill_line",
	"unix_line_discard",
	"beginning_of_line",
	"end_of_line",
	"clear_screen",
	"history_search_forward",
	"history_search_backward",
	"complete_path",
	"alias_expand_line",
	"backward_char",
	"backward_delete_char",
	"delete_char",
	"forward_char",
	"backward_word",
	"forward_word",
	"overwrite_mode",
	"menu_complete",
	"menu_complete_backward",
	"rerun_root",
	"backward_kill_line",
	"list_keys"
}


##### IconView Stuff #####

iconview_icons = ["bs-ng-style", "bs-ng-alias", "bs-ng-advanced",
		  "bs-ng-shopts", "bs-ng-git", "bs-ng-readline",
		  "bs-ng-vim", "bs-ng-nano", "bs-ng-ls", "bs-ng-man",
		  "bs-ng-keys", "bs-ng-custom",  "bs-ng-config",
		  "bs-ng-doc", "bs-ng-info" ]

iconview_labels = {
	"bs-ng-style" : _("General Style"),
	"bs-ng-alias" : _("Aliases"),
	"bs-ng-advanced" : _("Advanced"),
	"bs-ng-readline" : _("Readline"),
	"bs-ng-vim" : _("Vi improved"),
	"bs-ng-nano" : _("GNU Nano"),
	"bs-ng-ls" : _("LS colors"),
	"bs-ng-custom" : _("Custom Prompt Builder"),
	"bs-ng-shopts" : _("Shell Options"),
	"bs-ng-git" : _("Git"),
	"bs-ng-info" : _("About BashStyle-NG"),
	"bs-ng-keys" : _("Keybindings"),
	"bs-ng-config" : _("Configuration"),
	"bs-ng-doc" : _("Documentation"),
	"bs-ng-man" : _("Manpage Colors"),
}

notebook_pages = {

	_("General Style") : 1,
	_("Aliases") : 2,
	_("Advanced") : 3,
	_("Readline") : 4,
	_("Vi improved") : 5,
	_("GNU Nano") : 6,
	_("LS colors") : 7,
	_("Manpage Colors") : 15,
	_("Custom Prompt Builder") : 8,
	_("Shell Options") : 10,
	_("Git") : 9,
	_("About BashStyle-NG") : 12,
	_("Keybindings") : 11,
	_("BashStyle-NG StartUp") : 13,
	_("Configuration") : 14,
	_("Documentation") : 0,
}

##### Custom Prompt Builder #####

counters_p_c = {
	    1 : "\\$(systemkit countoverallfiles)",
	    2 : "\\$(systemkit countvisiblefiles)",
	   }

counters_ps1 = {
	    1 : "\\$(systemkit countoverallfiles)",
	    2 : "\\$(systemkit countvisiblefiles)",
	   }

load_getters_p_c = {
		1 : "$(systemkit load1)",
		2 : "$(systemkit load5)",
		3 : "$(systemkit load15)",
	       }

load_getters_ps1 = {
		1 : "\\$(systemkit load1)",
		2 : "\\$(systemkit load5)",
		3 : "\\$(systemkit load15)",
	       }

memory_getters_p_c = {
		  1 : "$(systemkit usedram)",
		  2 : "$(systemkit freeram)",
		  3 : "$(systemkit usedram%)",
		  4 : "$(systemkit freeram%)",
		 }

memory_getters_ps1 = {
		  1 : "\\$(systemkit usedram)",
		  2 : "\\$(systemkit freeram)",
		  3 : "\\$(systemkit usedram%)",
		  4 : "\\$(systemkit freeram%)",
		 }

space_getters_p_c = {
		  1 : "$(systemkit usedspace <device>)",
		  2 : "$(systemkit freespace <device>)",
		  3 : "$(systemkit usedspace% <device>)",
		  4 : "$(systemkit freespace% <device>)",
		 }

space_getters_ps1 = {
		  1 : "\\$(systemkit usedspace <device>)",
		  2 : "\\$(systemkit freespace <device>)",
		  3 : "\\$(systemkit usedspace% <device>)",
		  4 : "\\$(systemkit freespace% <device>)",
		 }

symbolic_colors_p_c = {
		   1 : "${ecolor_user}",
		   2 : "${ecolor_host}",
		   3 : "${ecolor_date}",
		   4 : "${ecolor_time}",
		   5 : "${ecolor_wdir}",
		   6 : "${ecolor_font}",
		   7 : "${ecolor_separator}",
		   8 : "${ecolor_uptime}",
		   9 : "${ecolor_ps}",
		  }

symbolic_colors_ps1 = {
		   1 : "${color_user}",
		   2 : "${color_host}",
		   3 : "${color_date}",
		   4 : "${color_time}",
		   5 : "${color_wdir}",
		   6 : "${color_font}",
		   7 : "${color_separator}",
		   8 : "${color_uptime}",
		   9 : "${color_ps}",
		  }
