#  تابعی بنویسید یک لیست بصورت ترکیبی از استزینگ و ارقام گرفته و بزرگترین مقدار لیست را خروجی دهد. (بزرگترین مقدار = استرینگی با بیشترین طول یا عددی با بیشترین مقدار)


        
def best_score(myList : list):

    numList = []
    counting = 0
    for i in range( len(myList) ):
        
        if type( myList[i] ) == int and float :
            numList.append( myList[i] )
        
        elif type( myList[i] ) == str :
            for i in myList[i] :
                counting += 1
            numList.append( counting ) 
    return print(f' Min number is { min(numList) } and Max number is { max(numList) }')



best_score( [ 4, 8, 'masoome', 12, 48, 'bahadori', 1, 'kahkeshanhaye door dast' ] )