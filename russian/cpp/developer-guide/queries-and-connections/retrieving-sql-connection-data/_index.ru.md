---
title: Получение данных соединения SQL с помощью C++
linktitle: Получение данных подключения к SQL
type: docs
weight: 10
url: /ru/cpp/retrieving-sql-connection-data/
description: Узнайте, как получить данные соединения SQL, включая URL сервера, имя пользователя, название таблицы и другие, с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells может помочь вам получить данные подключения к SQL. Это включает все данные, необходимые для подключения к серверу SQL, например, **URL сервера**, **имя пользователя**, **имя таблицы**, **полный SQL-запрос**, **тип запроса**, **местоположение таблицы** и **имя именованного диапазона**, связанного с ним.

{{% /alert %}}

В Microsoft Excel подключитесь к базе данных, выполнив следующее:

1. Нажмите меню **Данные** и выберите **Из других источников**, а затем **Из SQL Server**.
1. Затем выберите **Данные**, а затем **Подключения**.
1. Используйте мастер подключений для подключения к базе данных и создания запроса к базе данных.

Aspose.Cells предоставляет метод `Workbook::get_DataConnections()` для получения внешних соединений. Он возвращает коллекцию объектов `ExternalConnection` в рабочей книге.

Если объект `ExternalConnection` содержит данные соединения SQL, его можно привести к объекту `DBConnection`, и его свойства могут использоваться для получения команд базы данных, типа команды, описания соединения, информации о соединении, учетных данных и других.

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
