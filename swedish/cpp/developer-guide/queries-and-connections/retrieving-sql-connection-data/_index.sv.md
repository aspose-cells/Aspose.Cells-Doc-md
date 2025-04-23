---
title: Hämta SQL anslutningsdata med C++
linktitle: Hämta SQL anslutningsdata
type: docs
weight: 10
url: /sv/cpp/retrieving-sql-connection-data/
description: Lär dig hur man hämtar data om SQL anslutning, inklusive server URL, användarnamn, tabellnamn och mer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells kan hjälpa dig att hämta SQL-anslutningsdata. Detta inkluderar all data som krävs för att göra en anslutning till SQL-servern, till exempel **server-URL**, **användarnamn**, **tabellnamn**, **full SQL-fråga**, **frågetyp**, **platsen för tabellen**, och **namnet på namngiven omfattning** som är associerat med den.

{{% /alert %}}

I Microsoft Excel, anslut till en databas genom att:

1. Klicka på menyn **Data** och välj sedan **Från andra källor** följt av **Från SQL Server**.
1. Välj sedan **Data** följt av **Anslutningar**.
1. Använd Anslutningar-guiden för att ansluta till databasen och skapa en databasfråga.

Aspose.Cells ger `Workbook::get_DataConnections()`-metoden för att hämta externa anslutningar. Den returnerar en samling av `ExternalConnection`-objekt i arbetsboken.

Om `ExternalConnection`-objektet innehåller SQL-anslutningsdata, kan det typkastas till ett `DBConnection`-objekt och dess egenskaper kan användas för att hämta databaskommandon, kommandotyp, anslutningsbeskrivning, anslutningsinformation, autentiseringsuppgifter, och så vidare.

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
