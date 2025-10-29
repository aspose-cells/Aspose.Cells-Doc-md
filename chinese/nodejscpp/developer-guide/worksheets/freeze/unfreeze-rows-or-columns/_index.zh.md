---
title: 使用Node.js和C++解除冻结行或列
linktitle: 取消冻结窗格
type: docs
weight: 190
url: /zh/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: 在本文中，您将学习如何用Node.js API结合C++以编程方式取消冻结Excel工作表的行、列或窗格。
keywords: 取消冻结窗格、取消冻结行、取消冻结列、用Node.js和C++解除窗口冻结。
---

## **介绍**

在本文中，我们将学习如何取消冻结行、列和窗格。如果Excel文件中的工作表被冻结，有时我们希望取消冻结或调整冻结的行、列或窗格。


## **在Excel中**

1. 单击“查看”选项卡 > 冻结窗格 > 取消冻结窗格。

**![在Excel中取消冻结窗格](Unfreeze-Panes.png)**




## **使用Aspose.Cells for Node.js via C++取消冻结行、列或窗格**
使用Aspose.Cells for Node.js via C++轻松取消冻结窗格。请使用[**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--)方法取消冻结窗格。

1. 构造工作簿以打开冻结文件。
2. 使用Worksheet.unfreezePanes()方法取消冻结窗格。
3.保存文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

附有【示例源Excel文件】(Frozen.xlsx)。
{{< app/cells/assistant language="nodejs-cpp" >}}
