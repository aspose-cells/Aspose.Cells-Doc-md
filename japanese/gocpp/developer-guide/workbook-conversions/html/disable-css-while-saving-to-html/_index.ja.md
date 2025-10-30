---
title: HTMLを保存する際にCSSを無効にする（GolaingとC++経由）
linktitle: HTMLに保存する際にCSSを無効にする
type: docs
weight: 320
url: /ja/go-cpp/disable-css-while-saving-to-html/
description: Aspose.Cells for C++を使用してExcelファイルをHTMLに保存する際にCSSを無効にする方法を学びます。
---

## **可能な使用シナリオ**

Excelファイルを単一ページのHTMLとして保存すると、通常、CSS要素はHTMLファイル内に埋め込まれ、HEADセクションに配置されます。このファイルをメールのコンテンツまたは本文として添付すると、ほとんどのメールクライアントはCSS要素を除去し、正しく表示されなくなることがあります。Aspose.Cellsのバージョン24.12では、CSSをオプションで無効にし、スタイルを直接HTML要素内に適用できるオプションを導入しています。メールのコンテンツまたは本文にHTMLを設定したい場合は、[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) プロパティを使用し、それを **true** に設定してください。

## **HTML保存時にCSSを無効にする**

以下のサンプルコードは、[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) プロパティの使用方法を示しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
