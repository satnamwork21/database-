import pandas as pd

data = {  
    'Employee_id': ['4', '5', '6', '7', '8'],
    'Employee_name': ['Meera', 'Tia', 'Varsha', 'Williams', 'Ziva']
}
df2 = pd.DataFrame(data, columns=['Employee_id', 'Employee_name'])  
print(df2)