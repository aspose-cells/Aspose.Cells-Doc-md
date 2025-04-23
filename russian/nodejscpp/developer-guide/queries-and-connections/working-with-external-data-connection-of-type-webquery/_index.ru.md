---
title: Работа с внешним соединением данных типа WebQuery с Node.js через C++
linktitle: Работа с внешним подключением данных типа WebQuery
type: docs
weight: 30
url: /ru/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Узнайте, как работать с внешними соединениями данных типа WebQuery с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Вы можете получить доступ к внешнему подключению данных любого типа, используя коллекцию Workbook.DataConnections. Одним из таких подключений данных является WebQuery. В этой статье будет показано, как работать с подключением данных WebQuery. Вы можете создать подключение данных WebQuery в Microsoft Excel, используя меню **Данные** > **Из Интернета**.

{{% /alert %}}

## Работа с внешним подключением данных типа WebQuery

В следующем коде показано, как работать с внешним подключением данных типа **WebQuery**. Он использует [образец электронного файла](5112365.xlsx), который вы можете скачать по предоставленной ссылке. Вы также можете увидеть вывод консоли этого кода ниже.

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

## Вывод в консоль

Вот вывод консоли вышеуказанного кода с этим [образцом электронного файла](5112365.xlsx).

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
