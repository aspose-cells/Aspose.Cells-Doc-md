---
title: Golangを使用してC++経由でXLSおよびXLSXフォーマットがサポートする最大行数と列数を見つける
linktitle: 最大行数と列数を見つける
type: docs
weight: 20
url: /ja/go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: XLSとXLSXフォーマットでサポートされる最大行数と列数の見つけ方をAspose.Cells for C++を使って学ぶ。
---

## **可能な使用シナリオ**

Excelフォーマットでは、サポートされる行数と列数が異なります。例えば、XLSは65536行と256列をサポートし、XLSXは1048576行と16384列をサポートします。特定のフォーマットでサポートされる行数と列数を知りたい場合は、[**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/)と[**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/)プロパティを使用します。

## **XLSおよびXLSX形式がサポートする最大行数および列数を検索する**

次のサンプルコードは、最初にXLS形式でワークブックを作成し、その後XLSX形式で作成します。作成後、[**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/)と[**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/)の値を出力します。以下のコードのコンソール出力をご参照ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **コンソール出力**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
