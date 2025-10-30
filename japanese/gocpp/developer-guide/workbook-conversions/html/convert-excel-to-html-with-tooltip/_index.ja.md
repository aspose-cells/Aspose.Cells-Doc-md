---
title: ツールチップ付きでExcelをHTMLに変換（C++使用）
linktitle: ツールチップ付きでExcelをHTMLに変換する
type: docs
weight: 200
url: /ja/go-cpp/convert-excel-to-html-with-tooltip/
description: Aspose.Cellsを用いて、ツールチップを追加しながらExcelをHTMLに変換します。
---

## **ツールチップ付きでExcelをHTMLに変換する**

生成されたHTMLでテキストが切り取られる場合に、ホバー時に完全なテキストをツールチップとして表示したいことがあります。Aspose.Cellsはこれをサポートしており、[**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/)プロパティを設定します。[**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/)プロパティを**true**に設定すると、完全なテキストをツールチップとして追加します。

次の画像は、生成されたHTMLファイル内のツールチップを示しています。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

次のコードサンプルは、[源となるExcelファイル](98107416.xlsx)を読み込み、ツールチップ付きの[出力HTMLファイル](98107417.zip)を生成します。

サンプルコード

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
