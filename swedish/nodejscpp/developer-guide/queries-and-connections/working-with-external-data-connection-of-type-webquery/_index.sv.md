---
title: Arbeta med externa datakonnectioner av typen WebQuery med Node.js via C++
linktitle: Arbeta med extern datanslutning av typ WebQuery
type: docs
weight: 30
url: /sv/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Lär dig hur du arbetar med externa datakonnectioner av typen WebQuery med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Du kan komma åt extern datanslutning av vilken typ som helst genom att använda Workbook.DataConnections-samlingen. En typ av sådan datanslutning är WebQuery. Den här artikeln visar hur du arbetar med WebQuery-datanslutning. Du kan skapa WebQuery-datanslutning i Microsoft Excel med menyn **Data** > **Från webben**.

{{% /alert %}}

## Arbeta med extern datanslutning av typ WebQuery

Följande kod visar hur man arbetar med extern datanslutning av typ **WebQuery**. Den använder [exempel excelfilen](5112365.xlsx) som du kan ladda ner från den angivna länken. Du kan också se konsolens utdata av den här koden längre ner.

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

## Konsoloutput

Här är konsolens utdata av den ovanstående koden med denna [exempel excelfilen](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
