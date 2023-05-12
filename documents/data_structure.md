# Game Manager - Data Structure

## Games (class, stored in collection df saved in file *Collection*.gmlib)

Variable        | Type      | Unit/Entry
----------------|-----------|-----------
ID              | string    | game_%Y%m%d%H%M%S%f
name            | string    | required
min_num_players | int       | >= 1
max_num_players | int       | >= min_num_players
min_duration    | int       | minutes, >= 1
max_duration    | int       | minutes, >= min_duration
min_age         | int       | years, >= 1
complexity      | int-range | 1 - NUM_POINTS
difficulty      | int-range | 1 - NUM_POINTS
topic           | string    | Fantasy, Science Fiction, Real World, Abstract, Adaptation, other
skills          | string    | Logics, Dexterity, Intuition, Creativity, Knowledge, Strategy, Negotiation, Luck, Roleplay
physical_parts  | string    | board, cards, dice, supplementals, other
social_type     | string    | cooperative, 1_v_all, teams, all_v_all, other

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
