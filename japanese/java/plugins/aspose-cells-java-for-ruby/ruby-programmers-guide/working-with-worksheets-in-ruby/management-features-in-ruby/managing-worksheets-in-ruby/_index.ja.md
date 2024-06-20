---
title: Rubyでのワークシートの管理
type: docs
weight: 10
url: /ja/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - ワークシートの管理**
### **新しいExcelファイルにワークシートを追加する**
**Aspose.Cells Java for Ruby** を使用して新しいExcelファイルにワークシートを追加するには、**MangingWorksheets** モジュールの **add_worksheet** メソッドを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **デザイナースプレッドシートにワークシートを追加する**
デザイナースプレッドシートにワークシートを追加するプロセスは、上記のアプローチとまったく同じです。ただし、Excelファイルはすでに作成されており、ワークシートを追加する前にそのExcelファイルを開く必要があります。

**Ruby Code**

{{< highlight ruby >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **シート名を使用してワークシートにアクセスする**
**Aspose.Cells Java for Ruby** を使用してシート名でワークシートにアクセスするには、**MangingWorksheets** モジュールの **get_worksheet** メソッドを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **シート名を使用してワークシートを削除する**
**Aspose.Cells Java for Ruby** を使用してシート名でワークシートを削除するには、**MangingWorksheets** モジュールの **remove_worksheet_by_name** メソッドを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **Sheet Indexを使用してワークシートを削除する**
**Aspose.Cells Java for Ruby** を使用してシートインデックスでワークシートを削除するには、**MangingWorksheets** モジュールの **remove_worksheet_by_index** メソッドを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、**Managing Worksheets (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
