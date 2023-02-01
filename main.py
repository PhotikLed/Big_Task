import pygame as pg
import requests

from yandex_api import get_static
from io import BytesIO


class MapApp:
    def __init__(self, size):
        pg.init()
        self.screen = pg.display.set_mode(size)
        self.running = True
        self.map = None
        self.l = 'map'
        self.ll = '60.152500, 55.149571'
        self.update_map()

    # def request(self):
    #     response = requests.get

    def update_map(self):
        bytes_image = get_static(l=self.l, ll=self.ll, z=15, size='650, 450')
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
