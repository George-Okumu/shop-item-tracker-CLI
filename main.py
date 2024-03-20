from cli_methods import menu, exit, print_all_items, print_all_categories


class welcome():
    print("Welcome to myduka stock tracker, what do you want to do today?")
    
    def main():
        while True:
            
            menu()
            choice = input("> ")
            if choice == "0":
                exit()
            elif choice == "1":
                print_all_items()
            elif choice == "2":
                print_all_categories()
            else:
                print("Invalid choice")



    if __name__ == "__main__":
        main()