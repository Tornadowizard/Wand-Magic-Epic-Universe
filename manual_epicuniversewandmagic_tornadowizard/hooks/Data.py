# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:

	return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:

	# A list of Universal Character Names and a list of all vowels
	character_names = ["Cosme Acajor", "Newt Scamander", "Ringmaster Skender"]
	is_vowel = ["a", "e", "i", "o", "u"]

	# A list of other Universal Items that can be inserted as junk
	possible_filler_names = ["Lanyard", "Loungefly", "Decorative Popcorn Bucket", "Broken Wand"]

	# if the character name starts with a vowel, ad An + Pin, otherwise add A + Pin, and then add it to the list.
	for character in character_names:
		if character[0].lower() in is_vowel:
			choice = "An " + character + " Pin"
			possible_filler_names.append(choice)
		else:
			choice = "A " + character + " Pin"
			possible_filler_names.append(choice)

	# add each filler name to the filler list
	for filler_name in possible_filler_names:
		item_table.append({
			'name': filler_name,
			'category': [],
			'filler': True, # capitalized in Python, not in JSON
			'count': 0, # we want the items defined only so we can add it
			'metadata': {} # we have no metadata because we made this item up
		})

	return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
	return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:






	return location_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
	return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
	return category_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
	return meta_table

# called when an external tool (eg Univeral Tracker) ask for slot data to be read
# use this if you want to restore more data
# return True if you want to trigger a regeneration if you changed anything
def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> bool:
	return False
