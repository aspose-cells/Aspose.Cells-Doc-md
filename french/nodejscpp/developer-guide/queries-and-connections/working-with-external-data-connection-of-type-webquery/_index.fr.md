---
title: Travailler avec la connexion de données externe de type WebQuery avec Node.js via C++
linktitle: Travailler avec une connexion de données externe de type WebQuery
type: docs
weight: 30
url: /fr/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Apprenez à travailler avec les connexions de données externes de type WebQuery en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Vous pouvez accéder à n'importe quel type de connexion de données externe en utilisant la collection Workbook.DataConnections. Un type de cette connexion de données est WebQuery. Cet article vous montrera comment travailler avec la connexion de données WebQuery. Vous pouvez créer une connexion de données WebQuery dans Microsoft Excel en utilisant le menu **Données** > **À partir du Web**.

{{% /alert %}}

## Travail avec une connexion de données externe de type WebQuery

Le code suivant montre comment travailler avec une connexion de données externe de type **WebQuery.** Il utilise le [fichier Excel d'exemple](5112365.xlsx) que vous pouvez télécharger à partir du lien fourni. Vous pouvez également voir la sortie de la console de ce code ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "WebQuerySample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const connections = workbook.getDataConnections();
if (connections.getCount() > 0) {
const connection = connections.get(0);

if (connection instanceof AsposeCells.WebQueryConnection) {
const webQuery = connection;
console.log("Web Query URL: " + webQuery.getUrl());
}
}
```

## Sortie de la console

Voici la sortie de la console du code ci-dessus avec ce [fichier Excel d'exemple](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
