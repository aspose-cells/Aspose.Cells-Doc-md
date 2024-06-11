---
title: 在Ruby中复制和移动工作表
type: docs
weight: 10
url: /zh/java/copying-and-moving-worksheets-in-ruby/
---

## **Aspose.Cells - 复制和移动工作表**
### **在工作簿内复制工作表**
要在Ruby中使用**Aspose.Cells for Java**复制工作表，调用**copyworksheets**模块的**copy_worksheet**方法。下面是代码示例。

**Ruby 代码**

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
### **在工作簿内移动工作表**
要在Ruby中使用**Aspose.Cells for Java**移动工作表，调用**copyworksheets**模块的**move_worksheet**方法。下面是代码示例。

**Ruby 代码**

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
## **下载运行代码**
从以下任何社交编程网站下载**复制和移动工作表（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
