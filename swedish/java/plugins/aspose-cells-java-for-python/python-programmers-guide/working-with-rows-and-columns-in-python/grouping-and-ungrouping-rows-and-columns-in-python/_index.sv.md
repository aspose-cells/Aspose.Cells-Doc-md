---
title: Gruppera och dela upp rader och kolumner i Python
type: docs
weight: 40
url: /sv/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Lär dig hur du grupperar och delar upp rader och kolumner via Aspose.Cells for Python Via Java API.
keywords: How to Group and Ungroup Rows and Columns in Python Via Java, Group Rows and Columns using Python Via Java, Python Via Java Ungroup Rows and Columns. 
---
##  **Grupp- och dela upp hantering av rader och kolumner i Aspose.Cells for Python via Java**
###  **Så här grupperar du rader och kolumner i Python**
Det är möjligt att gruppera rader eller kolumner genom att anropa metoderna groupRows och groupColumns i samlingen Cells. Båda metoderna tar följande parametrar:

- Första rad-/kolumnindex, den första raden eller kolumnen i gruppen.
- Sista raden/kolumnindex, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som anger om rader/kolumner ska döljas efter gruppering eller inte.

**Python Kod**

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
###  **Så här delar du upp rader och kolumner med Python**
Dela upp grupperade rader eller kolumner genom att anropa Cells-samlingens metoder för UgroupRows och UngroupColumns. Båda metoderna tar samma parametrar:

- Första raden eller kolumnindex, den första raden/kolumnen som ska delas upp.
- Sista raden eller kolumnindex, den sista raden/kolumnen som ska delas upp.

**Python Kod**

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
##  **Ladda ner Running Code**
 Ladda ner**Gruppera och dela upp rader och kolumner (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
