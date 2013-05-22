import re

#LATEX Input
latex_input = open("src_tex.tex",'r')
content_latex_input = latex_input.readlines()
latex_input.close()

#HTML output
html_output = open("fichier.html", "w")

#Char strings#################################################################################
#Entête html
html_header = "<html>\n<head>\n\t<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"/>\n\t<link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\"/>\n</head>\n<body>\n"
html_end_of_file = "</body>\n</html>"

#chapter
check_latex_chapter = r"^\\chapter{.+}$"
latex_str_chapter_b = r"^\\chapter{"
latex_str_chapter_e = r"}$"
html_markup_chapter_b = "<h1>"
html_markup_chapter_e = "</h1>\n"

#section
check_latex_section = r"^\\section{.+}$"
latex_str_section_b = r"^\\section{"
latex_str_section_e = r"}$"
html_markup_section_b = "<h2>"
html_markup_section_e = "</h2>\n"

#subsection
check_latex_subsection = r"^\\subsection{.+}$"
latex_str_subsection_b = r"^\\subsection{"
latex_str_subsection_e = r"}$"
html_markup_subsection_b = "<h3>"
html_markup_subsection_e = "</h3>\n"

#subsubsection
check_latex_subsubsection = r"^\\subsubsection{.+}$"
latex_str_subsubsection_b = r"^\\subsubsection{"
latex_str_subsubsection_e = r"}$"
html_markup_subsubsection_b = "<h4>"
html_markup_subsubsection_e = "</h4>\n"

#emphasize
check_latex_emph = r".+\\emph{.+}.+"
check_latex_emph_b = r"\\emph{.+"
check_latex_emph_e = r".+}"
html_markup_emph = "r<em>.+</em>"
html_markup_emph_b = "<em>"
html_markup_emph_e = "</em>"

def remove_linejumps(charstring):
  return re.sub(r"\n",r"",charstring)

def is_structure(charstring):
  if re.match(check_latex_chapter, charstring):
    return True
  if re.match(check_latex_section, charstring):
    return True  
  if re.match(check_latex_subsection, charstring):
    return True  
  if re.match(check_latex_subsection, charstring):
    return True
  
def output_structure_pertype(charstring, check_latex_structure_type, latex_str_structure_type_b, latex_str_structure_type_e, html_markup_structure_type_b, html_markup_structure_type_e):
    if re.match(check_latex_structure_type, charstring):
      charstring = re.sub(latex_str_structure_type_b,r"",charstring)
      charstring = re.sub(latex_str_structure_type_e,r"",charstring)
      charstring = remove_linejumps(charstring)
      charstring = html_markup_structure_type_b + charstring + html_markup_structure_type_e
      return charstring

def output_structure(charstring):
  output = output_structure_pertype(charstring,check_latex_chapter, latex_str_chapter_b, latex_str_chapter_e, html_markup_chapter_b, html_markup_chapter_e)
  if output is not None:
    return output
  output = output_structure_pertype(charstring,check_latex_section, latex_str_section_b, latex_str_section_e, html_markup_section_b, html_markup_section_e)
  if output is not None:
    return output
  #output = output_structure_pertype(charstring,check_latex_subsection, latex_str_subsection_b, latex_str_subsection_e, html_markup_subsection_b, html_markup_subsection_e)
  #if output is not None:
    #return output
  #output = output_structure_pertype(charstring,check_latex_subsubsection, latex_str_subsubsection_b, latex_str_subsubsection_e, html_markup_subsubsection_b, html_markup_subsubsection_e)
  #if output is not None:
    #return output

def makeboldit (charstring):
 if re.match(check_latex_emph,charstring):
  words = charstring.split()
  commands_in_progress = []
  skip = 0
  output = ""
  for element in words:
   if re.match(r".+{.+",element) is None:
    if re.match(r".+}",element) is None:
     output = output + element + " "
   if re.match(r"\\emph{.+",element):
    element = re.sub(r"\\emph{","<em>",element)
    commands_in_progress.append("italic")
    output = output + element + " "
   if re.match(r"\\bfseries{.+",element):
    element = re.sub(r"\\bfseries{","<b>",element)
    commands_in_progress.append("bold")
    output = output + element + " "
   if re.match(r".+}",element):
     skip = 0
     if commands_in_progress[-1]=="bold":
      if skip==0:
       commands_in_progress.pop()
       element = re.sub(r"}",r"</b>",element)
       output = output + element + " "
       skip = 1
     if commands_in_progress[-1]=="italic":
      if skip==0:
       commands_in_progress.pop()
       element = re.sub(r"}",r"</em>",element)
       output = output + element + " "
       skip = 1
  output = output + "\n"
  return output

html_output.write(html_header)
for ligne in content_latex_input:
  currentline = ligne
  skip=0
  if is_structure(currentline) is True:
   if skip==0:
    output = output_structure(currentline)
    print(output)
    if makeboldit(output) is not None:
     output = makeboldit(output)
    print(output)
    skip=1
  if is_structure(currentline) is None:
   if skip==0:
    if makeboldit(currentline) is not None:
     output = makeboldit(currentline)
     print(output)
     skip=1
    if makeboldit(currentline) is None:
     print(currentline)
     skip=1
  #print(output)

html_output.write(html_end_of_file)
html_output.close()