  output = 'Yes'
   for word in note:
        magCount, noteCount = magazine.count(word), note.count(word)
        if magCount < noteCount:
            output = 'No'
    print(str(output))
