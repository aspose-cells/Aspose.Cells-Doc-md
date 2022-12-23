---
title: Excel から HTML への変換中に未使用のスタイルを除外する
type: docs
weight: 30
url: /ja/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **考えられる使用シナリオ**

Microsoft Excel ファイルには、未使用のスタイルが多数含まれている可能性があります。 Excel ファイルを HTML 形式でエクスポートすると、これらの未使用のスタイルもエクスポートされます。これにより、HTML のサイズが大きくなる可能性があります。[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles)財産。設定すると**真実**、未使用のスタイルはすべて出力 HTML から除外されます。次のスクリーンショットは、出力 HTML 内の未使用のスタイルの例を示しています。

![todo:画像_代替_文章](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excel から HTML への変換中に未使用のスタイルを除外する**

次のサンプル コードは、ワークブックを作成し、未使用の名前付きスタイルも作成します。以来、[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles)に設定されています**真実**、この未使用の名前付きスタイルはエクスポートされません[出力 HTML](61767778.zip).しかし、あなたがそれを**間違い**の場合、この未使用のスタイルは出力 HTML 内に存在し、上のスクリーンショットに示すように HTML マークアップで確認できます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
