---
title: Aspose.Cellsで先例と従属を追跡する
type: docs
weight: 130
url: /ja/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

複雑な財務ワークシート、特に共同で開発されたものは、最も厄介なエラーを隠すことができます。数式が参照元セルと従属セルを使用している場合、数式の正確性をチェックし、エラーの原因を見つけることが難しい場合があります。

- **先行細胞**別の Cell の数式によって参照されるセルです。たとえば、セル D10 に数式 =B5 が含まれている場合、セル B5 はセル D10 の参照元になります。
- **依存セル**他のセルを参照する数式が含まれています。たとえば、セル D10 に数式 =B5 が含まれている場合、セル D10 はセル B5 の依存セルです。

スプレッドシートを読みやすくするために、スプレッドシートのどのセルが数式で使用されているかを明確に示したい場合があります。同様に、他のセルの依存セルを抽出することもできます。

Aspose.Cells を使用すると、セルをトレースして、リンクされているセルを見つけることができます。

{{% /alert %}} 
## **先例と依存関係のトレース Cells: Microsoft Excel**
式は、クライアントによって行われた変更に基づいて変更される場合があります。たとえば、セル C1 が式を含む C3 および C4 に依存しており、C1 が変更された場合 (式が上書きされるため)、ビジネス ルールに基づいてスプレッドシートのバランスを取るために C3 および C4、または他のセルを変更する必要があります。

同様に、C1 に式 "=(B1*22)/(M2*N32)". C1 が依存するセル、つまり先行セル B1、M2、および N32 を見つけたいと考えています。

特定のセルの他のセルへの依存関係を追跡する必要がある場合があります。ビジネスルールが数式に埋め込まれている場合、依存関係を見つけて、それに基づいていくつかのルールを実行したいと考えています。同様に、特定のセルの値が変更された場合、ワークシート内のどのセルがその変更の影響を受けるでしょうか?

Microsoft Excel では、ユーザーは先例と依存関係を追跡できます。

1. 上で**ビュー ツールバー**、 選択する**フォーミュラ監査**.
 [式の監査] ダイアログが表示されます。
   **フォーミュラ監査ダイアログ** 

![todo:画像_代替_文章](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. トレースの前例:
1. 参照元セルを検索する数式を含むセルを選択します。
 1. アクティブ セルにデータを直接提供する各セルへのトレーサー矢印を表示するには、**前例をトレース**上で**フォーミュラ監査**ツールバー。
1. 特定のセル (依存セル) を参照する数式をトレースする
1. 依存セルを識別したいセルを選択します。
 1. アクティブなセルに依存する各セルへのトレーサ矢印を表示するには、[式の監査] ツールバーの [依存関係のトレース] をクリックします。
## **先例と従属をトレース Cells: Aspose.Cells**
### **前例をたどる**
Aspose.Cells を使用すると、先行セルを簡単に取得できます。単純な数式の参照元にデータを提供するセルを取得できるだけでなく、名前付き範囲を持つ複雑な数式の参照元にデータを提供するセルも検索できます。

以下の例では、テンプレートの Excel ファイル Book1.xls が使用されています。スプレッドシートには、最初のワークシートにデータと数式があります。

**入力スプレッドシート** 

![todo:画像_代替_文章](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells は、セルの参照元をトレースするために使用される Cell クラスの GetPrecedents メソッドを提供します。これは、ReferredAreaCollection を返します。上記のように、Book1.xls のセル B7 には数式「=SUM(A1:A3)」が含まれています。したがって、セル A1:A3 はセル B7 の先行セルです。次の例は、テンプレート ファイル Book1.xls を使用した参照元のトレース機能を示しています。

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **依存関係のトレース**
Aspose.Cells を使用すると、スプレッドシートで依存セルを取得できます。 Aspose.Cells は、単純な数式に関するデータを提供するセルを取得できるだけでなく、名前付き範囲を持つ複雑な数式の依存関係にデータを提供するセルを検索することもできます。

Aspose.Cells は、セルの依存をトレースするために使用される Cell クラスの GetDependents メソッドを提供します。たとえば、Book1.xlsx では、B2 セルと C2 セルにそれぞれ "=A1+20" と "=A1+30" という数式があります。次の例は、テンプレート ファイル Book1.xlsx を使用して A1 セルの依存関係をトレースする方法を示しています。

**C#**

{{< highlight "csharp" >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

