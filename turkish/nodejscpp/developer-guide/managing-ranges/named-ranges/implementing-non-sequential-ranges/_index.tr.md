---
title: Node.js ile C++ kullanarak Sıralı Olmayan Aralıkların Uygulanması
linktitle: Sıralı Olmayan Menzilleri Uygulama
type: docs
weight: 700
url: /tr/nodejs-cpp/implementing-non-sequential-ranges/
description: Aspose.Cells for Node.js via C++ ile isimli sıralı olmayan aralıklar oluşturmayı öğrenin. Bağlantısız hücre aralıklarını etkili bir şekilde kullanın.
---

{{% alert color="primary" %}} 

 Normalde, isimlendirilmiş aralıklar dikdörtgen şeklindedir ve hücreler birbirine bağlı ve ardışık olur. Ama bazen, hücreler birbirine bağlı olmayan sıralı olmayan hücre aralıklarını kullanmanız gerekebilir. Aspose.Cells for Node.js via C++, bağlı olmayan hücrelerle isimli aralıklar oluşturmayı destekler.

{{% /alert %}} 

Aşağıdaki kod örneği, Aspose.Cells for Node.js via C++ ile isimli sıralı olmayan bir aralık oluşturmayı gösterir.


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
