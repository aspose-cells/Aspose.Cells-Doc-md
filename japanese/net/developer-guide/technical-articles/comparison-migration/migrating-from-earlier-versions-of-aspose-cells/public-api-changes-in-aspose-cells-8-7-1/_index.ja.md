---
title: パブリック API Aspose.Cells 8.7.1 の変更点
type: docs
weight: 240
url: /ja/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.7.0 から 8.7.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **LookInType.OriginalValues プロパティを追加**
Aspose.Cells API はすでに[データの検索または検索](/cells/ja/net/find-or-search-data/)セル値と数式で特定のコンテンツを見つけるためのスプレッドシートの機能。ただし、この機能には、セルに適用される書式設定の側面が欠けていたため、内容の値だけでなく外観も変更される可能性があり、その結果、元の値を使用してテキストを検索できなくなります。 Aspose.Cells API のこのリリースでは、LookInType.OriginalValues という名前の別の定数がパブリック API に公開され、上記の状況を克服できます。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[元の値を使用してデータを検索する](/cells/ja/net/search-data-using-original-values/)

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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


### **GridWeb の OnBeforeColumnFilter イベントを追加**
Aspose.Cells.GridWeb for .NET 8.7.1 は、GridWeb UI を介して行われるフィルタリング メカニズムへのコールバックとして機能する OnBeforeColumnFilter イベントを公開しました。名前が示すように、イベントは列フィルタリングが適用される前にトリガーされ、フィルターを適用する必要がある列インデックスや値などのフィルター情報を取得するために使用できます。

簡単な使用シナリオは次のようになります。

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

イベントをGridWebコントロールに登録することを忘れないでください<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
