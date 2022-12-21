---
title: Ruby で行と列をコピーする
type: docs
weight: 30
url: /ja/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - 行と列のコピー**
### **行のコピー**
Aspose.Cells は、Cells クラスの copyRow メソッドを提供します。このメソッドは、数式、値、コメント、セル形式、非表示のセル、画像、およびその他の描画オブジェクトを含むすべての種類のデータをソース行から宛先行にコピーします。

copyRow メソッドは、次のパラメーターを取ります。

- ソース Cells オブジェクト、
- ソース行インデックス、および
- 宛先行インデックス。

**ルビーコード**

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
### **列のコピー**
Aspose.Cells は Cells クラスの copyColumn メソッドを提供します。このメソッドは、式 (更新された参照を含む) を含むすべてのタイプのデータ、および値、コメント、セル形式、非表示のセル、画像、およびその他の描画オブジェクトをソース列から宛先列にコピーします。

copyColumn メソッドは、次のパラメーターを取ります。

- ソース Cells オブジェクト、
- ソース列インデックス、および
- 宛先列のインデックス。

**ルビーコード**

{{< highlight "ruby" >}}

デフォルトcopy_columns（）

データ_dir = File.dirname(File.dirname(File.dirname(__ファイル__))) + '/データ/'



# Excel ファイル パスによる Workbook オブジェクトのインスタンス化

workbook = Rjb::import('com.aspose.cells.Workbook').new

# Excel ファイルの最初のワークシートにアクセスする

ワークシート = workbook.getWorksheets().get(0)

# データをヘッダー行に入れる (A1:A4)

私は= 0

私がいる間< 5

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
## **実行中のコードをダウンロード**
ダウンロード**行と列のコピー (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
