---
title: Release Unmanaged Resources of the Workbook with Node.js via C++
linktitle: Release Unmanaged Resources of the Workbook
type: docs
weight: 310
url: /nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Learn how to release unmanaged resources of Workbook object using Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) method to release the unmanaged resources of the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) object. The dispose pattern is used only for objects that access unmanaged resources, such as file and pipe handles, registry handles, wait handles, or pointers to blocks of unmanaged memory. This is because the garbage collector is very efficient at reclaiming unused managed objects, but it is unable to reclaim unmanaged objects.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) object now implements the *System.IDisposable* interface which has a single method [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--). You can either directly call the [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) method or you can use the *Using* statement to call this method automatically.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create workbook object
const wb1 = new AsposeCells.Workbook();

// Call Dispose method
wb1.dispose();

// Call Dispose method via a scoped approach
(async () => {
const wb2 = new AsposeCells.Workbook();
// Any other code goes here
wb2.dispose();
})();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
