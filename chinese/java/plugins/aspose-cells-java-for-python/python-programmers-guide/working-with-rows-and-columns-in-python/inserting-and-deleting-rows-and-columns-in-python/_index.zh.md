---
title: 在Python中插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "在Python中创建XLSX，在Python中创建XLS，XLS python，XLSX python，XLT python，XLTX python，插入行python，插入列python，Excel python"
description: 使用Python Excel API在Python中创建Excel电子表格。在您的Python应用程序中无需MS Office即可插入或删除XLSX或XLS中的行。
---

## **在Python中创建Excel电子表格 - 管理行/列**
### **插入行**
通过调用单元格集合的insertRows方法在任意位置插入行。insertRows方法将插入新行的行索引作为第一个参数，要插入的行数作为第二个参数。以下是步骤：

- 加载XLS或XLSX工作簿
- 访问工作表
- 插入行
- 保存为XLS或XLSX工作簿

**Python 代码**

{{< highlight python >}}

 def insert_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Row.xls")

print "Insert Row Successfully." 

{{< /highlight >}}
### **插入多行**
要在工作表中插入多行，请调用 Cells 集合的 insertRows 方法。InsertRows 方法需要两个参数：

- 行索引，新行将从该行插入。
- 行数，需要插入的总行数。

**Python 代码**

{{< highlight python >}}

 def insert_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a row into the worksheet at 3rd position

worksheet.getCells().insertRows(2,10)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Multiple Rows.xls")

print "Insert Multiple Rows Successfully." 


{{< /highlight >}}
### **删除行**
要在任何位置删除行，请调用 Cells 集合的 deleteRows 方法。DeleteRows 方法需要两个参数：

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

**Python 代码**

{{< highlight python >}}

 def delete_row(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 3rd row from the worksheet

worksheet.getCells().deleteRows(2,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Row.xls")

print "Delete Row Successfully." 

{{< /highlight >}}
### **删除多行**
要从工作表中删除多行，请调用 Cells 集合的 deleteRows 方法。DeleteRows 方法需要两个参数：

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

**Python 代码**

{{< highlight python >}}

 def delete_multiple_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting 10 rows from the worksheet starting from 3rd row

worksheet.getCells().deleteRows(2,10,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Multiple Rows.xls")

print "Delete Multiple Rows Successfully." 


{{< /highlight >}}
### **插入列**
开发人员还可以通过调用Cells集合的insertColumns方法在工作表的任意位置插入一列。insertColumns方法需要两个参数:

- 列索引，需要插入列的索引
- 列数，需要插入的列的总数

**Python 代码**

{{< highlight python >}}

 def insert_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Inserting a column into the worksheet at 2nd position

worksheet.getCells().insertColumns(1,1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Insert Column.xls")

print "Insert Column Successfully." 


{{< /highlight >}}
### **删除列**
要从工作表的任意位置删除一列，调用Cells集合的deleteColumns方法。deleteColumns方法需要以下参数:

- 列索引，需要删除列的索引
- 列数，需要删除的列的总数
- 移动单元格，布尔参数，指示删除后是否左移单元格

**Python 代码**

{{< highlight python >}}

 def delete_column(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Deleting a column from the worksheet at 2nd position

worksheet.getCells().deleteColumns(1,1,True)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Delete Column.xls")

print "Delete Column Successfully." 


{{< /highlight >}}
## **下载运行代码**
从以下社会编码网站中下载**管理行/列（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
