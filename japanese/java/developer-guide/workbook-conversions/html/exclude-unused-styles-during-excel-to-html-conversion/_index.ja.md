---
title: Excel から HTML への変換中に未使用のスタイルを除外する
type: docs
weight: 30
url: /ja/java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **考えられる使用シナリオ**

Microsoft Excel ファイルには、未使用のスタイルが多数含まれている可能性があります。 Excel ファイルを HTML 形式でエクスポートすると、これらの未使用のスタイルもエクスポートされます。これにより、HTML のサイズが大きくなる可能性があります。[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)財産。設定すると**真実**、未使用のスタイルはすべて出力 HTML から除外されます。次のスクリーンショットは、出力 HTML 内の未使用のスタイルの例を示しています。

![todo:画像_代替_文章](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Excel から HTML への変換中に未使用のスタイルを除外する**

次のサンプル コードは、ワークブックを作成し、未使用の名前付きスタイルも作成します。以来、[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)に設定されています**真実**、したがって、この未使用の名前付きスタイルはにエクスポートされません[出力 HTML](61767781.zip).でも設定すると**間違い**の場合、この未使用のスタイルは出力 HTML 内に存在し、上のスクリーンショットに示すように HTML マークアップで確認できます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
