---
title: 名前付き範囲の追加および参照
type: docs
weight: 120
url: /ja/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: この記事では、GridWebで名前付き範囲を使用する方法について紹介します。 
---

{{% alert color="primary" %}} 

通常、列ラベルと行ラベルがセルをユニークに参照するために使用されます。ただし、セル、セルの範囲、数式、または定数値を表す記述的な名前を作成できます。**Name**という単語は、セル、セルの範囲、数式、または定数値を表す文字列を指す場合があります。たとえば、Sales!C20:C30など、理解しにくい範囲を表すためにProductsなどの分かりやすい名前を使用します。ラベルは、同じワークシートのデータを参照する数式に使用できます。他のワークシートの範囲を表す場合は、名前を使用できます。**Named ranges**は、Microsoft Excelの最も強力な機能の1つです。ユーザーは範囲に名前を割り当て、その名前を数式で使用できます。Aspose.Cells.GridWebは、この機能をサポートしています。

{{% /alert %}} 
## **数式での名前付き範囲の追加/参照**
GridWebコントロールには、名前付き範囲を操作するための2つのクラス（GridNameおよびGridNameCollection）が用意されています。次のコードスニペットを使用すると、名前付き範囲の作成とそれを数式で使用する方法が理解できます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
