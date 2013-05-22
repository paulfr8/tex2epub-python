import re

class cmd_infos:
  def __init__(self, x=1, y=2):
    self.x = x
    self.y = y
  def fill_in(self,listattr,listvalues):
    listofvalues = listvalues
    i = 0
    for elt in listattr:
      setattr(self,elt,listofvalues[i])
      i = i +1

#def create_cmd_infos(name, list1, list2):
  #print(name)
  #print(list1)
  #print(list2)
  #name = cmd_infos()
  #name.fill_in(list1, list2)
  
	
att_name_list = ["name", "texb", "texe", "htlb", "htle"]
cmd_list = ["textbf", "emph", "chapter", "section", "subsection", "subsubsection"]
textbf_value_list = ["textbf", "\\textbf{", "}", "<b>", "</b>"]

def createcmd_infos(x):
  return cmd_infos(x)

cmd_infos("textbf")
textbf.x = 3

print(textbf.x)

#textbf = cmd_infos()
#emph = cmd_infos()

#chapter = cmd_infos()
#section = cmd_infos()
#subsection = cmd_infos()
#subsubsection = cmd_infos()

#textbf.fill_in(att_name_list, ["textbf", "\\textbf{", "}", "<b>", "</b>"])
#emph.fill_in(att_name_list, ["emph", "\\emph{", "}", "<em>", "</em>"])

#chapter.fill_in(att_name_list,["chapter", "\\chapter{", "}", "<h1>", "</h1>"])
#section.fill_in(att_name_list, ["section", "\\section{", "}", "<h2>", "</h2>"])
#subsection.fill_in(att_name_list, ["subsection", "\\subsection{", "}", "<h3>", "</h3>"])
#subsubsection.fill_in(att_name_list, ["subsubsection", "\\subsubsection{", "}", "<h4>", "</h4>"])
#textbf.name = "textbf"
#textbf.texb = "\\textbf{"
#textbf.texe = "}"
#textbf.htlb = "<b>"
#textbf.htle = "</b>"