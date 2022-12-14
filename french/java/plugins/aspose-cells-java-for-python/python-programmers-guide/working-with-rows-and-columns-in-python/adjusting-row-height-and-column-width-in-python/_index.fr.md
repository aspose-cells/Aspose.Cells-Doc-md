---
title: Réglage de la hauteur de ligne et de la largeur de colonne dans Python
type: docs
weight: 10
url: /fr/java/adjusting-row-height-and-column-width-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, row height python, column width python, Excel pytho
description: Utilisez Python Excel API pour créer des fichiers Excel dans Python. Ajustez la hauteur des lignes et la largeur des colonnes en XLSX ou XLS dans vos applications Python sans MS Office.
---
## **Feuilles de calcul Excel dans Python - Ajustement de la hauteur des lignes et de la largeur des colonnes**
### **Définition de la hauteur de ligne**
Avec Aspose.Cells, il est possible de définir la hauteur d'une seule ligne dans Python en appelant la méthode setRowHeight de la collection Cells. La méthode setRowHeight prend les paramètres suivants :

- **Indice de ligne**, l'index de la ligne dont vous modifiez la hauteur.
- **Hauteur de ligne**, la hauteur de ligne à appliquer sur la ligne.

**Code Python**

{{< highlight "python" >}}

 def set_row_height(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the height of the second row to 13

cells.setRowHeight(1, 13)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Row Height.xls")

print "Set Row Height Successfully." 

{{< /highlight >}}
### **Définition de la largeur de colonne**
Définissez la largeur d'une colonne en appelant la méthode setColumnWidth de la collection Cells. La méthode setColumnWidth prend les paramètres suivants :

- **Indice de colonne**, l'index de la colonne dont vous modifiez la largeur.
- **Largeur de colonne**, la largeur de colonne souhaitée.

**Code Python**

{{< highlight "python" >}}

 def set_column_width(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Set Column Width.xls")

print "Set Column Width Successfully." 

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Réglage de la hauteur des lignes et de la largeur des colonnes (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
