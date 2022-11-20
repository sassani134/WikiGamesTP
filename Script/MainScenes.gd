extends Control


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_ButtonSolo_pressed():
	get_tree().change_scene("res://Scenes/CreditScenes.tscn")
	return


func _on_ButtonMultiLocal_pressed():
	get_tree().change_scene("res://Scenes/CreditScenes.tscn")
	return

func _on_ButtonMulti_pressed():
	get_tree().change_scene("res://Scenes/CreditScenes.tscn")
	return

func _on_ButtonCredit_pressed():
	get_tree().change_scene("res://Scenes/CreditScenes.tscn")
	return

func _on_ButtonQuit_pressed():
	OS.kill(OS.get_process_id())
	return

func _on_ButtonQuit2_pressed():
	get_tree().quit()
	return
