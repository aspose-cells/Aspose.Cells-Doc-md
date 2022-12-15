---
title: 在 Jython 中复制行和列
type: docs
weight: 30
url: /zh/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - 复制行和列**
使用附加文件**Aspose.Cells Java 对于 Jython**.在这里您可以看到示例代码。

**Jython代码**

{{< highlight "java" >}}

从 aspose-cells 导入设置

从 com.aspose.cells 导入工作簿

类行和列：

定义__在里面__（自己）：



 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



 # 复制行

self.copy_rows()

 # 复制列

self.copy_columns()



 def copy_rows（dataDir）：

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # 通过excel文件路径实例化一个Workbook对象

工作簿 = 工作簿（dataDir + 'Book1.xls'）

 访问 Excel 文件中的第一个工作表

工作表 = workbook.getWorksheets().get(0)

 # 复制包含数据、格式、图像和绘图对象的第二行

 到工作表的第 12 行。

 worksheet.getCells().copyRow(worksheet.getCells(),1,11)

 # 以默认（即Excel 2003）格式保存修改后的Excel文件

workbook.save(dataDir + "复制行.xls")

打印“复制行成功。”



 def copy_columns（dataDir）：

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # 通过excel文件路径实例化一个Workbook对象

工作簿 = 工作簿（）

 访问 Excel 文件中的第一个工作表

工作表 = workbook.getWorksheets().get(0)

 # 将一些数据放入标题行 (A1:A4)

我 = 0

当我< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **下载运行代码**
下载**附加文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
