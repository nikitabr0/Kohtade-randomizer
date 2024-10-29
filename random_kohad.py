import logging

logging.basicConfig(filename = "log.txt", filemode = "w+")

from tkinter import filedialog
import pygame as pg
import json
from random import randint


# load configuration file

with open("config.txt", encoding="utf-8") as config_file:
	config = json.loads(config_file.read())


theme = []

for color in config["theme"]:
	theme.append(pg.Color(color))


class Desk:
	def __init__(self, surface : pg.Surface, x : int, y : int):
		self.surface = surface
		self.x = int(x)
		self.y = int(y)
		self.width = config["desk_width"]
		self.height = config["desk_height"]
		self.student = ""


	def draw(self):
		pg.draw.rect(self.surface, config["theme"][1], pg.Rect(self.x, self.y, self.width, self.height))
		pg.draw.rect(self.surface, config["theme"][2], pg.Rect(self.x + self.width * .05, self.y + self.height * .05, self.width * .9, self.height * .9))

		font = pg.font.SysFont("arial", int(self.height / 5))
		for i, line in enumerate(self.student.split(" ")):
			text = font.render(line, 1, config["theme"][3])
			self.surface.blit(text, (self.x + self.width / 2 - text.get_width() / 2, self.y + self.height /  len(self.student.split(" ")) + (i - 1) * 25 * (self.height /  100)))


	def click(self, event : pg.event.Event):
		if int(event.pos[0] / width) * width + 10 == self.x and int(event.pos[1] / (height * 1.5)) * height * 1.5 + 10 == self.y:
			return True

		return False



# load the list of students

with open("klass.txt", encoding="utf-8") as file:
	data = file.read().split("\n")


# initialize pygame and display window

pg.init()

display = pg.display.set_mode((config["d_x"], config["d_y"]), config["d_mode"])


width, height, b_scale = config["desk_width"], config["desk_height"], config["buttons_scale"] / 100


font = pg.font.SysFont("arial", int(75 * b_scale * .6))
text1 = font.render("randomize", 1, config["theme"][5])
text2 = font.render("load", 1, config["theme"][5])
text3 = font.render("save", 1, config["theme"][5])

desks = [Desk(display, 10, 10)]

running = True
while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
			break

		elif event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:

				if pg.Rect(config["randomize_x"], config["randomize_y"], 250 * b_scale, 75 * b_scale).collidepoint(event.pos[0], event.pos[1]):
					data_buffer = data[:]

					for desk in desks:
						if len(data_buffer) == 1:
							student_index = 0

						elif len(data_buffer) == 0:
							break

						else:
							student_index = randint(0, len(data_buffer) - 1)


						desk.student = data_buffer[student_index]

						data_buffer.pop(student_index)


					break


				# load
				elif pg.Rect(config["load_x"], config["load_y"], 100 * b_scale, 75 * b_scale).collidepoint(event.pos[0], event.pos[1]):
					filename = str(filedialog.askopenfilename(defaultextension='.kohad', filetypes=[("Kohtade_randomizer", ".Kohtade_randomizer"), ("text", ".txt")], initialdir="saves/"))

					if filename != "":
						with open(filename, "r", encoding="utf-8") as file:

							desks = []

							for desk in file.read().split("\n"):
								if desk != "":
									desks.append(Desk(display, int(desk.split(";")[0]), int(desk.split(";")[1])))
									desks[-1].student = desk.split(";")[2]


				# save
				elif pg.Rect(config["save_x"], config["save_y"], 100 * b_scale, 75 * b_scale).collidepoint(event.pos[0], event.pos[1]):
					filename = str(filedialog.asksaveasfile(defaultextension='.kohad', filetypes=[("Kohtade_randomizer", ".Kohtade_randomizer"), ("text", ".txt")], initialdir="saves/"))

					if filename != "None":
						with open(filename.split("'")[1], "w+", encoding="utf-8") as file:

							to_write = ""

							for desk in desks:
								to_write += "{};{};{}\n".format(desk.x, desk.y, desk.student)

							file.write(to_write)


				elif len(desks) != 0:
					for i, desk in enumerate(desks):

						if desk.click(event):

							desks.remove(desk)
							del desk

							break

						elif i == len(desks) - 1:
							desks.append(Desk(display, int(event.pos[0] / width) * width + 10, int(event.pos[1] / (height * 1.5)) * height * 1.5 + 10))

							break

				else:
					desks.append(Desk(display, int(event.pos[0] / width) * width + 10, int(event.pos[1] / (height * 1.5)) * height * 1.5 + 10))


	display.fill(config["theme"][0])


	for desk in desks:
		desk.draw()


	# draw randomize, load and save buttons

	pg.draw.rect(display, config["theme"][4], pg.Rect(config["randomize_x"], config["randomize_y"], 250 * b_scale, 75 * b_scale))
	pg.draw.rect(display, config["theme"][4], pg.Rect(config["load_x"], config["load_y"], 100 * b_scale, 75 * b_scale))
	pg.draw.rect(display, config["theme"][4], pg.Rect(config["save_x"], config["save_y"], 100 * b_scale, 75 * b_scale))

	display.blit(text1, (config["randomize_x"] + 250 * b_scale / 2 - text1.get_width() / 2, config["randomize_y"] + text1.get_height() / 5))
	display.blit(text2, (config["load_x"] + 100 * b_scale / 2 - text2.get_width() / 2, config["load_y"] + text2.get_height() / 5))
	display.blit(text3, (config["save_x"] + 100 * b_scale / 2 - text3.get_width() / 2, config["save_y"] + text3.get_height() / 5))


	pg.display.flip()
	pg.time.Clock().tick(config["FPS"])

