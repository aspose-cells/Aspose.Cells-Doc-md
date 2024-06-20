---
title: Excel を HTML に変換する際に未使用のスタイルを除外
type: docs
weight: 30
url: /ja/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **可能な使用シナリオ**

Microsoft Excel ファイルには多くの未使用スタイルが含まれる場合があります。Excel ファイルを HTML 形式にエクスポートすると、これらの未使用スタイルもエクスポートされます。これにより HTML のサイズが増加することがあります。[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) プロパティを使用して、Excel ファイルを HTML に変換する際に未使用のスタイルを除外できます。それを true に設定すると、すべての未使用のスタイルが出力される HTML から除外されます。次のスクリーンショットは、出力された HTML 内のサンプル未使用スタイルを表示しています。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **ExcelからHTMLへの変換時に未使用のスタイルを除外**

次のサンプルコードは、ワークブックを作成し、未使用の名前付きスタイルも作成します。[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) を true に設定しているため、この未使用の名前付きスタイルは [出力 HTML](61767781.zip) にエクスポートされません。false に設定すると、この未使用のスタイルは出力された HTML 内に含まれます。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
