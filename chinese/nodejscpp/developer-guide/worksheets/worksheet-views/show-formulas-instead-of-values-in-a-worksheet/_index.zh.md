---
title: 通过Node.js和C++显示公式而非值在工作表中，示例代码
linktitle: 在工作表中显示公式而不是值
type: docs
weight: 20
url: /zh/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: 本文提供了使用Node.js API通过C++以程序化方式显示Excel工作表中的公式而非计算值的示例代码。
---

{{% alert color="primary" %}}

可以在Microsoft Excel中使用“公式”功能区的“显示公式”选项，显示公式而非计算的值。启用后，Excel会在工作表中显示公式。你也可以通过Aspose.Cells for Node.js via C++实现相同的效果。

{{% /alert %}}

Aspose.Cells提供了一个[**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--)属性。将其设置为**true**，即可让Microsoft Excel显示公式。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Load the source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Show formulas of the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
