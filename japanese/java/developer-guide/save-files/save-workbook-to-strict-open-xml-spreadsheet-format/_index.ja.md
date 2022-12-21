---
title: ワークブックを厳密な Open XML スプレッドシート形式で保存する
type: docs
weight: 100
url: /ja/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---
## **考えられる使用シナリオ**

Aspose.Cells では、ワークブックを保存できます*Strict Open XML スプレッドシート*フォーマット。その目的のために、それは**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance)**財産。その値を**[OoxmlCompliance.ISO_29500_2008_STRICT](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO_29500_2008_STRICT)**の場合、出力 Excel ファイルは次の場所に保存されます。*Strict Open XML スプレッドシート*フォーマット。

## **ワークブックを厳密な Open XML スプレッドシート形式で保存する**

次のサンプル コードは、ワークブックを作成し、**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance)**プロパティとして**[OoxmlCompliance.ISO_29500_2008_STRICT](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO_29500_2008_STRICT)**そしてそれをとして保存します[出力エクセルファイル](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx).出力された Excel ファイルを Microsoft Excel で開き、*名前を付けて保存...*ダイアログボックスに、その形式が次のように表示されます*Strict Open XML スプレッドシート*このスクリーンショットに示すように。

![todo:画像_代替_文章](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
