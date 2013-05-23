import re

#TODO-List:
#Handle 2+ argument commands
#Handle tables
#Handle lists
#Handle 0-argument commands (e.g. \hline)
#Handle 1 argument commands splited over several lines

#Programs list
#Tables
#Lists
#2+ argument commands
#0 argument commands
#1 argument commands
#punctuation
#split files after big divisions <h1> or <h2>

oa_cmd_tex_op = []
oa_cmd_htm_op = []
oa_cmd_htm_ed = []

def oa_cmds_fillin (fcinp_oa_cmd_tex_op, fcinp_oa_cmd_htm_op, fcinp_oa_cmd_htm_ed):
	oa_cmd_tex_op.append(fcinp_oa_cmd_tex_op)
	oa_cmd_htm_op.append(fcinp_oa_cmd_htm_op)
	oa_cmd_htm_ed.append(fcinp_oa_cmd_htm_ed)
	
oa_cmds_fillin ("\\textbf{","<b>","</b>")
oa_cmds_fillin ("{\\bfseries","","</b>")
oa_cmds_fillin ("\\emph{","<em>","</em>")
oa_cmds_fillin ("{\\em","<em>","</em>")
oa_cmds_fillin ("\chapter{","<h1>","</h1>")
oa_cmds_fillin ("\\section{","<h2>","</h2>")
oa_cmds_fillin ("\\subsection{","<h3>","</h3>")
oa_cmds_fillin ("\\subsubsection{","<h4>","</h4>")



def is_there_oacmds (fcinp_charstring, fcinp_list):
	for elt in fcinp_list:
		if fcinp_charstring == elt:
			return True

def split_line (fcinp_char):
	fcout_list = []
	fcine_cmd = ""
	fcine_word = ""
	for char in fcinp_char:
		if char == "\\":
			fcine_cmd = fcine_cmd + char
			continue
		elif char == "{":
			if fcine_cmd != "":
				fcine_cmd = fcine_cmd + char
				fcout_list.append(fcine_cmd)
				fcine_cmd = ""
				continue
			else:
				fcine_cmd = fcine_cmd + char
				continue
		elif char == "}":
			fcout_list.append(char)
			continue
		elif char == " ":
			if fcine_cmd != "":
				fcout_list.append(fcine_cmd)
				fcine_cmd = ""
				fcout_list.append(char)
				continue
			else:
				fcout_list.append(char)
				continue
		else:
			if fcine_cmd != "":
				fcine_cmd = fcine_cmd + char
				continue
			else:
				fcout_list.append(char)
				continue
	return(fcout_list)
      	
def how_many_commands (fcinp_char):
	fcout_list = []
	fcine_cmd = ""
	fcine_word = ""
	fcine_nb_cmds = ""
	for char in fcinp_char:
		if char == "\\":
			fcine_cmd = fcine_cmd + char
			continue
		elif char == "{":
				fcine_cmd = fcine_cmd + char
				fcout_list.append(fcine_cmd)
				fcine_cmd = ""
				continue
		elif char == "}":
			continue
		elif char == " ":
			if fcine_cmd != "":
				fcout_list.append(fcine_cmd)
				fcine_cmd = ""
				continue
			else:
				continue
		else:
			if fcine_cmd != "":
				fcine_cmd = fcine_cmd + char
				continue
			else:
				continue
	fcine_nb_cmds = len(fcout_list)
	return(fcine_nb_cmds)      	

def replace_tex (fcinp_txt_list, fcinp_nb_cmds, fcinp_cmds_list, fcinp_cmds_listb, fcinp_cmds_listc):
	i = 0
	fcout_list = fcinp_txt_list
	test_break = 0
	while True:
		test_break = test_break + 1
		if test_break > 100:
			break
		if i == fcinp_nb_cmds:
			break
		fcine_cmd_inprogress = 0
		fcine_cmd_to_apply = ""
		elt_nb = 0
		for elt in fcinp_txt_list:
			if is_there_oacmds(elt, fcinp_cmds_list):
				if fcine_cmd_inprogress == 0:
					cmd_position = 0
					for cmd in fcinp_cmds_list:
						if elt == fcinp_cmds_list[cmd_position]:
							fcout_list[elt_nb] = fcinp_cmds_listb[cmd_position]
							fcine_cmd_to_apply = fcinp_cmds_listc[cmd_position]
							break
						else:
							cmd_position = cmd_position + 1
							continue
					fcine_cmd_inprogress = 1
					elt_nb = elt_nb + 1
					continue
				if fcine_cmd_inprogress != 0:
					fcine_cmd_inprogress = fcine_cmd_inprogress + 1
					elt_nb = elt_nb + 1
					continue
			elif elt == "}":
				if fcine_cmd_inprogress == 1:
					fcout_list[elt_nb] = fcine_cmd_to_apply 
					fcine_cmd_inprogress = 0
					i = i + 1
					elt_nb = elt_nb + 1
					continue
				if fcine_cmd_inprogress == 0:
					elt_nb = elt_nb + 1
					continue
				if fcine_cmd_inprogress > 1:
					fcine_cmd_inprogress = fcine_cmd_inprogress - 1
					elt_nb = elt_nb + 1
					continue
			else:
				elt_nb = elt_nb + 1
				continue
	return(fcout_list)
		
		

def txt_list_2_txt_str(fcinptxtlist):
	fcoutstring = ""
	for elt in fcinptxtlist:
		fcoutstring = fcoutstring + elt
		continue
	return (fcoutstring)

def replace_one_arg_cmds (fcinp_string, fcinp_list, fcinp_listb, fcinp_listc):
	fcine_split_line = split_line (fcinp_string)
	fcine_nbcmds = how_many_commands (fcinp_string)
	fcine_replaced_cmds = replace_tex (fcine_split_line, fcine_nbcmds, fcinp_list, fcinp_listb, fcinp_listc)
	fcout_string = txt_list_2_txt_str (fcine_replaced_cmds)
	return(fcout_string)

test_charstring = "{\em \\textbf{blab\emph{3}la} \\emph{Ro ro}}"
print (test_charstring)
final_string = replace_one_arg_cmds (test_charstring, oa_cmd_tex_op, oa_cmd_htm_op, oa_cmd_htm_ed)
print (final_string)
