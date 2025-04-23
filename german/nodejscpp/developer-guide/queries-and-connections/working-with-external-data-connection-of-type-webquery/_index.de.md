---
title: Arbeiten mit externer Datenverbindung vom Typ WebQuery mit Node.js über C++
linktitle: Arbeiten mit externer Datenverbindungstyp WebQuery
type: docs
weight: 30
url: /de/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Erfahren Sie, wie Sie mit externen Datenverbindungen vom Typ WebQuery mit Aspose.Cells for Node.js via C++ arbeiten. 
---

{{% alert color="primary" %}}

Sie können auf eine externe Datenverbindung beliebigen Typs über die Workbook.DataConnections-Sammlung zugreifen. Eine solche Datenverbindung ist z.B. WebQuery. In diesem Artikel wird gezeigt, wie Sie mit einer WebQuery-Datenverbindung arbeiten können. Sie können eine WebQuery-Datenverbindung in Microsoft Excel über das **Daten** > **Aus dem Web**-Menü erstellen.

{{% /alert %}}

## Arbeiten mit externer Datenverbindung des Typs WebQuery

Der folgende Code zeigt, wie Sie mit externen Datenverbindungen des Typs **WebQuery** arbeiten. Er verwendet die [Beispieldatei](5112365.xlsx), die Sie von dem bereitgestellten Link herunterladen können. Sie können auch die Konsolenausgabe dieses Codes weiter unten sehen.

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

## Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Codes mit dieser [Beispieldatei](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
