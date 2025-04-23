---
title: Récupération des données de connexion SQL avec C++
linktitle: Récupération des données de connexion SQL
type: docs
weight: 10
url: /fr/cpp/retrieving-sql-connection-data/
description: Apprenez comment récupérer les données de connexion SQL, y compris l URL du serveur, le nom d utilisateur, le nom de la table, et plus en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells peut vous aider à récupérer les données de connexion SQL. Cela inclut toutes les données nécessaires pour établir une connexion avec le serveur SQL, par exemple, **URL du serveur**, **nom d'utilisateur**, **nom de la table**, **requête SQL complète**, **type de requête**, **emplacement de la table**, et **nom de la plage nommée** associée.

{{% /alert %}}

Dans Microsoft Excel, se connecter à une base de données en :

1. Cliquant sur le menu **Données** et en sélectionnant **À partir d'autres sources**, puis **Depuis un serveur SQL**.
1. Ensuite, sélectionnez **Données** suivi de **Connexions**.
1. Utilisez l'assistant Connexions pour vous connecter à la base de données et créer une requête de base de données.

Aspose.Cells offre la méthode `Workbook::get_DataConnections()` pour récupérer les connexions externes. Elle retourne une collection d'objets `ExternalConnection` dans le classeur.

Si l'objet `ExternalConnection` contient des données de connexion SQL, il peut être casté en un objet `DBConnection` et ses propriétés peuvent être utilisées pour récupérer la commande de la base de données, le type de commande, la description de la connexion, les informations de connexion, les identifiants, etc.

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
