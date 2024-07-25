import requests
import streamlit as st
@st.cache_data
def get_pokemon_data(name):
    pokedata = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/").json()
    abilities = pokedata["abilities"]
    stats = pokedata["stats"]
    types = pokedata["types"]
    sprites = pokedata["sprites"]
    master_list = [[],[],[],[],{}] #natural abilities, hidden abilities, stats, types sprites
    for ability in abilities:
        new_ability = {}
        new_ability["name"] = ability["ability"]["name"]
        ability_response = requests.get(ability['ability']['url']).json()
        new_ability['description'] = ability_response["effect_entries"][1]["effect"]
        if(ability['is_hidden']):
            master_list[1].append(new_ability)
        else:
            master_list[0].append(new_ability)
    for type in types:
        master_list[3].append(type["type"]["name"].title())
    for stat in stats:
        master_list[2].append({stat["stat"]["name"]:stat["base_stat"]})
    for sprite in sprites:
        if sprite == "front_default" and sprites[sprite]:
            reformatted = sprite.replace("_", " ")
            reformatted=reformatted[6:]
            master_list[4][reformatted] = sprites[sprite]
        elif sprite == "front_female" and sprites[sprite]:
            reformatted = sprite.replace("_", " ")
            reformatted=reformatted[6:]
            master_list[4][reformatted] = sprites[sprite]
        elif sprite == "front_shiny" and sprites[sprite]:
            reformatted = sprite.replace("_", " ")
            reformatted=reformatted[6:]
            master_list[4][reformatted] = sprites[sprite]
        elif sprite == "front_shiny_female" and sprites[sprite]:
            reformatted = sprite.replace("_", " ")
            reformatted=reformatted[6:]
            master_list[4][reformatted] = sprites[sprite]
            

    return master_list
def display_pokemon_data(master_list, name):
    st.title(name)
    types = "**Types**: "
    for i in range (len(master_list[3])-1):
        types+=master_list[3][i]+', '
    types+=master_list[3][len(master_list[3])-1]
    st.write(types)
    for sprite in master_list[4]:
        st.image(master_list[4][sprite])
        st.caption(sprite.title())
    st.header("Abilities")
    st.subheader("Natural Abilities:")
    for ability in master_list[0]:
        st.subheader(ability["name"].title(),":")
        st.write(ability["description"])
    st.subheader("Hidden Abilities:")
    for ability in master_list[1]:
        st.subheader(ability["name"].title(),":")
        st.write(ability["description"])
    st.header("Stats:")
    for stat in master_list[2]:
        for key in stat:
            st.write(f"{key.title()}: {stat[key]}")

st.text_input("type a Pokemon's name", key = "name")
try:
    display_pokemon_data(get_pokemon_data(st.session_state.name.lower()), st.session_state.name.title())
except Exception as e: 
    st.error("Please select a pokemon")