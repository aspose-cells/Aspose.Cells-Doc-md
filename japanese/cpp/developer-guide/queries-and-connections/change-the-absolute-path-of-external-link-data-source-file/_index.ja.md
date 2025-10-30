---
title: C++を使用して外部リンクデータソースファイルの絶対パスを変更
linktitle: 外部リンクデータソースファイルの絶対パスを変更する
type: docs
weight: 290
url: /ja/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Aspose.Cellsで外部リンクデータソースファイルの絶対パスをC++で変更します。
---

## 可能な使用シナリオ

外部リンクデータソースファイルの絶対パスを変更したい場合は、[**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/)メソッドを使用してください。最初はExcelファイルを読み込んだ場所のパスに設定されていますが、空文字に設定したり、ローカルフォルダパスやリモートネットワークパスに設定したりできます。このプロパティを変更するたびに、外部リンクデータソースのパスも変更されます。

## 外部リンクデータソースファイルの絶対パスを変更する

次のサンプルコードは、外部リンクを含む[サンプルExcelファイル](5115146.xlsx)を読み込みます。最初に外部リンクのデータソースを出力し、リモートパスを表示します。その後リモートパスを削除して再度出力し、今回はローカルパスを出力します。次に、[**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/)メソッドのパスをローカルとリモートに変更し、外部リンクのデータソースを再出力します。変更はコンソール出力に反映されます。

上記のサンプルコードを実行した後のコンソールまたはデバッグ出力は、[サンプルExcelファイル](5115146.xlsx) で示されています。

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
