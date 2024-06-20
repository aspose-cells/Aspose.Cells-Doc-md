---
title: Ajustement de la hauteur de ligne et de la largeur de colonne en Python
type: docs
weight: 10
url: /fr/java/adjusting-row-height-and-column-width-in-python/
keywords: "créer XLSX en Python, créer XLS en Python, XLS python, XLSX python, hauteur de ligne python, largeur de colonne python, Excel python"
description: Utilisez Python Excel API pour créer des fichiers Excel en Python. Ajustez la hauteur de ligne et la largeur de colonne dans XLSX ou XLS dans vos applications Python sans MS Office.
---

## **Feuilles de calcul Excel en Python - Ajustement de la hauteur de ligne et de la largeur de colonne**
### **Définir la hauteur de la ligne**
Avec Aspose.Cells, il est possible de définir la hauteur d'une seule ligne en Python en appelant la méthode setRowHeight de la collection Cells. La méthode setRowHeight prend les paramètres suivants :

- **Index de ligne**, l'index de la ligne pour laquelle vous modifiez la hauteur.
- **Hauteur de la ligne**, la hauteur de la ligne à appliquer sur la ligne.

**Code Python**

{{< highlight python >}}

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
### **Définir la largeur de colonne**
Définissez la largeur d'une colonne en appelant la méthode setColumnWidth de la collection Cells. La méthode setColumnWidth prend les paramètres suivants:

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée.

**Code Python**

{{< highlight python >}}

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Ajustement de la hauteur de ligne et de la largeur de colonne (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
