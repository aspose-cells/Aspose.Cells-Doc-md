---
title: Infoga och ta bort rader och kolumner i Python
type: docs
weight: 60
url: /sv/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "skapa XLSX i Python, skapa XLS i Python, XLS python, XLSX python, XLT python, XLTX python, infoga rad python, infoga kolumn python, Excel python"
description: Använd Python Excel API för att skapa Excelspridblad i Python. Infoga eller ta bort rader från XLSX eller XLS i dina Python applikationer utan MS Office.
---

## **Skapa Excelspridblad i Python - Hantera rader/kolumner**
### **Infoga en rad**
Infoga en rad på valfri plats genom att anropa metoden insertRows i Cells-samlingen. Metoden insertRows tar index för raden där den nya raden ska infogas som första argument, och antalet rader som ska infogas som andra argument. Följande är stegen:

- Läs in XLS- eller XLSX-arbetsbok
- Öppna arket
- Infoga raden
- Spara som XLS- eller XLSX-arbetsbok

**Python-kod**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **Infoga flera rader**
För att infoga flera rader i arket, anropa insertRows metoden i Cells-kollektionen. InsertRows metoden tar två parametrar:

- Radindex, index för raden från vilken de nya raderna ska infogas.
- Antal rader, totalt antal rader som behöver infogas.

**Python-kod**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **Ta bort en rad**
För att ta bort en rad på valfri plats, anropa deleteRows metoden i Cells-kollektionen. DeleteRows metoden tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**Python-kod**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **Ta bort flera rader**
För att ta bort flera rader från ett kalkylblad, anropa deleteRows metoden i Cells-kollektionen. DeleteRows metoden tar två parametrar:

- Radindex, index för raden från vilken raderna ska tas bort.
- Antal rader, totalt antal rader som behöver raderas.

**Python-kod**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **Infoga en kolumn**
Utvecklare kan också infoga en kolumn i arbetsbladet på valfri plats genom att anropa metoden insertColumns i Cells-samlingen. insertColumns-metoden tar två parametrar:

- Kolumnindex, index av kolumn där kolumnen ska infogas
- Antal kolumner, totalt antal kolumner som behöver infogas

**Python-kod**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **Ta bort en kolumn**
För att ta bort en kolumn från arbetsbladet på valfri plats, anropas deleteColumns-metoden i Cells-samlingen. deleteColumns-metoden tar följande parametrar:

- Kolumnindex, index av kolumn där kolumnen ska tas bort.
- Antal kolumner, totalt antal kolumner som behöver tas bort.
- Skifta celler, en boolesk parameter för att indikera om cellerna ska skiftas åt vänster efter borttagning.

**Python-kod**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ned **Hantering av rader/kolumner (Aspose.Cells)** från någon av de nämnda sociala kodsajterna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
