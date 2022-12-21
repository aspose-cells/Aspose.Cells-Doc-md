---
title: Ruby での行と列の挿入と削除
type: docs
weight: 60
url: /ja/java/inserting-and-deleting-rows-and-columns-in-ruby/
---
## **Aspose.Cells - 行/列の管理**
### **行の挿入**
Cells コレクションの insertRows メソッドを呼び出して、任意の場所に行を挿入します。 insertRows メソッドは、新しい行が挿入される行のインデックスを最初の引数として取り、挿入される行の数を 2 番目の引数として取ります。

**ルビーコード**

{{< highlight "ruby" >}}

 def insert_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Row.xls")

    puts "Insert Row Successfully."

end   

{{< /highlight >}}
### **複数行の挿入**
ワークシートに複数の行を挿入するには、Cells コレクションの insertRows メソッドを呼び出します。 InsertRows メソッドは、次の 2 つのパラメーターを取ります。

- 行インデックス。新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の総数。

**ルビーコード**

{{< highlight "ruby" >}}

 def insert_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a row into the worksheet at 3rd position

    worksheet.getCells().insertRows(2,10)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Multiple Rows.xls")

    puts "Insert Multiple Rows Successfully."

end

{{< /highlight >}}
### **行の削除**
任意の場所で行を削除するには、Cells コレクションの deleteRows メソッドを呼び出します。 DeleteRows メソッドは、次の 2 つのパラメーターを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数、削除する必要がある行の総数。

**ルビーコード**

{{< highlight "ruby" >}}

 def delete_row()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 3rd row from the worksheet

    worksheet.getCells().deleteRows(2,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Row.xls")

    puts "Delete Row Successfully."

end

{{< /highlight >}}
### **複数行の削除**
ワークシートから複数の行を削除するには、Cells コレクションの deleteRows メソッドを呼び出します。 DeleteRows メソッドは、次の 2 つのパラメーターを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数、削除する必要がある行の総数。

**ルビーコード**

{{< highlight "ruby" >}}

 def delete_multiple_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting 10 rows from the worksheet starting from 3rd row

    worksheet.getCells().deleteRows(2,10,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Multiple Rows.xls")

    puts "Delete Multiple Rows Successfully."

end 

{{< /highlight >}}
### **列の挿入**
開発者は、Cells コレクションの insertColumns メソッドを呼び出して、ワークシートの任意の場所に列を挿入することもできます。 insertColumns メソッドは 2 つのパラメーターを取ります。

- 列インデックス、列が挿入される列のインデックス
- 列数、挿入が必要な列の総数

**ルビーコード**

{{< highlight "ruby" >}}

 def insert_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Inserting a column into the worksheet at 2nd position

    worksheet.getCells().insertColumns(1,1)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Insert Column.xls")

    puts "Insert Column Successfully."

end  

{{< /highlight >}}
### **列の削除**
ワークシートの任意の場所から列を削除するには、Cells コレクションの deleteColumns メソッドを呼び出します。 deleteColumns メソッドは、次のパラメーターを取ります。

- 列インデックス、列が削除される列のインデックス。
- 列数、削除する必要がある列の総数。
- セルをシフトします。削除後にセルを左にシフトするかどうかを示すブール型パラメーター。

**ルビーコード**

{{< highlight "ruby" >}}

 def delete_column()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Deleting a column from the worksheet at 2nd position

    worksheet.getCells().deleteColumns(1,1,true)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Delete Column.xls")

    puts "Delete Column Successfully."

end   

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**行/列の管理 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
