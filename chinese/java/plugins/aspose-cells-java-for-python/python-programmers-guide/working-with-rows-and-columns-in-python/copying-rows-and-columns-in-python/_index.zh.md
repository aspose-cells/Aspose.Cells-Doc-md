---
title: 在 Python 中复制行和列
type: docs
weight: 30
url: /zh/java/copying-rows-and-columns-in-python/
---
## **Aspose.Cells - 复制行和列**
### **复制行**
Aspose.Cells提供了Cells类的copyRow方法。此方法将所有类型的数据（包括公式、值、注释、单元格格式、隐藏单元格、图像和其他绘图对象）从源行复制到目标行。

copyRow 方法采用以下参数：

- 源 Cells 对象，
- 源行索引，和
- 目标行索引。

**Python 代码**

{{< highlight "java" >}}

 def copy_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Copy the second row with data, formattings, images and drawing objects

\# to the 12th row in the worksheet.

worksheet.getCells().copyRow(worksheet.getCells(),1,11)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Rows.xls")

print "Copy Rows Successfully." 

{{< /highlight >}}
### **复制列**
Aspose.Cells 提供了 Cells 类的 copyColumn 方法，该方法将所有类型的数据，包括公式（带有更新的引用）和值、注释、单元格格式、隐藏单元格、图像和其他绘图对象从源列复制到目标列。

copyColumn 方法采用以下参数：

- 源 Cells 对象，
- 源列索引，和
- 目标列索引。

**Python 代码**

{{< highlight "ruby" >}}



def copy_columns（自我）：

\# 通过excel文件路径实例化一个Workbook对象

工作簿 = self.Workbook()

\# 访问 Excel 文件中的第一个工作表

工作表 = workbook.getWorksheets().get(0)

\# 将一些数据放入标题行 (A1:A4)

我 = 0

当我< 5:

worksheet.getCells().get(i, 0).setValue("Header Row #i")





\# Put some detail data (A5:A999)

i = 5

while i < 1000:

worksheet.getCells().get(i, 0).setValue("Detail Row #i")


\# Create another Workbook.

workbook1 = Workbook()

\# Get the first worksheet in the book.

worksheet1 = workbook1.getWorksheets().get(0)

\# Copy the first column from the first worksheet of the first workbook into

\# the first worksheet of the second workbook.

worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

\# Autofit the column.

worksheet1.autoFitColumn(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Columns.xls")

print "Copy Columns Successfully." 

{{< /highlight >}}
## **下载运行代码**
下载**复制行和列 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
