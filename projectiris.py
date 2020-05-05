#Practica de iris by Ara version 2.0
import matplotlib.pyplot as plt
import pandas as pd
import csv
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader

iris_df = pd.read_csv("iris.csv")
#sepal_width 
mean_sepal_width=iris_df['sepal_width'].mean()
median_sepal_width=iris_df['sepal_width'].median()
moda_sepal_width=iris_df['sepal_width'].mode().values
max_sepal_width=iris_df['sepal_width'].max()
min_sepal_width=iris_df['sepal_width'].min()

setosa_df = iris_df[iris_df["species"] == "setosa"]
virginica_df = iris_df[iris_df["species"] == "virginica"]
versicolord_df = iris_df[iris_df["species"]=="versicolor"]

#sepal_length
mean_sepal_length=iris_df['sepal_length'].mean()
median_sepal_length=iris_df['sepal_length'].median()
moda_sepal_length=iris_df['sepal_length'].mode().values
max_sepal_length=iris_df['sepal_length'].max()
min_sepal_length=iris_df['sepal_length'].min()

#petal_length
mean_petal_length=iris_df['petal_length'].mean()
median_petal_length=iris_df['petal_length'].median()
moda_petal_length=iris_df['petal_length'].mode().values
max_petal_length=iris_df['petal_length'].max()
min_petal_length=iris_df['petal_length'].min()

#petal_width
mean_petal_width=iris_df['petal_width'].mean()
median_petal_width=iris_df['petal_width'].median()
moda_petal_width=iris_df['petal_width'].mode().values
max_petal_width=iris_df['petal_width'].max()
min_petal_width=iris_df['petal_width'].min()

#CSV

text="Mean","Median","Moda","Max","Min","Feathers"
text1 = [mean_sepal_width,median_sepal_width,moda_sepal_width[0],max_sepal_width,min_sepal_width,"sepal_width"]
text2 = [mean_sepal_length,median_sepal_length,moda_sepal_length[0],max_sepal_length,min_sepal_length,"sepal_length"]
text3 = [mean_petal_width,median_petal_width,moda_petal_width[0],max_petal_width,min_petal_width,"petal_width"]
text4 = [mean_petal_length,median_petal_length,moda_sepal_length[0],max_petal_length,min_sepal_width,"petal_length"]

file = open("information_iris.csv", "w")
writer = csv.writer(file)
writer.writerow(text)
writer.writerow(text1)
writer.writerow(text2)
writer.writerow(text3)
writer.writerow(text4)
file.close()

df_description_file= pd.read_csv("information_iris.csv")

print(df_description_file)
     
print("\n Writing a information_iris.csv completed \n")

#graficas

print("Choose an option: ")
print("\n1. Histogram sepal_width and save graph"
    "\n2. Histogram sepal_length and save graph"
    "\n3. Histogram petal_width and save graph"
    "\n4. Histogram petal_length and save graph"
    "\n5. Show all histograms and save graphs"
    "\n6. Close")
try:
    option = int(input("Option: "))
except:
    print("Error")
    exit()

