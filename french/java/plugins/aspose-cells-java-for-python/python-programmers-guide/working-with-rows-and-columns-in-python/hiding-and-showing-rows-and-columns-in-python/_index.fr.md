---
title: Masquer et afficher des lignes et des colonnes dans Python
type: docs
weight: 50
url: /fr/java/hiding-and-showing-rows-and-columns-in-python/
description: Découvrez comment masquer et afficher les lignes et les colonnes via le Aspose.Cells for Python via le Java API.
keywords: How to Hide and Show Rows and Columns in Python Via Java, Hide Rows and Columns using Python Via Java, Python Via Java Show Rows and Columns. 
---
##  **Aspose.Cells - Contrôle de la visibilité des lignes et des colonnes**
###  **Comment masquer les lignes et les colonnes**
Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes HideRow et HideColumn de la collection Cells. Les deux méthodes prennent l'index de ligne/colonne comme paramètre pour masquer la ligne ou la colonne spécifique.

**Code Rubis**

{{< highlight "ruby" >}}

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
###  **Comment afficher les lignes et les colonnes**
Les développeurs peuvent afficher n'importe quelle ligne ou colonne masquée en appelant respectivement les méthodes UnhideRow et UnhideColumn de la collection Cells. Les deux méthodes prennent deux paramètres :

- **Index des colonnes Rowor**l'index d'une ligne ou d'une colonne utilisé pour afficher la ligne ou la colonne spécifique.
- **Hauteur de ligne ou largeur de colonne**- la hauteur de ligne ou la largeur de colonne attribuée à la ligne ou à la colonne après son affichage.

**Code Rubis**

{{< highlight "ruby" >}}

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
##  **Télécharger le code d'exécution**
 Télécharger**Contrôle de la visibilité des lignes et des colonnes (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
