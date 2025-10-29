---
title: 通过 C++ 在 Node.js 中释放工作簿的非托管资源
linktitle: 释放工作簿的非托管资源
type: docs
weight: 310
url: /zh/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 释放 Workbook 对象的非托管资源。 
---

{{% alert color="primary" %}}

Aspose.Cells 提供 [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) 方法以释放 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 对象的非托管资源。Dispose 模式仅用于访问非托管资源的对象，例如文件和管道句柄、注册表句柄、等待句柄或指向非托管内存块的指针。这是因为垃圾收集器在回收未使用的托管对象方面非常高效，但无法回收非托管对象。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 对象现在实现了 *System.IDisposable* 接口，该接口包含唯一的方法 [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--)。你可以直接调用 [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) 方法，或者使用 *Using* 语句自动调用此方法。

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
