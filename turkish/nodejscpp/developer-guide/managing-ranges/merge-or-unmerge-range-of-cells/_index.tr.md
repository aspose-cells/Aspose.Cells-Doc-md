---
title: Node.js ve C++ kullanarak Hücre Aralıklarını Birleştir veya Ayır
linktitle: Hücre Aralığını Birleştirin veya Ayırın
type: docs
weight: 190
url: /tr/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Excel de Node.js kullanarak bir aralıktaki Hücreleri Birleştir ve Ayır kodu.
keywords: Node.js ile bir aralıktaki hücreleri birleştir ve ayır, Node.js ile aralıkta hücreleri birleştir ve ayır, Node.js kullanarak aralıktaki hücreleri birleştir ve ayır, Node.js kullanarak hücreleri birleştir ve ayır, Excel de Node.js ile hücreleri birleştir ve ayır, Node.js ile Excel de hücreleri birleştir ve ayır, Node.js ile Excel de hücreleri birleştir, Node.js ile Excel de hücreleri ayır, Node.js ile aralıkta hücreleri birleştir
---

{{% alert color="primary" %}}

Aspose.Cells'i kullanarak hücre aralığını birleştirmek veya bölmek için [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) ve [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) yöntemlerini kullanabilirsiniz. Bu makale, bir hücre aralığını tek bir hücreye birleştirmenin nasıl gerçekleştirileceğini açıklar.

{{% /alert %}}

## **Örnek**

Aşağıdaki örnek kod ilk olarak A1:D4 aralığını oluşturur, ardından [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) metodunu kullanarak aralıktaki hücreleri tek bir hücreye birleştirir. Benzer şekilde, hücreleri bölmek için bir aralık oluşturup [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) metodunu çağırabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
