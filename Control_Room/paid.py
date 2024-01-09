# Server script for different actions

# Define the action you want to perform (e.g., 'Activate', 'Deactivate', 'Free')
action = 'Activate'

# Check the action and execute corresponding code
if action == 'Activate':
    # If action is 'Activate', send a message indicating key approval status
    Activate()  
    # You can perform additional actions or call corresponding functions here

elif action == 'Deactivate':
    # If action is 'Deactivate', execute Deactivate function
    Deactivate()

elif action == 'Free':
    # If action is 'Free', execute Free function
    Free()

# Add more conditions for other actions if needed


