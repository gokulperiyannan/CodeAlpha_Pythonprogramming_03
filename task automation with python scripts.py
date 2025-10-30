import re
import os

def extract_emails_from_file(input_filename, output_filename):
    
    extracted_emails = set() # Use a set to store unique emails

    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()

            # Regular expression for email addresses
            # This regex is quite comprehensive but not exhaustive for all edge cases
            # (e.g., highly unusual TLDs or quoted local parts).
            # It generally matches: word.word@domain.tld
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

            # Find all matches
            found_emails = re.findall(email_pattern, content)

            for email in found_emails:
                extracted_emails.add(email)

        if not extracted_emails:
            print(f"No email addresses found in '{input_filename}'.")
            return

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            for email in sorted(extracted_emails): # Write unique emails in sorted order
                outfile.write(email + '\n')

        print(f"Successfully extracted {len(extracted_emails)} unique email addresses.")
        print(f"Emails saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "emails.txt"

    # Create a dummy input file if it doesn't exist for demonstration
    if not os.path.exists(input_file):
        print(f"Creating a sample '{input_file}' for demonstration...")
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("Hello, my name is Alice. You can reach me at alice@example.com or support@company.org.\n")
            f.write("I also have an old email: a.wonderland@domain.net. Please contact us for more info.\n")
            f.write("My friend Bob's email is bob.the.builder@work.co.uk. Invalid email here: test@.com\n")
            f.write("Another one: info-team@sub.domain.io.\n")
            f.write("Duplicate email test: alice@example.com again.\n")
        print(f"'{input_file}' created successfully.")
    else:
        print(f"Using existing '{input_file}'.")

    extract_emails_from_file(input_file, output_file)

    # Optional: Display content of the output file
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        print("\n--- Content of 'emails.txt' ---")
        with open(output_file, 'r', encoding='utf-8') as f:
            print(f.read())