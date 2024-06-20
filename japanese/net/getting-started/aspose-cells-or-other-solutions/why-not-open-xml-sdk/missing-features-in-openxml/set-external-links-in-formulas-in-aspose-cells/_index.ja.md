---
title: Aspose.Cellsでのフォーミュラの外部リンクの設定
type: docs
weight: 90
url: /ja/net/set-external-links-in-formulas-in-aspose-cells/
---

{{% alert color="primary" %}} 

場合によっては、セルや範囲の値を外部ファイルに対して評価するために、フォーミュラに外部ファイルへのリンクを含める必要があります。Aspose.Cellsはこの機能を提供しており、このドキュメントではその使用方法について説明しています。

{{% /alert %}} 

以下のサンプルコードは、数式に外部ファイルを含める方法を示しています。

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Set External Links in Formula.xlsx";

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get first Worksheet

Worksheet sheet = workbook.Worksheets[0];

//Get Cells collection

Aspose.Cells.Cells cells = sheet.Cells;

//Set formula with external links

cells["A1"].Formula = "=SUM('[book1.xls]Sheet1'!A2, '[book1.xls]Sheet1'!A4)";

//Set formula with external links

cells["A2"].Formula = "='[book1.xls]Sheet1'!A8";

//Save the workbook

workbook.Save(FileName);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **実行例のダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
