---
title: 厳密なOpen XMLスプレッドシート形式へのブックの保存
type: docs
weight: 100
url: /ja/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **可能な使用シナリオ**

Aspose.Cellsでは、ワークブックを*Strict Open XML Spreadsheet*形式で保存することができます。そのために、[**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance)プロパティを提供しています。その値を[**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT)に設定すると、出力されるExcelファイルは*Strict Open XML Spreadsheet*形式で保存されます。

## **ストリクトなOpen XMLスプレッドシート形式でワークブックを保存**

次のサンプルコードでは、ワークブックを作成し、[**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance)プロパティの値を[**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT)に設定して保存し、[出力Excelファイル](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx)として保存します。出力ExcelファイルをMicrosoft Excelで開き、*名前を付けて保存...*ダイアログボックスを開くと、その形式がこのスクリーンショットに示されているように*Strict Open XML Spreadsheet*となります。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
{{< app/cells/assistant language="java" >}}
