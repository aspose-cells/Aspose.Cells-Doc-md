---
title: Excel から HTML への変換中に未使用のスタイルを除外する
type: docs
weight: 30
url: /ja/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Excel から HTML への変換中に未使用のスタイルを除外する**
Microsoft Excel ファイルには、未使用のスタイルが多数含まれている場合があります。これらのファイルを HTML 形式にエクスポートすると、未使用のスタイルもエクスポートされます。これにより、出力 HTML のサイズが大きくなります。 Aspose.Cells for Python via Java は、Excel ファイルを HTML に変換する際にこれらのスタイルを除外することをサポートしています。このために、API は[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)財産。値の設定[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)プロパティへ**真実**未使用のスタイルをすべて出力 HTML から除外します。

次のスクリーンショットは、HTML ファイルで使用されていないスタイルを示しています。[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)プロパティへ**真実**.

![todo:画像_代替_文章](HtmlSaveOptions-Exclude-Unused-Styles.png)

次のサンプル コードは、Excel から HTML への変換中に未使用のスタイルを削除する方法を示しています。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
