---
title: セルから HTML5 文字列を取得
type: docs
weight: 40
url: /ja/python-java/get-html5-string-from-cell/
---

## **セルからHTML5文字列を取得**
Aspose.Cells for Python via Javaを使用すると、APIが提供する[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\))メソッドを使用して、セルからHTML文字列を取得できます。パラメータとして**false**を渡すと、通常のHTMLが返されますが、**true**を渡すとHTML5文字列が返されます。

以下のサンプルコードは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1にテキストを追加します。その後、APIの[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\))メソッドを使用してセルA1から通常のHTMLとHTML5文字列を取得し、それらを出力します。
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

上記のコードスニペットで生成される出力は次のとおりです。
## **出力**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
