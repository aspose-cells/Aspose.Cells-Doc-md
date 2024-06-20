---
title: Masquer et Afficher des Lignes et des Colonnes en Python
type: docs
weight: 50
url: /fr/java/hiding-and-showing-rows-and-columns-in-python/
description: Apprenez à Masquer et Afficher des Lignes et des Colonnes via l API Aspose.Cells pour Python via Java.
keywords: Comment Masquer et Afficher des Lignes et des Colonnes en Python via Java, Masquer les Lignes et les Colonnes à l aide de Python via Java, Afficher les Lignes et les Colonnes à l aide de Python via Java. 
---

## **Aspose.Cells - Contrôle de la visibilité des lignes & colonnes**
### **Comment masquer des lignes et des colonnes**
Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes HideRow et HideColumn de la collection Cells. Les deux méthodes prennent l'index de la ligne/colonne comme paramètre pour masquer la ligne ou la colonne spécifique.

**Code Ruby**

{{< highlight ruby >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
### **Comment afficher des lignes et des colonnes**
Les développeurs peuvent afficher toute ligne ou colonne masquée en appelant respectivement les méthodes UnhideRow et UnhideColumn de la collection Cells. Les deux méthodes prennent deux paramètres:

- **Index de la ligne ou colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne attribuée à la ligne ou la colonne après l'avoir affichée.

**Code Ruby**

{{< highlight ruby >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Contrôle de la visibilité des lignes & colonnes (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
