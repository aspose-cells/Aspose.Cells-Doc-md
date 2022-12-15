---
title: Kopiera och flytta arbetsblad på Python
type: docs
weight: 10
url: /sv/java/copying-and-moving-worksheets-in-python/
---
## **Aspose.Cells - Kopiera och flytta arbetsblad**
### **Kopiera arbetsblad i en arbetsbok**
 För att kopiera kalkylblad med**Aspose.Cells for Java i Ruby** , ringa upp**copy_worksheet** metod av**copyworksheets** modul. Nedan kan du se kodexempel.

**Python Kod**

{{< highlight "java" >}}

 def copy_worksheet(self):  

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")


\# Create a Worksheets object with reference to the sheets of the Workbook.

sheets = workbook.getWorksheets()

\# Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Worksheet.xls")

print "Copy worksheet, please check the output file."

h5. Move Worksheets within a Workbook


{color:#333333}To move worksheet using{color} {color:#333333}{*}Aspose.Cells for Java in Ruby{*}{color}{color:#333333}, call{color} {color:#333333}{*}move_worksheet{*}{color} {color:#333333}method of{color} {color:#333333}{*}copyworksheets{*}{color} {color:#333333}module. Below you can see code example.{color}

{code:language=python|title= Python Code }

def move_worksheet(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")


\# Get the first worksheet in the book.

sheet = workbook.getWorksheets().get(0)

\# Move the first sheet to the third position in the workbook.

sheet.moveTo(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Move_Worksheet.xls")

print "Move worksheet, please check the output file."

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Kopiera och flytta arbetsblad (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
