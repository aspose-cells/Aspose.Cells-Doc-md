---
title: Phpでページブレイクプレビュー
type: docs
weight: 60
url: /ja/java/page-break-preview-in-php/
---

## **Aspose.Cells - ページ区切りプレビュー**
**Aspose.Cells Java for PHP**を使用してワークシートをページブレイクプレビューに設定するには、簡単に**PageBreakPreview**モジュールを呼び出してください。

**PHPコード**

{{< highlight php >}}

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
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、Aspose.Cellsのページ区切りプレビューをダウンロードする

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/PageBreakPreview.php)
