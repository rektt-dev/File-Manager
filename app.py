import os
def create_file(filename): #defining function to create file
    try:
        with open(filename,'x') as f:
            print(f'File {filename} Created Successfully! ')
    except FileExistsError:
        print(f'File {filename} already exists! ') 
    except Exception as E:
        print("An Error Occured ")

def view_all_files(): #defining function to view all files present
    files = os.listdir()
    if not files:
        print("No file found")
    else:
        for file in files:
            print(file)
            
def delete_file(filename): #defining function to delete mentioned file
    try:
        os.remove(filename)
        print(f"File {filename} has been removed successfully !")
        
    except FileNotFoundError:
        print('File not Found !')
    except Exception as e:
        print("An error Occured")

def read_file(filename): #defining function to read a file
    try:
        with open(filename, 'r')as f:
            content = f.read()
            print(f'The contents of {filename} are - \n')
            print(content)
            
    except FileNotFoundError:
        print(f'{filename} does not exist')
    except Exception as e:
        print("An Error Occured !")

def edit_file(filename): #defining function to edit a file
    try:
        with open(filename,'a') as f:
            content = input('Enter data to add -')
            f.write(content + "\n")
            print(f'content added to {filename} successful')
           
    except FileNotFoundError:
        print(f'{filename} does not exist')
    except Exception as e:
        print("An Error Occured !")

def main(): #main function
    while True:
        print()
        print()
        print()
        print()
        print("--------FILE MANAGEMENT APP--------")
        print('1.Create file')
        print('2.View all files')
        print('3.Delete file')
        print('4.Read file')
        print('5.Edit file')
        print('6.Exit')
        print('------------------------------------')

        choice = input('Enter your choice (1-6):')
        
        if choice == '1':
            filename= input('Enter the file-name to create = ')
            create_file(filename)

        elif choice == '2':
            view_all_files()
            
        elif choice == '3':
            filename = input('Enter the name of file you want to delete ')
            delete_file(filename)

        elif choice == '4':
            filename = input('Enter file-name to read -  ')
            read_file(filename)

        elif choice =='5':
            filename = input('Enter file name to edit -  ')
            edit_file(filename)   
        
        elif choice == '6':
            print('Closing the app........')
            break

        else:
            print('Invalid Choice')

if __name__ == "__main__" :
    main()            

        
