---
title: 在 Ruby 中复制行和列
type: docs
weight: 30
url: /zh/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - 复制行和列**
### **复制行**
Aspose.Cells提供了Cells类的copyRow方法。此方法将所有类型的数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）从源行复制到目标行。

copyRow 方法采用以下参数：

- 源 Cells 对象，
- 源行索引，和
- 目标行索引。

**红宝石代码**

{{< highlight "ruby" >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **复制列**
Aspose.Cells 提供了 Cells 类的 copyColumn 方法，该方法将所有类型的数据，包括公式（带有更新的引用）和值、注释、单元格格式、隐藏单元格、图像和其他绘图对象从源列复制到目标列。

copyColumn 方法采用以下参数：

- 源 Cells 对象，
- 源列索引，和
- 目标列索引。

**红宝石代码**

{{< highlight "ruby" >}}

def copy_columns()

数据_dir = File.dirname(File.dirname(File.dirname(__文件__))) + '/数据/'



# 通过excel文件路径实例化一个Workbook对象

workbook = Rjb::import('com.aspose.cells.Workbook').new

# 访问 Excel 文件中的第一个工作表

工作表 = workbook.getWorksheets().get(0)

# 将一些数据放入标题行 (A1:A4)

我 = 0

当我< 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **下载运行代码**
下载**复制行和列 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
