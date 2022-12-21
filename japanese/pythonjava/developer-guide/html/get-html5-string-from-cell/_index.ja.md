---
title: Cell から HTML5 文字列を取得
type: docs
weight: 40
url: /ja/python-java/get-html5-string-from-cell/
---
## **Cell から HTML5 文字列を取得**
Aspose.Cells for Python via Java を使用すると、セルから HTML 文字列を取得できます。これは、[getHtmlString(ブール値 html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)）APIが提供する方法。**間違い**パラメータとして、通常のHTMLを返しますが、渡すと**真実**パラメータとして、HTML5 文字列を返します。

次のサンプル コードは、ブック オブジェクトを作成し、最初のワークシートのセル A1 にテキストを追加します。次に、セル A1 から通常の HTML および HTML5 文字列を取得します。[getHtmlString(ブール値 html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) メソッドを実行し、それらを出力します。
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

以下は、上記のコード スニペットによって生成された出力です。
## **出力**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
