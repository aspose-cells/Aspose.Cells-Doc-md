---
title: Php でのワークシートの管理
type: docs
weight: 10
url: /ja/java/managing-worksheets-in-php/
---
## **Aspose.Cells - ワークシートの管理**
### **新しい Excel ファイルへのワークシートの追加**
を使用して新しい Excel ファイルにワークシートを追加するには**Aspose.Cells Java for PHP**、単に呼び出す**add_worksheet**方法**ワークシートの管理**モジュール。

**PHPコード**

{{< highlight "php" >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **シート名を使用してワークシートを削除する**
を使用してシート名でワークシートを削除するには**Aspose.Cells Java for PHP**、単に呼び出す**remove_worksheet_by_name**方法**ワークシートの管理**モジュール。

**PHPコード**

{{< highlight "php" >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **シート インデックスを使用してワークシートを削除する**
を使用してシート インデックスごとにワークシートを削除するには**Aspose.Cells Java for PHP**、単に呼び出す**remove_worksheet_by_index**方法**ワークシートの管理**モジュール。

**PHPコード**

{{< highlight "php" >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートの管理 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
