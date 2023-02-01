import pygame as pg
from yandex_api_library import get_static, geocode, get_coord_toponym
from io import BytesIO


class MapApp:
    def __init__(self, size):
        pg.init()
        self.DELTA = 60
        self.screen = pg.display.set_mode(size)
        self.running = True
        self.map = None
        self.z = 0
        self.long = 0
        self.lat = 0
        self.layer = 'sat'
        self.update_map()

    def update_map(self):
        ll = ','.join(map(str, (self.long, self.lat)))
        bytes_image = get_static(l=self.layer, ll=ll, z=self.z, size='650,450')
        self.map = pg.image.load(BytesIO(bytes_image))

    def key_handler(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_PAGEUP:
                self.z = min(17, self.z + 1)
            elif event.key == pg.K_PAGEDOWN:
                self.z = max(0, self.z - 1)
            elif event.key == pg.K_LEFT:
                self.long = self.long - self.DELTA / 2 ** self.z
                if self.long < -180:
                    self.long += 360
            elif event.key == pg.K_RIGHT:
                self.long = self.long + self.DELTA / 2 ** self.z
                if self.long > 180:
                    self.long -= 360
            elif event.key == pg.K_UP:
                self.lat = min(85, self.lat + self.DELTA / 2 ** self.z)
            elif event.key == pg.K_DOWN:
                self.lat = max(-85, self.lat - self.DELTA / 2 ** self.z)
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

