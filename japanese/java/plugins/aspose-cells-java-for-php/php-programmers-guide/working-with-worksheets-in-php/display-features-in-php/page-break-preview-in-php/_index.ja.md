---
title: PHP での改ページ プレビュー
type: docs
weight: 60
url: /ja/java/page-break-preview-in-php/
---
## **Aspose.Cells - 改ページのプレビュー**
を使用してワークシートを改ページプレビューに設定するには**Aspose.Cells Java for PHP**、単に呼び出す**改ページプレビュー**モジュール。

**PHPコード**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Displaying the worksheet in page break preview

$worksheet->setPageBreakPreview(true);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**改ページプレビュー (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
