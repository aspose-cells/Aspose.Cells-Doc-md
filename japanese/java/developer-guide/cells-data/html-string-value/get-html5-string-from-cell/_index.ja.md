---
title: Cell から HTML5 文字列を取得
type: docs
weight: 90
url: /ja/java/get-html5-string-from-cell/
---
## **考えられる使用シナリオ**

Aspose.Cells は、セルの HTML 文字列を返します。[**getHtmlString(ブール値 html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)方法。合格すれば**間違い**パラメータとして、通常のHTMLを返しますが、渡すと**真実**パラメータとして、HTML5 文字列を返します。

## **Cell から HTML5 文字列を取得**

次のサンプル コードは、ブック オブジェクトを作成し、最初のワークシートのセル A1 にテキストを追加します。次に、セル A1 から通常の HTML および HTML5 文字列を取得します。[**getHtmlString(ブール値 html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)メソッドを実行し、それらをコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
