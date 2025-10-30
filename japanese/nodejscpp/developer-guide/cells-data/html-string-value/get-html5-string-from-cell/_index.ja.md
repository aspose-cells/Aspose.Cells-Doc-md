---
title: セルから HTML5 文字列を取得
type: docs
weight: 90
url: /ja/nodejs-cpp/get-html5-string-from-cell/
description: CellからHTML5文字列を取得する方法をAspose.Cells for Node.js via C++ APIで学びます。
keywords: Cell Node.jsからHTML5文字列をC++経由で取得、Cell Node.jsからHTML5文字列をC++経由で取得、Cell Node.jsのHTML5文字列をC++経由で管理
---

## **可能な使用シナリオ**

Aspose.Cellsは、ブールパラメータを受け取る[**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-)メソッドを使用してセルのHTML文字列を返します。パラメータに**false**を渡すと通常のHTMLを返し、**true**を渡すとHTML5文字列を返します。

## **セルからHTML5文字列を取得**

次のサンプルコードはワークブックオブジェクトを作成し、最初のシートのセルA1にいくつかのテキストを追加します。その後、セルA1から通常のHTMLとHTML5文字列を[**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-)メソッドを使って取得し、コンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **コンソール出力**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
