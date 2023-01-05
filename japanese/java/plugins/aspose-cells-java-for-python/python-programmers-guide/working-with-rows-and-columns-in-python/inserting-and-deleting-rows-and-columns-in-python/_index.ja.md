---
title: Python の行と列の挿入と削除
type: docs
weight: 60
url: /ja/java/inserting-and-deleting-rows-and-columns-in-python/
keywords: create XLSX in Python, create XLS in Python, XLS python, XLSX python, XLT python, XLTX python, insert row python, insert column python, Excel pytho
description: Python Excel API を使用して、Python で Excel スプレッドシートを作成します。MS Office を使用しない Python アプリケーションで、XLSX または XLS から行を挿入または削除します。
---
## **Python で Excel スプレッドシートを作成する - 行/列の管理**
### **行の挿入**
Cells コレクションの insertRows メソッドを呼び出して、任意の場所に行を挿入します。 insertRows メソッドは、新しい行が挿入される行のインデックスを最初の引数として取り、挿入される行の数を 2 番目の引数として取ります。手順は次のとおりです。

- XLS または XLSX ワークブックを読み込む
- ワークシートにアクセスする
- 行を挿入する
- XLS または XLSX ワークブックとして保存

**Python コード**

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
### **複数行の挿入**
ワークシートに複数の行を挿入するには、Cells コレクションの insertRows メソッドを呼び出します。 InsertRows メソッドは、次の 2 つのパラメーターを取ります。

- 行インデックス。新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の総数。

**Python コード**

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
### **行の削除**
任意の場所で行を削除するには、Cells コレクションの deleteRows メソッドを呼び出します。 DeleteRows メソッドは、次の 2 つのパラメーターを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数、削除する必要がある行の総数。

**Python コード**

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
### **複数行の削除**
ワークシートから複数の行を削除するには、Cells コレクションの deleteRows メソッドを呼び出します。 DeleteRows メソッドは、次の 2 つのパラメーターを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数、削除する必要がある行の総数。

**Python コード**

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
### **列の挿入**
開発者は、Cells コレクションの insertColumns メソッドを呼び出して、ワークシートの任意の場所に列を挿入することもできます。 insertColumns メソッドは 2 つのパラメーターを取ります。

- 列インデックス、列が挿入される列のインデックス
- 列数、挿入が必要な列の総数

**Python コード**

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
### **列の削除**
ワークシートの任意の場所から列を削除するには、Cells コレクションの deleteColumns メソッドを呼び出します。 deleteColumns メソッドは、次のパラメーターを取ります。

- 列インデックス、列が削除される列のインデックス。
- 列数、削除する必要がある列の総数。
- セルをシフトします。削除後にセルを左にシフトするかどうかを示すブール型パラメーター。

**Python コード**

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
## **実行中のコードをダウンロード**
ダウンロード**行/列の管理 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
