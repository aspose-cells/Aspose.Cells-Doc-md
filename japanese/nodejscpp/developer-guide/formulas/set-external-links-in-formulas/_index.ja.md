---
title: C++を使用してNode.jsでの数式に外部リンクを設定する
linktitle: 数式で外部リンクを設定する
type: docs
weight: 20
url: /ja/nodejs-cpp/set-external-links-in-formulas/
description: Aspose.Cells for Node.js via C++を使用して数式に外部リンクを設定する方法を学びます。 
keywords: Node.js経由でC++を使用した数式に外部リンクを設定し、外部ファイルを数式に含める（例：セルや範囲の値を評価）。Aspose.Cells for Node.js via C++はこの機能を提供しており、このドキュメントではその使い方を説明します。 
---

{{% alert color="primary" %}} 

時には、数式に外部ファイルへのリンクを含める必要があります。例えば、セルや範囲の値を評価する場合です。Aspose.Cells for Node.js via C++はこの機能を提供しており、本ドキュメントはその使用方法を説明します。

{{% /alert %}} 

以下のサンプルコードは、数式に外部ファイルを含める方法を示しています。



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get first Worksheet
const sheet = workbook.getWorksheets().get(0);

// Get Cells collection
const cells = sheet.getCells();

// Set formula with external links
cells.get("A1").setFormula(`=SUM('[${filePath}]Sheet1'!A2, '[${filePath}]Sheet1'!A4)`);

// Set formula with external links
cells.get("A2").setFormula(`='[${filePath}]Sheet1'!A8`);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
