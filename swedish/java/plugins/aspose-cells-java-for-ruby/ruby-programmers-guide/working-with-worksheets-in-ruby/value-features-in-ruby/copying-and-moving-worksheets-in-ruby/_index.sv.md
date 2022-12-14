---
title: Kopiera och flytta arbetsblad i Ruby
type: docs
weight: 10
url: /sv/java/copying-and-moving-worksheets-in-ruby/
---
## **Aspose.Cells - Kopiera och flytta arbetsblad**
### **Kopiera arbetsblad i en arbetsbok**
 För att kopiera kalkylblad med**Aspose.Cells för Java i Ruby** , ringa upp**copy_worksheet** metod av**copyworksheets** modul. Nedan kan du se kodexempel.

**Ruby kod**

{{< highlight "ruby" >}}

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
### **Flytta kalkylblad i en arbetsbok**
 För att flytta kalkylblad med**Aspose.Cells för Java i Ruby** , ringa upp**move_worksheet** metod av**copyworksheets** modul. Nedan kan du se kodexempel.

**Ruby kod**

{{< highlight "ruby" >}}

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
## **Ladda ner Running Code**
Ladda ner**Kopiera och flytta arbetsblad (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
