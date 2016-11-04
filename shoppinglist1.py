store_dict = {"Whole Foods" : ["apples", "oranges", "bananas"], 
            "Safeway" : ["dish soap", "cereal", "watermelon"],
            "Trader Joe's" : ["potstickers", "chocolate", "lentils"],
            "Sprouts" : ["pretzels", "broccoli", "coffee"] }

def display_menu():
    print """
    Hello welcome to the main menu.  Please select an option.  
    0 for Main Menu, 
    1 to Show all lists, 
    2 to Show a specific list, 
    3 to Add a new shopping list, 
    4 to Add an item to a shopping list,
    5 to Remove an item from a shopping list,
    6 to Remove a list by nickname,
    7 to Exit when you are done
    """
def menu_choice():
    choice = 2 #int(raw_input("Press a number between 0 and 7."))
    return choice 

def show_all_lists():
    print store_dict

def show_specific_list():
    list_choice = "Whole Foods" #raw_input("What list would you like to see?")
    if list_choice in store_dict:
        print store_dict[list_choice] 
    # elif list_choice == "Safeway":
    #     print store_dict[l]
    # elif list_choice == "Trader Joe's":
    #     print store_dict["Trader Joe's"]
    # elif list_choice == "Sprouts":
    #     print store_dict["Sprouts"]
    else:
        print "Make another choice." 
                                
def add_new_shopping_list():
    #ratings['subway'] = 8
    new_store_name = "Ann's" #raw_input("Ok, where are you shopping?")
    # new_items = "art" #raw_input("Enter one item you'd

    store_dict[new_store_name] = []
    return store_dict

def add_new_item(store):
    list_choice = store 
    new_items = "art" #raw_input("Enter one item you'd like to buy.") 
    store_dict[list_choice].append(new_items)
    return store_dict   


def main():
    # display_menu()
    # user_choice = menu_choice()
    # print user_choice
    # print show_specific_list()
    print add_new_shopping_list()
    print add_new_item("Ann's")





if __name__ == '__main__':
    main()
