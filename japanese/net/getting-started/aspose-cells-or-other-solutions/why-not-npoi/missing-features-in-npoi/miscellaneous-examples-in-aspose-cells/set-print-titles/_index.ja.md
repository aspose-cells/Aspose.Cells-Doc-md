---
title: 印刷タイトルの設定
type: docs
weight: 30
url: /ja/net/set-print-titles/
---
## **Aspose.Cells - 印刷タイトルの設定**
Aspose.Cells を使用すると、印刷されたワークシートのすべてのページで行ヘッダーと列ヘッダーを繰り返すように指定できます。これを行うには、[ページ設定](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)クラス PrintTitleColumns および PrintTitleRows プロパティ。

繰り返される行または列は、行番号または列番号を渡すことによって定義されます。たとえば、行は $1:$2 として定義され、列は $A:$B として定義されます。

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**印刷タイトルの設定**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[印刷オプションの設定](/cells/ja/net/setting-print-options/).

{{% /alert %}}
