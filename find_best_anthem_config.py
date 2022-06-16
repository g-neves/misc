'''
PT: 
Em uma estrada existem n edificações, cada uma localizada no km eᵢ. 
Você precisa instalar antenas de celular ao longo dessa estrada, de 
forma que nenhuma edificação fique a mais de k km de distância de uma antena.
Faça um programa que encontre o menor número de antenas necessárias.

EN:
In a road there are n buildings, each one located at km eᵢ. You
need to install cellphone anthems along the road, in a way that neither building
stands more than k km from at least one anthem.
Create a program that finds the minimum number of needed anthems.
'''

# buildings = [e0, e1, e2, e3, e4, ..., eN]


def create_building_range(building_position, k):
    """Returns a tuple with the available range for an anthem to be built"""
    return building_position - k, building_position + k 


def find_best_anthem_config(buildings_list, k):
    # Creates the ranges for each building
    buildings_ranges = [create_building_range(building, k) for building in buildings_list]
 
    anthems_positions = [] 
    last_anthem_position = None
    for idx, building_range in enumerate(buildings_ranges):
        if last_anthem_position is None:
            anthems_positions.append(building_range[1])
            last_anthem_position = building_range[1]
            continue 
        if building_range[0] < last_anthem_position:
            continue
        else:
            anthems_positions.append(building_range[1])
            last_anthem_position = building_range[1]
            continue

    return anthems_positions


def check_solution(buildings_list, anthems_positions):
    """Checks if the solution is right"""
    for building in buildings_list:
        is_building_covered = False
        for anthem in anthems_positions:
            if abs(building - anthem) <= 30:
                is_building_covered = True 
        
        if not is_building_covered:
            return False

    return True

if __name__ == '__main__':
    k = 30
    buildings_list = list({10, 20, 30, 40, 80, 90, 110, 190, 200, 230, 250, 300})
    buildings_list.sort()
    anthems_positions = find_best_anthem_config(buildings_list, k)

    assert check_solution(buildings_list, anthems_positions)
    print("Buildings list:")
    print(buildings_list)
    print("Anthems positions:")
    print(anthems_positions)



