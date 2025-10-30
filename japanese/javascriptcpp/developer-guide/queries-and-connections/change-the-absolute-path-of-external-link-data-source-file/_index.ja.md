---
title: C++経由のJavaScriptを使用して外部リンクデータソースファイルの絶対パスを変更する方法
linktitle: 外部リンクデータソースファイルの絶対パスを変更する
type: docs
weight: 290
url: /ja/javascript-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: C++経由でAspose.Cells for JavaScriptを使用し、外部リンクデータソースファイルの絶対パスの変更方法を学習する。 
---

## 可能な使用シナリオ

外部リンクデータソースファイルの絶対パスを変更したい場合は、[**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--)プロパティを使用してください。初期状態では、このプロパティはExcelファイルを読み込んだパスに設定されます。ただし、空の文字列に設定したり、ローカルフォルダのパスやリモートネットワークパスに設定することもできます。このプロパティを変更すると、外部リンクデータソースのパスも変更されます。

## 外部リンクデータソースファイルの絶対パスを変更する

次のサンプルコードは外部リンクを含む[サンプルExcelファイル](5115146.xlsx)をロードします。最初に外部リンクデータソースを出力し、リモートパスを表示します。その後、リモートパスを削除し、もう一度出力します。今回はローカルパスの外部リンクデータソースを出力します。その後、[**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--)プロパティをローカルとリモートのパスに設定し、再び外部リンクデータソースを出力し、変更がコンソール出力に反映されていることを確認します。



{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
