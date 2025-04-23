---
title: Trabajar con conexiones de datos externas del tipo WebQuery con Node.js a través de C++
linktitle: Trabajar con conexión de datos externos de tipo WebQuery
type: docs
weight: 30
url: /es/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Aprende cómo trabajar con conexiones de datos externas del tipo WebQuery usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Puede acceder a conexiones de datos externas de cualquier tipo utilizando la colección Workbook.DataConnections. Un tipo de dicha conexión de datos es WebQuery. Este artículo le mostrará cómo trabajar con una conexión de datos de tipo WebQuery. Puede crear una conexión de datos de tipo WebQuery en Microsoft Excel utilizando el menú **Datos** > **Desde la Web**.

{{% /alert %}}

## Trabajando con Conexiones de Datos Externas de tipo WebQuery

El siguiente código muestra cómo trabajar con una conexión de datos externa de tipo **WebQuery**. Utiliza el [archivo de Excel de ejemplo](5112365.xlsx) que puede descargar desde el enlace proporcionado. También puede ver la salida de la consola de este código más abajo.

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

## Salida de la consola

Aquí está la salida de la consola del código anterior con este [archivo de Excel de ejemplo](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
