---
title: ExcelをJSONに変換(C++) via Golang
linktitle: ExcelをJSONに変換します。
type: docs
weight: 300
url: /ja/go-cpp/convert-excel-to-json/
description: C++を使用してExcelファイルをJSONに変換する方法を学びます。
keywords: Office 2013、Office 2016、Office 2019、およびOffice 365なしでブックをJSONにエクスポートする
---

{{% alert color="primary" %}}

Aspose.CellsはワークブックをJson(JavaScript Object Notation)ファイルに変換することをサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

ExcelブックをJSONに変換する方法に関する最良のソリューションがAspose.Cells for C++ライブラリにあります。APIはスプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第2引数に[**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/)を渡します。また、[**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)クラスを使用して追加設定も可能です。

次のコード例は、ExcelワークブックをJSONにエクスポートする例です。[ソースファイル](sample.xlsx)の変換に使用したコード例も参考にしてください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
次のコード例では、JsonSaveOptionsクラスを使用して追加設定を行い、ExcelワークブックをJSONにエクスポートします。[ソースファイル](sample.xlsx)をJSONファイルに変換する例も参照してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
