---
title: Recuperare i dati di connessione SQL con C++
linktitle: Recupero dei Dati di Connessione SQL
type: docs
weight: 10
url: /it/cpp/retrieving-sql-connection-data/
description: Impara come recuperare i dati di connessione SQL, incluso URL del server, nome utente, nome della tabella e altro usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells può aiutarti a recuperare i dati di connessione SQL. Ciò include tutti i dati necessari per stabilire una connessione con il server SQL, ad esempio, **URL server**, **nome utente**, **nome tabella**, **query SQL completa**, **tipo di query**, **posizione della tabella**, e **nome dell'intervallo con nome** ad esso associato.

{{% /alert %}}

In Microsoft Excel, connettersi a un database tramite:

1. Cliccando sul menu **Dati** e selezionando **Da Altre Origini** seguito da **Da Server SQL**.
1. Poi selezionare **Dati** seguito da **Connessioni**.
1. Utilizzare la procedura guidata di connessione per collegarsi al database e creare una query del database.

Aspose.Cells fornisce il metodo `Workbook::get_DataConnections()` per recuperare le connessioni esterne. Restituisce una collezione di oggetti `ExternalConnection` nel workbook.

Se l'oggetto `ExternalConnection` contiene dati di connessione SQL, può essere castato al tipo `DBConnection` e le sue proprietà possono essere usate per recuperare comando del database, tipo di comando, descrizione della connessione, informazioni sulla connessione, credenziali e altro.

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
