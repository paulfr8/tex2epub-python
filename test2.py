import re

#LATEX Input
latex_input = open("src_tex.tex",'r')
content_latex_input = latex_input.readlines()
latex_input.close()

#HTML output
html_output = open("fichier.html", "w")

html_header = "<html>\n<head>\n\t<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"/>\n\t<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\"/>\n</head>\n<body>\n"
html_end_of_file = "</body>\n</html>"

html_output.write(html_header)

def remove_linejumps(charstring):
  return re.sub(r"\n",r"",charstring)


def parsestring (charstring):
 charstring = remove_linejumps(charstring)
 words = re.split(' ',charstring)
 listcommands = []
 listcommands.append("blank")
 big_output = ""
 for element in words:
  if(re.match(r"\\",element) or re.match(r".+\\",element) or re.match(r"\\.+",element) or re.match(r".+\\.+",element)):
   if(re.match(r"\\chapter{",element) or re.match(r".+\\chapter{",element) or re.match(r"\\chapter{+.",element) or re.match(r".+\\chapter{.+",element)):
    element = re.sub(r"\\chapter{",r"<h1>",element)
    listcommands.append("chapter")
    print(listcommands)
   if(re.match(r"\\emph{",element) or re.match(r".+\\emph{",element) or re.match(r"\\emph{.+",element or re.match(r".+\\emph{.+",element))):
    element = re.sub(r"\\emph{",r"<em>",element)
    listcommands.append("emph")
    print(listcommands)
   if(re.match(r"\\textbf{",element) or re.match(r".+\\textbf{",element) or re.match(r"\\textbf{.+",element or re.match(r".+\\textbf{.+",element))):
    element = re.sub(r"\\textbf{",r"<b>",element)
    listcommands.append("textbf")
    print(listcommands)
   if(re.match(r"}",element) or re.match(r".+}",element) or re.match(r"}.+",element) or re.match(r".+}.+",element)):
    print("There is a end of command")
    bracket = re.split('}',element)
    output = ""
    print(bracket)
    for bracket in element:
     if (listcommands[-1]=="textbf" and listcommands[-1]=="blank" is False):
      listcommands.pop()
      output = bracket + "</b>"
      print(listcommands)
      continue
     if (listcommands[-1]=="emph" and listcommands[-1]=="blank" is False):
      listcommands.pop()
      output = bracket + "</em>"
      print(listcommands)
      continue
     if (listcommands[-1]=="chapter" and listcommands[-1]=="blank" is False):
      listcommands.pop()
      output = bracket + "</h1>"
      print(listcommands)
      continue
    element = element + output
  print(element)
# print(words)
  #commands_in_progress = []
  #skip = 0
  #output = ""
  #for element in words:
   #if re.match(r".+{.+",element) is None:
    #if re.match(r".+}",element) is None:
     #output = output + element + " "
   #if re.match(r"\\emph{.+",element):
    #element = re.sub(r"\\emph{","<em>",element)
    #commands_in_progress.append("italic")
    #output = output + element + " "
   #if re.match(r"\\bfseries{.+",element):
    #element = re.sub(r"\\bfseries{","<b>",element)
    #commands_in_progress.append("bold")
    #output = output + element + " "
   #if re.match(r".+}",element):
     #skip = 0
     #if commands_in_progress[-1]=="bold":
      #if skip==0:
       #commands_in_progress.pop()
       #element = re.sub(r"}",r"</b>",element)
       #output = output + element + " "
       #skip = 1
     #if commands_in_progress[-1]=="italic":
      #if skip==0:
       #commands_in_progress.pop()
       #element = re.sub(r"}",r"</em>",element)
       #output = output + element + " "
       #skip = 1
  #output = output + "\n"
  #return output


for ligne in content_latex_input:
 currentline = ligne
 output = parsestring(currentline)
  

html_output.write(html_end_of_file)
html_output.close()