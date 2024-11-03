class RotateString(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        for i, char in enumerate(s):
            s = self.move(s)
            if s == goal:
                return True

        return False

    def move(self, s):
        first_char = s[0]
        return s[1:] + first_char
