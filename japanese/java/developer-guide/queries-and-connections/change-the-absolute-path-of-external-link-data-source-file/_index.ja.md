---
title: 外部リンク データ ソース ファイルの絶対パスを変更する
type: docs
weight: 1020
url: /ja/java/change-the-absolute-path-of-external-link-data-source-file/
---
## **考えられる使用シナリオ**
外部リンク データ ソース ファイルの絶対パスを変更する場合は、[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)財産。最初に、このプロパティは、Excel ファイルが読み込まれた場所からのパスに設定されます。ただし、空の文字列に設定することも、ローカル フォルダー パスまたはリモート ネットワーク パスに設定することもできます。このプロパティを変更すると、外部リンク データ ソース ファイルのパスも変更されます。
## **外部リンク データ ソース ファイルの絶対パスを変更する**
次のサンプル コードは、[サンプルエクセルファイル](5472589.xlsx)外部リンクが含まれています。最初に、リモート パスを出力する外部リンク データ ソースを出力します。次に、リモート パスを削除して再度出力します。今回は、ローカル パスを使用して外部リンク データ ソースを出力します。次に、[Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath)プロパティをローカルおよびリモート パスに追加し、外部リンク データ ソースを再度出力すると、変更がコンソール出力に反映されます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **コンソール出力**
以下は、上記のサンプル コードを実行した後のコンソールまたはデバッグ出力です。[サンプルエクセルファイル](5472589.xlsx).

{{< highlight "java" >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
