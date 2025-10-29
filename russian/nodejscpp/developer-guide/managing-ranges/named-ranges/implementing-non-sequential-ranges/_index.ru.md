---
title: Реализация несеквентных диапазонов с Node.js через C++
linktitle: Реализация неупорядоченных диапазонов
type: docs
weight: 700
url: /ru/nodejs-cpp/implementing-non-sequential-ranges/
description: Узнайте, как создавать именованные несеквентные диапазоны с помощью Aspose.Cells for Node.js via C++. Эффективно используйте диапазоны несмежных ячеек.
---

{{% alert color="primary" %}} 

 Обычно именованные диапазоны являются прямоугольными с непрерывными и смежными ячейками. Но иногда вам может понадобиться использовать несеквентный диапазон ячеек, в котором ячейки не смежные. Aspose.Cells for Node.js via C++ поддерживает создание именованного диапазона с несмежными ячейками.

{{% /alert %}} 

 Пример кода ниже показывает, как создать именованный несеквентный диапазон с помощью Aspose.Cells for Node.js via C++.


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