def options(option):
    def sepal_width():
        plt.rcParams['axes.facecolor'] = "bisque"
        plt.subplot(131)
        x1 = setosa_df["sepal_width"]
        plt.title("Setosa Sepal Width", fontsize=9, fontstyle="italic")
        plt.suptitle('Histogram Sepal width', fontsize=18)
        plt.hist(x1, bins=20, color="gold",edgecolor = 'black')


        plt.subplot(132)
        x2 = virginica_df["sepal_width"]
        plt.title("Virginica Sepal Width", fontsize=9, fontstyle="italic")
        plt.hist(x2, bins=20,color="tomato", edgecolor = 'black')


        plt.subplot(133)
        x3 = versicolord_df["sepal_width"]
        plt.title("Versicolor Sepal Width", fontsize=9, fontstyle="italic")
        plt.hist(x3, bins=20,color = "skyblue", edgecolor = 'black')
        plt.savefig("Histogram_1.pdf")
        plt.show(block=False)
        plt.pause(5)
        plt.close()

    def sepal_length():
        plt.rcParams['axes.facecolor'] = "plum"
        plt.subplot(131)
        x1 = setosa_df["sepal_length"]
        plt.title("Setosa Sepal Length", fontsize=9, fontstyle="italic")
        plt.suptitle('Histogram Sepal Length', fontsize=18)
        plt.hist(x1, bins=20, color="gold",edgecolor = 'black')


        plt.subplot(132)
        x2 = virginica_df["sepal_length"]
        plt.title("Virginica Sepal Length", fontsize=9, fontstyle="italic")
        plt.hist(x2, bins=20,color="tomato", edgecolor = 'black')


        plt.subplot(133)
        x3 = versicolord_df["sepal_length"]
        plt.title("Versicolor Sepal Length", fontsize=9, fontstyle="italic")
        plt.hist(x3, bins=20,color = "skyblue", edgecolor = 'black')
        plt.savefig("Histogram_2.pdf")
        plt.show(block=False)
        plt.pause(5)
        plt.close()

    def petal_width():

        plt.rcParams['axes.facecolor'] = "wheat"
        plt.subplot(131)
        x1 = setosa_df["petal_width"]
        plt.title("Setosa Petal Width", fontsize=9, fontstyle="italic")
        plt.suptitle('Histogram Petal width', fontsize=18)
        plt.hist(x1, bins=20, color="gold",edgecolor = 'black')


        plt.subplot(132)
        x2 = virginica_df["petal_width"]
        plt.title("Virginica Petal Width", fontsize=9, fontstyle="italic")
        plt.hist(x2, bins=20,color="tomato", edgecolor = 'black')


        plt.subplot(133)
        x3 = versicolord_df["petal_width"]
        plt.title("Versicolor Petal Width", fontsize=9, fontstyle="italic")
        plt.hist(x3, bins=20,color = "skyblue", edgecolor = 'black')
        plt.savefig("Histogram_3.pdf")
        plt.show(block=False)
        plt.pause(5)
        plt.close()

    def petal_length():

        plt.rcParams['axes.facecolor'] = "palegreen"
        plt.subplot(131)
        x1 = setosa_df["petal_length"]
        plt.title("Setosa Petal Length", fontsize=9, fontstyle="italic")
        plt.suptitle('Histogram Petal Length', fontsize=18)
        plt.hist(x1, bins=20, color="gold",edgecolor = 'black')


        plt.subplot(132)
        x2 = virginica_df["petal_length"]
        plt.title("Virginica Petal Length", fontsize=9, fontstyle="italic")
        plt.hist(x2, bins=20,color="tomato", edgecolor = 'black')


        plt.subplot(133)
        x3 = versicolord_df["petal_length"]
        plt.title("Versicolor Petal Length", fontsize=9, fontstyle="italic")
        plt.hist(x3, bins=20,color = "skyblue", edgecolor = 'black')
        plt.savefig("Histogram_4.pdf")
        plt.show(block=False)
        plt.pause(5)
        plt.close()

    if option ==1:
        sepal_width()
    if option==2:
        sepal_length()
    if option==3:
        petal_width()
    if option==4:
        petal_length()
    if option==5:
        sepal_width()
        sepal_length()
        petal_width()
        petal_length()

        inputs = ["portada.pdf","Histogram_1.pdf","Histogram_2.pdf","Histogram_3.pdf","Histogram_4.pdf"]
        
        def pdf_combine(pdf_list):
            merger = PyPDF2.PdfFileMerger()
            for pdf in pdf_list:
                merger.append(pdf)
            merger.write('Allgraphs.pdf')
        pdf_combine(inputs)

    if option==6:
        exit()


if 1<=option<=6:
        options(option)
else:
    print("Error")
    exit()
