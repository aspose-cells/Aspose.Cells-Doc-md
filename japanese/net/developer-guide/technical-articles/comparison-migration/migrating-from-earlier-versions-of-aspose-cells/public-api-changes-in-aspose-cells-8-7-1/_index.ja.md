---
title: Aspose.Cells 8.7.1 での公開 API 変更
type: docs
weight: 240
url: /ja/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.7.0 から 8.7.1 への変更について、モジュール/アプリケーション開発者に興味を持つ可能性がある内容が記載されています。新しいおよび更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の背後での挙動に変更があった場合についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **LookInType.OriginalValuesプロパティを追加しました**
Aspose.Cells APIはすでに[データの検索](/cells/ja/net/find-or-search-data/)機能をサポートしており、スプレッドシート内で特定のコンテンツを見つけるためにセルの値や式を検索します。しかし、この機能には、セルに適用された書式が欠けており、見た目やコンテンツの値を変更する可能性があります。その結果、元の値を使用してテキストを検索できなくなります。Aspose.Cells APIのこのリリースでは、LookInType.OriginalValuesという名前の定数が公開APIに公開され、上記の状況を克服することができます。

{{% alert color="primary" %}} 

この機能の詳細については、[元の値を使用したデータの検索](/cells/ja/net/search-data-using-original-values/)の詳細記事をご覧ください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **GridWeb用のOnBeforeColumnFilterイベントを追加しました**
Aspose.Cells.GridWeb for .NET 8.7.1では、GridWeb UIを介したフィルタリングメカニズムに対するコールバックとしてOnBeforeColumnFilterイベントが公開されました。イベント名が示すように、このイベントは列のフィルタリングが適用される前にトリガされ、フィルタリング情報（列インデックスやフィルタを適用する値など）を取得するために使用できます。

シンプルな使用シナリオは次のようになります。

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
