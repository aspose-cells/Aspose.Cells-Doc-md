---
title: Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする
type: docs
weight: 70
url: /ja/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能な使用シナリオ**

Microsoft ExcelはWebブラウザでサポートされていないような点線の境界線などをサポートしています。Aspose.Cellsを使用してこのようなExcelファイルをHTMLに変換すると、そのような境界線が削除されますが、[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)プロパティで類似の境界線も表示できるようになります。その値を**true**に設定してください。これにより、サポートされていない境界線もHTMLファイルにエクスポートされます。

## **Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする**

次のサンプルコードは、次のスクリーンショットに示されているサポートされていない境界線を含む[sample Excelファイル](64716832.xlsx)を読み込みます。このスクリーンショットは、[output HTML](64716831.zip)内の[**HtmlSaveOptions.ExportSimilarBorderStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportSimilarBorderStyle)プロパティの効果をさらに説明しています。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportSimilarBorderStyle.java" >}}
