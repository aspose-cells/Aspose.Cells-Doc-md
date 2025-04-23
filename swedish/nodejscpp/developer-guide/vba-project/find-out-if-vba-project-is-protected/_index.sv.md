---
title: Hitta om VBA projekt är skyddat med Node.js via C++
linktitle: Ta reda på om VBA projektet är skyddat
type: docs
weight: 20
url: /sv/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Hitta om VBA-projekt är skyddat i Node.js**

Du kan avgöra om VBA (Visual Basic Applications) projektet för din Excel-fil är skyddat eller inte med Aspose.Cells med [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--)-egenskapen.

## **Exempelkod**

Följande exempel skapar en arbetsbok och kontrollerar om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen. Se dess konsolutdata för referens. Innan skyddet returnerar [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) **false**, men efter skyddet returnerar det **true**.

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

## **Konsoloutput**

Detta är konsoloutputen av den ovanstående exempelkoden som referens.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
