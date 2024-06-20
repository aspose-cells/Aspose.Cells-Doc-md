---
title: Aspose.Cells での先行および後続のトレース
type: docs
weight: 130
url: /ja/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

特に共同で開発された複雑な財務ワークシートは、最も恥ずかしいエラーを隠すことがあります。式の正確さをチェックし、エラーの原因を特定することは、先行セルおよび従属セルを使用する式をチェックする際に困難になるかもしれません。

- **先行セル** は、他のセルの数式で参照されているセルです。たとえば、セル D10 が数式 =B5 を含む場合、セル B5 はセル D10 の先行セルです。
- **後続セル** には他のセルを参照する数式が含まれています。たとえば、セル D10 が数式 =B5 を含む場合、セル D10 はセル B5 の後続セルです。

スプレッドシートをわかりやすくするために、スプレッドシートに含まれるセルが式で使用されているかを明確に表示することがあります。同様に、他のセルの従属セルを抽出することがあります。

Aspose.Cells を使用すると、セルをトレースしてリンクされているセルを特定することができます。

{{% /alert %}} 
## **先行および従属セルのトレース： Microsoft Excel**
数式はクライアントによる変更に基づいて変更される場合があります。たとえば、セル C1 が C3 と C4 に基づく数式を含んでおり、C1 が変更された場合（つまり数式が上書きされた場合）、C3 および C4、または他のセルは、ビジネスルールに基づいてスプレッドシートをバランスさせるために変更する必要があります。

同様に、C1 に数式 "=(B1*22)/(M2*N32)" が含まれているとします。C1 が依存するセル（先行セルである）、つまり B1、M2、および N32 を見つけたいとします。

特定のセルの依存関係を他のセルにトレースする必要があることがあります。ビジネスルールが数式に埋め込まれている場合、依存関係を調べてそのルールに基づいていくつかのルールを実行したいとします。同様に、特定のセルの値が変更された場合、その変更によってワークシート内のどのセルが影響を受けるかを知りたいとします。

Microsoft Excel を使用すると、先行および従属をトレースすることができます。

1. **表示ツールバー** で、**数式監査** を選択します。
   数式監査ダイアログが表示されます。 
   **数式監査ダイアログ** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. 先行をトレース：
   1. 先行セルを特定したい式を含むセルを選択します。
   1. 直接データを提供する各セルにトレーサーアローを表示するには、 **式監査** ツールバーの **先行をトレース** をクリックします。
1. 特定のセルを参照する式をトレースする（従属）
   1. 従属セルを特定したいセルを選択します。
   1. アクティブセルに依存している各セルにトレーサーアローを表示するには、 **式監査** ツールバーの **従属をトレース** をクリックします。
## **先行および従属セルをトレース： Aspose.Cells**
### **先行をトレース**
Aspose.Cells では、先行セルを簡単に取得することができます。単純な数式の先行セルにデータを提供するセルを取得するだけでなく、名前付き範囲で複雑な数式の先行セルにデータを提供するセルを見つけることもできます。

以下の例では、テンプレートの Excel ファイルである Book1.xls を使用しています。スプレッドシートには最初のワークシートにデータと数式が含まれています。

**入力スプレッドシート** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells では、Cell クラスの GetPrecedents メソッドを使用してセルの先行セルをトレースすることができます。これは ReferredAreaCollection を返します。上記の例では、Book1.xls で、セル B7 に数式 "=SUM(A1:A3)" が含まれています。したがって、セル B7 の先行セルはセル A1:A3 です。次の例は、テンプレートファイル Book1.xls を使用して、先行セルをトレースする機能を示しています。

**C#**

{{< highlight csharp >}}

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
### **従属をトレース**
Aspose.Cells では、スプレッドシート内の依存するセルを取得することができます。Aspose.Cells では、単純な数式に関するデータを提供するセルを取得するだけでなく、名前付き範囲で複雑な数式に関するデータを提供するセルを見つけることもできます。

Aspose.Cells では、Cell クラスの GetDependents メソッドを使用してセルの依存するセルをトレースすることができます。たとえば、Book1.xlsx には、B2 セルおよび C2 セルに "=A1+20" および "=A1+30" の数式があります。次の例は、テンプレートファイル Book1.xlsx を使用して、A1 セルの依存するセルをトレースする方法を示しています。

**C#**

{{< highlight csharp >}}

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

