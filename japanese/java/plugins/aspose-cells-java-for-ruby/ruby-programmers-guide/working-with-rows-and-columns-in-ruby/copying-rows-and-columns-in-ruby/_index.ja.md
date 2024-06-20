---
title: Ruby で行と列をコピー
type: docs
weight: 30
url: /ja/java/copying-rows-and-columns-in-ruby/
---

## **Aspose.Cells - 行と列のコピー**
### **行のコピー**
Aspose.CellsはCellsクラスのcopyRowメソッドを提供しています。このメソッドは、ソース行から宛先行に数式、値、コメント、セルフォーマット、非表示セル、画像、および他の描画オブジェクトを含む、すべての種類のデータをコピーします。

copyRowメソッドには、次のパラメーターがあります：

- ソースのCellsオブジェクト
- ソースの行インデックス、および
- 宛先の行インデックス。

**Ruby Code**

{{< highlight ruby >}}

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
Aspose.CellsはCellsクラスのcopyColumnメソッドを提供しており、このメソッドは、数式（参照を更新）、値、コメント、セルフォーマット、非表示セル、画像、および他の描画オブジェクトを含む、ソース列から宛先列にすべての種類のデータをコピーします。

copyColumnメソッドには、次のパラメーターがあります：

- ソースのCellsオブジェクト
- ソースの列インデックス、および
- 宛先の列インデックス。

**Ruby Code**

{{< highlight ruby >}}

 def copy_columns()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Put some data into header rows (A1:A4)

    i = 0

    while i < 5

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
## **ランニングコードのダウンロード**
以下に挙げるどのソーシャルコーディングサイトから、**行と列のコピー（Aspose.Cells）**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
