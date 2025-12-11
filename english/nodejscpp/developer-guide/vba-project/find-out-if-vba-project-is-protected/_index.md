---
title: Find out if VBA Project is Protected with Node.js via C++
linktitle: Find out if VBA Project is Protected
type: docs
weight: 20
url: /nodejs-cpp/find-out-if-vba-project-is-protected/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Find out if VBA Project is Protected in Node.js**

You can determine whether the VBA (Visual Basic for Applications) Project of your Excel file is protected using Aspose.Cells via the [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) property.

## **Sample Code**

The following sample code creates a workbook and then checks if its VBA project is protected. It then protects the VBA project and checks again. Please see the console output for reference. Before protection, [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) returns **false**, but after protection, it returns **true**.

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access the VBA project of the workbook.
const vbaProj = wb.getVbaProject();

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - Before Protecting VBA Project: " + vbaProj.isProtected());

// Protect the VBA project.
vbaProj.protect(true, "11");

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - After Protecting VBA Project: " + vbaProj.isProtected());
```

## **Console Output**

This is the console output of the above sample code for reference.

{{< highlight javascript >}}
IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True
{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
