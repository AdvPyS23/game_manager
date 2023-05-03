# Data Structure

## Games
Variable        | Type   | Unit/Entry
----------------|--------|-----------
name            | string | required
ID              | string | game_%Y%m%d%H%M%S%f
min_num_players | int    | >= 1
max_num_players | int    | >= min_num_players
min_duration    | int    | minutes
max_duration    | int    | minutes
min_age         | int    | years, >= 1
complexity      | int    | 1 - NUM_POINTS
difficulty      | int    | 1 - NUM_POINTS
topic           | string | Fantasy, Science Fiction, Real World, Abstract, Adaptation, other
skills          | string | Logics, Dexterity, Intuition, Creativity, Knowledge, Strategy, Negotiation, Luck, Roleplay
physical_parts  | string | board, cards, dice, supplementals, other
social_type     | string | all_v_all, cooperative, one_v_all, teams, other

## History
Variable        | Type     | Unit/Entry
----------------|----------|-----------
hist_ID         | string   | hist_%Y%m%d%H%M%S%f  
game_ID         | string   | game_%Y%m%d%H%M%S%f
date            | datetype |   
num_players     | int      | >= 1
duration        | int      | minutes
rating          | int      | 1 - NUM_POINTS
comment         | string   |   
