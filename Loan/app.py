#Command_Line_Implimantation Method to deploy the ML Model
# import pandas as pd
# model=pd.read_pickle('loan_model.pickle')
# cols=model.feature_names_in_

# query_data=[]
# for col in cols:
#     query=eval(input(f'Enter {col}:')) #eval is convert into numeric
#     query_data.append(query)

# query_df=pd.DataFrame([query_data],columns=cols)
# result=model.predict(query_df).tolist()[0]
# result='Probable' if result==1 else 'Not Probable'
# print(f'This customer is {result} for Personal Loan')

#Form Flask ML Model I
import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    result=''
    if request.method=='POST':
        model=pd.read_pickle('loan_model.pickle')
        cols=model.feature_names_in_
        query_data=[]
        for col in cols:
            query=eval(request.form[col])
            query_data.append(query)
        
        query_df=pd.DataFrame([query_data],columns=cols)
        result=model.predict(query_df).tolist()[0]
        result='Probable' if result==1 else 'Not Probable'
        result=f'This customer is {result} for Personal Loan'
    
    return render_template('index.html',result=result)

app.run(debug=True)
