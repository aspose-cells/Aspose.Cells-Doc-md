---
title: Phpでワークシートを非表示または表示
type: docs
weight: 50
url: /ja/java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - ワークシートを非表示または表示する**
### **ワークシートを非表示にする**
Aspose.Cells Java for PHPを使用してワークシートを非表示にするには、**hideunhideworksheet**モジュールを呼び出してください。

**PHPコード**

{{< highlight php >}}

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
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、Aspose.Cellsのワークシートの非表示または表示をダウンロードする

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
