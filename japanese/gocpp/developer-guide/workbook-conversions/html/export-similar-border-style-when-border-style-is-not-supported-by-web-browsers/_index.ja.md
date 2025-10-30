---
title: Webブラウザでサポートされていない境界線スタイルの場合に類似の境界線スタイルをGolanggをC++経由でエクスポートする方法
linktitle: Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする
type: docs
weight: 70
url: /ja/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: GolangをC++経由でAspose.Cellsを使用してサポートされていない場合の類似の境界線スタイルをエクスポートする方法を学ぶ
---

## **可能な使用シナリオ**

Microsoft Excelは、Webブラウザがサポートしない点線の境界線タイプをいくつかサポートしています。Aspose.Cellsを使用してこのようなExcelファイルをHTMLに変換すると、そのような境界線は削除されます。ただし、Aspose.Cellsは[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)プロパティを使用してその境界線を表示させることも可能です。その値を**true**に設定すると、サポートされていない境界線もHTMLファイルにエクスポートされます。

## **Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする**

以下のサンプルコードは、サポートされていない境界線を含む[sample Excelファイル](64716806.xlsx)を読み込み、次のスクリーンショットに示すようにエクスポートします。スクリーンショットはまた、[出力HTML](64716804.zip)内の[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)プロパティの効果を示しています。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
