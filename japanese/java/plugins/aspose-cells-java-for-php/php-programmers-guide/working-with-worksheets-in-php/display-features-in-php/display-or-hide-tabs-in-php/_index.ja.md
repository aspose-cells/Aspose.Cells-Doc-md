---
title: PHPでタブを表示または非表示にする
type: docs
weight: 30
url: /ja/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - タブの表示または非表示**
### **タブを非表示にする**
Aspose.Cells Java for PHPを使用してタブを非表示にするには、**displayhidetabs**モジュールを呼び出します。

**PHPコード**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、Aspose.CellsのHide or Display or Hide Tabsをダウンロードする: 

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
