---
title: Ruby でのワークシートの管理
type: docs
weight: 10
url: /ja/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells - ワークシートの管理**
### **新しい Excel ファイルへのワークシートの追加**
を使用して新しい Excel ファイルにワークシートを追加するには**Aspose.Cells Ruby の場合は Java**、単に呼び出す**add_worksheet**方法**ワークシートの管理**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

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
### **Designer スプレッドシートへのワークシートの追加**
ワークシートをデザイナー スプレッドシートに追加するプロセスは、Excel ファイルが既に作成されており、ワークシートを追加する前にまずその Excel ファイルを開く必要があることを除いて、上記のアプローチのプロセスとまったく同じです。

**ルビーコード**

{{< highlight "ruby" >}}

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
を使用してシート名でワークシートにアクセスするには**Aspose.Cells Ruby の場合は Java**、単に呼び出す**get_worksheet**方法**ワークシートの管理**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

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
を使用してシート名でワークシートを削除するには**Aspose.Cells Ruby の場合は Java**、単に呼び出す**remove_worksheet_by_name**方法**ワークシートの管理**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

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
### **シート インデックスを使用してワークシートを削除する**
を使用してシート インデックスごとにワークシートを削除するには**Aspose.Cells Ruby の場合は Java**、単に呼び出す**remove_worksheet_by_index**方法**ワークシートの管理**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

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
## **実行中のコードをダウンロード**
ダウンロード**ワークシートの管理 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
