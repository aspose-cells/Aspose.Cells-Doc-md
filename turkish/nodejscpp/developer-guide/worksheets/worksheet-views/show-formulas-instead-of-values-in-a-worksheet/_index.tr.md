---
title: Node.js ve C++ kullanarak Bir Çalışma Sayfasında Formüller Yerine Değerleri Göster
linktitle: Çalışma Sayfasında Değerler Yerine Formülleri Gösterme
type: docs
weight: 20
url: /tr/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Bu makale, Excel çalışma sayfasında veya elektronik tablodaki değerler yerine formülleri programlı olarak göstermek için Node.js API sinin C++ aracılığıyla nasıl kullanılacağını örnek kodlarla sağlar.
---

{{% alert color="primary" %}}

Microsoft Excel'de **Formülleri Göster** seçeneği kullanılarak hesaplanan değerler yerine formüllerin gösterilmesi mümkündür. Formüller gösterildiğinde, Microsoft Excel çalışma sayfasında formülleri görüntüler. Aynı sonucu Aspose.Cells for Node.js via C++ kullanarak da elde edebilirsiniz.

{{% /alert %}}

Aspose.Cells, [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--) adlı bir özellik sağlar. Bu değeri **true** yaparak Microsoft Excel'e formülleri gösterecek şekilde ayarlayabilirsiniz.

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
