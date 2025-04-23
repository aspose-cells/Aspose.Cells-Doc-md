---
title: Hämta unik ID för arbetsblad med Node.js via C++
linktitle: Få arbetsbladets unika id
type: docs
weight: 190
url: /sv/nodejs-cpp/get-worksheet-unique-id/
description: Den här artikeln visar hur man hämtar unikt ID för Excel arbetsblad med Node.js bibliotek och C++ API programmering.
keywords: unikt id excel arbetsblad Node.js via C++, unikt id arbetsblad Node.js via C++
---

## **Få arbetsbladets unika id**

Aspose.Cells for Node.js via C++ ger möjlighet att få det unika ID:t för ett arbetsblad genom att använda [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)-egenskapen. Följande kodexempel visar hur man använder [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)-egenskapen för att skriva ut det unika ID:t för ett arbetsblad. Följande kodexempel använder denna [exempel-Excel-fil](105480213.xlsx).

### Källkod

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
