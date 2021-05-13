import urllib
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    list = book_to_words()
    largest = 0
    for i in list:
        if len(i) > largest:
            largest = len(i)
    largest *= -1

    for i in range(-1, largest-1, -1):
        list = counting_sort(list, i)
    return list    

def counting_sort(lst, idx):
    list = [0 for i in lst]
    res = ['' for i in lst]
    size = [0 for i in range (128)]

    for i in lst:
        if len(i) >= -idx:
            size[i[idx]] += 1
        else:
            size[0] += 1
    
    for i in range (128):
        size[i] += size[i-1]

    for i in range (len(lst)-1, -1, -1):
        if -idx <= len(lst[i]):
            list[size[lst[i][idx]]-1] = lst[i]
            size[lst[i][idx]] -= 1
        else:
            list[size[0]-1] = lst[i]
            size[0] -= 1

    for i in range(len(lst)):
        res[i] = list[i]
    return res

def test_book(link='https://www.gutenberg.org/files/84/84-0.txt'):
    r_sort_lst = radix_a_book(link)
    print(r_sort_lst[:20], r_sort_lst[1000:1020], r_sort_lst[10000:10020], r_sort_lst[70000:70020], r_sort_lst[-20:], sep='\n')    

def main():
    test_book() # frankenstein
    test_book('https://www.gutenberg.org/files/2701/2701-0.txt') # moby dick
    test_book('https://www.gutenberg.org/files/4300/4300-0.txt') # ulysses (last words are pretty funny)
    test_book('https://www.gutenberg.org/files/345/345-0.txt') # dracula
    
    test_list_1 = [b'Act', b'Bear', b'Cat', b'125', b'Dog', b'it', b'the']
    for i in range(-1, -len('bear') -1, -1):
        test_list_1 = counting_sort(test_list_1, i)
        print(test_list_1) 


main()