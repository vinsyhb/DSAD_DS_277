import Interpreter

langInter = Interpreter.Interpreter()
langInter.readApplication("abcd")
# langInter.showAll()
# langInter.displayCandidates("Gujarati")
# langInter.findDirectTranslator("Punjabi", "Tamil")
# langInter.findDirectTranslatorDFS("Kannada", "English")
# langInter.findTransTranslatorDFS("Punjabi", "Tamil")
langInter.displayHireList()
