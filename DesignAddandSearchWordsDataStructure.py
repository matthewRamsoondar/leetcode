class Node:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.word = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(root, i: int) -> bool:
            if i == n:
                return False

            cur = word[i]
            if cur == ".":
                if i == n - 1:
                    for c in root.children:
                        if root.children[c].word:
                            return True
                else:
                    for c in root.children:
                        if dfs(root.children[c], i + 1):
                            return True
                    return False

            if cur not in root.children:
                return False

            if i == n - 1:
                return root.children[word[i]].word
            else:
                return dfs(root.children[cur], i + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
