---
title: ブック内のワークシートをコピー
type: docs
weight: 20
url: /ja/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells**は、**Aspose.Cells.WorksheetCollection.AddCopy()**というオーバーロードされたメソッドを提供し、ワークシートをコレクションに追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの1つのバージョンはソースワークシートのインデックスをパラメータとして取ります。もう1つのバージョンは、ソースワークシートの名前をパラメータとして取ります。

次の例は、ブック内で既存のワークシートをコピーする方法を示しています。

{{< highlight csharp >}}

 //Create a new Workbook.

//Open an existing Excel file.

Workbook wb = new Workbook("ResultedBook.xls");

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing

//sheet within the Workbook.

sheets.AddCopy("MySheet");

//Save the Excel file.

wb.Save("Copy Worksheet.xls");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
