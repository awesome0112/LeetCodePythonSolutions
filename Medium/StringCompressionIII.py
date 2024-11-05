class StringCompressionIII(object):
    def compressedString(self, word):
        comp = ""
        current = '#'
        app = 0
        for char in word:
            if char == current:
                app = app + 1
                if app == 9:
                    comp = comp + str(app) + current
                    app = 0
                    current = '#'

            else:
                if current != '#':
                    comp = comp + str(app) + current

                current = char
                app = 1

        if current != '#':
            comp = comp + str(app) + current

        return comp