
def missingNumbers(nums: list) -> int:
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i+1]-nums[i]>1:
            return nums[i]+1  # Sonlar orasidagi farq 1 dan katta bo'lsa tushib qolgan sonni qaytarish
    
    return nums[len(nums)-1]+1 # Sonlar orasidagi farq faqat 1 ga teng bo'lsa oxirgi songa 1 qo'shib qaytarish



if __name__ == "__main__":

    nums = list(map(int,input("Bir qatorda sonlar kiriting: ").split()))
    
    print(missingNumbers(nums))