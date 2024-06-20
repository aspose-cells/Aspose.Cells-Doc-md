---
title: XLSおよびXLSX形式がサポートする最大行数および列数を検索する
type: docs
weight: 60
url: /ja/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **可能な使用シナリオ**
Excel形式でサポートされる行数と列数は異なります。たとえば、XLSは65536行と256列をサポートし、XLSXは1048576行と16384列をサポートします。与えられた形式でサポートされる行数と列数を知りたい場合は、[Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)および[Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)プロパティを使用できます。
## **XLSおよびXLSX形式がサポートする最大行数および列数を検索する**
次のサンプルコードでは、最初にXLSおよび次にXLSX形式でワークブックを作成します。作成後、[Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)および[Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)プロパティの値を出力します。次のコードのコンソール出力を参照してください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

コンソール出力

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
