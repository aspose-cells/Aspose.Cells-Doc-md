---
title: Lavorare con la connessione dati esterna di tipo WebQuery con Node.js tramite C++
linktitle: Lavorare con la connessione dati esterna di tipo WebQuery
type: docs
weight: 30
url: /it/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Impara come lavorare con le connessioni dati esterne di tipo WebQuery usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puoi accedere alle connessioni dati esterne di qualsiasi tipo utilizzando la raccolta Workbook.DataConnections. Un tipo di connessione dati del genere è WebQuery. Questo articolo ti mostrerà come lavorare con la connessione dati WebQuery. Puoi creare una connessione dati WebQuery in Microsoft Excel utilizzando il menu **Dati** > **Da Web**.

{{% /alert %}}

## Lavorare con la connessione dati esterna di tipo WebQuery

Il seguente codice mostra come lavorare con la connessione dati esterna di tipo **WebQuery**. Utilizza il [file di Excel di esempio](5112365.xlsx), che puoi scaricare dal link fornito. Puoi anche vedere l'output della console di questo codice di seguito.

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

## Output della console

Ecco l'output della console del codice precedente con questo [file di Excel di esempio](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
