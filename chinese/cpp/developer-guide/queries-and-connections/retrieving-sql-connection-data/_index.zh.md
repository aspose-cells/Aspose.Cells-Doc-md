---
title: 用C++提取SQL连接数据
linktitle: 检索SQL连接数据
type: docs
weight: 10
url: /zh/cpp/retrieving-sql-connection-data/
description: 学习如何使用Aspose.Cells for C++检索SQL连接数据，包括服务器URL、用户名、表名等。
---

{{% alert color="primary" %}}

Aspose.Cells可以帮助您检索SQL连接数据。这包括建立SQL服务器连接所需的所有数据，例如**服务器URL**，**用户名**，**表名**，**完整SQL查询**，**查询类型**，**表的位置**和与之关联的命名范围的**名称**。

{{% /alert %}}

在Microsoft Excel中，通过以下步骤连接数据库：

1. 单击**数据**菜单，选择**来自其他源**，然后选择**来自SQL Server**。
2. 然后选择**数据**，然后选择**连接**。
3.使用连接向导连接到数据库并创建数据库查询。

Aspose.Cells提供`Workbook::get_DataConnections()`方法，用于检索外部连接。它返回工作簿中的`ExternalConnection`对象集合。

如果`ExternalConnection`对象包含SQL连接数据，可以将其强制转换为`DBConnection`对象，并利用其属性检索数据库命令、命令类型、连接描述、连接信息、凭据等。

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
