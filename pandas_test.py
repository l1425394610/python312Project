import pandas as pd
import pymysql
import sqlalchemy

if __name__ == "__main__":
    engine = sqlalchemy.create_engine("mysql+pymysql://root:mysql7@10.170.3.145:3307/lims?charset=utf8")
    sql = "select * from ccm_inspection_plan"
    df = pd.read_sql(sql=sql, con=engine)
    print(df.head(5).loc[:, "code"])

    # df = pd.read_excel("file/temp.xls")
    # df = df.drop(df.columns[0], axis=1)
    # print(df.iloc[:, 0])
    # print(df.head(2).to_string())
