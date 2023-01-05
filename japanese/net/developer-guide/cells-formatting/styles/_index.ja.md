---
title: セルのスタイルの取得と設定
linktitle: スタイル
type: docs
weight: 50
url: /ja/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 では、セルをフォーマットするための 2 つの新しいメソッドが導入されました: Cell.GetStyle および Cell.SetStyle。この記事では、Cell.GetStyle/SetStyle アプローチを調べて、どの手法が自分に最も適しているかを判断できるようにします。

{{% /alert %}} 
## **フォーマット Cells**
以下に示すように、セルをフォーマットするには 2 つの方法があります。
### **GetStyle() の使用**
次のコードでは、書式設定時にセルごとに Style オブジェクトが開始されます。 Style オブジェクトは大きなオブジェクトであるため、大量のセルをフォーマットすると大量のメモリが消費されます。これらの Style オブジェクトは、Workbook.Save メソッドが呼び出されるまで解放されません。



**C#**

{{< highlight "csharp" >}}

 cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **SetStyle() の使用**
最初のアプローチは簡単でわかりやすいのに、なぜ 2 番目のアプローチを追加したのでしょうか。

メモリ使用量を最適化する 2 番目のアプローチを追加しました。 Cell.GetStyle メソッドを使用して Style オブジェクトを取得した後、それを変更し、Cell.SetStyle メソッドを使用してそれをこのセルに戻します。この Style オブジェクトは保持されず、参照されていない場合は .NET GC によって収集されます。

Cell.SetStyle メソッドを呼び出すと、Style オブジェクトはセルごとに保存されません。代わりに、この Style オブジェクトを内部の Style オブジェクト プールと比較して、再利用できるかどうかを確認します。 Workbook オブジェクトごとに、既存のものとは異なる Style オブジェクトのみが保持されます。これは、Excel ファイルごとに数千ではなく、数百の Style オブジェクトしかないことを意味します。セルごとに、Style オブジェクト プールへのインデックスのみが保持されます。



**C#**

{{< highlight "csharp" >}}

スタイル スタイル = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(スタイル);


## **先行トピック**
- [CellsFactory クラスを使用して Style オブジェクトを作成する](/cells/ja/net/create-style-object-using-cellsfactory-class/)
- [既存のスタイルを変更する](/cells/ja/net/modify-an-existing-style/)
- [スタイル オブジェクトの再利用](/cells/ja/net/reusing-style-objects/)
- [組み込みスタイルの使用](/cells/ja/net/using-built-in-styles/)


