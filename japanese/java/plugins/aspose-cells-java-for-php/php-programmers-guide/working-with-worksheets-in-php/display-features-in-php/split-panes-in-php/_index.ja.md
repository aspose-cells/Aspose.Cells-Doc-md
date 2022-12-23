---
title: Php でペインを分割する
type: docs
weight: 70
url: /ja/java/split-panes-in-php/
---
## **Aspose.Cells - ペインの分割**
を使用してペインを分割するには**Aspose.Cells Java for PHP**、単に呼び出す**SplitPanes**モジュール。

**PHP コード**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

//Instantiate a new workbook

//Open a template file

$book = new Workbook($dataDir . "book.xls");

//Set the active cell

$book->getWorksheets()->get(0)->setActiveCell("A20");

//Split the worksheet window

$book->getWorksheets()->get(0)->split();

//Save the excel file

$book->save($dataDir . "book.out.xls", $saveFormat->EXCEL_97_TO_2003);

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**分割ペイン (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/SplitPanes.php)
