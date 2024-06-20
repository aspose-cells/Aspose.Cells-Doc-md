---
title: Kopiera och flytta kalkylblad i Ruby
type: docs
weight: 10
url: /sv/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - Kopiera och flytta kalkylblad**
### **Kopiera Kalkylblad inom en Arbetsbok**
För att kopiera kalkylblad med **Aspose.Cells for Java i Ruby**, anropa **copy_worksheet**-metoden i **copyworksheets**-modulen. Nedan kan du se kodexemplet.

**Ruby-kod**

{{< highlight ruby >}}

 def copy_worksheet(workbook)

    # Create a Worksheets object with reference to the sheets of the Workbook.

    sheets = workbook.getWorksheets()

    # Copy data to a new sheet from an existing sheet within the Workbook.

    sheets.addCopy("Sheet1")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Copy Worksheet.xls")

    puts "Copy worksheet, please check the output file."

end 

{{< /highlight >}}
### **Flytta kalkylblad inom en arbetsbok**
För att flytta kalkylblad med **Aspose.Cells for Java i Ruby**, anropa **move_worksheet**-metoden i **copyworksheets**-modulen. Nedan kan du se kodexemplet.

**Ruby-kod**

{{< highlight ruby >}}

 def move_worksheet(workbook)

    # Get the first worksheet in the book.

    sheet = workbook.getWorksheets().get(0)

    # Move the first sheet to the third position in the workbook.

    sheet.moveTo(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Move Worksheet.xls")

    puts "Move worksheet, please check the output file."

end 

{{< /highlight >}}
## **Ladda ned körbar kod**
Hämta **Kopiera och Flytta Arbeitsblad (Aspose.Cells)** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
