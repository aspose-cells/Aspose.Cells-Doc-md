---
title: Php でタブを表示または非表示にする
type: docs
weight: 30
url: /ja/java/display-or-hide-tabs-in-php/
---
## **Aspose.Cells - タブの表示または非表示**
### **タブを非表示にする**
を使用してタブを非表示にするには**Aspose.Cells Java for PHP**、 電話**表示非表示タブ**モジュール。

**PHP コード**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**タブを非表示または表示または非表示にする (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
