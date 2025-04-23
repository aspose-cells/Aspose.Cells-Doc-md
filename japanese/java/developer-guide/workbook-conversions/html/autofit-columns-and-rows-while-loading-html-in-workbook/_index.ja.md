---
title: ワークブックにHTMLをロードする際の列と行を自動調整する
type: docs
weight: 70
url: /ja/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **可能な使用シナリオ**

[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) オブジェクト内でHTMLファイルをロードする際、列と行を自動調整できます。この目的のために[**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)プロパティを **true** に設定してください。

## **ワークブックにHTMLをロードする際の列と行を自動調整する**

次のサンプルコードでは、まずロードオプションなしでサンプルHTMLをワークブックにロードし、XLSX形式で保存します。そして、[**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)プロパティを **true** に設定してサンプルHTMLを再びワークブックにロードし、XLSX形式で保存します。[**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) プロパティの効果は、以下のスクリーンショットに示されています。[自動調整なしの出力Excelファイル](outputWithout_AutoFitColsAndRows.xlsx) および [自動調整ありの出力Excelファイル](outputWith_AutoFitColsAndRows.xlsx) をダウンロードしてください。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
{{< app/cells/assistant language="java" >}}
