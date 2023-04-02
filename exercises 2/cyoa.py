"""Chose Your Own Adventure !"""
__author__ = "730605138"
import random
NAMED_CONSTANT = "\U0001f600"
Questions: dict = {}
Questions.update({"Do You Like Spring?": {"1": ["Cadbury Creme Egg", "Starburst Jelly Beans", "Robins Eggs", "Peeps Chick", "Cadbury Mini Eggs"], "0": ["Reese's Egg", "Chocolate Bunny", "Easter Candy Corn"]}, 
                  "Are You Allergic To Peanut Butter?": {"1": ["Cadbury Creme Egg", "Starburst Jelly Bean", "Robins Eggs", "Chocolate Bunny", "Peeps Chick", "Cadbury Mini Eggs", "Easter Candy Corn"], "0": ["Reese's Egg"]},
                  "Do you enjoy spending time outdoors in spring?": {"1": ['Cadbury Mini Eggs', 'Starburst Jelly Bean', "Reese's Egg", 'Peeps Chick'], "0": ['Cadbury Creme Egg', 'Easter Candy Corn', 'Robins Eggs', 'Chocolate Bunny']},
                  "Would you rather spend spring in a city or in the countryside?": {"1": ['Chocolate Bunny', 'Robins Eggs', 'Cadbury Mini Eggs', 'Peeps Chick'], "0": ['Starburst Jelly Bean', 'Cadbury Creme Egg', "Reese's Egg", 'Easter Candy Corn']},
                  "Is spring your favorite season?": {"1": ['Robins Eggs', "Reese's Egg", 'Peeps Chick', 'Chocolate Bunny'], "0": ['Robins Eggs', 'Easter Candy Corn', 'Cadbury Mini Eggs', 'Peeps Chick']},
                  "Do you enjoy gardening in the spring?": {"1": ['Cadbury Mini Eggs', 'Cadbury Creme Egg', 'Robins Eggs', 'Peeps Chick'], "0": ['Robins Eggs', 'Cadbury Creme Egg', "Reese's Egg", 'Easter Candy Corn']},
                  "Do you prefer warm or cool spring weather?": {"1": ['Chocolate Bunny', 'Cadbury Creme Egg', "Reese's Egg", 'Starburst Jelly Bean'], "0": ['Cadbury Mini Eggs', 'Easter Candy Corn', 'Robins Eggs', 'Peeps Chick']},
                  "Would you rather go on a spring picnic or attend a spring festival?": {"1": ['Cadbury Creme Egg', 'Robins Eggs', 'Chocolate Bunny', "Reese's Egg"], "0": ['Robins Eggs', 'Chocolate Bunny', "Reese's Egg", 'Cadbury Creme Egg']},
                  "Do you enjoy spring cleaning your home?": {"1": ['Easter Candy Corn', 'Peeps Chick', "Reese's Egg", 'Cadbury Creme Egg'], "0": ['Starburst Jelly Bean', 'Cadbury Mini Eggs', 'Chocolate Bunny', 'Robins Eggs']},
                  "Is spring your preferred season for hiking and outdoor activities?": {"1": ['Chocolate Bunny', 'Starburst Jelly Bean', 'Peeps Chick', "Reese's Egg"], "0": ['Robins Eggs', 'Cadbury Mini Eggs', 'Easter Candy Corn', 'Cadbury Creme Egg']},
                  "Do you prefer wearing light jackets or heavy coats in spring?": {"1": ['Cadbury Mini Eggs', 'Robins Eggs', 'Cadbury Creme Egg', 'Chocolate Bunny'], "0": ['Peeps Chick', "Reese's Egg", 'Starburst Jelly Bean', 'Easter Candy Corn']},
                  "Would you rather take a spring vacation to the beach or the mountains?": {"1": ['Starburst Jelly Bean', 'Robins Eggs', 'Easter Candy Corn', 'Peeps Chick'], "0": ['Cadbury Creme Egg', 'Chocolate Bunny', 'Cadbury Mini Eggs', "Reese's Egg"]},
                  "Do you enjoy seeing the cherry blossoms in spring?": {"1": ["Reese's Egg", 'Easter Candy Corn', 'Cadbury Creme Egg', 'Robins Eggs'], "0": ['Peeps Chick', 'Cadbury Mini Eggs', 'Starburst Jelly Bean', 'Chocolate Bunny']},
                  "Is spring the best time for photography in your opinion?": {"1": ['Chocolate Bunny', 'Cadbury Creme Egg', 'Robins Eggs', 'Cadbury Mini Eggs'], "0": ["Reese's Egg", 'Easter Candy Corn', 'Peeps Chick', 'Starburst Jelly Bean']},
                  "Would you rather go on a spring road trip or a spring cruise?": {"1": ['Robins Eggs', 'Chocolate Bunny', "Reese's Egg", 'Peeps Chick'], "0": ['Cadbury Creme Egg', 'Robins Eggs', 'Chocolate Bunny', 'Easter Candy Corn']},
                  "Do you enjoy cooking with seasonal spring produce?": {"1": ["Reese's Egg", 'Peeps Chick', 'Cadbury Mini Eggs', 'Starburst Jelly Bean'], "0": ['Cadbury Mini Eggs', 'Robins Eggs', 'Peeps Chick', "Reese's Egg"]},
                  "Do you prefer spring colors like pastels or brighter hues?": {"1": ['Cadbury Mini Eggs', "Reese's Egg", 'Peeps Chick', 'Easter Candy Corn'], "0": ["Reese's Egg", 'Cadbury Mini Eggs', 'Easter Candy Corn', 'Peeps Chick']},
                  "Do you enjoy spring sports like baseball or soccer?": {"1": ['Chocolate Bunny', 'Cadbury Creme Egg', 'Robins Eggs', "Reese's Egg"], "0": ["Reese's Egg", 'Chocolate Bunny', 'Robins Eggs', 'Cadbury Creme Egg']},
                  "Is spring your preferred season for camping?": {"1": ["Reese's Egg", 'Chocolate Bunny', 'Robins Eggs', 'Cadbury Creme Egg'], "0": ['Starburst Jelly Bean', 'Easter Candy Corn', 'Robins Eggs', 'Peeps Chick']},
                  "Would you rather go on a spring hike or a spring bike ride?": {"1": ['Cadbury Mini Eggs', "Reese's Egg", 'Chocolate Bunny', 'Cadbury Creme Egg'], "0": ['Peeps Chick', "Reese's Egg", 'Cadbury Creme Egg', 'Starburst Jelly Bean']},
                  "Do you prefer spring weather to summer weather?": {"1": ['Cadbury Mini Eggs', 'Robins Eggs', 'Chocolate Bunny', 'Easter Candy Corn'], "0": ['Easter Candy Corn', 'Robins Eggs', 'Cadbury Creme Egg', 'Peeps Chick']},
                  "Is spring your preferred time for romantic walks?": {"1": ['Chocolate Bunny', 'Easter Candy Corn', 'Peeps Chick', "Reese's Egg"], "0": ['Robins Eggs', 'Easter Candy Corn', 'Chocolate Bunny', "Reese's Egg"]}})
