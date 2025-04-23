---
title: セルから HTML5 文字列を取得
type: docs
weight: 90
url: /ja/net/get-html5-string-from-cell/
description: Aspose.Cells for .NET APIを介してセルからHTML5文字列を取得する方法を学ぶ
keywords: セルからHTML5文字列を取得、セルからHTML5文字列を取得、セルのHTML5文字列を管理
---

## **可能な使用シナリオ**

Aspose.Cellsは、booleanパラメータを受け入れる[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)メソッドを使って、セルのHTML文字列を返します。パラメータとして**false**を渡すと、通常のHTMLを返し、**true**を渡すと、HTML5文字列を返します。

## **セルからHTML5文字列を取得**

次のサンプルコードはワークブックオブジェクトを作成し、最初のワークシートのセルA1にテキストを追加します。そして、[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)メソッドを使用してセルA1から通常のHTMLとHTML5文字列を取得し、それらをコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **コンソール出力**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
