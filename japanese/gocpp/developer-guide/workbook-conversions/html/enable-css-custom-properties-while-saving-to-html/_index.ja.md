---
title: HTMLに保存する際にCSSのカスタムプロパティを有効にする（GolaingとC++経由）
linktitle: HTML保存時にCSSカスタムプロパティを有効にする方法を学びます。
type: docs
weight: 320
url: /ja/go-cpp/enable-css-custom-properties-while-saving-to-html/
description: Aspose.Cells for C++を使用してExcelファイルをHTMLに保存する際に、CSSカスタムプロパティを有効にする方法を学びます。冗長な画像データを減らしてパフォーマンスを向上させます。
---

## **可能な使用シナリオ**

ExcelファイルをHTMLに保存する際に、同じbase64画像が複数回出現する場合、カスタムプロパティを使用することで画像データを一度だけ保存し、生成されるHTMLのパフォーマンスを向上させることができます。[**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/) プロパティを使用し、それを **true** に設定してください。

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **次のサンプルコードは、{0} 属性の使用例を示しています。このプロパティがTrueに設定されていない場合の効果もスクリーンショットで示しています。[サンプルExcelファイル](50528260.xlsx)と生成された[出力HTML](50528261.zip)をダウンロードして参照してください。**

以下のサンプルコードは [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/) プロパティの使用例を示しています。スクリーンショットはこのプロパティが true に設定されていない場合の効果を示しています。このコードで使用されたサンプルExcelファイル（50528260.xlsx）と、生成された出力HTML（50528261.zip）をダウンロードしてください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnableCssCustomPropertiesWhileSavingToHtml.go" >}}
