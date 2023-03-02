import pandas as pd 

df = pd.read_csv('Class data - Sheet1.csv')

df.sample(5)


biggest_shoe_size_by_state = df.groupby(['State']
                  ).agg(biggest_shoe_size = ('Shoe size', 'max')
                  ).reset_index()
                  
Youngest_person_by_state = df.groupby(['State']
                  ).agg(biggest_shoe_size = ('Age', 'min')
                  ).reset_index()
                  
                  
print(biggest_shoe_size_by_state, Youngest_person_by_state)
