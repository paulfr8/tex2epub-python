import re

1a_cmd_tex_op = []
1a_cmd_htm_op = []
1a_cmd_htm_ed = []

def 1a_cmds_fillin (fcinp_1a_cmd_tex_op, fcinp_1a_cmd_htm_op, fcinp_1a_cmd_htm_ed):
	1a_cmd_tex_op.append(fcinp_1a_cmd_tex_op)
	1a_cmd_htm_op.append(fcinp_1a_cmd_htm_op)
	1a_cmd_htm_ed.append(fcinp_1a_cmd_htm_ed)
	
1a_cmds_fillin ("\\textbf{","<b>","</b>")
1a_cmds_fillin ("\\emph{","<em>","</em>")

print(1a_cmd_tex_op)
print(1a_cmd_htm_op)
print(1a_cmd_htm_ed)

def split_line (fcinp_char):
	fcout_list = []
	fcine_cmd = ""
	fcine_word = ""
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

def replace_tex (fcinp_txt_list, fcinp_nb_cmds):#add list with the commands replacement settings
	i = 0
	fcout_list = fcinp_txt_list
	while True:
		if i == fcinp_nb_cmds:
			break
		fcine_cmd_inprogress = 0
		fcine_cmd_to_apply = ""
		elt_nb = 0
		for elt in fcinp_txt_list:
			if (elt == "\\textbf{" or elt == "\\emph{"):
				if fcine_cmd_inprogress == 0:
					if elt == "\\textbf{":
						fcout_list[elt_nb] = "<b>"
						fcine_cmd_to_apply = "</b>"
						fcine_cmd_inprogress = 1
						elt_nb = elt_nb + 1
						continue
					elif elt == "\\emph{":
						fcout_list[elt_nb] = "<em>"
						fcine_cmd_to_apply = "</em>"
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

def replace_one_arg_cmds (fcinp_string):
	fcine_split_line = split_line (fcinp_string)
	fcine_nbcmds = how_many_commands (fcinp_string)
	fcine_replaced_cmds = replace_tex (fcine_split_line, fcine_nbcmds)
	fcout_string = txt_list_2_txt_str (fcine_replaced_cmds)
	return (fcout_string)

test_charstring = "\\textbf{blab\emph{3}la} \emph{Ro ro}"
final_string = replace_one_arg_cmds (test_charstring)
