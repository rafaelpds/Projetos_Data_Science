import streamlit as st 

import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

    # Título
html_title = """
<div style='background-color:#ffffff;text-align:center'>
<p style='color:#000000;font-size:40px;'>Análise Exploratória dos Dados - DICAF v1.0</p>
</div>
"""
st.markdown(html_title, unsafe_allow_html=True)

# Subtítulo
html_subtitle = """
<div style='background-color:#ffffff;text-align:center'>
<p style='color:#000000;font-size:20px;'>Esta ferramenta tem como premissa possiblitar que o auditor tenha uma visão detalhada dos dados e assim possa desenvolver novas análises durante o trabalho de auditoria.</p>
</div>
"""
st.markdown(html_subtitle, unsafe_allow_html=True)

#st.set_option('deprecation.showPyplotGlobalUse', False)

data = st.file_uploader("Importe o Dataset", type=["csv", "txt"])

def main():
    

    activities = ["Análise Exploratória","Gráficos"]	
    choice = st.sidebar.radio("Selecione uma opção:",activities)
    

    if choice == 'Análise Exploratória':
        st.subheader("Análise Exploratória dos Dados")


        if data is not None:

            df = pd.read_csv(data)

            if st.checkbox("Lista com os 5 primeiros registros:"):
                st.dataframe(df.head())
            
            if st.checkbox("Total de Nulos:"):
                st.dataframe(df.isnull().sum())


            if st.checkbox("Total de Linhas e Colunas:"):
                st.write("Linhas:",df.shape[0])
                st.write("Colunas:",df.shape[1])
                

            if st.checkbox("Lista das Colunas da sua base:"):
                all_columns = df.columns.to_list()
                st.write(all_columns)

            if st.checkbox("Estatistica Descritiva:"):
                st.write(df.describe())

            #if st.checkbox("Show Selected Columns"):
            #   selected_columns = st.multiselect("Select Columns",all_columns)
            #new_df = df[selected_columns]
            #	st.dataframe(new_df)

            if st.checkbox("Quantidade de Valores:"):
                all_columns = df.columns.to_list()
                column = st.selectbox("Selecione uma coluna",all_columns)
                st.write(df[column].value_counts())

            if st.checkbox("Correlation Plot(Matplotlib)"):
                plt.matshow(df.corr())
                st.pyplot()

            if st.checkbox("Correlation Plot(Seaborn)"):
                st.write(sns.heatmap(df.corr(),annot=True))
                st.pyplot()


            if st.checkbox("Pie Plot"):
                column_to_plot = st.selectbox("Select 1 Column",all_columns)
                pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
                st.write(pie_plot)
                st.pyplot()



    elif choice == 'Gráficos':
        st.subheader("Data Visualization")
        #data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
        if data is not None:
            df = pd.read_csv(data)
            st.write("Top 5 data")
            st.dataframe(df.head())


            if st.checkbox("Show Value Counts"):
                st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
                st.pyplot()

            # Customizable Plot

            all_columns_names = df.columns.tolist()
            type_of_plot = st.radio("Select Type of Plot",["area","bar","line","hist","box","kde"])
            selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

            if st.button("Generate Plot"):
                st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

            # Plot By Streamlit
                if type_of_plot == 'area':
                    cust_data = df[selected_columns_names]
                    st.area_chart(cust_data)

                elif type_of_plot == 'bar':
                    cust_data = df[selected_columns_names]
                    st.bar_chart(cust_data)

                elif type_of_plot == 'line':
                    cust_data = df[selected_columns_names]
                    st.line_chart(cust_data)

                # Custom Plot 
                elif type_of_plot:
                    cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
                    st.write(cust_plot)
                    st.pyplot()
    


if __name__ == '__main__':
	main()