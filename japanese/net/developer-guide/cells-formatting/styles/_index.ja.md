---
title: セルのスタイルを取得および設定する
description: Aspose.Cells for .NET でデータの書式設定とスタイル設定 (テキストの書式設定、数値の書式設定、日付の書式設定、その他のスタイル設定オプションを含む) を実行する方法を説明します。私たちのガイドは、魅力的な書式設定を備えたプロフェッショナルな外観のスプレッドシートを作成するのに役立ちます。
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: スタイル
type: docs
weight: 50
url: /ja/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 では、セルを書式設定するための 2 つの新しいメソッド、Cell.GetStyle と Cell.SetStyle が導入されました。この記事では、どの手法が自分に最適かを判断するのに役立つように、Cell.GetStyle/SetStyle アプローチを検討します。

{{% /alert %}} 
##  **フォーマット中 Cells**
以下に示すように、セルを書式設定するには 2 つの方法があります。
###  **GetStyle() の使用**
次のコードでは、書式設定時にセルごとに Style オブジェクトが開始されます。多数のセルを書式設定すると、Style オブジェクトが大きいため、大量のメモリが消費されます。これらの Style オブジェクトは、Workbook.Save メソッドが呼び出されるまで解放されません。



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **SetStyle() の使用**
最初のアプローチは簡単で単純ですが、なぜ 2 番目のアプローチを追加したのでしょうか?

メモリ使用量を最適化するための 2 番目のアプローチを追加しました。 Cell.GetStyle メソッドを使用して Style オブジェクトを取得した後、それを変更し、Cell.SetStyle メソッドを使用してそれをこのセルに設定し直します。この Style オブジェクトは保持されず、参照されていない場合は .NET GC によって収集されます。

Cell.SetStyle メソッドを呼び出すとき、Style オブジェクトはセルごとに保存されません。代わりに、この Style オブジェクトを内部の Style オブジェクト プールと比較して、再利用できるかどうかを確認します。各 Workbook オブジェクトには、既存のものと異なる Style オブジェクトのみが保持されます。これは、各 Excel ファイルに Style オブジェクトが数千ではなく数百しか存在しないことを意味します。各セルについては、スタイル オブジェクト プールへのインデックスのみが保存されます。



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **アドバンストトピック**
- [CellsFactoryクラスを使用してStyleオブジェクトを作成する](/cells/ja/net/create-style-object-using-cellsfactory-class/)
- [既存のスタイルを変更する](/cells/ja/net/modify-an-existing-style/)
- [スタイルオブジェクトの再利用](/cells/ja/net/reusing-style-objects/)
- [組み込みスタイルの使用](/cells/ja/net/using-built-in-styles/)


