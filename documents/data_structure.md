# Game Manager - Data Structure

## Games (class, instances stored in library)

Variable        | Type      | Unit/Entry
----------------|-----------|-----------
self.id         | string    | game_%Y%m%d%H%M%S%f
self.name       | string    | required
self.details:
*min_num_players* | int       | >= 1
*max_num_players* | int       | >= min_num_players
*min_duration*    | int       | minutes, >= 1
*max_duration*    | int       | minutes, >= min_duration
*min_age*         | int       | years, >= 1
*complexity*      | int-range | 1 - NUM_POINTS
*difficulty*      | int-range | 1 - NUM_POINTS
*topic*           | string    | Fantasy, Science Fiction, Real World, Abstract, Adaptation, other
*skills*          | string    | Logics, Dexterity, Intuition, Creativity, Knowledge, Strategy, Negotiation, Luck, Roleplay
*physical_form*   | string    | board, cards, dice, supplementals, other
*social_type*     | string    | cooperative, 1_v_all, teams, all_v_all, *other*

## Library (dictionary storing games, saved in file library.gm)

Keys:   string, name of the game (ensured to be equal to the name of the game objects)

Values: instance of class game (given the id and name by the library)

## History (df saved in file history.gmhist)
Variable        | Type     | Unit/Entry
----------------|----------|-----------
hist_ID         | string   | hist_%Y%m%d%H%M%S%f  
game_ID         | string   | game_%Y%m%d%H%M%S%f
date            | datetype |   
num_players     | int      | >= 1
duration        | int      | minutes
rating          | int      | 1 - NUM_POINTS
comment         | string   |   
