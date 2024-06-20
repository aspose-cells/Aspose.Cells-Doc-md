---
title: Excel を HTML に変換する際に未使用のスタイルを除外
type: docs
weight: 30
url: /ja/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **ExcelからHTMLへの変換時に未使用のスタイルを除外**
Microsoft Excelファイルには多くの未使用のスタイルが含まれている場合があります。これらのファイルをHTML形式にエクスポートすると、未使用のスタイルもエクスポートされます。これにより、出力HTMLのサイズが増加します。Aspose.Cells for Python via Javaは、ExcelファイルをHTMLに変換する際にこれらのスタイルを除外する機能をサポートしています。そのために、APIは[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)プロパティを提供しています。[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)プロパティの値を**True**に設定すると、出力HTMLからすべての未使用スタイルが除外されます。

以下のスクリーンショットは、[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)プロパティの値を**True**に設定して削除されるHTMLファイル内の未使用スタイルを示しています。

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

以下のサンプルコードは、ExcelからHTMLに変換する際に未使用のスタイルを削除する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
