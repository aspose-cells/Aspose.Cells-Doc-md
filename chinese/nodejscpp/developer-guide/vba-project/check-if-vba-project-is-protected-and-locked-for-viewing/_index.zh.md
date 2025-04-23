---
title: 通过Node.js的C++检查VBA项目是否受保护并且锁定以供查看
linktitle: 检查VBA项目是否受保护并已锁定以供查看
type: docs
weight: 30
url: /zh/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: 学习如何使用Aspose.Cells for Node.js via C++检查Excel文件中的VBA项目是否受保护和被锁定以供查看。
---

## 在Node.js中检查VBA项目是否受保护并锁定以供查看

Aspose.Cells允许你检测Excel文件的VBA（Visual Basic for Applications）项目是否已受保护且锁定查看。API提供[**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--)属性，如果被锁定查看，则返回[**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--)为**true**。

## **示例代码**

以下示例代码加载[示例Excel文件](43352065.xlsm)，并检查Excel文件的VBA（Visual Basic for Applications）项目是否受保护和锁定以供查看。请同时查看其控制台输出以获取参考。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **控制台输出**

这是上述示例代码在使用提供的[示例Excel文件](43352065.xlsm)时执行时的控制台输出。

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
