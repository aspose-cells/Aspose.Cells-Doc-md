---
title: 通过 C++ 使用 Node.js 实现非连续区域
linktitle: 实现非连续范围
type: docs
weight: 700
url: /zh/nodejs-cpp/implementing-non-sequential-ranges/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 创建命名的非连续区域。有效利用不相邻的单元格区域。
---

{{% alert color="primary" %}} 

通常，命名范围是矩形，单元格连续且相邻。但有时你可能需要使用非连续的单元格区域，其中单元格不相邻。Aspose.Cells for Node.js via C++ 支持创建包含非相邻单元格的命名范围。

{{% /alert %}} 

下面的代码示例展示了如何使用 Aspose.Cells for Node.js via C++ 创建一个命名的非连续区域。


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a Name for non sequenced range
const index = workbook.getWorksheets().getNames().add("NonSequencedRange");

const name = workbook.getWorksheets().getNames().get(index);

// Creating a non sequence range of cells
name.setRefersTo("=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

// Save the workbook
workbook.save(path.join(dataDir, "Output.out.xlsx"));
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
