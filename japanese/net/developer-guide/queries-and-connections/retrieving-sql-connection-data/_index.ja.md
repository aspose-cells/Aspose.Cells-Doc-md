---
title: SQL 接続データの取得
type: docs
weight: 10
url: /ja/net/retrieving-sql-connection-data/
---
{{% alert color="primary" %}}

Aspose.Cells は、SQL 接続データの取得に役立ちます。これには、SQL サーバーへの接続に必要なすべてのデータが含まれます。**サーバー URL**, **ユーザー名**, **テーブル名**, **完全な SQL クエリ**, **クエリの種類**, **テーブルの場所**、 と**名前付き範囲の名前**それに関連付けられています。

{{% /alert %}}

Microsoft Excel で、次の方法でデータベースに接続します。

1. をクリックすると**データ**メニューと選択**他の情報源から**に続く**SQL Server から**.
1. 次に選択します**データ**に続く**接続**.
1. 接続ウィザードを使用してデータベースに接続し、データベース クエリを作成します。

Aspose.Cells は、外部接続を取得するための Workbook.DataConnections プロパティを提供します。ブック内の ExternalConnection オブジェクトのコレクションを返します。

ExternalConnection オブジェクトに SQL 接続データが含まれている場合、DBConnection オブジェクトにタイプキャストすることができ、そのプロパティを使用して、データベース コマンド、コマンド タイプ、接続の説明、接続情報、資格情報などを取得できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
