---
title: Formüllerde Dış Bağlantıları Node.js kullanarak C++ ile ayarlayın
linktitle: Formüllerde Dış Bağlantıları Ayarlama
type: docs
weight: 20
url: /tr/nodejs-cpp/set-external-links-in-formulas/
description: Aspose.Cells for Node.js via C++ kullanarak formüllerde dış bağlantıları nasıl ayarlayacağınızı öğrenin. 
keywords: Formüllerde dış bağlantıları Node.js kullanarak C++ ile ayarlayın; formüllerde dış dosyaları dahil edin, Node.js kullanarak C++ ile 
---

{{% alert color="primary" %}} 

Bazen, dış dosyalara bağlantı eklemek gerekebilir; örneğin, bir hücre veya aralık değerini bu dosyalara karşı değerlendirmek için. Aspose.Cells for Node.js via C++ bu özelliği sağlar ve bu belge, nasıl kullanılacağını açıklar.

{{% /alert %}} 

Aşağıdaki örnek kod, formüllerde harici dosyaların nasıl dahil edileceğini gösterir.



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
{{< app/cells/assistant language="nodejs-cpp" >}}
