---
title: Php でスクロール バーを表示または非表示にする
type: docs
weight: 20
url: /ja/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells - スクロール バーの表示または非表示**
### **スクロール バーを非表示にする**
を使用してスクロール バーを非表示にするには**Aspose.Cells Java for PHP**、 電話**スクロールバーを非表示にする**モジュール。

**PHPコード**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**スクロールバーを表示または非表示にする (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
