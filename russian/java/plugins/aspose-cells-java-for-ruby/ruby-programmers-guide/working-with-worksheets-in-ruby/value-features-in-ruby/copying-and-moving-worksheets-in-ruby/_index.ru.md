---
title: Копирование и перемещение листов в Ruby
type: docs
weight: 10
url: /ru/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - Копирование и перемещение листов**
### **Копировать листы в рамках рабочей книги**
Чтобы скопировать лист с помощью **Aspose.Cells for Java в Ruby**, вызовите метод **copy_worksheet** модуля **copyworksheets**. Ниже приведен пример кода.

**Код на Ruby**

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
### **Перемещение листов в рамках книги**
Чтобы переместить лист с помощью **Aspose.Cells for Java в Ruby**, вызовите метод **move_worksheet** модуля **copyworksheets**. Ниже приведен пример кода.

**Код на Ruby**

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
## **Скачать работающий код**
Загрузите **Копирование и перемещение листов (Aspose.Cells)** с любого из указанных ниже социальных сайтов для разработки:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
