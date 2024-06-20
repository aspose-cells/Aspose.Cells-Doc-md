---
title: PHPでスクロールバーを表示または非表示にする
type: docs
weight: 20
url: /ja/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - スクロールバーの表示または非表示**
### **スクロールバーを非表示にする**
Aspose.Cells Java for PHPを使用してスクロールバーを非表示にするには、**displayhidescrollbars**モジュールを呼び出します。

**PHPコード**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
**Aspose.Cells**のDisplay or Hide Scroll Barsを以下に示すソーシャルコーディングサイトからダウンロードする:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
