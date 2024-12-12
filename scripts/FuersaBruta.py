import sys
import time
import itertools
import string

def simulate_brute_force(target_user, target_password, max_attempts):
    start_time = time.time()

    attempts = 0
    success = False

    # Define a basic character set for password guessing
    charset = string.ascii_lowercase + string.digits

    # Generate combinations of passwords
    for length in range(1, len(target_password) + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempts += 1
            guessed_password = ''.join(attempt)

            # Check if the guessed credentials match
            if target_user == "admin" and guessed_password == target_password:
                success = True
                break

            if attempts >= max_attempts:
                break

        if success or attempts >= max_attempts:
            break

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display results
    if success:
        print(f"Login successful! User: {target_user}, Password: {target_password}")
    else:
        print("Login failed. Limit of attempts reached.")

    print(f"Attempts made: {attempts}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Total combinations tried: {attempts}")

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            print("Usage: python brute_force_sim.py <user> <password> <max_attempts>")
            sys.exit(1)

        user = sys.argv[1]
        password = sys.argv[2]
        max_attempts = int(sys.argv[3])

        simulate_brute_force(user, password, max_attempts)
    except ValueError:
        print("Error: max_attempts must be an integer.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
