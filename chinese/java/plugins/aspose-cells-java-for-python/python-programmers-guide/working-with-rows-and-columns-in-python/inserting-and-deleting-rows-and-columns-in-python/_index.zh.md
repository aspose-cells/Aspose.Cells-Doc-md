---
title: 在 Python 中插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, XLT python, XLTX python, insert row python, insert column python, Excel pytho
description: 使用 Python Excel API 在 Python 中创建 Excel 电子表格。在没有 MS Office 的情况下，在 Python 应用程序中插入或删除 XLSX 或 XLS 中的行。
---
## **在 Python 中创建 Excel 电子表格 - 管理行/列**
### **插入一行**
通过调用 Cells 集合的 insertRows 方法在任意位置插入一行。 insertRows 方法将要插入新行的行的索引作为第一个参数，将要插入的行数作为第二个参数。以下是步骤：

- 加载 XLS 或 XLSX 工作簿
- 访问工作表
- 插入行
- 另存为 XLS 或 XLSX 工作簿

**Python 代码**

{{< highlight "python" >}}

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
要向工作表中插入多行，请调用 Cells 集合的 insertRows 方法。 InsertRows 方法有两个参数：

- 行索引，将插入新行的行的索引。
- Number of rows，需要插入的总行数。

**Python 代码**

{{< highlight "python" >}}

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
### **删除一行**
要删除任何位置的行，请调用 Cells 集合的 deleteRows 方法。 DeleteRows 方法有两个参数：

- 行索引，将从中删除行的行的索引。
- 行数，需要删除的总行数。

**Python 代码**

{{< highlight "python" >}}

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
要从工作表中删除多行，请调用 Cells 集合的 deleteRows 方法。 DeleteRows 方法有两个参数：

- 行索引，将从中删除行的行的索引。
- 行数，需要删除的总行数。

**Python 代码**

{{< highlight "python" >}}

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
开发人员还可以通过调用 Cells 集合的 insertColumns 方法在工作表的任意位置插入一列。 insertColumns 方法有两个参数：

- 列索引，将插入列的列的索引
- Number of columns，需要插入的总列数

**Python 代码**

{{< highlight "python" >}}

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
要从工作表中的任何位置删除列，请调用 Cells 集合的 deleteColumns 方法。 deleteColumns 方法采用以下参数：

- 列索引，列将被删除的列的索引。
- 列数，需要删除的总列数。
- Shift cells，布尔型参数，表示删除后单元格是否左移。

**Python 代码**

{{< highlight "python" >}}

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
下载**管理行/列 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
