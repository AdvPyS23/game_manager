# Data Structure

## Games
Variable        | Type      | Unit/Entry
----------------|-----------|-----------
name            | string    | 
ID              | string    | game_%Y%m%d%H%M%S%f
min_num_players | int       |
max_num_players | int       |
min_duration    | int       | minutes
max_duration    | int       | minutes
min_age         | int       | years
complexity      | int-range | 1 - NUM_POINTS
difficulty      | int-range | 1 - NUM_POINTS
topic           | choice    | Fantasy, Science Fiction, Real World, Abstract, Adaptation, other
skills          | choice    | Logics, Dexterity, Intuition, Creativity, Knowledge, Strategy, Negotiation, Luck, Roleplay
physical_parts  | choice    | board, cards, dice, supplementals, other
social_type     | choice    | cooperative, 1_v_all, teams, all_v_all, other


## Collection
Variable        | Type      | Unit/Entry
----------------|-----------|-----------


## History
Variable        | Type      | Unit/Entry
----------------|-----------|-----------
name            | string    |   
ID              | string    | history_%Y%m%d%H%M%S%f
date            | datetype  |   
players         | int       | 
rating          | int-range | 1 - NUM_POINTS
comment         | string    |   
