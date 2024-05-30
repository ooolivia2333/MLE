import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # 2877. Create a DataFrame from List
    column_names = ["student_id", "age"]
    result_dataframe = pd.DataFrame(student_data, columns=column_names)
    return result_dataframe