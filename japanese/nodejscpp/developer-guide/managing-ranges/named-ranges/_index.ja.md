---
title: Node.jsを使用してC++経由でブックとシートのスコープの名前付き範囲を作成する
linktitle: 名前付き範囲
type: docs
weight: 40
url: /ja/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Aspose.Cells for Node.js via C++を使って、ブックとシートのスコープの名前付き範囲の作成方法を学びます。 
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ワークブック（またはグローバルスコープとしても知られています）とワークシートの2つの異なるスコープで名前付き範囲を定義できます。

- ワークブックスコープの名前付き範囲は、そのワークブック内の任意のワークシートから、名前を単純に使用することでアクセスできます。
- ワークシートスコープの名前付き範囲は、それが作成された特定のワークシートの参照でアクセスされます。

Aspose.Cells for Node.js via C++は、Microsoft Excelと同じ機能を提供し、ブックとシートのスコープの名前付き範囲を追加します。シートスコープの名前付き範囲を作成する際は、その名前付き範囲にシート参照を含めて、シートスコープの名前付き範囲として指定します。

{{% /alert %}} 
## **ブックスコープで名前を付けられた範囲を追加する**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **ワークシートスコープを持つ名前付き範囲を追加する**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **高度なトピック**
- [アクセスの作成とコピーした名前付き範囲](/cells/ja/nodejs-cpp/create-access-and-copy-named-ranges/)
- [名前付き範囲の書式と変更](/cells/ja/nodejs-cpp/format-and-modify-named-ranges/)
- [外部リンク付きの範囲を取得する](/cells/ja/nodejs-cpp/get-range-with-external-links/)
- [非連続範囲の実装](/cells/ja/nodejs-cpp/implementing-non-sequential-ranges/)


{{< app/cells/assistant language="nodejs-cpp" >}}
