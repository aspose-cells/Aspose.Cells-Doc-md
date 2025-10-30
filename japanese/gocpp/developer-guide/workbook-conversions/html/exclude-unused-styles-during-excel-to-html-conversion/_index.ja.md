---
title: GolangをC++経由でExcelからHTMLへの変換中に未使用のスタイルを除外する
linktitle: 未使用のスタイルを除外
type: docs
weight: 30
url: /ja/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Aspose.Cells for C++を使用してExcelからHTMLへの変換時に未使用のスタイルを除外する方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelファイルには多くの未使用のスタイルが含まれる場合があります。これらをHTMLにエクスポートすると、HTMLのサイズが増加する可能性があります。変換時にこれらの未使用スタイルを除外するには、[**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) プロパティを使用します。これを **true** に設定すると、未使用のスタイルはすべて出力HTMLから除外されます。以下のスクリーンショットは、出力HTML内の未使用スタイルのサンプルを示しています。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **ExcelからHTMLへの変換時に未使用のスタイルを除外**

以下のサンプルコードは workbook を作成し、未使用の名前付きスタイルも作成します。[**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) が **true** に設定されている場合、この未使用の名前付きスタイルは [出力HTML](61767778.zip) にエクスポートされません。ただし、これを **false** に設定すると、この未使用のスタイルは出力HTML内に存在し、上記スクリーンショットのようにHTMLマークアップで確認できます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
