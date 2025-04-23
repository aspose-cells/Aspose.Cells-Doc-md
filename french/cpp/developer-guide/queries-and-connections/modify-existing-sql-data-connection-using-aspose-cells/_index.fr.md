---
title: Modifier la connexion de données SQL existante avec C++ en utilisant Aspose.Cells
linktitle: Modifier la connexion de données SQL existante
type: docs
weight: 20
url: /fr/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Apprenez comment modifier la connexion de données SQL existante dans les fichiers Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la modification de la connexion de données SQL existante. Cet article expliquera comment utiliser Aspose.Cells pour modifier différentes propriétés de la connexion de données SQL.

Vous pouvez ajouter ou consulter des connexions de données dans Microsoft Excel en suivant la commande de menu **Données > Connexions**.

De même, Aspose.Cells offre les moyens d’accéder et de modifier les connexions de données en utilisant la collection `Workbook.DataConnections`.

{{% /alert %}}

## Modifier une connexion de données SQL existante à l'aide d'Aspose.Cells

L'exemple suivant illustre l'utilisation d'Aspose.Cells pour modifier la connexion de données SQL du classeur. Vous pouvez télécharger le fichier Excel source utilisé dans ce code et le fichier Excel de sortie généré par le code à partir des liens suivants.

- [Fichier Excel Source](5112357.xlsx)
- [Fichier Excel de Sortie](5112356.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataConnection.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Access first Data Connection
    ExternalConnection conn = workbook.GetDataConnections().Get(0);

    // Change the Data Connection Name and Odc file
    conn.SetName(u"MyConnectionName");
    conn.SetOdcFile(u"C:\\Users\\MyDefaulConnection.odc");

    // Change the Command Type, Command and Connection String
    DBConnection dbConn = conn;
    dbConn.SetCommandType(OLEDBCommandType::SqlStatement);
    dbConn.SetCommand(u"Select * from AdminTable");
    dbConn.SetConnectionString(u"Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Data connection updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
