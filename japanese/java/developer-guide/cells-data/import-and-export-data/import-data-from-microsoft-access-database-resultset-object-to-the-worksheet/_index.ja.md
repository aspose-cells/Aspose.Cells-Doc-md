---
title: Microsoft Access データベース ResultSet オブジェクトからワークシートへのデータのインポート
type: docs
weight: 200
url: /ja/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **考えられる使用シナリオ**
Aspose.Cells は、任意のデータベースから作成できる ResultSet オブジェクトからデータをワークシートにインポートできます。ただし、この記事では具体的に Microsoft Access データベースから ResultSet オブジェクトを作成します。コードはすべてのタイプのデータベースで同じであるため、一般的に使用できます。
## **UCanAccess - Microsoft Access データベースへの接続に必要**
ダウンロードしてください[UCanAccess](http://ucanaccess.sourceforge.net/site.html).以下の JAR ファイルが含まれています。それらをすべてクラスパスに追加します。

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

さらにヘルプが必要な場合は、このスタック オーバーフロー リンクにアクセスしてください。

- [プロジェクトに JAR を手動で追加する](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **サンプル コード内で使用されるサンプル Microsoft Access 2016 データベース ファイル**
次のサンプル Microsoft Access 2016 データベース ファイルは、サンプル コード内で使用されました。任意のデータベース ファイルを使用することも、独自のファイルを作成することもできます。

- [学生.accdb](48496712.accdb)

次のスクリーンショットは、Microsoft Access 2016 で開いたときのデータベース ファイルを示しています。

![todo:画像_代替_文章](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Microsoft Access データベース ResultSet オブジェクトからワークシートにデータをインポートします。**
次のサンプル コードは、Microsoft Access データベースから SQL クエリを実行し、ResultSet オブジェクトを作成します。次に、ResultSet オブジェクトからワークシートにデータをインポートします。[Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)） 方法。最初は行インデックスと列インデックスを使用し、次にセル名を使用してデータをワークシートにインポートします。最後に、ワークブックを[出力 Excel ファイル](48496713.xlsx).スクリーンショットは、参照用の出力 Excel ファイルに対するサンプル コードの効果を示しています。

![todo:画像_代替_文章](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
