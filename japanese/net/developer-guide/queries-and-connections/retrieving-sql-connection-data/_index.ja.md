---
title: SQL接続データの取得
type: docs
weight: 10
url: /ja/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、SQL接続データを取得できます。これには、SQLサーバへの接続に必要なすべてのデータが含まれます。たとえば、**サーバーURL**、**ユーザー名**、**テーブル名**、**完全なSQLクエリ**、**クエリの種類**、**テーブルの場所**、およびそれに関連付けられた**名前付き範囲の名前**などです。

{{% /alert %}}

Microsoft Excelでは、データベースに接続するには:

1. **データ**メニューをクリックし、**その他のソース**、その後 **SQL Server** を選択します。
1. 次に、**データ**、その後 **Connections** を選択します。
1. Connectionsウィザードを使用してデータベースに接続し、データベースクエリを作成します。

Aspose.Cellsは、外部接続の取得のためのWorkbook.DataConnectionsプロパティを提供します。これはワークブック内のExternalConnectionオブジェクトのコレクションを返します。

ExternalConnectionオブジェクトにSQL接続データが含まれている場合、それをDBConnectionオブジェクトに型変換し、データベースコマンド、コマンドの種類、接続の説明、接続情報、資格情報などを取得できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
