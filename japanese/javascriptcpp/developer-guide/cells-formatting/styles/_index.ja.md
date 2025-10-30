---
title: セルのスタイルを取得および設定する
description: C++を通じてAspose.Cells for JavaScriptでデータフォーマットとスタイリングを行う方法について学びます。これには、テキストフォーマット、数値フォーマット、日付フォーマット、その他のスタイリングオプションが含まれます。私たちのガイドは、魅力的なフォーマットでプロフェッショナルなスプレッドシートを作成するのに役立ちます。
keywords: C++を通じてAspose.Cells for JavaScriptでのデータフォーマット、スタイリング、テキストフォーマット、数値フォーマット、日付フォーマット、スタイリングオプション、スプレッドシート、魅力的なフォーマット、プロフェッショナルな見た目。
linktitle: スタイル
type: docs
weight: 50
url: /ja/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

C++を通じてAspose.Cells for JavaScriptでセルのフォーマット用に新たに導入された2つのメソッド：Cell.styleとCell.style。この記事では、Cell.style/スタイルアプローチを検討し、どちらの手法が適しているかを判断します。

{{% /alert %}} 
## **セルの書式設定**
セルの書式設定には2つの方法があります。以下に示します。
### **スタイルを使用して**
このコードでは、書式設定時に各セルのために Style オブジェクトが初期化されます。多くのセルをフォーマットする場合、Style オブジェクトは大きいため多くのメモリを消費します。これらの Style オブジェクトは、Workbook.save メソッドが呼び出されるまで解放されません。

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **スタイルを使用して**
最初の方法は簡単で直感的ですが、なぜ2つ目の方法を追加したのでしょうか？

メモリ使用量を最適化するために、2番目のアプローチを追加しました。Cell.styleプロパティを使ってStyleオブジェクトを取得し、それを変更して再びCell.styleに設定します。このStyleオブジェクトは保持されず、JavaScriptのガベージコレクターによって不要になったときに収集されます。

Cell.styleプロパティを設定すると、そのStyleオブジェクトは各セルごとに保存されません。代わりに、このStyleオブジェクトを内部のStyleプールと比較して再利用可能かどうかを判断します。異なる場合のみ、Styleオブジェクトが各Workbookに対して保持されます。つまり、各Excelファイルには数百のStyleオブジェクトしかなく、何千もありません。各セルには、Styleオブジェクトプールのインデックスのみが保持されます。

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **高度なトピック**
- [CellsFactoryクラスを使用してスタイルオブジェクトを作成する](/cells/ja/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [既存のStyleを修正する](/cells/ja/javascript-cpp/modify-an-existing-style/)
- [Styleオブジェクトの再利用](/cells/ja/javascript-cpp/reusing-style-objects/)
- [組み込みのスタイルを使用する](/cells/ja/javascript-cpp/using-built-in-styles/)
