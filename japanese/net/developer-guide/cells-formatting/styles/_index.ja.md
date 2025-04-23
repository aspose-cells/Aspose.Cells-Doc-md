---
title: セルのスタイルを取得および設定する
description: Aspose.Cells for .NETでのデータの書式設定とスタイルの実行方法、テキストの書式設定、数値の書式設定、日付の書式設定、その他のスタイルオプションについて調べてください。当ガイドは、魅力的な書式設定を施し、プロフェッショナルな見栄えのスプレッドシートを作成するための手助けをします。
keywords: Aspose.Cells for .NET、データの書式設定、スタイル、テキストの書式設定、数値の書式設定、日付の書式設定、スタイルのオプション、スプレッドシート、魅力的な書式設定、プロフェッショナルな見栄え
linktitle: スタイル
type: docs
weight: 50
url: /ja/net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2では、セルの書式設定に2つの新しいメソッド、Cell.GetStyleおよびCell.SetStyleが導入されました。この記事では、Cell.GetStyle/SetStyleのアプローチについて調査し、お好みのテクニックを判断できるようにします。

{{% /alert %}} 
## **セルの書式設定**
セルの書式設定には2つの方法があります。以下に示します。
### **GetStyle()を使用する**
次のコードを使用して、各セルの書式設定時にStyleオブジェクトが初期化されます。多くのセルが書式設定されている場合、Styleオブジェクトは大きいため、大量のメモリが消費されます。これらのStyleオブジェクトはWorkbook.Saveメソッドが呼び出されるまで解放されません。



**C#**

{{< highlight csharp >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **SetStyle()を使用する**
最初の方法は簡単で直感的ですが、なぜ2つ目の方法を追加したのでしょうか？

メモリ使用量を最適化するために2つ目の方法を追加しました。セル.GetStyleメソッドを使用してStyleオブジェクトを取得し、それを変更してセルに戻す際にセル.SetStyleメソッドを使用します。このStyleオブジェクトは保存されず、それが参照されない場合に.NET GCがそれを収集します。

Cell.SetStyleメソッドを呼び出すと、Styleオブジェクトは各セルに保存されません。代わりに、このStyleオブジェクトを内部のStyleオブジェクトプールと比較して再利用できるかどうかを確認します。既存のものと異なるStyleオブジェクトのみが各Workbookオブジェクトに保存されます。これにより、各Excelファイルには数百個のStyleオブジェクトしかありません。各セルにはStyleオブジェクトプールへのインデックスのみが保存されます。



**C#**

{{< highlight csharp >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

## **高度なトピック**
- [CellsFactoryクラスを使用してスタイルオブジェクトを作成する](/cells/ja/net/create-style-object-using-cellsfactory-class/)
- [既存のStyleを修正する](/cells/ja/net/modify-an-existing-style/)
- [Styleオブジェクトの再利用](/cells/ja/net/reusing-style-objects/)
- [組み込みのスタイルを使用する](/cells/ja/net/using-built-in-styles/)


{{< app/cells/assistant language="csharp" >}}
