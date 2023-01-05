---
title: Php でのワークシートの保護
type: docs
weight: 10
url: /ja/java/protecting-worksheets-in-php/
---
## **Aspose.Cells - ワークシートの保護**
を使用してワークシートを保護するには**Aspose.Cells Java for PHP**、 電話**保護ワークシート**方法**保護**モジュール。

**PHP コード**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$excel = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $excel->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//The following 3 methods are only for Excel 2000 and earlier formats

$protection->setAllowEditingContent(false);

$protection->setAllowEditingObject(false);

$protection->setAllowEditingScenario(false);

//Protects the first worksheet with a password "1234"

$protection->setPassword("1234");

//Saving the modified Excel file in default format

$excel->save($dataDir . "output.xls");  

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートの保護 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/ProtectingWorksheet.php)
