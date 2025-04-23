---
title: Node.js 経由で C++ を使用して非連続範囲を実装する
linktitle: 非連続範囲の実装
type: docs
weight: 700
url: /ja/nodejs-cpp/implementing-non-sequential-ranges/
description: Aspose.Cells for Node.js via C++ を使用して、名前付き非連続範囲を作成する方法を学びます。非隣接セル範囲を効果的に使用します。
---

{{% alert color="primary" %}} 

通常、名前付き範囲は長方形であり、セルは連続し隣接しています。しかし、時には隣接しないセル範囲を使用する必要があります。Aspose.Cells for Node.js via C++ は、非隣接セルを含む名前付き範囲の作成をサポートします。

{{% /alert %}} 

以下のコード例は、Aspose.Cells for Node.js via C++ を使用して非連続範囲を作成する方法を示しています。


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
