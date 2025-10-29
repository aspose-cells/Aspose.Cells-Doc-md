---
title: Поиск и замена данных в диапазоне с помощью Node.js через C++
linktitle: Поиск и замена данных в диапазоне
type: docs
weight: 170
url: /ru/nodejs-cpp/search-and-replace-data-in-a-range/
description: Эта статья показывает, как искать и заменять данные в диапазоне в Excel с использованием Node.js через код C++.
keywords: node.js поиск и замена данных в excel, node.js поиск данных в excel, node.js поиск и замена данных в диапазоне, node.js поиск данных в диапазоне, node.js поиск данных в диапазоне, node.js поиск данных в диапазоне, node.js поиск данных в excel, node.js поиск данных в диапазоне, поиск и замена данных в excel с помощью node.js, поиск и замена данных в диапазоне с помощью node.js, поиск и замена данных в диапазоне с помощью node.js
---

{{% alert color="primary" %}}

Иногда необходимо искать и заменять конкретные данные в диапазоне, игнорируя значения ячеек за пределами нужного диапазона. Aspose.Cells for Node.js via C++ позволяет ограничить поиск конкретным диапазоном. В этой статье объясняется, как это сделать.

{{% /alert %}}

Aspose.Cells for Node.js via C++ предоставляет метод [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) для указания диапазона при поиске данных. Ниже приведен пример кода, который ищет и заменяет данные в диапазоне.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

const area = AsposeCells.CellArea.createCellArea("E9", "H15");

const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);

let cell = null;

do {
cell = worksheet.getCells().find("search", cell, opts);
if (cell === null || cell.isNull()) {
break;
}
cell.putValue("replace");
} while (true);

workbook.save(path.join(dataDir, "output.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
