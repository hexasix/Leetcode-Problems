# find the number of digits
# return the amount of even number of digits in an array

arr = [111, 1111, 1, 11,111111]  # should return 2


def find_even(nums: list):
    digit_count = 0
    even_count = 0
    for num in nums:
        while num>0:
            num = num//10
            digit_count += 1
        print("digits=",digit_count)
        if digit_count % 2 == 0:
            even_count+=1
        digit_count=0

    return even_count


print(find_even(arr))
