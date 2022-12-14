---
title: Kopieren und Verschieben von Arbeitsblättern in Ruby
type: docs
weight: 10
url: /de/java/copying-and-moving-worksheets-in-ruby/
---
## **Aspose.Cells – Kopieren und Verschieben von Arbeitsblättern**
### **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**
 Arbeitsblatt kopieren mit**Aspose.Cells for Java in Rubin** , Anruf**copy_worksheet** Methode von**Arbeitsblätter kopieren** Modul. Unten sehen Sie ein Codebeispiel.

**Ruby-Code**

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
### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**
 Arbeitsblatt verschieben mit**Aspose.Cells for Java in Rubin** , Anruf**move_worksheet** Methode von**Arbeitsblätter kopieren** Modul. Unten sehen Sie ein Codebeispiel.

**Ruby-Code**

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
## **Laufcode herunterladen**
Download**Arbeitsblätter kopieren und verschieben (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
