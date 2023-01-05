---
title: XLS および XLSX 形式でサポートされている行と列の最大数を見つける
type: docs
weight: 20
url: /ja/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **考えられる使用シナリオ**

Excel 形式でサポートされている行と列の数が異なります。たとえば、XLS は 65536 行と 256 列をサポートし、XLSX は 1048576 行と 16384 列をサポートします。特定の形式でサポートされている行と列の数を知りたい場合は、次を使用できます[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow)と[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)プロパティ。

## **XLS および XLSX 形式でサポートされている行と列の最大数を見つける**

次のサンプル コードでは、最初に XLS 形式で、次に XLSX 形式でブックを作成します。作成後、値を出力します[**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow)と[**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn)プロパティ。以下のコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
