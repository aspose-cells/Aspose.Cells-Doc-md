---
title: C++を使用したSQL接続データの取得
linktitle: SQL接続データの取得
type: docs
weight: 10
url: /ja/cpp/retrieving-sql-connection-data/
description: SQL接続データ（サーバーURL、ユーザー名、テーブル名など）を取得する方法をAspose.Cells for C++を使用して学習します。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、SQL接続データを取得できます。これには、SQLサーバへの接続に必要なすべてのデータが含まれます。たとえば、**サーバーURL**、**ユーザー名**、**テーブル名**、**完全なSQLクエリ**、**クエリの種類**、**テーブルの場所**、およびそれに関連付けられた**名前付き範囲の名前**などです。

{{% /alert %}}

Microsoft Excelでは、データベースに接続するには:

1. **データ**メニューをクリックし、**その他のソース**、その後 **SQL Server** を選択します。
1. 次に、**データ**、その後 **Connections** を選択します。
1. Connectionsウィザードを使用してデータベースに接続し、データベースクエリを作成します。

Aspose.Cells は、外部接続を取得する `Workbook::get_DataConnections()` メソッドを提供します。これにより、ブック内の `ExternalConnection` オブジェクトのコレクションが返されます。

`ExternalConnection` オブジェクトにSQL接続データが含まれている場合、それを `DBConnection` オブジェクトに型キャストし、そのプロパティを使用してデータベースコマンド、コマンドタイプ、接続説明、接続情報、資格情報などを取得できます。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object from source file
    Workbook workbook(srcDir + u"connection.xlsx");

    // Access the external collections
    ExternalConnectionCollection connections = workbook.GetDataConnections();

    int connectionCount = connections.GetCount();

    ExternalConnection connection;

    for (int i = 0; i < connectionCount; i++)
    {
        connection = connections.Get(i);

        // Check if the Connection is DBConnection, then retrieve its various properties
        if (connection.GetClassType() == ExternalConnectionClassType::Database)
        {
            DBConnection dbConn = static_cast<DBConnection&>(connection);

            // Retrieve DB Connection Command
            std::cout << "Command: " << dbConn.GetCommand().ToUtf8() << std::endl;

            // Retrieve DB Connection Command Type
            std::cout << "Command Type: " << static_cast<int>(dbConn.GetCommandType()) << std::endl;

            // Retrieve DB Connection Description
            std::cout << "Description: " << dbConn.GetConnectionDescription().ToUtf8() << std::endl;

            // Retrieve DB Connection ID
            std::cout << "Id: " << dbConn.GetId() << std::endl;

            // Retrieve DB Connection Info
            std::cout << "Info: " << dbConn.GetConnectionString().ToUtf8() << std::endl;

            // Retrieve DB Connection Credentials
            std::cout << "Credentials: " << static_cast<int>(dbConn.GetCredentialsMethodType()) << std::endl;

            // Retrieve DB Connection Name
            std::cout << "Name: " << dbConn.GetName().ToUtf8() << std::endl;

            // Retrieve DB Connection ODC File
            std::cout << "OdcFile: " << dbConn.GetOdcFile().ToUtf8() << std::endl;

            // Retrieve DB Connection Source File
            std::cout << "Source file: " << dbConn.GetSourceFile().ToUtf8() << std::endl;

            // Retrieve DB Connection Type
            std::cout << "Type: " << static_cast<int>(dbConn.GetSourceType()) << std::endl;

            // Retrieve DB Connection Parameters Collection
            ConnectionParameterCollection paramCollection = dbConn.GetParameters();

            int paramCount = paramCollection.GetCount();

            // Iterate the Parameter Collection
            for (int j = 0; j < paramCount; j++)
            {
                ConnectionParameter param = paramCollection.Get(j);

                // Retrieve Parameter Cell Reference
                std::cout << "Cell reference: " << param.GetCellReference().ToUtf8() << std::endl;

                // Retrieve Parameter Name
                std::cout << "Parameter name: " << param.GetName().ToUtf8() << std::endl;

                // Retrieve Parameter Prompt
                std::cout << "Prompt: " << param.GetPrompt().ToUtf8() << std::endl;

                // Retrieve Parameter SQL Type
                std::cout << "SQL Type: " << static_cast<int>(param.GetSqlType()) << std::endl;

                // Retrieve Parameter Type
                std::cout << "Param Type: " << static_cast<int>(param.GetType()) << std::endl;

                // Retrieve Parameter Value
                std::cout << "Param Value: " << param.GetValue().ToString().ToUtf8() << std::endl;

            } // End for
        } // End if
    } // End for

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
