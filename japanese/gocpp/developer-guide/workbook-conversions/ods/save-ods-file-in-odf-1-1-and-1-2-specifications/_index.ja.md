---
title: Golangを使ってC++でODF 1.1、1.2、1.3仕様のODSファイルを保存する
linktitle: ODF 1.1、1.2、および1.3として保存
description: Aspose.Cellsを使用してC++でExcelをODF 1.1、1.2、1.3仕様に変換します。
type: docs
weight: 230
url: /ja/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ODSファイル（**OpenDocument Spreadsheet**）をODF（**OpenDocument Format**）1.1、1.2、1.3仕様で保存することをサポートしています。Aspose.Cellsには[**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/)プロパティがあり、ODSファイルの保存時に使用するODFバージョンを指定します。このプロパティのデフォルト値は[**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)であり、この設定なしで保存されたODSファイルは1.2仕様を使用します。

{{% /alert %}}

以下のサンプルコードは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1に値を追加し、その後ODF 1.1、1.2、1.3仕様でODSファイルを保存する例です。デフォルトでは、ODSファイルはODF 1.2仕様で保存されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
