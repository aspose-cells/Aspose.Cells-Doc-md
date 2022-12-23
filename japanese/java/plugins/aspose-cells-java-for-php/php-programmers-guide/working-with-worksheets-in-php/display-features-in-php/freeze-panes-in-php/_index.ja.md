---
title: Phpでペインをフリーズ
type: docs
weight: 40
url: /ja/java/freeze-panes-in-php/
---
## **Aspose.Cells - フリーズペイン**
を使用してスプレッドシート ドキュメントのペインを固定するには**Aspose.Cells Java for PHP**、単に呼び出す**FreezePanes**モジュール。

**PHP コード**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**フリーズペイン (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
