---
title: Copier des lignes et des colonnes en Python
type: docs
weight: 30
url: /fr/java/copying-rows-and-columns-in-python/
---

## **Aspose.Cells - Copier des lignes et des colonnes**
### **Copier des lignes**
Aspose.Cells propose la méthode copyRow de la classe Cells. Cette méthode copie tous les types de données, y compris les formules, les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets graphiques de la ligne source à la ligne de destination.

La méthode copyRow prend les paramètres suivants :

- l'objet source Cells,
- l'indice de ligne source, et
- l'indice de ligne de destination.

**Code Python**

{{< highlight java >}}

 def copy_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Copy the second row with data, formattings, images and drawing objects

\# to the 12th row in the worksheet.

worksheet.getCells().copyRow(worksheet.getCells(),1,11)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Rows.xls")

print "Copy Rows Successfully." 

{{< /highlight >}}
### **Copier des colonnes**
Aspose.Cells propose la méthode copyColumn de la classe Cells, cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, les formats de cellule, les cellules masquées, les images et autres objets graphiques de la colonne source à la colonne de destination.

La méthode copyColumn prend les paramètres suivants :

- l'objet source Cells,
- indice de la colonne source, et
- indice de la colonne de destination.

**Code Python**

{{< highlight ruby >}}



def copy_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Put some data into header rows (A1:A4)

i = 0

while i < 5:

worksheet.getCells().get(i, 0).setValue("Header Row #i")





\# Put some detail data (A5:A999)

i = 5

while i < 1000:

worksheet.getCells().get(i, 0).setValue("Detail Row #i")


\# Create another Workbook.

workbook1 = Workbook()

\# Get the first worksheet in the book.

worksheet1 = workbook1.getWorksheets().get(0)

\# Copy the first column from the first worksheet of the first workbook into

\# the first worksheet of the second workbook.

worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

\# Autofit the column.

worksheet1.autoFitColumn(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Columns.xls")

print "Copy Columns Successfully." 

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Télécharger **Copier les lignes et les colonnes (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
