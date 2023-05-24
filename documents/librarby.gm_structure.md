CSV format:

"id","name","details"


"details" =
min_num_players,
max_num_players,
min_duration,
max_duration,
min_age,
complexity,
difficulty,
topic,
skills,
physical_form,
social_type

Ex.: "4,6,45,60,14,6,7,12,29,01,1"



id	--> wozu? wo gespeichert? wenn neues game object aus library geladen?
	--> nur eintrag in library? Oder ganz weglassen, und nur name gebrauchen?

FRAGE: UMBENENNEN ?

Vermutlich: ID = unänderbar, aber gemacht, wenn in library eingetragen, NICHT wenn Objekt generiert...
Name: änderbar (aber zwingend einzigartig)
--> umbenennen = neuer Eintrag in library mit der gleichen ID (& details), aber neuem Namen --> alten löschen