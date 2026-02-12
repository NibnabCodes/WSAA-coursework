# Write the code to get the books from http://andrewbeatty1.pythonanywhere.com/books 
import requests 
url = "http://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(url) 
#print (response.json())

def getAllBooks():
    response = requests.get(url)
    return response.json()
#print(getAllBooks())

# Convert that into a function and call it from inside a if __name__ == “__main__”:
def readbooks():
    response = requests.get(url)
    response.raise_for_status()  # checks for HTTP errors
    return response.json()

if __name__ == "__main__":
    print(readbooks()) 
    
# Write the function for find by id and test it (you need to write the testing code) 
def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    print(f"Status code:", {response.status_code})
    print(f"Response text:", {response.text})
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print(getBookById(1))
    # The function is correct. A 500 error indicates a server-side issue, 
    # so I handle it using exception handling rather than changing the client code. 
    
# write the code to create and test it (you need to write your own testing code) 
def createbook(book):
    response = requests.post(url, json=book)

    # 201 = Created (expected for POST)
    if response.status_code != 201:
        raise Exception(
        f"Failed to create book "
        f"(Status: {response.status_code}) "
        f"Response: {response.text}"
    )
    
    return response.json()

# Write the update function
def updatebook(id, book):
    puturl = f"{url}/{id}"
    response = requests.put(puturl, json=book)

    if response.status_code != 200:
        raise Exception(
            f"Failed to update book "
            f"(Status: {response.status_code}) "
            f"Response: {response.text}"
        )

    return response.json()

# Write the delete function 
def deletebook(id): 
    deleteurl = URL + "/" + str(id) 
    response = requests.delete(deleteurl)
    
    if response.status_code != 200:
        raise Exception(
            f"Failed to update book "
            f"(Status: {response.status_code}) "
            f"Response: {response.text}"
        )
        
    return response.json() 
