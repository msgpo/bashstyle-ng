#!/usr/bin/env bashstyle --python
#coding=utf-8
#########################################################
# 							#
# This is BashStyle-NG  				#
#							#
# Licensed under GNU GENERAL PUBLIC LICENSE v3		#
#							#
# Copyright 2007 - 2015 Christopher Bratusek		#
#							#
#########################################################

MODULES = [ 'sys', 'undobuffer', 'widgethandler', 'dicts', 'prompts' ]

FAILED = []

for module in MODULES:
	try:
		globals()[module] = __import__(module)
	except ImportError:
		FAILED.append(module)

try:
	from gi.repository import Gtk
except ImportError:
	FAILED.append(_("Gtk (from gi.repository)"))

if FAILED:
    print(_("The following modules failed to import: %s") % (" ".join(FAILED)))
    sys.exit(1)

class PromptBuilder(object):

	def __init__(self, config):
		######################## load translations & widgethandler #########################
		gtkbuilder = widgethandler.gtkbuilder

		self.prompt_command = gtkbuilder.get_object("prompt_command")

		self.prompt_command_buffer = undobuffer.UndoableBuffer()
		self.prompt_command.set_buffer(self.prompt_command_buffer)
		self.prompt_command_buffer.set_text("%s" % config["Custom"]["command"])

		def set_prompt_command(widget, data=None):
			start = widget.get_start_iter()
			end = widget.get_end_iter()
			config["Custom"]["command"] = widget.get_text(start, end, False)

		self.prompt_command_buffer.connect("changed", set_prompt_command)

		self.active_buffer = "P_C"

		self.custom_prompt = gtkbuilder.get_object("custom_prompt")

		self.custom_prompt_buffer = undobuffer.UndoableBuffer()
		self.custom_prompt.set_buffer(self.custom_prompt_buffer)
		self.custom_prompt_buffer.set_text("%s" % config["Custom"]["prompt"])

		def set_custom_prompt(widget, data=None):
			start = widget.get_start_iter()
			end = widget.get_end_iter()
			config["Custom"]["prompt"] = widget.get_text(start, end, False)

		self.custom_prompt_buffer.connect("changed", set_custom_prompt)

		###

		self.place_p_c = gtkbuilder.get_object("place_p_c")

		def do_place_p_c(widget, data=None):
			self.prompt_command.set_sensitive(1)
			self.custom_prompt.set_sensitive(0)
			self.active_buffer = "P_C"

		self.place_p_c.connect("clicked", do_place_p_c)

		self.place_ps1 = gtkbuilder.get_object("place_ps1")

		def do_place_ps1(widget, data=None):
			self.prompt_command.set_sensitive(0)
			self.custom_prompt.set_sensitive(1)
			self.active_buffer = "PS1"

		self.place_ps1.connect("clicked", do_place_ps1)

		def prompt_add(widget, text):
			if self.active_buffer == "P_C":
				self.prompt_command_buffer.insert_at_cursor(text)
			elif self.active_buffer == "PS1":
				self.custom_prompt_buffer.insert_at_cursor(text)

		def prompt_add_combo(widget, dict):
			if widget.get_active() != 0:
				text = dict[widget.get_active()]
				prompt_add(widget, text)

		def prompt_set(text):
			if self.active_buffer == "P_C":
				self.prompt_command_buffer.set_text(text)
			elif self.active_buffer == "PS1":
				self.custom_prompt_buffer.set_text(text)

		###

		self.empty_pc = gtkbuilder.get_object("empty_pc")

		def do_empty_pc(widget, data=None):
			self.prompt_command_buffer.set_text("")

		self.empty_pc.connect("clicked", do_empty_pc)

		self.undo_pc = gtkbuilder.get_object("undo_pc")

		def do_undo_pc(widget, data=None):
			self.prompt_command_buffer.undo()

		self.undo_pc.connect("clicked", do_undo_pc)

		self.redo_pc = gtkbuilder.get_object("redo_pc")

		def do_redo_pc(widget, data=None):
			self.prompt_command_buffer.redo()

		self.redo_pc.connect("clicked", do_redo_pc)

		self.empty_ps1 = gtkbuilder.get_object("empty_ps1")

		def do_empty_ps1(widget, data=None):
			self.custom_prompt_buffer.set_text("")

		self.empty_ps1.connect("clicked", do_empty_ps1)

		self.undo_ps1 = gtkbuilder.get_object("undo_ps1")

		def do_undo_ps1(widget, data=None):
			self.custom_prompt_buffer.undo()

		self.undo_ps1.connect("clicked", do_undo_ps1)

		self.redo_ps1 = gtkbuilder.get_object("redo_ps1")

		def do_redo_ps1(widget, data=None):
			self.custom_prompt_buffer.redo()

		self.redo_ps1.connect("clicked", do_redo_ps1)

		self.show_toolbox = gtkbuilder.get_object("show_toolbox")

		def do_show_toolbox(widget, data=None):
                        toolbox = gtkbuilder.get_object("Toolbox")
                        toolbox_close = gtkbuilder.get_object("toolbox.close")
                        toolbox.show_all()
                        toolbox_close.connect("clicked", lambda w: toolbox.hide() or True)
                        toolbox.connect("delete-event", lambda w, e: w.hide() or True)

		self.show_toolbox.connect("clicked", do_show_toolbox)

		######
		def load_toolbutton(object, text):
			widget = gtkbuilder.get_object("%s" % object)
			widget.connect("clicked", prompt_add, text)

		load_toolbutton("username", "\\u")
		load_toolbutton("hostname", "\\h")
		load_toolbutton("fhostname", "\\H")
		load_toolbutton("time", "\\t")
		load_toolbutton("date", "\\d")
		load_toolbutton("sign", "\\$")
		load_toolbutton("fworkdir", "\\w")
		load_toolbutton("workdir", "\\W")
		load_toolbutton("euid", "$EUID")
		load_toolbutton("jobs", "\\j")
		load_toolbutton("bang", "\\!")
		load_toolbutton("number", "\\#")
		load_toolbutton("pid", "$BASHPID")
		load_toolbutton("shlvl", "$SHLVL")
		load_toolbutton("truncpwd", "\\$(truncpwd)")
		load_toolbutton("showsize", "\\$(systemkit dirsize)")
		load_toolbutton("countprocesses", "\\$(systemkit processes)")
		load_toolbutton("showuptime", "\\$(systemkit uptime)")
		load_toolbutton("showtty", "\\$(systemkit tty)")
		load_toolbutton("showcpuload", "\\$(systemkit cpuload)")
		load_toolbutton("showseconds", "\\$SECONDS)")
		load_toolbutton("showbatteryload", "\\$(systemkit battery)")

		###

		def load_toolcombo(object, dict):
			widget = gtkbuilder.get_object("%s" % object)
			widget.set_active(0)
			widget.connect("changed", prompt_add_combo, dict)

		load_toolcombo("showmem", dicts.memory_getters)
		load_toolcombo("showspace", dicts.space_getters)
		load_toolcombo("countfiles", dicts.counters)
		load_toolcombo("showload", dicts.load_getters)
		load_toolcombo("insert_color", dicts.symbolic_colors)

		self.insert_prompt = gtkbuilder.get_object("insert_prompt")
		self.insert_prompt.set_active(0)

		styles_pc = {
			      1 : prompts.empty_pc,
			      2 : prompts.empty_pc,
			      3 : prompts.floating_clock_pc,
			      4 : prompts.equinox_pc,
			      5 : prompts.empty_pc,
			      6 : prompts.poweruser_pc,
			      7 : prompts.empty_pc,
			      8 : prompts.empty_pc,
			      9 : prompts.empty_pc,
			     10 : prompts.empty_pc,
			     11 : prompts.empty_pc,
			     12 : prompts.ayoli_pc,
			    }

		styles_ps1 = {
			       1 : prompts.separator_ps,
			       2 : prompts.vector_ps,
			       3 : prompts.floating_clock_ps,
			       4 : prompts.equinox_ps,
			       5 : prompts.elite_ps,
			       6 : prompts.poweruser_ps,
			       7 : prompts.dirks_ps,
			       8 : prompts.dotprompt_ps,
			       9 : prompts.sepang_ps,
			      10 : prompts.quirk_ps,
			      11 : prompts.sputnik_ps,
			      12 : prompts.ayoli_ps,
			     }

		def do_insert_prompt(widget, data=None):
			selection = widget.get_active()
			if selection != 0:
				self.prompt_command_buffer.set_text(styles_pc[selection])
				self.custom_prompt_buffer.set_text(styles_ps1[selection])

		self.insert_prompt.connect("changed", do_insert_prompt)
