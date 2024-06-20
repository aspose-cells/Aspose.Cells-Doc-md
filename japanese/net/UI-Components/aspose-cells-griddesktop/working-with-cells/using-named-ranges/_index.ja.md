---
title: 名前付き範囲を使用する
type: docs
weight: 110
url: /ja/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop、名前付き範囲、名前
description: この記事では、GridDesktopの名前付き範囲について紹介します。
---

{{% alert color="primary" %}} 

通常、ワークシート上の列や行のラベルを使用して、それらの列や行内のセルを参照します。ただし、セル、セル範囲、数式、または定数値を表す記述的な名前を作成することができます。**名前**という言葉は、セル、セル範囲、数式、または定数値を表す文字列を指すことができます。たとえば、Sales!C20:C30のように理解しにくい範囲をProductsのような分かりやすい名前で参照するために使用できます。ラベルは同じワークシートのデータを参照する数式で使用できます。別のワークシート上の範囲を表す場合、名前を使用することができます。**名前付き範囲**は、Microsoftの最も強力な機能の1つです。ユーザーは名前を名前付き範囲に割り当てることができ、このセル範囲を数式で名前で参照できます。**Aspose.Cells.GridDesktop**はこの機能をサポートしています。

{{% /alert %}} 
## **数式での名前付き範囲の追加/参照**
GridDesktopコントロールは、Excelファイルで名前付き範囲のインポート/エクスポートをサポートしており、名前（**Name**）と名前コレクション（**NameCollection**）の2つのクラスを提供しています。

次のコードスニペットは、それらの使用方法を示します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
