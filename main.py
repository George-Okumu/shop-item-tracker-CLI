from cli_methods import menu, exit, print_all_items, print_all_categories, get_item_details_from_cli, get_category_details_from_cli


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
            elif choice == "3":
                get_category_details_from_cli()
            elif choice == "4":
                get_item_details_from_cli()
            else:
                print("Invalid choice")
                
    main()