---
title: Arbeitsblätter kopieren und verschieben in Ruby
type: docs
weight: 10
url: /de/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - Kopieren und Verschieben von Arbeitsblättern**
### **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**
Um ein Arbeitsblatt mit **Aspose.Cells for Java in Ruby** zu kopieren, rufen Sie die Methode **copy_worksheet** des Moduls **copyworksheets** auf. Im Folgenden finden Sie ein Codebeispiel.

**Ruby-Code**

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
### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**
Um ein Arbeitsblatt mit **Aspose.Cells for Java in Ruby** zu verschieben, rufen Sie die Methode **move_worksheet** des Moduls **copyworksheets** auf. Im Folgenden finden Sie ein Codebeispiel.

**Ruby-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Kopieren und Verschieben von Arbeitsblättern (Aspose.Cells)** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
