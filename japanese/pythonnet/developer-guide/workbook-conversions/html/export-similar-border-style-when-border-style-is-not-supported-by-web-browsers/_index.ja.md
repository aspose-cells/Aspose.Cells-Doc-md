---
title: Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする
type: docs
weight: 70
url: /ja/python-net/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
---

## **可能な使用シナリオ**

Microsoft Excelはブラウザでサポートされていない破線の境界線の種類をサポートしています。Aspose.Cells for Python via .NETを使用してそのようなExcelファイルをHTMLに変換すると、そのような境界線は削除されます。ただし、Aspose.Cells for Python via .NETは[**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style)プロパティをサポートし、その値を**true**に設定すると、そのような境界線も表示できます。

## **Webブラウザでサポートされていない場合の類似の境界線スタイルをHTMLにエクスポートする**

次のサンプルコードは、[サンプルExcelファイル](64716806.xlsx)を読み込み、{0}プロパティを{1}に設定した後、[output HTML](64716804.zip)に保存します。スクリーンショットは、**default output**から**{2}**が出力されたHTMLへの影響を示しています。

![todo:image_alt_text](1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportSimilarBorderStyle.py" >}}
{{< app/cells/assistant language="python-net" >}}
