def palindrome_checker():
    while True:
        print('\nWelcome! Please enter a sentence, and I will check if it is a palindrome or not.')

        CHECK = str(input())

        if CHECK == CHECK[::-1]:
            print('\nYay, it\'s a palindrome!')
        else:
            print('\nNo, it\'s not a palindrome.')

        play_again = input('Do you want to check another sentence? (yes/no): ').lower()
        if play_again != 'yes':
            print('Goodbye!')
            break

palindrome_checker()
