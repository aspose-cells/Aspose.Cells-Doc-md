---
title: Php でグリッド線を表示または非表示にする
type: docs
weight: 10
url: /ja/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells - グリッド線の表示または非表示**
### **グリッド線を非表示にする**
を使用してワークシートを非表示にするには**Aspose.Cells Java for PHP**、 電話**表示非表示グリッド線**モジュール。

**PHP コード**

{{< highlight "php" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**グリッド線を表示または非表示にする (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
