---
title: 厳密なOpen XMLスプレッドシート形式へのブックの保存
type: docs
weight: 150
url: /ja/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用すると、ブックを*Strict Open XML Spreadsheet*形式で保存できます。そのために、[**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)プロパティを提供しています。その値を[**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)に設定すると、出力ExcelファイルはStrict Open XMLスプレッドシート形式で保存されます。

## **ストリクトなOpen XMLスプレッドシート形式でワークブックを保存**

次のサンプルコードは、ブックを作成し、[**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)プロパティの値を[**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)に設定して[出力Excelファイル](67338272.xlsx)として保存します。出力ExcelファイルをMicrosoft Excelで開いて、名前を付けて保存...ダイアログボックスを開くと、その形式が*Strict Open XML Spreadsheet*として表示されます。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
