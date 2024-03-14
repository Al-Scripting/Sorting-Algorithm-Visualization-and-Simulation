# Attempt to import the winsound module for Windows. If unavailable, disable sound effects.
try:
    import winsound

    sound_enabled = True
except ImportError:
    sound_enabled = False


# ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    FINAL = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def play_swap_sound():
    if sound_enabled:
        print(f"{Colors.WARNING}Playing swap sound effect...{Colors.ENDC}")
        filename = 'sound-effect.wav'
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    else:
        print(f"{Colors.WARNING}Swap sound effect...{Colors.ENDC}")


def merge_sort(arr, step_counter=[0], original_array=None):
    if original_array is None:
        original_array = arr.copy()

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        print(f"{Colors.OKBLUE}Step {step_counter[0]}: Preparing to merge{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Left half: {L}, Right half: {R}{Colors.ENDC}")
        step_counter[0] += 1

        merge_sort(L, step_counter, original_array)
        merge_sort(R, step_counter, original_array)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                print(f"{Colors.OKGREEN}Merging {L[i]} from left half: {L} into the array{Colors.ENDC}")
                arr[k] = L[i]
                i += 1
            else:
                print(f"{Colors.OKGREEN}Merging {R[j]} from right half: {R} into the array{Colors.ENDC}")
                arr[k] = R[j]
                j += 1
            play_swap_sound()
            k += 1

        while i < len(L):
            print(f"{Colors.OKGREEN}Merging {L[i]} from left half: {L} into the array{Colors.ENDC}")
            arr[k] = L[i]
            play_swap_sound()
            i += 1
            k += 1

        while j < len(R):
            print(f"{Colors.OKGREEN}Merging {R[j]} from right half: {R} into the array{Colors.ENDC}")
            arr[k] = R[j]
            play_swap_sound()
            j += 1
            k += 1

        print(f"{Colors.HEADER}Step {step_counter[0]}: Merge completed. Merged array: {arr}{Colors.ENDC}")
        step_counter[0] += 1
        print(f"{Colors.FAIL}-----------------------------------------------{Colors.ENDC}")

    elif len(arr) == 1:
        print(f"{Colors.OKBLUE}Step {step_counter[0]}: Single element {arr} is already sorted.{Colors.ENDC}")
        step_counter[0] += 1
        print(f"{Colors.FAIL}-----------------------------------------------{Colors.ENDC}")


# User input section
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23] #example array

#user_input = input("Enter a list of numbers separated by spaces: ")
#arr = [int(item) for item in user_input.split(',')]  # Convert input string to a list of integers
original_array = arr.copy()

print(f"{Colors.BOLD}Original array:{Colors.ENDC} {original_array}")
merge_sort(arr)
print(f"{Colors.FINAL}{Colors.BOLD}Sorted array:{Colors.ENDC} {arr}{Colors.ENDC}")
print(f"{Colors.FINAL}{Colors.BOLD}Original array was:{Colors.ENDC} {original_array}{Colors.ENDC}")
