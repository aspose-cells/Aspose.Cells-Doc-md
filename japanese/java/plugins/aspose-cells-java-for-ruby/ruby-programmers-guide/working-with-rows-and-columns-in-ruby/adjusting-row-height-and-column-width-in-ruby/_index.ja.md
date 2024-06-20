---
title: Ruby で行の高さと列の幅を調整する
type: docs
weight: 10
url: /ja/java/adjusting-row-height-and-column-width-in-ruby/
---

## **Aspose.Cells - 行の高さと列の幅の調整**
### **行の高さの設定**
単一行の高さを設定するには、Cells コレクションの setRowHeight メソッドを呼び出します。setRowHeight メソッドは以下のパラメータを取ります：

- **行インデックス**：高さを変更する行のインデックス。
- **行の高さ**：行に適用する行の高さ。

**Ruby Code**

{{< highlight ruby >}}

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
### **列の幅の設定**
Cells 集合の setColumnWidth メソッドを呼び出すことで、列の幅を設定することが可能です。 setColumnWidth メソッドは、以下のパラメータを取ります。

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**：設定したい列の幅。

**Ruby Code**

{{< highlight ruby >}}

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
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから、**Adjusting Row Height and Column Width (Aspose.Cells)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
