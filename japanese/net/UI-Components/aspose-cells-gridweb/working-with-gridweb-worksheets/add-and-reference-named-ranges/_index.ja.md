---
title: 名前付き範囲の追加と参照
type: docs
weight: 120
url: /ja/net/add-and-reference-named-ranges/
---
{{% alert color="primary" %}} 

通常、列と行のラベルは、セルを一意に参照するために使用されます。ただし、セル、セルの範囲、数式、または定数値を表すわかりやすい名前を作成できます。言葉**名前**セル、セル範囲、数式、または定数値を表す文字列を参照できます。たとえば、Products などのわかりやすい名前を使用して、Sales!C20:C30 などのわかりにくい範囲を参照します。ラベルは、同じワークシートのデータを参照する数式で使用できます。別のワークシートで範囲を表したい場合は、名前を使用できます。**名前付き範囲** Microsoft Excel の最も強力な機能の 1 つです。ユーザーは範囲に名前を割り当て、その名前を数式で使用できます。 Aspose.Cells.GridWeb はこの機能をサポートしています。

{{% /alert %}} 
## **数式での名前付き範囲の追加/参照**
GridWeb コントロールには、名前付き範囲を操作するための 2 つのクラス (GridName と GridNameCollection) が用意されています。次のコード スニペットは、名前付き範囲を作成し、数式でアクセスする方法を理解するのに役立ちます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
