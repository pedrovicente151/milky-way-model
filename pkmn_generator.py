
def get_pkmn_info():
    evs_list = []
    evs_converted = ""
    moves = []

    pkmn_name = input("Pokemon Name: ")
    pkmn_gender = input("Pokemon Gender (M/F): ")
    item = input("Pokemon Item: ")
    shiny = input("Shiny? (Yes/No): ")

    hp_EVs = input("HP EVs: ")
    atk_EVs = input("Attack EVs: ")
    def_EVs = input("Defense EVs: ")
    spA_EVs = input("Sp.Atk EVs: ")
    spD_EVs = input("Sp.Def EVs: ")
    spe_EVS = input("Speed EVs: ")

    if hp_EVs != "0":
        evs_list.append(f"{hp_EVs} HP")
    if atk_EVs != "0":
        evs_list.append(f"{atk_EVs} Atk")
    if def_EVs != "0":
        evs_list.append(f"{def_EVs} Def")
    if spA_EVs != "0":
        evs_list.append(f"{spA_EVs} SpA")
    if spD_EVs != "0":
        evs_list.append(f"{spD_EVs} SpD")
    if spe_EVS != "0":
        evs_list.append(f"{spe_EVS} Spe")

    for ev in evs_list:
        evs_converted += f"{ev} / "

    evs_converted = evs_converted[:-2]

    ability = input("Ability: ")
    level = input("Level: ")
    nature = input("Nature: ")

    move_one = input("Move One: ")
    move_two = input("Move Two: ")
    move_three = input("Move Three: ")
    move_four = input("Move Four: ")

    moves_str = f"- {move_one} - {move_two} - {move_three} - {move_four}"

    final_command = f"!bdsptrade {pkmn_name} ({pkmn_gender}) @ {item} Shiny: {shiny} EVs: {evs_converted}" \
                    f"Ability: {ability} Level: {level} {nature} Nature {moves_str}"

    print(final_command)

if __name__ == '__main__':
    get_pkmn_info()