---
title: Cell から HTML5 文字列を取得
type: docs
weight: 90
url: /ja/net/get-html5-string-from-cell/
---
## **考えられる使用シナリオ**

Aspose.Cells は、セルの HTML 文字列を返します。[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)ブール値のパラメーターを受け入れるメソッド。合格すれば**間違い**パラメータとして、通常の HTML を返しますが、渡すと**真実**パラメータとして、HTML5 文字列を返します。

## **Cell から HTML5 文字列を取得**

次のサンプル コードは、ブック オブジェクトを作成し、最初のワークシートのセル A1 にテキストを追加します。次に、セル A1 から通常の HTML および HTML5 文字列を取得します。[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)メソッドを実行し、それらをコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
