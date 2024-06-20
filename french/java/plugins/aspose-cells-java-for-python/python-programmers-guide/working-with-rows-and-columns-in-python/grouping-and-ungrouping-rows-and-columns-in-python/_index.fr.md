---
title: Regrouper et dégrouper des lignes et des colonnes en Python
type: docs
weight: 40
url: /fr/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Apprenez à regrouper et dégrouper des lignes et des colonnes à travers l API Aspose.Cells pour Python via Java.
keywords: Comment regrouper et dégrouper des lignes et des colonnes en Python via Java, regrouper des lignes et des colonnes en utilisant Python via Java, dégrouper des lignes et des colonnes en Python via Java. 
---

## **Gestion du regroupement et du dégroupement des lignes et des colonnes dans Aspose.Cells pour Python via Java**
### **Comment regrouper des lignes et des colonnes en Python**
Il est possible de regrouper des lignes ou des colonnes en appelant les méthodes groupRows et groupColumns de la collection Cells. Les deux méthodes prennent les paramètres suivants:

- Indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- Indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

**Code Python**

{{< highlight python >}}

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
### **Comment dégrouper des lignes et des colonnes à l'aide de Python**
Dégrouper les lignes ou les colonnes groupées en appelant les méthodes UngroupRows et UngroupColumns de la collection Cells. Les deux méthodes prennent les mêmes paramètres:

- Indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- Indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

**Code Python**

{{< highlight python >}}

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Grouper et Dégrouper des lignes et des colonnes (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
