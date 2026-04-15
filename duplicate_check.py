import pandas as pd

# Initial table (you can keep it empty if you want)
data = {
    'id': [1, 2,3,4],
    'name': ['Rhamya sri A K ', 'Shakthi Shree','Pradeepa','Sandhiya'],
    'email': ['rhamyasri@gmail.com', 'shakthishree@gmail.com','pradeepa@gmail.com','sandhiya@gmail.com']
}

df = pd.DataFrame(data)

# Function to add new user
def add_user(df):
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    # Check if email already exists
    if email in df['email'].values:
        existing_user = df[df['email'] == email]['name'].values[0]
        print(f" This email is already used by {existing_user}")
    else:
        new_id = df['id'].max() + 1 if not df.empty else 1
        new_row = pd.DataFrame([[new_id, name, email]], columns=['id', 'name', 'email'])
        df = pd.concat([df, new_row], ignore_index=True)
        print("User added successfully!")

    return df

# Run program
while True:
    df = add_user(df)
    
    choice = input("Do you want to add another user? (yes/no): ").lower()
    if choice != 'yes':
        break

print("\nFinal Table:")
print(df)