extends Control


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var output = []

# Called when the node enters the scene tree for the first time.
func _ready():
	print("start")
	#OS.execute("sh", ["res://commander.sh/"], true)
	#OS.execute("python3", ["res://python/TestPy.py"], true, output, true, true)
	OS.execute("python3", ["v3.py"], true, output, true, true)
	#print(OS.execute("python3", ["res://v2.py/"], true))
	#execute ( String path, 
	# PoolStringArray arguments,
	# bool blocking=true, 
	# Array output=[ ],
	# bool read_stderr=false,
	# bool open_console=false )
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
