---
title: 外部リンクデータソースファイルの絶対パスを変更する
type: docs
weight: 290
url: /ja/net/change-the-absolute-path-of-external-link-data-source-file/
---

## 可能な使用シナリオ

外部リンクデータソースファイルの絶対パスを変更したい場合は、[**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) プロパティを使用してください。最初はこのプロパティは、Excelファイルの読み込み元のパスに設定されます。しかし、空の文字列に設定するか、ローカルフォルダパスまたはリモートネットワークパスに設定できます。このプロパティを変更すると、外部リンクデータソースファイルのパスも変更されます。

## 外部リンクデータソースファイルの絶対パスを変更する

以下のサンプルコードは、外部リンクを含む [サンプルExcelファイル](5115146.xlsx) をロードします。最初にリモートパスを出力し、次にリモートパスを削除して、今度はローカルパスを出力します。その後、[**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath) プロパティをローカルパスとリモートパスに変更し、再度外部リンクデータソースを出力し、変更がコンソール出力に反映されます。

上記のサンプルコードを実行した後のコンソールまたはデバッグ出力は、[サンプルExcelファイル](5115146.xlsx) で示されています。

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
