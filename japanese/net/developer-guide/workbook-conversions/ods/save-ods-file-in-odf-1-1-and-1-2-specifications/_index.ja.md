---
title: ODF 1.1、1.2、1.3仕様でODSファイルを保存
linktitle: ODF 1.1、1.2、1.3として保存
description: Aspose.Cellsを使用してExcelをODF 1.1、1.2、1.3仕様に変換。
type: docs
weight: 230
url: /ja/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ODSファイル（**OpenDocument Spreadsheet**）をODF（**OpenDocument Format**）1.1、1.2、1.3仕様で保存することをサポートしています。Aspose.Cellsには[**OdsSaveOptions.OdfStrictVersion**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/odfstrictversion/)プロパティがあり、ODSファイルの保存時に使用するODFバージョンを指定します。このプロパティのデフォルト値は[**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/net/aspose.cells.ods/opendocumentformatversiontype/)であり、この設定なしで保存されたODSファイルは1.2仕様を使用します。

{{% /alert %}}

以下のサンプルコードは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1に値を追加し、その後ODF 1.1、1.2、1.3仕様でODSファイルを保存する例です。デフォルトでは、ODSファイルはODF 1.2仕様で保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
{{< app/cells/assistant language="csharp" >}}
