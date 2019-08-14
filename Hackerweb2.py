def sherlockAndAnagrams(s):
    listS = list(s)
    completed = []
    totalAnagrams = 0
    for i in listS:
        letCount = listS.count(i)
        if letCount > 1:
            if not i in completed:
                completed.append(i)
                print(completed)
                while letCount > 1:
                    totalAnagrams = totalAnagrams + letCount
                    letCount = letCount - 1
    return(totalAnagrams)


print(sherlockAndAnagrams('kkkk'))
