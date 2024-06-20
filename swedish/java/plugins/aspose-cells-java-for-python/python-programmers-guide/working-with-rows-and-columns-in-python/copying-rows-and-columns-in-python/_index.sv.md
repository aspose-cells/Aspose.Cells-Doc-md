---
title: Kopiera rader och kolumner i Python
type: docs
weight: 30
url: /sv/java/copying-rows-and-columns-in-python/
---

## **Aspose.Cells - Kopiera rader och kolumner**
### **Kopiera rader**
Aspose.Cells tillhandahåller metoden copyRow av klassen Cells. Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till destinationsraden.

Metoden copyRow tar följande parametrar:

- källobjektet Cells,
- källradens index, och
- destinationsradens index.

**Python-kod**

{{< highlight java >}}

 def copy_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Copy the second row with data, formattings, images and drawing objects

\# to the 12th row in the worksheet.

worksheet.getCells().copyRow(worksheet.getCells(),1,11)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Rows.xls")

print "Copy Rows Successfully." 

{{< /highlight >}}
### **Kopiera kolumner**
Aspose.Cells tillhandahåller metoden copyColumn av klassen Cells, denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källkolumnen till destinationskolumnen.

Metoden copyColumn tar följande parametrar:

- källobjektet Cells,
- källkolumnens index och
- destinationskolumnens index.

**Python-kod**

{{< highlight ruby >}}



def copy_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Put some data into header rows (A1:A4)

i = 0

while i < 5:

worksheet.getCells().get(i, 0).setValue("Header Row #i")





\# Put some detail data (A5:A999)

i = 5

while i < 1000:

worksheet.getCells().get(i, 0).setValue("Detail Row #i")


\# Create another Workbook.

workbook1 = Workbook()

\# Get the first worksheet in the book.

worksheet1 = workbook1.getWorksheets().get(0)

\# Copy the first column from the first worksheet of the first workbook into

\# the first worksheet of the second workbook.

worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

\# Autofit the column.

worksheet1.autoFitColumn(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Columns.xls")

print "Copy Columns Successfully." 

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Kopiera rader och kolumner (Aspose.Cells)** från någon av nedan nämnda sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
