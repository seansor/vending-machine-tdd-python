#def count_upper_case(message):
#    count = 0
#    for c in message:
#        if c.isupper():
#            count += 1
#   return count

def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "empty string"
assert count_upper_case("A") == 1, "one uppercase"
assert count_upper_case("a") == 0, "one lowercase"
assert count_upper_case("£$%^") == 0, "special characters"
assert count_upper_case("Hello World"), "two uppercase"

print("All the tests passed")