---
title: Working with External Data Connection of type WebQuery with Node.js via C++
linktitle: Working with External Data Connection of type WebQuery
type: docs
weight: 30
url: /nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Learn how to work with external data connections of type WebQuery using Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

You can access external data connection of any type using the Workbook.DataConnections collection. One type of such data connection is WebQuery. This article will show you how to work with WebQuery data connection. You can create WebQuery data connection in Microsoft Excel using the **Data** > **From Web** menu.

{{% /alert %}}

## Working with External Data Connection of type WebQuery

The following code shows how to work with external data connection of type **WebQuery**. It uses the [sample excel file](5112365.xlsx) which you can download from the provided link. You can also see the console output of this code further below.

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

## Console Output

Here is the console output of the above code with this [sample excel file](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}