---
title: Regroupement et dissociation de lignes et de colonnes dans Python
type: docs
weight: 40
url: /fr/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Découvrez comment regrouper et dissocier des lignes et des colonnes via le Aspose.Cells for Python via Java API.
keywords: How to Group and Ungroup Rows and Columns in Python Via Java, Group Rows and Columns using Python Via Java, Python Via Java Ungroup Rows and Columns. 
---
##  **Gestion des groupes et des dissociations des lignes et des colonnes dans Aspose.Cells for Python via Java**
###  **Comment regrouper des lignes et des colonnes dans Python**
Il est possible de regrouper des lignes ou des colonnes en appelant les méthodes groupRows et groupColumns de la collection Cells. Les deux méthodes prennent les paramètres suivants :

- Index de première ligne/colonne, première ligne ou colonne du groupe.
- Index de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est masqué, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

**Python Code**

{{< highlight "python" >}}

 def group_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Grouping first six rows (from 0 to 5) and making them hidden by passing true

cells.groupRows(0,5,True)

\# Grouping first three columns (from 0 to 2) and making them hidden by passing true

cells.groupColumns(0,2,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Group Rows And Columns.xls")

print "Group Rows And Columns Successfully." 

{{< /highlight >}}
###  **Comment dissocier les lignes et les colonnes à l'aide de Python**
Dissociez les lignes ou les colonnes groupées en appelant les méthodes UngroupRows et UngroupColumns de la collection Cells. Les deux méthodes prennent les mêmes paramètres :

- Index de première ligne ou de colonne, première ligne/colonne à dissocier.
- Index de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

**Python Code**

{{< highlight "python" >}}

 def ungroup_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Ungrouping first six rows (from 0 to 5)

cells.ungroupRows(0,5)

\# Ungrouping first three columns (from 0 to 2)

cells.ungroupColumns(0,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")

print "Ungroup Rows And Columns Successfully." 

{{< /highlight >}}
##  **Télécharger le code d'exécution**
 Télécharger**Regrouper et dissocier les lignes et les colonnes (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
