---
title: Recuperación de datos de conexión SQL con C++
linktitle: Recuperación de datos de conexión SQL
type: docs
weight: 10
url: /es/cpp/retrieving-sql-connection-data/
description: Aprenda cómo recuperar datos de conexión SQL, incluyendo URL del servidor, nombre de usuario, nombre de tabla y más utilizando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells puede ayudarte a recuperar datos de conexión SQL. Esto incluye cualquier dato necesario para realizar una conexión al servidor SQL, por ejemplo, URL del servidor, nombre de usuario, nombre de la tabla, consulta SQL completa, tipo de consulta, ubicación de la tabla y nombre del rango con nombre asociado.

{{% /alert %}}

En Microsoft Excel, conectarse a una base de datos mediante:

1. Haga clic en el menú **Datos** y seleccione **Desde otras fuentes** seguido de **Desde SQL Server**.
1. Luego seleccione **Datos** seguido de **Conexiones**.
1. Utilice el asistente de conexiones para conectarse a la base de datos y crear una consulta de base de datos.

Aspose.Cells proporciona el método `Workbook::get_DataConnections()` para recuperar conexiones externas. Devuelve una colección de objetos `ExternalConnection` en el libro.

Si el objeto `ExternalConnection` contiene datos de conexión SQL, puede ser convertido al tipo `DBConnection`, y sus propiedades pueden usarse para recuperar comando de base de datos, tipo de comando, descripción de la conexión, información de la conexión, credenciales y más.

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
