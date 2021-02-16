import re, os

def inBracket(x):
   return x[x.find("[") + 1 : x.find("]")]

def isNotComment(line):
   return not re.match("^;", line)

class LIML:
   def __init__(self, limlstr):
      self.liml = limlstr.split("\n")
      self.parsed = {}

      for rawln in self.liml:
         self.ln = rawln.replace("\n", "") 

         if isNotComment(self.ln):
            if len(self.ln) > 0 and self.ln[0] == "[" and self.ln[-1] == "]":
               self.section = inBracket(self.ln)
               self.parsed[self.section] = []
            
            elif self.ln == "":
               pass

            else:
               self.parsed[self.section].append(self.ln)
               
   def toDict(self):
      return self.parsed

   def update(self, route, new):

      self.factors = route.split(".")
      self.sectionFactor = self.factors[0]
      self.indexFactor = self.factors[1]

      self.parsed[self.sectionFactor][int(self.indexFactor)] = new
   
   def addSection(self, section, values=[]):
      if not section in self.parsed.keys():
         self.parsed[section] = values
      
      else:
         print("hey you cannot add idiot")
   
   def toStr(self):
      self.count = 0
      self.lines = []

      for sect in self.parsed.keys():

         if self.count != 0: 
            self.lines.append(f"\n[{sect}]\n")

         else:
            self.lines.append(f"[{sect}]\n")
            self.count += 1

         for val in self.parsed[sect]:
            self.lines.append(f"{val}\n")
         
      return ''.join(self.lines)
