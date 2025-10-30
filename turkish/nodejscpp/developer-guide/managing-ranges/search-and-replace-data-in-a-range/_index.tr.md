---
title: Node.js kullanarak C++ ile Bir Aralıkta Veri Arama ve Değiştirme
linktitle: Excel de Bir Aralıktaki Verileri Arama ve Değiştirme
type: docs
weight: 170
url: /tr/nodejs-cpp/search-and-replace-data-in-a-range/
description: Bu makale, Node.js kullanarak C++ kodu aracılığıyla Excel de bir aralıkta veri arama ve değiştirmeyi gösterir.
keywords: node.js excel de veri arama ve değiştirme, node.js ile excel de veri arama, node.js ile bir aralıkta veri arama ve değiştirme, node.js ile aralıkta veri arama, node.js ile aralıkta veri arama, node.js ile aralıkta veri arama, node.js ile excel de veri arama, node.js ile aralıkta veri arama, node.js ile excel de veri arama ve değiştirme, node.js ile aralıkta veri arama ve değiştirme, node.js ile aralıkta veri arama ve değiştirme
---

{{% alert color="primary" %}}

Bazen, aradığınız aralıkta belirli verileri aramak ve değiştirmek istersiniz ve istediğiniz aralık dışındaki hücre değerlerini görmezden gelirsiniz. Aspose.Cells for Node.js via C++, aramayı belirli bir aralıkla sınırlandırmanıza olanak tanır. Bu makale nasıl yapıldığını açıklar.

{{% /alert %}}

Aspose.Cells for Node.js via C++, veri ararken bir aralık belirtmek için [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) metodunu sağlar. Aşağıdaki kod örneği, bir aralıkta veri arama ve değiştirmeyi gösterir.

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
