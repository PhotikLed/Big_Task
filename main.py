import pygame as pg
from yandex_api_library import get_static, geocode, get_coord_toponym
from io import BytesIO


class MapApp:
    def __init__(self, size):
        pg.init()
        self.screen = pg.display.set_mode(size)
        self.running = True
        self.map = None
        self.update_map()

    def update_map(self):
        bytes_image = get_static(l='map', ll='60.152994,55.152774', z=15, size='650,450')
        self.map = pg.image.load(BytesIO(bytes_image))

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.screen.fill('black')
            self.screen.blit(self.map, (0, 0))
            pg.display.flip()


size = 650, 450
app = MapApp(size)
app.run()
