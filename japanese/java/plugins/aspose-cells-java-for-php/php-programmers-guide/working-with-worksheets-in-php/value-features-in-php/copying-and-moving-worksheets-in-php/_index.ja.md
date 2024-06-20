---
title: Phpでのワークシートのコピーと移動
type: docs
weight: 10
url: /ja/java/copying-and-moving-worksheets-in-php/
---

## **Aspose.Cells - ワークシートのコピーと移動**
### **ブック内でのワークシートのコピー**
**PHPでAspose.Cells for Javaを使用してワークシートをコピーする**場合は、**copyworksheets**モジュールの**copy_worksheet**メソッドを呼び出します。以下に、コード例が示されています。

**PHPコード**

{{< highlight php >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **ワークブック内でワークシートを移動する**
**PHPでAspose.Cells for Javaを使用してワークシートを移動する**場合は、**copyworksheets**モジュールの**move_worksheet**メソッドを呼び出します。以下に、コード例が示されています。

**PHPコード**

{{< highlight php >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のどちらかのソーシャルコーディングサイトから、**Aspose.Cells**の**ワークシートのコピーと移動**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
