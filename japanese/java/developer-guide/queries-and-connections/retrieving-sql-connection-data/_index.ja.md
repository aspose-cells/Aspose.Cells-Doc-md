---
title: SQL接続データの取得
type: docs
weight: 20
url: /ja/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用して、SQL接続データを取得できます。これには、SQLサーバーに接続するために必要なすべてのデータが含まれます。たとえば、**サーバーのURL**、**ユーザー名**、**テーブル名**、**完全なSQLクエリ**、**クエリタイプ**、**テーブルの場所**、それに関連付けられた**名前付き範囲の名前**などです。

{{% /alert %}} 

Microsoft Excelでは、データベースに接続するには:

1. **データ**メニューをクリックし、**その他のソース**、その後 **SQL Server** を選択します。
1. 次に、**データ**、その後 **Connections** を選択します。
1. Connectionsウィザードを使用してデータベースに接続し、データベースクエリを作成します。

**Microsoft ExcelでのSQL接続オプションの表示** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cellsは、Workbook.getDataConnections()メソッドを使用して外部接続の取得を行います。これは、ワークブック内のExternalConnectionオブジェクトのコレクションを返します。

ExternalConnectionオブジェクトにSQL接続データが含まれている場合、DBConnectionオブジェクトに型変換し、そのプロパティを使用してデータベースのコマンド、コマンドタイプ、接続の説明、接続情報、資格情報などを取得することができます。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






{{< app/cells/assistant language="java" >}}
