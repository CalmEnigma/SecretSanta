# Import libraries
import numpy as np
import pandas as pd
import random

# Define groups
people = ["Giovanna", "Francesco", "Alberto", "Marghe", "Lorenzo",
          "Luigi", "Benedetta", "Marco", "Arlene", "Albert", "Allegra"]
families = {'Marco': ['Marco', 'Arlene', 'Luigi'],
            'Giovanna': ['Giovanna', 'Francesco', 'Alberto', 'Marghe', 'Lorenzo'],
            'Benedetta': ['Benedetta' , 'Allegra', 'Albert']}

# Create df
df = pd.DataFrame(people, columns = ['Name'])

# Assign families
## Reverse dictionary
result_dict = {}
for ele in df['Name']:
    result_dict[ele] = []
    for key in families.keys():
        if ele in families[key]:
            result_dict[ele].append(key)

## Map dictionary
df['Family'] = df['Name'].map(result_dict)

## Convert to string
df['Family'] = df['Family'].apply(lambda l: str(l[0]))


# Add selection pool
df['Pool'] = df['Family'].apply(lambda l:
                              [name for name in df['Name'] if name not in families[l]])
    

# Assign random person from pool
assigned = []
for i in df['Name']:
    
    # Get pool list
    pool = df['Pool'][df['Name']==i].reset_index(drop=True)
    pool = pool[0]
    
    # Drop people already assigned
    pool = [person for person in pool if person not in assigned]
    
    # Make random assignment
    assignment = random.choice(pool)
    
    # Add to list of people already assigned
    assigned.append(assignment)
    
    # Print
    print(i, assignment)
    

# Final df
final = pd.DataFrame(df['Name'], columns = ['Name'])
final['Assignment'] = assigned
