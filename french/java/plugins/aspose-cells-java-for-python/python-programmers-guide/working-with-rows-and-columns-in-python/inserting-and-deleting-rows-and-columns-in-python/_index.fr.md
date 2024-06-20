---
title: Insérer et Supprimer des Lignes et des Colonnes en Python
type: docs
weight: 60
url: /fr/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: Créer XLSX en Python, créer XLS en Python, XLS python, XLSX python, XLT python, XLTX python, insérer une ligne en python, insérer une colonne en python, Excel en python
description: Utilisez l API Excel de Python pour créer des feuilles de calcul Excel en Python. Insérez ou supprimez des lignes de XLSX ou XLS dans vos applications Python sans MS Office.
---

## **Créer des feuilles de calcul Excel en Python - Gérer les lignes/colonnes**
### **Insérer une ligne**
Insérez une ligne à n'importe quel emplacement en appelant la méthode insertRows de la collection Cells. La méthode insertRows prend l'index de la ligne où la nouvelle ligne sera insérée comme premier argument, et le nombre de lignes à insérer comme second argument. Voici les étapes :

- Charger le classeur XLS ou XLSX
- Accéder à la feuille de calcul
- Insérer la ligne
- Enregistrer en tant que classeur XLS ou XLSX

**Code Python**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **Insertion de plusieurs lignes**
Pour insérer plusieurs lignes dans la feuille de calcul, appelez la méthode InsertRows de la collection Cells. La méthode InsertRows prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, nombre total de lignes à insérer.

**Code Python**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **Suppression d'une ligne**
Pour supprimer une ligne à n'importe quel emplacement, appelez la méthode DeleteRows de la collection Cells. La méthode DeleteRows prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, nombre total de lignes à supprimer.

**Code Python**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **Suppression de plusieurs lignes**
Pour supprimer plusieurs lignes d'une feuille de calcul, appelez la méthode DeleteRows de la collection Cells. La méthode DeleteRows prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, nombre total de lignes à supprimer.

**Code Python**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **Insertion d'une colonne**
Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode InsertColumns de la collection Cells. La méthode InsertColumns prend deux paramètres :

- Index de colonne, l'index de la colonne à partir de laquelle la colonne sera insérée.
- Nombre de colonnes, nombre total de colonnes à insérer

**Code Python**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **Supprimer une colonne**
Pour supprimer une colonne de la feuille de calcul à n'importe quel emplacement, appelez la méthode deleteColumns de la collection Cells. La méthode deleteColumns prend les paramètres suivants:

- Index de colonne, l'index de la colonne à partir de laquelle la colonne sera supprimée.
- Nombre de colonnes, nombre total de colonnes à supprimer.
- Décaler les cellules, paramètre booléen pour indiquer s'il faut décaler les cellules vers la gauche après la suppression.

**Code Python**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Gestion des lignes/colonnes (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
