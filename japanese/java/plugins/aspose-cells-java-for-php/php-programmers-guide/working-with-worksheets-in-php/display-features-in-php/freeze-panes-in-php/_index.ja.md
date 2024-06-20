---
title: PHPでウィンドウを固定する
type: docs
weight: 40
url: /ja/java/freeze-panes-in-php/
---

## **Aspose.Cells - ペインを固定する**
Aspose.Cells Java for PHPを使用してスプレッドシートドキュメントでウィンドウを固定するには、**FreezePanes**モジュールを単純に呼び出します。

**PHPコード**

{{< highlight php >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、Aspose.CellsのFreeze Panesをダウンロードする

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
