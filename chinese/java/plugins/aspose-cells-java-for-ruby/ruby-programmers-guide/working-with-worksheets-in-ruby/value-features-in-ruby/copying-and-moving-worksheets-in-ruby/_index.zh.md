---
title: 在 Ruby 中复制和移动工作表
type: docs
weight: 10
url: /zh/java/copying-and-moving-worksheets-in-ruby/
---
## **Aspose.Cells - 复制和移动工作表**
### **在工作簿中复制工作表**
使用复制工作表**红宝石中的 Aspose.Cells for Java**， 称呼**复制工作表**的方法**抄作业**模块。您可以在下面看到代码示例。

**红宝石代码**

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
### **在工作簿中移动工作表**
使用移动工作表**红宝石中的 Aspose.Cells for Java**， 称呼**移动工作表**的方法**抄作业**模块。您可以在下面看到代码示例。

**红宝石代码**

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
## **下载运行代码**
下载**复制和移动工作表 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/copyworksheets.rb)
