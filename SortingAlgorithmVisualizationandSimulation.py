#Sorting Algorithm Visualization and Simulation by Al Muqshith Mohammed Shifan
#100862739



# Attempt to import the winsound module for Windows. If unavailable, disable sound effects.
try:
    import winsound

    sound_enabled = True
except ImportError:
    sound_enabled = False


# ANSI escape codes for colors
class Colors:
    """
        Defines color codes for terminal output to enhance readability.
        Each color is associated with a specific part of the merge sort process for clarity.
        """
    HEADER = '\033[95m'  # Purple, for headers and final messages
    OKBLUE = '\033[94m'  # Blue, for highlighting the preparation to merge
    OKCYAN = '\033[96m'  # Cyan, for showing left and right halves before merging
    OKGREEN = '\033[92m'  # Green, for individual merge operations
    WARNING = '\033[93m'  # Yellow, for playing sound effects
    FAIL = '\033[91m'  # Red, for separators
    FINAL = '\033[90m'  # Grey, for final output
    ENDC = '\033[0m'  # Reset to default color
    BOLD = '\033[1m'  # Bold text for emphasis
    UNDERLINE = '\033[4m'  # Underline text for emphasis

def play_swap_sound():
    """
        Plays a swap sound effect during the merge operations.
        Requires 'sound-effect.wav' to be present in the working directory.
        """
    if sound_enabled:
        print(f"{Colors.WARNING}Playing swap sound effect...{Colors.ENDC}")
        filename = 'sound-effect.wav'
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    else:
        print(f"{Colors.WARNING}Swap sound effect...{Colors.ENDC}")


def merge_sort(arr, step_counter=[0], original_array=None):
    """
       Performs merge sort on an array, showing each step of the process.
       Prints the array's state at various stages and plays sound effects for swaps.
       """

    if original_array is None:
        original_array = arr.copy()

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        print(f"{Colors.OKBLUE}Step {step_counter[0]}: Preparing to merge{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Left half: {L}, Right half: {R}{Colors.ENDC}")
        step_counter[0] += 1

        # Recursively sort both halves
        merge_sort(L, step_counter, original_array)
        merge_sort(R, step_counter, original_array)

        i = j = k = 0

        # Merge the two halves
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

        # Copy the remaining elements of L, if there are any
        while i < len(L):
            print(f"{Colors.OKGREEN}Merging {L[i]} from left half: {L} into the array{Colors.ENDC}")
            arr[k] = L[i]
            play_swap_sound()
            i += 1
            k += 1

        # Copy the remaining elements of R, if there are any
        while j < len(R):
            print(f"{Colors.OKGREEN}Merging {R[j]} from right half: {R} into the array{Colors.ENDC}")
            arr[k] = R[j]
            play_swap_sound()
            j += 1
            k += 1

        # Indicate completion of this merge step
        print(f"{Colors.HEADER}Step {step_counter[0]}: Merge completed. Merged array: {arr}{Colors.ENDC}")
        step_counter[0] += 1
        print(f"{Colors.FAIL}-----------------------------------------------{Colors.ENDC}")

    elif len(arr) == 1:
        # Handle the case of a single-element array (already sorted)
        print(f"{Colors.OKBLUE}Step {step_counter[0]}: Single element {arr} is already sorted.{Colors.ENDC}")
        step_counter[0] += 1
        print(f"{Colors.FAIL}-----------------------------------------------{Colors.ENDC}")


#example array
#arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]

# User input section
user_input = input("Enter a list of number ID's separated by spaces: ")
arr = [int(item) for item in user_input.split(',')]  # Convert input string to a list of integers
original_array = arr.copy()

# Print the original and sorted arrays, and indicate the start of the array
print(f"{Colors.BOLD}Original array:{Colors.ENDC} {original_array}")
merge_sort(arr)

# Final output, now using a distinct color
print(f"{Colors.FINAL}{Colors.BOLD}Sorted array of ID's:{Colors.ENDC} {arr}{Colors.ENDC}")
print(f"{Colors.FINAL}{Colors.BOLD}Original array of ID's:{Colors.ENDC} {original_array}{Colors.ENDC}")
