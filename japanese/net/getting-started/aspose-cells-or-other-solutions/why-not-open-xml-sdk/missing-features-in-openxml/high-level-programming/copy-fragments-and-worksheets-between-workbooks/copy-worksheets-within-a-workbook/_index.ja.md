---
title: ワークブック内でワークシートをコピーする
type: docs
weight: 20
url: /ja/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells**オーバーロードされたメソッドを提供し、**Aspose.Cells.WorksheetCollection.AddCopy()**、ワークシートをコレクションに追加し、既存のワークシートからデータをコピーするために使用されます。メソッドの 1 つのバージョンは、ソース ワークシートのインデックスをパラメーターとして受け取ります。もう 1 つのバージョンは、ソース ワークシートの名前をパラメーターとして受け取ります。

次の例は、ブック内の既存のワークシートをコピーする方法を示しています。

{{< highlight "csharp" >}}

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
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
