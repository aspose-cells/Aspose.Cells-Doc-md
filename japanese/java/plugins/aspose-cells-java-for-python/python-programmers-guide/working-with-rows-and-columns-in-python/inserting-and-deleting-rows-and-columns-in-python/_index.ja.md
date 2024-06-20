---
title: Pythonで行および列を挿入および削除
type: docs
weight: 60
url: /ja/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: "PythonでXLSXを作成し、PythonでXLSを作成し、XLS python、XLSX python、XLT python、XLTX python、行を挿入するpython、列を挿入するpython、Excel python"
description: Python Excel APIを使用してPythonでExcelスプレッドシートを作成します。 MS OfficeなしでPythonアプリケーションからXLSXまたはXLSの行を挿入または削除します。
---

## **PythonでExcelスプレッドシートを作成する - 行/列の管理**
### **行の挿入**
CellsコレクションのinsertRowsメソッドを呼び出すことにより、任意の場所に行を挿入します。 insertRowsメソッドは、新しい行が挿入される行のインデックスを最初の引数として、挿入される行の数を2番目の引数として取ります。以下は手順です:

- XLSまたはXLSXワークブックをロード
- ワークシートへのアクセス
- 行を挿入
- XLSまたはXLSXワークブックとして保存

**Pythonコード**

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
### **複数の行の挿入**
ワークシートに複数の行を挿入するには、CellsコレクションのinsertRowsメソッドを呼び出します。InsertRowsメソッドは2つのパラメータを取ります:

- 行インデックス、新しい行が挿入される行のインデックス。
- 行の数、挿入する必要がある合計の行数。

**Pythonコード**

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
### **行の削除**
任意の場所で行を削除するには、CellsコレクションのdeleteRowsメソッドを呼び出します。DeleteRowsメソッドは2つのパラメータを取ります:

- 行インデックス、削除される行のインデックス。
- 行の数、削除する必要がある合計の行数。

**Pythonコード**

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
### **複数の行の削除**
ワークシートから複数の行を削除するには、CellsコレクションのdeleteRowsメソッドを呼び出します。DeleteRowsメソッドは2つのパラメータを取ります:

- 行インデックス、削除される行のインデックス。
- 行の数、削除する必要がある合計の行数。

**Pythonコード**

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
### **列の挿入**
開発者は、CellsコレクションのinsertColumnsメソッドを呼び出すことで、ワークシートに列を任意の場所に挿入することもできます。insertColumnsメソッドには2つのパラメータが必要です:

- 列インデックス: 挿入する列のインデックス
- 列の数、挿入する必要のある合計列数

**Pythonコード**

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
### **列の削除**
任意の場所のワークシートから列を削除するには、CellsコレクションのdeleteColumnsメソッドを呼び出します。deleteColumnsメソッドには以下のパラメータが必要です:

- 列インデックス、列が削除される列のインデックス
- 列の数、削除する必要のある合計列数
- セルのシフト、削除後にセルを左にシフトするかどうかを示すブール値

**Pythonコード**

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
## **ランニングコードのダウンロード**
**Managing Rows/Columns (Aspose.Cells)** を以下に挙げるいずれかのソーシャルコーディングサイトからダウンロード:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
