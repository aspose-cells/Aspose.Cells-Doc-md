---
title: XLSおよびXLSX形式がサポートする最大行数および列数を検索する
type: docs
weight: 20
url: /ja/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **可能な使用シナリオ**

Excelフォーマットでサポートされる行数と列数が異なります。たとえば、XLSは65536行と256列をサポートし、XLSXは1048576行と16384列をサポートします。与えられたフォーマットでサポートされる行数と列数を知りたい場合は、[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow)および[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)プロパティを使用できます。

## **XLSおよびXLSX形式がサポートする最大行数および列数を検索する**

次のサンプルコードでは、まずXLS形式でブックを作成し、次にXLSX形式で作成します。作成後、[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow)および[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)プロパティの値を印刷します。以下に示すコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
