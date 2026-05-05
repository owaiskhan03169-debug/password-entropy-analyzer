import math
import time
import sys

# Terminal styling constants
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def hacker_type(text, delay=0.02):
    """Simulates a terminal typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def analyze_password(password):
    length = len(password)
    pool_size = 0
    
    # Character pool logic
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    if has_lower: pool_size += 26
    if has_upper: pool_size += 26
    if has_digit: pool_size += 10
    if has_symbol: pool_size += 32

    # Avoid math errors for empty strings
    if pool_size == 0: return 0, 0, "N/A"

    # Entropy calculation: E = L * log2(R)
    entropy = length * math.log2(pool_size)
    combinations = pool_size ** length
    
    # Assuming 100 Billion hashes per second (standard high-end GPU rig)
    hashes_per_sec = 100_000_000_000
    seconds_to_crack = combinations / hashes_per_sec
    
    return entropy, seconds_to_crack, (has_upper, has_lower, has_digit, has_symbol)

def format_time(seconds):
    
    if seconds < 1: return "Less than a second"
    
    intervals = (
        ('centuries', 3153600000),
        ('years', 31536000),
        ('days', 86400),
        ('hours', 3600),
        ('minutes', 60),
        ('seconds', 1),
    )

    for name, count in intervals:
        value = seconds // count
        if value > 0:
            return f"{int(value)} {name}"
    return "Instant"

def main():
    # ASCII Header for Portfolio flair
    print(f"{CYAN}{BOLD}")
    print(" ___________________________________________ ")
    print("|          PASSWORD_X_TERMINAL v1.0         |")
    print("|       System Entropy Analysis Tool        |")
    print("|___________________________________________|")
    print(f"{RESET}")

    password = input(f"{YELLOW}[LOG] Enter target password to scan: {RESET}")
    print(f"\n{CYAN}[...] Initializing Cryptographic Analysis...{RESET}")
    time.sleep(1)

    entropy, crack_time, checks = analyze_password(password)
    u, l, d, s = checks

    # Display Diagnostics
    hacker_type(f"{GREEN if u else RED}[{'✓' if u else '✗'}] Uppercase letters{RESET}")
    hacker_type(f"{GREEN if l else RED}[{'✓' if l else '✗'}] Lowercase letters{RESET}")
    hacker_type(f"{GREEN if d else RED}[{'✓' if d else '✗'}] Numeric digits{RESET}")
    hacker_type(f"{GREEN if s else RED}[{'✓' if s else '✗'}] Special symbols{RESET}")

    # Results Section
    print(f"\n{BOLD}ANALYSIS RESULTS:{RESET}")
    print(f"---------------------------")
    print(f"Entropy Score: {CYAN}{entropy:.2f} bits{RESET}")
    
    # Determine Strength based on entropy
    strength = f"{RED}VULNERABLE" if entropy < 40 else f"{YELLOW}MODERATE" if entropy < 60 else f"{GREEN}UNBREAKABLE"
    print(f"Security Class: {strength}{RESET}")
    
    readable_time = format_time(crack_time)
    print(f"Estimated Crack Time: {BOLD}{readable_time}{RESET}")
    print(f"---------------------------")

    if entropy < 50:
        print(f"{YELLOW}[ADVICE] Add symbols or increase length to prevent brute-force attacks.{RESET}")
    else:
        print(f"{GREEN}[SUCCESS] Password meets high-security encryption standards.{RESET}")

if __name__ == "__main__":
    main()