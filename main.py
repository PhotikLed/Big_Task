import pygame as pg
from yandex_api_library import get_static, geocode, get_coord_toponym
from io import BytesIO


class MapApp:

    def __init__(self, size):
        pg.init()
        self.DELTA = 0.01
        self.MAX_Z = 17
        self.screen = pg.display.set_mode(size)
        self.running = True
        self.map = None
        self.z = 15
        self.long = 60
        self.lat = 55
        self.layer = 'map'
        self.update_map()

    # def req(self):
    #     pass

    def update_map(self):
        ll = ','.join(map(str, (self.long, self.lat)))
        bytes_image = get_static(l=self.layer, ll=ll, z=self.z, size='650,450')
        self.map = pg.image.load(BytesIO(bytes_image))

    def key_handler(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_PAGEUP:
                self.z = min(25, self.z + 1)
            elif event.key == pg.K_PAGEDOWN:
                self.z = max(0, self.z - 1)
            elif event.key == pg.K_LEFT:
                self.long -= self.DELTA
            elif event.key == pg.K_RIGHT:
                self.long += self.DELTA
            elif event.key == pg.K_UP:
                self.lat += self.DELTA
            elif event.key == pg.K_DOWN:
                self.lat -= self.DELTA
            self.update_map()

    def run(self):
        while self.running:
            for event in pg.event.get():
                self.key_handler(event)
                if event.type == pg.QUIT:
                    self.running = False
            self.screen.fill('black')
            self.screen.blit(self.map, (0, 0))
            pg.display.flip()


size = 650, 450
app = MapApp(size)
app.run()
