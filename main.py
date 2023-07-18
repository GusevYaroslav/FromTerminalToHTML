import filehandling as fhl

print("===============================================================================================================")
print("========================================= FromTerminalToHTML===================================================")
print("===============================================================================================================")

print("type h for help")

while True:
    inn = input(">>>")

    if inn == 'h' or inn == 'help':
        print('''
=====================================
h(help) - get help
n(new) - create a new file
i(info) - get help about the program
=====================================
        ''')

    elif inn == 'n' or inn == 'new':
        print("++ file mode ++")

        new_file_name = input("Enter file name: ")
        fhl.file_open(new_file_name)

        print(f'++ {new_file_name} file editing. ++')
        print('''
Commands for writing to a file:

t - text 
tl - text & link
img - image
h - header

exit - leave edit mode
            ''')

        print("\n")

        while True:
            lnn = input(">>>")

            if lnn == 't':
                print('You can fill in the file like this: [your_text]')
                text = input(">>>")
                fhl.text_write(text)
                print("successfully\n")

            elif lnn == 'tl':
                print('You can fill in the file like this: [your_text] [your_link]')
                text, link = map(input(">>>").split())
                fhl.link_write(text, link)
                print("successfully\n")

            elif lnn == 'img':
                print('Enter the path to the image:')
                path = input(">>>")
                fhl.image_write(path)
                print("successfully\n")

            elif lnn == 'h':
                print('You can fill in the file like this: [your_header]')
                text = input(">>>")
                fhl.header_write(text)
                print("successfully\n")

            elif lnn == 'exit':
                fhl.file_close()
                print("You have exited the write mode\n")
                break

    elif inn == 'i' or inn == 'info':
        print('''
From Terminal To HTML
        
Version - b.0.1
Date - 18.07.2023
Python 3.10.9

(c)Gusev Yaroslav
email - gusevyaroslaveggg666@gmail.com

        ''')

