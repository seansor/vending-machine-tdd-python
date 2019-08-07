def even_number_of_evens(numbers):
    if len(numbers) > 1:
        count = 0
        for number in numbers:
            if number % 2 == 0:
                count += 1
            else:
                count = count
        if count > 1 and count % 2 == 0:
            return True
        else:
            return False
    else:
        return False

assert even_number_of_evens([]) == False, "No numbers"   
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")