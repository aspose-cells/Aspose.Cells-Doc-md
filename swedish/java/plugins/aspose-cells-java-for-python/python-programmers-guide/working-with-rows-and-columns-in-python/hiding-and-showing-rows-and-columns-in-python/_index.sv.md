---
title: Dölja och visa rader och kolumner i Python
type: docs
weight: 50
url: /sv/java/hiding-and-showing-rows-and-columns-in-python/
description: Lär dig hur man döljer och visar rader och kolumner via Aspose.Cells för Python via Java API.
keywords: Hur man döljer och visar rader och kolumner i Python via Java, Dölj rader och kolumner med hjälp av Python via Java, Python via Java Visa rader och kolumner. 
---

## **Aspose.Cells - Kontrollera synligheten av rader & kolumner**
### **Hur man döljer rader och kolumner**
Utvecklare kan dölja en rad eller kolumn genom att anropa HideRow och HideColumn metoderna i Cells-kollektionen respektive. Båda metoderna tar rad/kolumnindexet som parameter för att dölja den specifika raden eller kolumnen.

**Ruby-kod**

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
### **Hur man visar rader och kolumner**
Utvecklare kan återvisa dolda rader eller kolumner genom att anropa UnhideRow och UnhideColumn metoderna i Cells-kollektionen respektive. Båda metoderna tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjd eller kolumnbredd tilldelad till raden eller kolumnen efter att den visas.

**Ruby-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Kontrollera synligheten av rader & kolumner (Aspose.Cells)** från någon av nedanstående sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
