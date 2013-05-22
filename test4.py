import re

def add_to_cmds_list(output_list, inputlist):
  output_list.append(inputlist)
  return output_list

def define_cmd_attr(var1, var2, var3, var4, var5):
  output_list = [var1, var2, var3, var4, var5]
  return output_list

cmds_list = []
add_to_cmds_list(cmds_list, ["textbf", r".*\\textbf{.*", r"\\textbf{", ".*}.*", "}", r"<b>", "</b>"])
add_to_cmds_list(cmds_list, ["emph", r".*\\emph{.*", r"\\emph{", ".*}.*", "}", r"<em>", "</em>"])
add_to_cmds_list(cmds_list, ["chapter", r".*\\chapter{.*", r"\\chapter{", ".*}.*", "}", r"<h1>", "</h1>"])
add_to_cmds_list(cmds_list, ["section", r".*\\section{.*", r"\\section{", ".*}.*", "}", r"<h2>", "</h2>"])
add_to_cmds_list(cmds_list, ["subsection", r".*\\subsection{.*", r"\\subsection{", ".*}.*", "}", r"<h3>", "</h3>"])
add_to_cmds_list(cmds_list, ["subsubsection", r".*\\subsubsection{.*", r"\\subsubsection{", ".*}.*", "}", r"<h4>", "</h4>"])

def return_cmds_list(inputlist):
  output_list = []
  for elt in inputlist:
    output_list.append(elt[0])
  return(output_list)
  
original_charstring = "\\chapter{Chapitre 1} \\section{Section 1} \\section{2}"

def check_if_cmds (inputchar, inputlist):
  for elt in inputlist:
    if re.match(".*" + elt[1] + ".*", inputchar):
      return True

def check_if_closing_cmds (inputchar, inputlist):
  for elt in inputlist:
    if re.match(elt[3], inputchar):
      return True

def check_if_one_cmd (inputchar, test):
  if re.match(test, inputchar):
    return True
      
def remplace_opening_cmds(inputchar, inputlist):
  words = re.split(' ', inputchar)
  cmd_in_progress = []
  output_char = ""
  for word in words:
    if check_if_cmds(word, inputlist):
      for elt in inputlist:
        if check_if_one_cmd (word, elt[1]):
          cmd_in_progress.append(elt[0])
          word = re.sub(elt[2],elt[5],word)
          output_char = output_char + " " + word
    else:
      output_char = output_char + " " + word
  return([output_char, cmd_in_progress])

def remplace_closing_cmds(inputchar, inputlist, inputlistcmds):
  words = re.split(' ', inputchar)
  output_char = ""
  cmds_list = inputlistcmds
  cmds_list.reverse()
  nb_cmds = len (inputlistcmds)
  for word in words:
    if check_if_closing_cmds (word, inputlist):
      for elt in inputlist:
        if re.match(elt[3], word):
          if len(cmds_list) == 0:
            break
          if elt[0]==cmds_list[-1]:
            word = re.sub(elt[4], elt[6], word, 1)
            cmds_list.pop()
            output_char = output_char + " " + word
    else:
      output_char = output_char + " " + word
  return(output_char)

check_if_cmds(original_charstring, cmds_list)
result_cmd = remplace_opening_cmds(original_charstring, cmds_list)
charstring = result_cmd[0]
cmds_in_progress = result_cmd[1]

#print(charstring)
#print(cmds_in_progress)

final_charstring=remplace_closing_cmds(charstring, cmds_list, cmds_in_progress)

print(original_charstring)
print(final_charstring)