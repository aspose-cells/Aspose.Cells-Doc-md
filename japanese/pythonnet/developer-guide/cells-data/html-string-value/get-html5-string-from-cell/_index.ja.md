---
title: セルから HTML5 文字列を取得
type: docs
weight: 90
url: /ja/python-net/get-html5-string-from-cell/
description: Aspose.Cells for Python via .NET APIを介してセルからHTML5文字列を取得する方法を学ぶ
keywords: Python Excelライブラリ、PythonでHTML5文字列を取得する、Pythonを使用してセルからHTML5文字列を取得する、PythonでセルのHTML5文字列を管理する
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETは、ブール値を受け入れる[**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool)メソッドを使用してセルのHTML文字列を返します。ブール値として**false**を渡すと、通常のHTMLが返されますが、**true**を渡すとHTML5文字列が返されます。

## **セルからHTML5文字列を取得**

次のサンプルコードはワークブックオブジェクトを作成し、最初のワークシートのセルA1にテキストを追加します。そして、[**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool)メソッドを使用してセルA1から通常のHTMLとHTML5文字列を取得し、それらをコンソールに出力します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **コンソール出力**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
