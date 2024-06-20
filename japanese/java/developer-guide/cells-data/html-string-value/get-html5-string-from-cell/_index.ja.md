---
title: セルから HTML5 文字列を取得
type: docs
weight: 90
url: /ja/java/get-html5-string-from-cell/
---

## **可能な使用シナリオ**

Aspose.Cells は、[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) メソッドを使用してセルの HTML 文字列を返します。パラメータとして **false** を渡すと、通常の HTML を返し、**true** を渡すと HTML5 文字列を返します。

## **セルからHTML5文字列を取得**

以下のサンプルコードは、ワークブック オブジェクトを作成し、最初のワークシートのセル A1 にテキストを追加します。次に、[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) メソッドを使用してセル A1 から通常の HTML と HTML5 文字列を取得し、それらをコンソールに表示します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **コンソール出力**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
