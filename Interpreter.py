import utils

class Interpreter:
    adjMatrix = []
    languages = []
    candidates = []
    vertices = []
    def readApplication(self, inputFile):
        text = open("./innputPS25.txt", "r")
        data = text.read()
        dataEntries = data.split("\n")
        text.close()
        vertices = utils.getVertices(dataEntries)
        self.vertices= vertices
        Interpreter.adjMatrix = [
            [0 for i in range(len(vertices))] for x in range(len(vertices))]
        for record in dataEntries:
            rowEntries = record.split("/")
            nameIndex = vertices.index(rowEntries[0])
            self.candidates.append(rowEntries[0])
            for item in rowEntries[1:]:
                if item not in self.languages:
                    self.languages.append(item)
                langIndex = vertices.index(item)
                Interpreter.addEdge(self, nameIndex, langIndex)
        print()

    def addEdge(self, node1, node2):
        Interpreter.adjMatrix[node1][node2] = 1
        Interpreter.adjMatrix[node2][node1] = 1
    
    def showAll(self):
        print("show ALL")
        print("Total number of candidates", len(self.candidates))
        print("Total number of languages", len(self.languages))
        print("list of candidates")
        for i in self.candidates:
            print(i)
        print("list of languages")
        for i in self.languages:
            print(i)

    def displayHireList(self):
        candidates=[]
        for lang in self.languages:
            langIndex = self.vertices.index(lang)
            candidateFound = False
            for j in candidates:
                candidateIndex = self.vertices.index(j)
                if self.adjMatrix[langIndex][candidateIndex] == 1:
                    candidateFound = True
            if candidateFound == True:
                continue
            for i in range(len(self.vertices)):
                if self.adjMatrix[langIndex][i] == 1:
                    candidates.append(self.vertices[i])
                    break
        
        print(candidates)
        print("displayHireList")

    def displayCandidates(self, lang):
        langIndex = self.vertices.index(lang)
        print(self.adjMatrix[langIndex])
        for i in range(len(self.vertices)):
            if self.adjMatrix[langIndex][i] == 1:
                print(self.vertices[i], "can speak", lang)
        print("displayCandidates")

    def findDirectTranslator(self, langA, langB):
        print("findDirectTranslator")
        langAIndex = self.vertices.index(langA)
        langBIndex = self.vertices.index(langB)
        translator = ""
        for i in range(len(self.vertices)):
            if (self.adjMatrix[langAIndex][i] == 1 and self.adjMatrix[langBIndex][i] == 1):
                translator = self.vertices[i]
                break
        print("direct tran", translator)
        return translator

    def findDirectTranslatorDFS(self, langA, langB):
        print("findDirectTranslatorDFS")
        visited = set()
        langAIndex = self.vertices.index(langA)
        langBIndex = self.vertices.index(langB)
        step = 0
        personIndex = self.DFSUtil(langAIndex, langBIndex, visited, step, 1, [])
        print("personIndexpersonIndex", personIndex)
        if personIndex == -1:
            print("no translator available")
        else:
            print(self.vertices[personIndex], "can tranlate from", langA, "to", langB)
    
    def findTransTranslatorDFS(self, langA, langB):
        print("findTransTranslatorDFS")
        visited = set()
        langAIndex = self.vertices.index(langA)
        langBIndex = self.vertices.index(langB)
        step = 0
        path = []
        personIndex = self.DFSUtil(langAIndex, langBIndex, visited, step, 3, path)
        print("PATH", path)
        print(langA)
        for i in path:
            print(self.vertices[i])
        print(langB)
        print("personIndexpersonIndex", personIndex)
        if personIndex == -1:
            print("no translator available")
        else:
            print(self.vertices[personIndex], "can tranlate from", langA, "to", langB)

    def DFSUtil(self, startIndex, destIndex, visited, step, stepCount,path):
        for i in range(len(self.vertices)):
            if self.adjMatrix[startIndex][i] == 1 and i not in visited:
                if i == destIndex and step == stepCount:
                    print("reached destination")
                    return startIndex
                elif step > stepCount:
                    return -1
                else:
                    visited.add(startIndex)
                    path.append(i)
                    translator = self.DFSUtil(
                        i, destIndex, visited, step + 1, stepCount, path)
                    if translator != -1:
                        return translator
                    path.remove(i)
                    visited.remove(startIndex)
        return -1

