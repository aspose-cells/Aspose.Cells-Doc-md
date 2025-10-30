---
title: Ermitteln, ob das VBA Projekt mit Node.js via C++ geschützt ist
linktitle: Herausfinden, ob das VBA Projekt geschützt ist
type: docs
weight: 20
url: /de/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Ermitteln, ob das VBA-Projekt in Node.js geschützt ist**

Sie können feststellen, ob das VBA (Visual Basic for Applications) Projekt Ihrer Excel-Datei mit Aspose.Cells mit [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--)-Eigenschaft geschützt ist.

## **Beispielcode**

Der folgende Beispielcode erstellt eine Arbeitsmappe und überprüft, ob ihr VBA-Projekt geschützt ist oder nicht. Dann schützt er das VBA-Projekt und überprüft erneut, ob das VBA-Projekt geschützt ist oder nicht. Bitte sehen Sie sich die Konsolenausgabe zur Referenz an. Vor dem Schutz gibt [**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--) **false** zurück, nach dem Schutz gibt es **true** zurück.

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

## **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes als Referenz.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
