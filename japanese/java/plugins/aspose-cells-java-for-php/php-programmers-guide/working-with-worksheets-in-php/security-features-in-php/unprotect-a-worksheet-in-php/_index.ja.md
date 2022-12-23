---
title: Php でワークシートの保護を解除する
type: docs
weight: 20
url: /ja/java/unprotect-a-worksheet-in-php/
---
## **Aspose.Cells - ワークシートの保護を解除する**
を使用してワークシートを保護するには**Aspose.Cells Java for PHP**、 電話**unprotect_worksheet**方法**保護**モジュール。

**PHP コード**

{{< highlight "php" >}}

 $filesFormatType = new FileFormatType();

//Instantiating a Workbook object

$workbook = new Workbook($dataDir . "book1.xls");

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$protection = $worksheet->getProtection();

//Unprotecting the worksheet with a password

$worksheet->unprotect("aspose");

// Save the excel file.

$workbook->save($dataDir . "output.xls", $filesFormatType->EXCEL_97_TO_2003); 

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートの保護を解除する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/SecurityFeatures/UnprotectingPasswordProtectedWorksheet.php)
