---
title: SQL Verbindungsdaten mit C++ abrufen
linktitle: SQL Verbindungsdaten abrufen
type: docs
weight: 10
url: /de/cpp/retrieving-sql-connection-data/
description: Lernen, wie man SQL Verbindungsdaten einschließlich Server URL, Benutzername, Tabellennamen und mehr mit Aspose.Cells for C++ abruft.
---

{{% alert color="primary" %}}

Aspose.Cells kann Ihnen helfen, SQL-Verbindungsdaten abzurufen. Dazu gehören alle Daten, die zum Herstellen einer Verbindung zum SQL-Server erforderlich sind, z. B. **Server-URL**, **Benutzername**, **Tabellenname**, **vollständige SQL-Abfrage**, **Abfragetyp**, **Speicherort der Tabelle** und **Name des benannten Bereichs**, der damit verbunden ist.

{{% /alert %}}

In Microsoft Excel eine Datenbankverbindung herstellen, indem Sie:

1. Zum **Daten**-Menü gehen und **Aus anderen Quellen** gefolgt von **Vom SQL Server** auswählen.
1. Dann **Daten** gefolgt von **Verbindungen** auswählen.
1. Verwenden Sie den Verbindungs-Assistenten, um eine Verbindung zur Datenbank herzustellen und eine Datenbankabfrage zu erstellen.

Aspose.Cells bietet die Methode `Workbook::get_DataConnections()`, um externe Verbindungen abzurufen. Sie gibt eine Sammlung von `ExternalConnection`-Objekten im Arbeitsbuch zurück.

Wenn das `ExternalConnection`-Objekt SQL-Verbindungsdaten enthält, kann es in ein `DBConnection`-Objekt gecastet werden, und seine Eigenschaften können verwendet werden, um Datenbankbefehl, Befehlsart, Verbindungsbeschreibung, Verbindungsinformationen, Anmeldeinformationen usw. abzurufen.

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
