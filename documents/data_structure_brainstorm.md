# Data Structure

## Games
Variable        | Type   | Unit/Entry
----------------|--------|-----------
name            | string | 
ID              | string | game_%Y%m%d%H%M%S%f
min_num_players | int    |
max_num_players | int    |
min_duration    | int    | minutes
max_duration    | int    | minutes
min_age         | int    | years
complexity      | int    | 1 - NUM_POINTS
difficulty      | int    | 1 - NUM_POINTS
topic           | string | Fantasy, Science Fiction, Real World, Abstract, Adaptation, other
skills          | string | Logics, Dexterity, Intuition, Creativity, Knowledge, Strategy, Negotiation, Luck, Roleplay
physical_parts  | string | board, cards, dice, supplementals, other
social_type     | string | cooperative, 1_v_all, teams, all_v_all, other

## History
Variable        | Type     | Unit/Entry
----------------|----------|-----------
name            | string   |   
ID              | string   | game_%Y%m%d%H%M%S%f
date            | datetype |   
players         | int      | 
rating          | int      | 1 - NUM_POINTS
comment         | string   |   
