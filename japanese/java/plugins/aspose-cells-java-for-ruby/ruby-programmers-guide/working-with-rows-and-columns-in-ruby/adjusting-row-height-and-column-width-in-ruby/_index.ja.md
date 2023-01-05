---
title: Ruby で行の高さと列の幅を調整する
type: docs
weight: 10
url: /ja/java/adjusting-row-height-and-column-width-in-ruby/
---
## **Aspose.Cells - 行の高さと列の幅の調整**
### **行の高さの設定**
Cells コレクションの setRowHeight メソッドを呼び出すことで、1 行の高さを設定できます。 setRowHeight メソッドは、次のパラメーターを取ります。

- **行インデックス**、高さを変更する行のインデックス。
- **行の高さ**、行に適用する行の高さ。

**ルビーコード**

{{< highlight "ruby" >}}

 def set_row_height()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Setting the height of the second row to 13

    cells.setRowHeight(1, 13)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Set Row Height.xls")

    puts "Set Row Height Successfully."

end

{{< /highlight >}}
### **列幅の設定**
Cells コレクションの setColumnWidth メソッドを呼び出して、列の幅を設定します。 setColumnWidth メソッドは、次のパラメーターを取ります。

- **列インデックス**、幅を変更する列のインデックス。
- **列幅**、目的の列幅。

**ルビーコード**

{{< highlight "ruby" >}}

 def set_column_width()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    cells = worksheet.getCells()

    # Setting the width of the second column to 17.5

    cells.setColumnWidth(1, 17.5)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Set Column Width.xls")

    puts "Set Column Width Successfully."

end

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**行の高さと列の幅を調整する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
