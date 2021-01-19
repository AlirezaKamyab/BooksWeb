#This is for managing the database
from .models import Book

def AddBook(request):
    try:
        newBook = Book()
        newBook.BookName = request.POST['BookName']
        newBook.Author = request.POST['Author']
        newBook.Pages = request.POST['Pages']
        newBook.Rating = request.POST['Rating']
        newBook.Checked = True if len(request.POST.getlist('Checked')) == 1 else False
        if request.user.is_authenticated : 
            newBook.user = request.user
        else: 
            return False

        newBook.save()
        return True

    except: return False

def GetBookByUser(account):
    try:
        if account.is_authenticated:
            lst = Book.objects.filter(user=account)
            return lst
        else: return []
    except: return []

def RemoveItemById(id):
    try:
        book = Book.objects.get(pk=id)
        book.delete()
        return True
    except:
        return False

def BooksRead(username):
    try:
        counter = 0
        all = 0
        book = Book.objects.filter(user=username)
        for i in book:
            if i.Checked: counter += 1
            all += 1
        else: return all, counter
    except:
        return 0, 0