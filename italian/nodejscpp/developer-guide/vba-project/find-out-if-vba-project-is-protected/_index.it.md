---
title: Scopri se il progetto VBA è protetto con Node.js tramite C++
linktitle: Scopri se il progetto VBA è Protetto
type: docs
weight: 20
url: /it/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Scopri se il progetto VBA è protetto in Node.js**

Puoi scoprire se il progetto VBA (Visual Basic Applications) del tuo file Excel è protetto o meno con Aspose.Cells utilizzando la proprietà [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--).

## **Codice di Esempio**

Il seguente esempio di codice crea un workbook e poi verifica se il suo progetto VBA è protetto o meno. Successivamente protegge il progetto VBA e di nuovo verifica se è protetto o meno. Consulta l'output della console come riferimento. Prima della protezione, [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) restituisce **false**, ma dopo la protezione, restituisce **true**.

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

## **Output della console**

Questo è l'output della console del codice di esempio sopra per un riferimento.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
