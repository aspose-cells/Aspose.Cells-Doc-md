---
title: Cell から HTML5 文字列を取得します
type: docs
weight: 90
url: /ja/net/get-html5-string-from-cell/
description: Cell から Aspose.Cells for .NET API までの HTML5 文字列を取得する方法を学びます。
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---
##  **考えられる使用シナリオ**

Aspose.Cells は、[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)ブール値パラメータを受け取るメソッド。合格したら**間違い**パラメータとして、Normal HTML を返しますが、渡すと**真実**パラメータとして HTML5 文字列を返します。

##  **Cell から HTML5 文字列を取得します**

次のサンプル コードでは、ワークブック オブジェクトを作成し、最初のワークシートのセル A1 にテキストを追加します。次に、[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)メソッドを実行し、コンソールに出力します。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

##  **コンソール出力**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
