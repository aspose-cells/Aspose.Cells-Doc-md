---
title: Gruppera och avgruppera rader och kolumner i Python
type: docs
weight: 40
url: /sv/java/grouping-and-ungrouping-rows-and-columns-in-python/
description: Lär dig hur du grupperar och avgrupperar rader och kolumner genom Aspose.Cells for Python Via Java API.
keywords: Hur man grupperar och avgrupperar rader och kolumner i Python Via Java, Gruppera rader och kolumner med hjälp av Python Via Java, Python Via Java Avgruppera rader och kolumner. 
---

## **Grupp- och avgrupperingshantering av rader & kolumner i Aspose.Cells for Python via Java**
### **Hur man grupperar rader & kolumner i Python**
Det är möjligt att gruppera rader eller kolumner genom att anropa metoderna groupRows och groupColumns i Cells-samlingen. Båda metoderna tar följande parametrar:

- Första radens/kolumnens index, den första raden eller kolumnen i gruppen.
- Sista radens/kolumnens index, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.

**Python-kod**

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
### **Hur man avgrupperar rader och kolumner med Python**
Avgruppera grupperade rader eller kolumner genom att anropa Cells-samlingens UngroupRows och UngroupColumns metoder. Båda metoderna tar samma parametrar:

- Första radens/kolumnens index, den första raden/kolumnen att avgrupperas.
- Sista radens/kolumnens index, den sista raden/kolumnen att avgrupperas.

**Python-kod**

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
## **Ladda ned körbar kod**
Ladda ner Grupp- och avgruppera rader och kolumner (Aspose.Cells) från någon av de nedan nämnda sociala kodsajterna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
