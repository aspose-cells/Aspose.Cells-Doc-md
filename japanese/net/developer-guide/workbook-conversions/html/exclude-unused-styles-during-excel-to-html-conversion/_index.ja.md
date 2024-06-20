---
title: Excel を HTML に変換する際に未使用のスタイルを除外
type: docs
weight: 30
url: /ja/net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **可能な使用シナリオ**

Microsoft Excelファイルには多くの未使用のスタイルが含まれている場合があります。ExcelファイルをHTML形式にエクスポートすると、これらの未使用のスタイルもエクスポートされます。これによりHTMLのサイズが増加する可能性があります。[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles)プロパティを使用して、ExcelファイルをHTMLに変換する際に未使用のスタイルを除外することができます。これを**true**に設定すると、すべての未使用のスタイルが出力されたHTMLから除外されます。次のスクリーンショットは、出力されたHTML内のサンプル未使用スタイルを表示しています。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **ExcelからHTMLへの変換時に未使用のスタイルを除外**

[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles)を**true**に設定すると、この未使用の名前付きスタイルは[output HTML](61767778.zip)にエクスポートされません。ただし**false**に設定すると、この未使用のスタイルが出力されたHTML内に存在し、上のスクリーンショットでHTMLマークアップに表示されます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
