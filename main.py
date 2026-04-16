# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("zmaqsood@calpoly.edu")
print(message)

#Task 3
def smallest(n: float, m: float) -> float:
   if n < m:
      return n  # This is evaluated when n is less than m
   else:
      return m


first = smallest(3, 2)  # first = 2
second = smallest(2, 2)  # second = 2, this is reasonable because when n = m, else branch returns m
print()


def function2(a: int, b: int, c: int) -> int:
   if a > b and a > c:
      return a - b  # In general, when will a call to this function evaluate this statement? A call to this function will evaluate this statement when a is the largest value
   elif b > c:
      return b + c  # In general, when will a call to this function evaluate this statement? When a is not the largest, and b > c
   else:
      return 2 * c  # In general, when will a call to this function evaluate this statement? When c is greater than or equal to to a or b


answer1 = function2(3, 2, 1)  # What is the value of answer1? 1
answer2 = function2(2, 3, 1)  # What is the value of answer2? 4
answer3 = function2(2, 1, 3)  # What is the value of answer3? 6
print()

#Task 4

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? True or False
    if test:                            # What is this check preventing? preventing accessing a sequence that doesn't exist
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? True and False--> False
second = checked_access([1, 0, 1], 2)    # What is the value of second? True and True--> True
print()


def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # For which call below is this statement evaluated? First call
   elif len(L) > 1:  # and what are the values being added? [4]+[2]+[3]
      result = len(L[0]) + len(L[1])  # For which call below is this statement evaluated? Third call
   elif len(L) > 0:  # and what are the values being added? [7]+[4]
      result = len(L[0])  # For which call below is this statement evaluated? second call
   else:  # and what are the value[s] being added? 11
      result = 0
   return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# What is the value of words at this point? ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
# What are the values of first and second at this point? ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
# What happened? By using appendix, we alter the original list such that the both calls will be referencing the same updated list.
print()