candy_dic: dict = {}
player: str = ""
points: int = 0


def main() -> None:
    """Main Function !"""
    global points
    points = 0
    global candy_dic
    global player
    player = ""
    greet()
    dict_builder()
    done: bool = True
    while done:
        print(f"your points are {points}")
        point_multiplier: str = input("Do you want to do a point multiplier? 1 : Yes, 0 : No ")
        type_check: bool = True
        if point_multiplier not in ["1", "0"]:
            while type_check:
                point_multiplier = input("Do you want to do a point multiplier? 1 : Yes, 0 : No ")
                if point_multiplier in ["1", "0"]:
                    type_check = False

        if point_multiplier == "1":
            number_multiplier: str = input("What would you like the number multiplier to be? ")
            type_check = True
            if not number_multiplier.isnumeric():
                while type_check:
                    number_multiplier = input("what would you like the number multiplier to be? enter an integer ")
                    if number_multiplier.isnumeric():
                        type_check = False
            points = custom_function(number_multiplier, points)
        else:
            custom_procedure()
        potentially_done: str = input("are you done with the game? 1 : Yes, 0 : No ")
        type_check = True
        if potentially_done not in ["1", "0"]:
            while type_check:
                potentially_done = input("are you done with the game? 1 : Yes, 0 : No ")
                if potentially_done in ["1", "0"]:
                    type_check = False
        if potentially_done == "1":
            done = False
            print(f"You are a {max(candy_dic, key=candy_dic.get)}, {NAMED_CONSTANT}")
    return


def greet() -> None:
    """Greet Function!"""
    print("Welcome to which Easter Candy are You!")
    global player 
    player = input("What is Your name! ")
    print(f"I hope You enjoy the quiz {player}")
    return


def custom_procedure() -> None:
    """Custom Procedure! Asks a question and records answer and adds 1 to all values of keys that apply!"""
    question: dict = Questions.popitem()
    print(question[0])
    yes_no: str = input(f"{player} please enter 1 for yes or first option and 0 for no or second option")
    type_check: bool = True
    if yes_no not in ["1", "0"]:
        while type_check:
            yes_no = input("please enter a number 1 or 0")
            if yes_no in ["1", "0"]:
                type_check = False
    for i in question[1].get(yes_no):
        candy_dic[i] += 1
    global points
    points += 1
    return points


def custom_function(x: int, point: int) -> int:
    """Custom Function!takes in an x and multiplies the change in values to candy dic!"""
    question: dict = Questions.popitem()
    print(question[0])
    yes_no: str = input(f"{player} please enter 1 for yes or first option and 0 for no or second option")
    type_check: bool = True
    if yes_no not in ["1", "0"]:
        while type_check:
            yes_no = input("please input a number 1 or 0")
            if yes_no in ["1", "0"]:
                type_check = False
    for i in question[1].get(yes_no):
        candy_dic[i] += (1 * int(x))
    point += 1
    return point * random.randint(1, 10)


def dict_builder() -> None:
    """Builds dictionary in which the score for every candy is kept!"""
    candy_list: list[str] = ["Cadbury Creme Egg", "Reese's Egg", "Starburst Jelly Bean", "Robins Eggs", "Chocolate Bunny", "Peeps Chick", "Cadbury Mini Eggs", "Easter Candy Corn"]
    global candy_dic
    for i in candy_list:
        candy_dic[i] = 0
    return


if __name__ == "__main__":
    main()
