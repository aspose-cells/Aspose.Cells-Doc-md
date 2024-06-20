---
title: Microsoft AccessデータベースのResultSetオブジェクトからワークシートへのデータのインポート
type: docs
weight: 200
url: /ja/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **可能な使用シナリオ**
Aspose.Cellsは、任意のデータベースから作成できるResultSetオブジェクトを使用してワークシートにデータをインポートできます。ただし、この記事では特にMicrosoft AccessデータベースからResultSetオブジェクトを作成しています。コードはすべての種類のデータベースで同じですので、一般的に使用できます。
## **UCanAccess - Microsoft Accessデータベースへの接続に必要**
[UCanAccess](http://ucanaccess.sourceforge.net/site.html)をダウンロードしてください。以下のJARファイルが含まれています。すべてのファイルをクラスパスに追加してください。

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

詳細については、Stack Overflowの以下のリンクを参照してください。

- [プロジェクトにJARファイルを手動で追加する](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **サンプルのMicrosoft Access 2016データベースファイル**
以下のサンプルMicrosoft Access 2016データベースファイルがサンプルコードで使用されました。任意のデータベースファイルを使用するか、独自のファイルを作成できます。

- [Students.accdb](48496712.accdb)

Microsoft AccessデータベースのResultSetオブジェクトからワークシートへのデータのインポート

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **以下のサンプルコードは、Microsoft AccessデータベースのSQLクエリを実行しResultSetオブジェクトを作成します。その後、[Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\))メソッドを使用して、ResultSetオブジェクトからワークシートにデータをインポートします。最初に、行および列のインデックスを使用し、次にセル名を使用してワークシートにデータをインポートします。最後に、ワークブックを[出力Excelファイル](48496713.xlsx)として保存します。スクリーンショットは、出力Excelファイルへのサンプルコードの影響を示しています。**
次のサンプルコードは、Microsoft AccessデータベースからSQLクエリを実行し、ResultSet オブジェクトを作成します。次に、[Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) メソッドを使用してResultSet オブジェクトからワークシートにデータをインポートします。最初に、行および列インデックスを使用してデータをワークシートにインポートし、次にセル名を使用してデータをインポートします。最後に、ワークブックを[出力Excelファイル](48496713.xlsx)として保存します。スクリーンショットは、サンプルコードの出力Excelファイルへの影響を示しています。

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
