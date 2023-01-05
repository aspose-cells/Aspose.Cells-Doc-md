---
title: Php でのワークシートのコピーと移動
type: docs
weight: 10
url: /ja/java/copying-and-moving-worksheets-in-php/
---
## **Aspose.Cells - ワークシートのコピーと移動**
### **ワークブック内でワークシートをコピーする**
を使用してワークシートをコピーするには**Aspose.Cells PHP で for Java**、 電話**copy_worksheet**方法**コピーワークシート**モジュール。以下にコード例を示します。

**PHP コード**

{{< highlight "php" >}}

 # Create a Worksheets object with reference to the sheets of the Workbook.

$sheets = $workbook->getWorksheets();

\# Copy data to a new sheet from an existing sheet within the Workbook.

$sheets->addCopy("Sheet1");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Copy Worksheet.xls");


{{< /highlight >}}
### **ワークブック内でワークシートを移動する**
を使用してワークシートを移動するには**Aspose.Cells PHP で for Java**、 電話**move_worksheet**方法**コピーワークシート**モジュール。以下にコード例を示します。

**PHP コード**

{{< highlight "php" >}}

 # Get the first worksheet in the book.

$sheet = $workbook->getWorksheets()->get(0);

\# Move the first sheet to the third position in the workbook.

$sheet->moveTo(2);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Move Worksheet.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートのコピーと移動 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/CopyingAndMovingWorksheets.php)
