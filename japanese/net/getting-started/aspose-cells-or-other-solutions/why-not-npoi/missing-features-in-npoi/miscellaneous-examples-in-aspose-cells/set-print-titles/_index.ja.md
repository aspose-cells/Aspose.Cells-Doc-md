---
title: 印刷タイトルの設定
type: docs
weight: 30
url: /ja/net/set-print-titles/
---

## **Aspose.Cells - 印刷タイトルの設定**
Aspose.Cellsを使用して印刷されたワークシートのすべてのページで繰り返される行や列の見出しを指定できます。これには、[PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラスのPrintTitleColumnsおよびPrintTitleRowsプロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**印刷タイトルの設定**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[印刷オプションの設定](/cells/ja/net/setting-print-options/)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
