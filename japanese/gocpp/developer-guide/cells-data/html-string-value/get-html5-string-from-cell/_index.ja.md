---
title: Golangを使用してC++経由でセルからHTML5文字列を取得します
linktitle: セルからHTML5文字列を取得
type: docs
weight: 90
url: /ja/go-cpp/get-html5-string-from-cell/
description: Aspose.Cells for C++ APIを使用してセルからHTML5文字列を取得する方法を学びます。
keywords: セルからHTML5文字列を取得、セルからHTML5文字列を取得、セルのHTML5文字列を管理
---

## **可能な使用シナリオ**

Aspose.Cellsは、ブール値のパラメータを受け取る[**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/)メソッドを使用してセルのHTML文字列を返します。**false**をパラメータとして渡すと通常のHTMLを返し、**true**を渡すとHTML5文字列を返します。

## **セルからHTML5文字列を取得**

次のサンプルコードはワークブックオブジェクトを作成し、最初のワークシートのセルA1にテキストを追加します。そして、[**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/)メソッドを使用してセルA1から通常のHTMLとHTML5文字列を取得し、それらをコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **コンソール出力**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
