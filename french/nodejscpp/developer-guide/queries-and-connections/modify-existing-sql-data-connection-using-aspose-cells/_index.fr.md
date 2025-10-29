---  
title: Modifier une connexion de données SQL existante avec Aspose.Cells for Node.js via C++  
linktitle: Modifier une connexion de données SQL existante à l aide d Aspose.Cells  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Apprenez comment modifier les propriétés de la connexion de données SQL existante en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells prend en charge la modification de connexions de données SQL existantes. L'article expliquera comment utiliser Aspose.Cells pour modifier différentes propriétés de la connexion de données SQL.  
Vous pouvez ajouter ou consulter des connexions de données dans Microsoft Excel en suivant la commande de menu **Données > Connexions**.  
De même, Aspose.Cells offre des moyens d'accéder et de modifier les connexions de données en utilisant la collection Workbook.dataConnections.  
{{% /alert %}}  

## Modifier une connexion de données SQL existante à l'aide d'Aspose.Cells  

L’échantillon suivant illustre l’utilisation de Aspose.Cells for Node.js via C++ pour modifier la connexion de données SQL du classeur. Vous pouvez télécharger le fichier Excel source utilisé dans ce code ainsi que le fichier Excel de sortie généré par le code à partir des liens suivants.  

- [Fichier Excel Source](5112357.xlsx)  
- [Fichier Excel de Sortie](5112356.xlsx)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataConnection.xlsx"));


// Access first Data Connection
const conn = workbook.getDataConnections().get(0);

// Change the Data Connection Name and Odc file
conn.setName("MyConnectionName");
conn.setOdcFile("C:\\Users\\MyDefaulConnection.odc");

// Change the Command Type, Command and Connection String
const dbConn = conn;
dbConn.setCommandType(AsposeCells.OLEDBCommandType.SqlStatement);
dbConn.setCommand("Select * from AdminTable");
dbConn.setConnectionString("Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
