---
title: セルのスタイルを取得および設定する
description: Aspose.Cells for Python via .NETでのデータの書式設定とスタイル設定の方法を紹介します。テキストの書式設定、数値の書式設定、日付の書式設定、およびその他のスタイリングオプションについて解説します。私たちのガイドは、プロフェッショナルな外観のスプレッドシートを魅力的な書式設定で作成するお手伝いをします。
keywords: Aspose.Cells for Python via .NET、データ書式設定、スタイリング、テキスト書式設定、数値書式設定、日付書式設定、スタイリングオプション、スプレッドシート、魅力的な書式設定、プロフェッショナルな外観。
linktitle: スタイル
type: docs
weight: 50
url: /ja/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NETは、セルの書式設定のために新たに2つのメソッド、Cell.GetStyleとCell.SetStyleを導入しました。この記事では、Cell.GetStyle/SetStyleのアプローチを検討し、どちらの技術が最適か判断できるようにしています。

{{% /alert %}} 

## **セルの書式設定**
セルの書式設定には2つの方法があります。以下に示します。

### **GetStyle()を使用する**
次のコードを使用して、各セルの書式設定時にStyleオブジェクトが初期化されます。多くのセルが書式設定されている場合、Styleオブジェクトは大きいため、大量のメモリが消費されます。これらのStyleオブジェクトはWorkbook.Saveメソッドが呼び出されるまで解放されません。


**Python**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **SetStyle()を使用する**
最初の方法は簡単で直感的ですが、なぜ2つ目の方法を追加したのでしょうか？

メモリ使用量を最適化するために2つ目の方法を追加しました。セル.GetStyleメソッドを使用してStyleオブジェクトを取得し、それを変更してセルに戻す際にセル.SetStyleメソッドを使用します。このStyleオブジェクトは保存されず、それが参照されない場合に.NET GCがそれを収集します。

Cell.SetStyleメソッドを呼び出すと、Styleオブジェクトは各セルに保存されません。代わりに、このStyleオブジェクトを内部のStyleオブジェクトプールと比較して再利用できるかどうかを確認します。既存のものと異なるStyleオブジェクトのみが各Workbookオブジェクトに保存されます。これにより、各Excelファイルには数百個のStyleオブジェクトしかありません。各セルにはStyleオブジェクトプールへのインデックスのみが保存されます。



**Python**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **高度なトピック**
- [CellsFactoryクラスを使用してスタイルオブジェクトを作成する](/cells/ja/python-net/create-style-object-using-cellsfactory-class/)
- [既存のStyleを修正する](/cells/ja/python-net/modify-an-existing-style/)
- [Styleオブジェクトの再利用](/cells/ja/python-net/reusing-style-objects/)
- [組み込みのスタイルを使用する](/cells/ja/python-net/using-built-in-styles/)


