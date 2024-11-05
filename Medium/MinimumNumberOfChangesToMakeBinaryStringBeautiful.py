class MinimumNumberOfChangesToMakeBinaryStringBeautiful(object):
    def minChanges(self, s):
        count = 0
        app = 1
        current = s[0]
        for i in range(1, len(s)):
            tmp = s[i]
            if current == tmp:
                app += 1
            else:
                if app % 2 != 0:
                    count += 1
                    app += 1
                else:
                    current = tmp
                    app = 1

        return count