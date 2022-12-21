---
title: 名前付き範囲の使用
type: docs
weight: 110
url: /ja/net/using-named-ranges/
---
{{% alert color="primary" %}} 

通常、ワークシートの列と行のラベルを使用して、それらの列と行内のセルを参照します。ただし、セル、セルの範囲、数式、または定数値を表すわかりやすい名前を作成できます。言葉**名前**セル、セル範囲、数式、または定数値を表す文字列を参照できます。たとえば、Sales!C20:C30 のように、セル、セルの範囲、数式、または定数値を表すために、Products などのわかりやすい名前を使用して、理解しにくい範囲を参照します。ラベルは、同じワークシートのデータを参照する数式で使用できます。別のワークシートで範囲を表したい場合は、名前を使用できます。**名前付き範囲**は、Microsoft の最も強力な機能の 1 つです。ユーザーは名前付き範囲に名前を割り当てて、このセル範囲を数式でその名前で参照できるようにすることができます。**Aspose.Cells.GridDesktop**はこの機能をサポートしています。

{{% /alert %}} 
## **数式での名前付き範囲の追加/参照**
GridDesktop コントロールは、Excel ファイル内の名前付き範囲のインポート/エクスポートをサポートしており、2 つのクラス (**名前**と**NameCollection**) 名前付き範囲を操作します。

次のコード スニペットは、それらの使用方法に役立ちます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
