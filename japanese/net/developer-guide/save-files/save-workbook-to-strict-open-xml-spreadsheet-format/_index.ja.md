---
title: ワークブックを厳密な Open XML スプレッドシート形式で保存する
type: docs
weight: 150
url: /ja/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---
## **考えられる使用シナリオ**

Aspose.Cells では、ワークブックを保存できます*Strict Open XML スプレッドシート*フォーマット。その目的のために、それは**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**財産。その値を**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**の場合、出力 Excel ファイルは Strict Open XML スプレッドシート形式で保存されます。

## **ワークブックを厳密な Open XML スプレッドシート形式で保存する**

次のサンプル コードは、ワークブックを作成し、**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**プロパティとして**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**そしてそれをとして保存します[出力エクセルファイル](67338272.xlsx) .出力された Excel ファイルを Microsoft Excel で開き、[名前を付けて保存...] ダイアログ ボックスを開くと、その形式が次のように表示されます。*Strict Open XML スプレッドシート*このスクリーンショットに示すように。

![todo:画像_代替_文章](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
