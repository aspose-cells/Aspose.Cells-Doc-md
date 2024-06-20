---
title: 外部リンクデータソースファイルの絶対パスを変更する
type: docs
weight: 1020
url: /ja/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **可能な使用シナリオ**
外部リンクデータソースファイルの絶対パスを変更したい場合は、[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)プロパティを使用してください。このプロパティは最初はExcelファイルをロードした場所のパスに設定されます。しかし、空の文字列に設定するか、あるいはローカルフォルダのパスやリモートネットワークのパスに設定することができます。このプロパティを変更すると、外部リンクデータソースファイルのパスも変更されます。
## **外部リンクデータソースファイルの絶対パスを変更する**
次のサンプルコードは、外部リンクを含む[サンプルExcelファイル](5472589.xlsx)をロードします。最初に外部リンクデータソースを表示し、リモートパスを表示します。その後、リモートパスを削除し、再度表示します。このとき、外部リンクデータソースはローカルパスで表示されます。その後、[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)プロパティをローカルおよびリモートパスに変更し、再び外部リンクデータソースを表示します。その変更がコンソール出力に反映されています。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **コンソール出力**
以下は、与えられた[サンプルExcelファイル](5472589.xlsx)を使用して上記のサンプルコードを実行した後のコンソール出力またはデバッグ出力です。

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
