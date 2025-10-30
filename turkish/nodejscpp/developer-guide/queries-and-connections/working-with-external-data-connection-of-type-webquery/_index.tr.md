---
title: Node.js ile WebQuery türü Harici Veri Bağlantısı üzerinde çalışmak
linktitle: WebQuery Türünden Dış Veri Bağlantısı ile Çalışmak
type: docs
weight: 30
url: /tr/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Aspose.Cells for Node.js via C++ kullanarak WebQuery türündeki harici veri bağlantılarıyla nasıl çalışılacağını öğrenin. 
---

{{% alert color="primary" %}}

Çalışma Kitabı.DataConnections koleksiyonunu kullanarak herhangi bir türdeki harici veri bağlantısına erişebilirsiniz. Bu türden bir veri bağlantısı WebQuery'dir. Bu makale, WebQuery veri bağlantısıyla nasıl çalışılacağını gösterecektir. Microsoft Excel'de **Veri** > **Web'den** menüsünü kullanarak WebQuery veri bağlantısı oluşturabilirsiniz.

{{% /alert %}}

## WebQuery türündeki Harici Veri Bağlantısı ile Çalışma

Aşağıdaki kod, **WebQuery** türündeki harici veri bağlantısıyla nasıl çalışılacağını göstermektedir. İndirebileceğiniz [örnek excel dosyası](5112365.xlsx) kullanılmaktadır. Ayrıca bu kodun konsol çıktısını aşağıda görebilirsiniz.

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

## Konsol Çıkışı

Yukarıdaki kodun [örnek excel dosyası](5112365.xlsx)'nın konsol çıktısı aşağıda verilmiştir.

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
