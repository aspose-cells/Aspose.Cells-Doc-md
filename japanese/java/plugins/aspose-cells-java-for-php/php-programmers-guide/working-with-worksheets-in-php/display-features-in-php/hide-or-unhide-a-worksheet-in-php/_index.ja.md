---
title: Php でワークシートを非表示または再表示する
type: docs
weight: 50
url: /ja/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells - ワークシートを非表示または再表示する**
### **ワークシートを非表示にする**
Aspose.Cells Java for PHP を使用してワークシートを非表示にするには、次のように呼び出します。**hideunhideワークシート**モジュール。

**PHPコード**

{{< highlight "php" >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ワークシートを非表示または再表示する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
