---
title: ワークブック内でワークシートを移動する
type: docs
weight: 30
url: /ja/net/move-worksheets-within-workbook/
---
Aspose.Cells は、ワークシートをスプレッドシート内の別の場所に移動するために使用される Aspose.Cells.Worksheet.MoveTo() メソッドを提供します。このメソッドは、対象のワークシート インデックスをパラメーターとして受け取ります。

次の例は、ワークシートをブック内の別の場所に移動する方法を示しています。

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Move Worksheet.xlsx";

//Open an existing excel file.

Workbook wb = new Workbook(FileName);

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Get the first worksheet.

Worksheet worksheet = sheets[0];

string test = worksheet.Name;

//Move the first sheet to the third position in the workbook.

worksheet.MoveTo(2);

//Save the excel file.

wb.Save(FileName);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
