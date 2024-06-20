---
title: セルの範囲の書式設定
type: docs
weight: 60
url: /ja/net/aspose-cells-griddesktop/formatting-a-range-of-cells/
keywords: GridDesktop,format,style,cells
description: この記事では、GridDesktop のセルにスタイル書式を適用する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックも、セルにフォント設定やその他の書式設定を適用するトピックシリーズに属しています。最後のトピックでは、このような機能について詳しく説明しています。たとえば、[セルのフォントと色の変更](/cells/ja/net/changing-the-font-and-color-of-a-cell/) および [セルにスタイルを適用する](/cells/ja/net/applying-styles-on-cells/) トピックを参照して、同じ機能について学ぶことができます。 すでにこれらの概念をカバーしているなら、このトピックではどのような新しいものがあるのでしょうか。 このトピックが前のものと異なる唯一の点は、単一のセルではなく、セルの範囲に書式設定（フォントやその他のスタイルに関するもの）を適用することです。 このトピックがあなたにとって有用であることを願っています。

{{% /alert %}} 
## **セルのフォントとスタイルの設定**
書式設定について話す前に（以前のトピックですでにたくさん話している）、セルの範囲を作成する方法について知っておく必要があります。 さて、**CellRange** クラスを使用してセルの範囲を作成できます。このクラスのコンストラクタは、セルの範囲を指定するためのいくつかのパラメータを取ります。 開始セルおよび終了セルの**名前**または**行および列のインデックス**を使用してセルの範囲を指定できます。

**CellRange** オブジェクトを作成したら、Worksheet の**SetStyle**、**SetFont**、**SetFontColor** メソッドのオーバーロードされたバージョンを使用して、指定したセルの範囲に書式設定を適用できます。

この基本的な概念を理解するための例を見てみましょう。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FormattingCellRange-1.cs" >}}
