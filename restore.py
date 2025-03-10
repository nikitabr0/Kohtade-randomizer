import json


config = {
    "d_mode": 0,
	"d_x": 1000,
	"d_y": 500,
	"FPS": 30,

	"randomize_x": 725,
	"randomize_y": 25,

	"load_x": 875,
	"load_y": 125,

	"save_x": 875,
	"save_y": 225,
    "buttons_scale": 100,

	"desk_width": 50,
	"desk_height": 50,

	"theme": [[50, 50, 100], [200, 250, 200], [150, 200, 150], "black", [250, 250, 250], "black"],
    
	"enable_experimental_features" : False
}

with open("config.txt", "w+") as file:
    file.write(json.dumps(config, separators=(",\n\t", ": ")))

