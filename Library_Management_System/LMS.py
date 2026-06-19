# Library Management System

books=[]

def add_book():
    book_id=(int(input("Enter book ID: ")))
    title=input("Enter Book title: ")
    author=input("Enter Author's name: ")
    genre=input("Enter genre: ")
    status="Available"
    for b in books:
        if b['id']==book_id:
            print("Book already exists!")
            return
    books.append({"id":book_id,"title":title,"author":author,"genre":genre,"status":status})

    print("Book added successfully")

def view_books():
    if not books:
        print("No record for books found")
    else:
        for b in books:
            print(f"Title : {b['title']}, ID : {b['id']}, Author : {b['author']}, Genre : {b['genre']} ,Status : {b['status']}")

def search_book():
    search_id=int(input("Enter book id: "))
    for b in books:
        if(b['id']==search_id):
            print(f"Title : {b['title']}, ID : {b['id']}, Author : {b['author']}, Genre : {b['genre']} ,Status : {b['status']}")
            return
    print(f"Book {search_id} not found!!")

def issue_book():
    search_id=int(input("Enter book id: "))
    for b in books:
        if b['id']==search_id:
            if b['status'].lower()=="available":
                b['status']="Issued"
                print("Book issued successfully")
                return
            else:
                print("Book already issued")
                return
    print(f"Book {search_id} not found!!")

def return_book():
    search_id=int(input("Enter book id: "))
    for b in books:
        if b['id']==search_id:
            if b['status'].lower()=="issued":
                b['status']="Available"
                print("Book returned successfully")
                return
            else:
                print("Book was not issued")
                return
    print(f"Book {search_id} not found!!")

def delete_book():
        search_id=int(input("Enter book id: "))
        for b in books:
            if(b['id']==search_id):
                Confirmation=input("Do you want to delete the book?")
                if(Confirmation.lower()=="y"):
                    books.remove(b)
                    print("Book deleted successfully")
                    return
                else:
                    print("Book not deleted")
                    return
        print(f"Book {search_id} not found!!")

def library_statistics():
    total_books=len(books)
    books_issued=sum(1 for b in books if b['status'].lower()=="issued")
    available_books=total_books-books_issued

    print(f"Total books: {total_books}")
    print(f"Issued Books: {books_issued}")
    print(f"Available books: {available_books}")

def sort_books():
    sorted_list=sorted(books,key=lambda x:x['id'])
    for b in sorted_list:
        print(f"Title : {b['title']}, ID : {b['id']}, Author : {b['author']}, Status : {b['status']}")

def main():
    while True:
        print("\n---Library Management System---")
        print("********************")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Library Statistics")
        print("8. Sort Books")
        print("9. Exit")
        print("********************")

        choice=int(input("Enter your choice: "))
        if choice==1:
            add_book()
        elif choice==2:
            view_books()
        elif choice==3:
            search_book()
        elif choice==4:
            issue_book()
        elif choice==5:
            return_book()
        elif choice==6:
            delete_book()
        elif choice==7:
            library_statistics()
        elif choice==8:
            sort_books()
        elif choice==9:
            break
        else:
            print("Invalid choice, please try again.")

if __name__=="__main__":
    main()