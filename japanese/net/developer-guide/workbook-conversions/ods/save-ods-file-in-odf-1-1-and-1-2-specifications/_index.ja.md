---
title: ODSファイルをODF 1.1および1.2の仕様に保存
linktitle: ODF 1.1および1.2として保存 
description: Aspose.Cellsは、ODF（OpenDocument Format）1.1および1.2の仕様でODSファイル（OpenDocument Spreadsheet）を保存する機能をサポートしています。Aspose.Cellsには、ODSファイルを保存する際にODF 1.1規格を使用するかどうかを指定するための{0}プロパティがあります。このプロパティのデフォルト値は false なので、この設定を使用しないで保存されるODSファイルは1.2の仕様を使用します。
type: docs
weight: 230
url: /ja/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ODF（OpenDocument Format）1.1および1.2仕様でODSファイル（**OpenDocument Spreadsheet**）を保存する機能をサポートしています。Aspose.Cellsには、ODSファイルを保存する際にODF 1.1仕様の使用を指定する[**OdsSaveOptions.IsStrictSchema11**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/properties/isstrictschema11)プロパティがあります。このプロパティのデフォルト値は**false**であり、この設定なしで保存されたODSファイルは1.2仕様を使用します。

{{% /alert %}}

以下のサンプルコードでは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1にいくつかの値を追加し、ODF 1.1および1.2の仕様でODSファイルを保存します。デフォルトでは、ODSファイルはODF 1.2の仕様で保存されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
