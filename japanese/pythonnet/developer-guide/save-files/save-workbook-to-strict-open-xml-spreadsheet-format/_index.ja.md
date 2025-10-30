---
title: 厳密なOpen XMLスプレッドシート形式へのブックの保存
type: docs
weight: 150
url: /ja/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NET は、`Strict Open XML Spreadsheet` 形式でワークブックを保存可能です。そのために、[**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) プロパティが提供されており、その値を [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) に設定すると、出力の Excel ファイルは Strict Open XML Spreadsheet 形式で保存されます。

## **ストリクトなOpen XMLスプレッドシート形式でワークブックを保存**

次のサンプルコードは、ブックを作成し、[**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance)プロパティの値を[**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance)に設定して[出力Excelファイル](67338272.xlsx)として保存します。出力ExcelファイルをMicrosoft Excelで開いて、名前を付けて保存...ダイアログボックスを開くと、その形式が*Strict Open XML Spreadsheet*として表示されます。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

{{< app/cells/assistant language="python-net" >}}
