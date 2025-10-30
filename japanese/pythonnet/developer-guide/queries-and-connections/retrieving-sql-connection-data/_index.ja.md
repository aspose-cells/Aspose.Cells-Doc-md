---
title: SQL接続データの取得
type: docs
weight: 10
url: /ja/python-net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET では、SQL 接続データの取得を支援します。これには、SQL サーバーへの接続に必要なすべてのデータ（例：**サーバーURL**、**ユーザー名**、**テーブル名**、**完全な SQL クエリー**、**クエリタイプ**、**テーブルの位置**、および関連付けられた**名前付き範囲**）が含まれます。

{{% /alert %}}

Microsoft Excelでは、データベースに接続するには:

1. **データ**メニューをクリックし、**その他のソース**、その後 **SQL Server** を選択します。
1. 次に、**データ**、その後 **Connections** を選択します。
1. Connectionsウィザードを使用してデータベースに接続し、データベースクエリを作成します。

Aspose.Cells for Python via .NET は、外部接続を取得するための Workbook.DataConnections プロパティを提供します。これにより、ワークブック内の ExternalConnection オブジェクトのコレクションが返されます。

ExternalConnectionオブジェクトにSQL接続データが含まれている場合、それをDBConnectionオブジェクトに型変換し、データベースコマンド、コマンドの種類、接続の説明、接続情報、資格情報などを取得できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
