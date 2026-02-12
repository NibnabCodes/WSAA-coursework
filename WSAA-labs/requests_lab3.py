# Write the code to get the books from http://andrewbeatty1.pythonanywhere.com/books 
import requests 
import json 
url = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url) 

def getAllBooks():
    response = requests.get(url)
    return response.json()

# Convert that into a function and call it from inside a if __name__ == “__main__”:
def readbooks():
    response = requests.get(url)
    response.raise_for_status()  # checks for HTTP errors
    return response.json()
    
# Write the function for find by id and test it (you need to write the testing code) 
def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    print(f"Status code:", {response.status_code})
    print(f"Response text:", {response.text})
    response.raise_for_status()
    return response.json()

# write the code to create and test it (you need to write your own testing code) 
def createbook(book):
    response = requests.post(url, json=book)

    # 201 = Created (expected for POST)
    if response.status_code != 200:
        raise Exception(
        f"Failed to create book "
        f"(Status: {response.status_code}) "
        f"Response: {response.text}"
    )
    
    return response.json()

# Write the update function
def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)

    if response.status_code != 200:
        raise Exception(
            f"Failed to update book "
            f"(Status: {response.status_code}) "
            f"Response: {response.text}"
        )
    return response.json()

# Write the delete function 
def deletebook(id): 
    deleteurl = url + "/" + str(id) 
    response = requests.delete(deleteurl)
    
    if response.status_code != 200:
        raise Exception(
            f"Failed to update book "
            f"(Status: {response.status_code}) "
            f"Response: {response.text}"
        )
        
    return response.json() 

if __name__ == "__main__":
    book= {
        'author':"F. Scott Fitzgerald",
        'title':"The Great Gatsby",
        "price": 123
    }
    bookdiff= {
        "price": 444
    }
    #print(response.json())
    #print(getAllBooks())
    #print(readbooks())
    print(getBookById(1630))
    #print(createbook(book))
    print(updateBook(1630, bookdiff))
    #print(deletebook(1625))