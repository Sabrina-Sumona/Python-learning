class Dancer:
    def __init__(self, style):
        self.style = style

    def dance(self):
        print(f'Dancing in {self.style}')


class Singer:
    def __init__(self, genre):
        self.genre = genre

    def sing(self):
        print(f'Singing {self.genre} music')


class Artist:
    def __init__(self, painting_material):
        self.painting_material = painting_material

    def paint(self):
        print(f'Painting with {self.painting_material}')


class SuperHuman(Dancer, Singer, Artist):
    def __init__(self, style, genre, paint_materials, sport):
        Dancer.__init__(self, style)
        Singer.__init__(self, genre)
        Artist.__init__(self, paint_materials)
        self.sport = sport

    def play_sport(self):
        print(f'Playing {self.sport}')

    # Overriding the Dance method of Dancer class
    def dance(self, competition="Fresher's Cup"):
        print(f'Dancing with my own {self.style} in the competition {competition}')


# s = SuperHuman('Hip-Hop', 'Classical', 'Acrylic', 'Football')
# print(s.style)
# print(s.genre)
# print(s.painting_material)
# print(s.sport)
# s.dance()
# s.sing()
# s.paint()
# s.play_sport()

print(help(SuperHuman))
