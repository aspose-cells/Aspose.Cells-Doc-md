---
title: Node.js kullanarak C++ ile çalışma sayfası benzersiz kimliğini alın
linktitle: Çalışma sayfası benzersiz kimliğini alma
type: docs
weight: 190
url: /tr/nodejs-cpp/get-worksheet-unique-id/
description: Bu makale, Node.js kütüphanesi ve C++ API programını kullanarak Excel çalışma sayfası benzersiz kimliğini nasıl alınacağını gösterir.
keywords: benzersiz kimlik excel çalışma sayfası Node.js via C++, benzersiz kimlik çalışma sayfası Node.js via C++
---

## **Çalışma sayfası benzersiz kimliğini alın**

Aspose.Cells for Node.js via C++, bir çalışma sayfasının benzersiz kimliğini [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) özelliğini kullanarak alabilme yeteneği sağlar. Aşağıdaki kod örneği, bir çalışma sayfasının benzersiz kimliğini yazdırmak için [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) özelliğinin kullanımını göstermektedir. Aşağıdaki kod örneği bu [örnek excel dosyasını](105480213.xlsx) kullanır.

### Kaynak Kodu

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
