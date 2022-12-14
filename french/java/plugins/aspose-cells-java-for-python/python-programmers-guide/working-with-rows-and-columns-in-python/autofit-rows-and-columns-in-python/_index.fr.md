---
title: Ajustement automatique des lignes et des colonnes dans Python
type: docs
weight: 20
url: /fr/java/autofit-rows-and-columns-in-python/
---
## **Aspose.Cells - Ajustement automatique des lignes et des colonnes**
### **Ligne d'ajustement automatique**
L'approche la plus simple pour dimensionner automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode autoFitRow de la classe Worksheet. La méthode autoFitRow prend un index de ligne (de la ligne à redimensionner) comme paramètre.

**Code Python**

{{< highlight "python" >}}

 def autofit_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 3rd row of the worksheet

worksheet.autoFitRow(2)

\# Auto-fitting the 3rd row of the worksheet based on the contents in a range of

\# cells (from 1st to 9th column) within the row

# worksheet.autoFitRow(2,0,8) # Uncomment this line if you to do AutoFit Row in a Range of Cells. Also, comment line 288.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Row.xls")

print "Autofit Row Successfully." 

{{< /highlight >}}
### **Colonne d'ajustement automatique**
Le moyen le plus simple de redimensionner automatiquement la largeur et la hauteur d'une colonne consiste à appeler la méthode autoFitColumn de la classe Worksheet. La méthode autoFitColumn prend l'index de colonne (de la colonne sur le point d'être redimensionnée) comme paramètre.

**Code Python**

{{< highlight "python" >}}

 def autofit_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Auto-fitting the 4th column of the worksheet

worksheet.autoFitColumn(3)

\# Auto-fitting the 4th column of the worksheet based on the contents in a range of

\# cells (from 1st to 9th row) within the column

# worksheet.autoFitColumn(3,0,8) #Uncomment this line if you to do AutoFit Column in a Range of Cells. Also, comment line 310.

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Autofit Column.xls")

print "Autofit Column Successfully." 

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Ajustement automatique des lignes et des colonnes (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
