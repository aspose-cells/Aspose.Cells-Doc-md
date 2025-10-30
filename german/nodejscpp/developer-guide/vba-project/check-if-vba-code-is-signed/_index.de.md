---
title: Überprüfen, ob VBA Code mit Node.js via C++ signiert ist
linktitle: Überprüfen, ob VBA Code signiert ist
type: docs
weight: 100
url: /de/nodejs-cpp/check-if-vba-code-is-signed/
description: Erfahren Sie, wie Sie überprüfen können, ob das VBA Code Projekt mit Aspose.Cells for Node.js via C++ signiert ist. 
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es dem Benutzer zu prüfen, ob das VBA-Codeprojekt signiert ist oder nicht. Bitte verwenden Sie die [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--)-Eigenschaft, um zu überprüfen, ob das VBA-Codeprojekt signiert ist oder nicht.

{{% /alert %}}

Der folgende Code erklärt, wie überprüft wird, ob der VBA-Code mit der [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--)-Eigenschaft signiert ist. Sie können jede Ihrer Excel-Dateien zum Testen dieses Codes verwenden. Für Testzwecke können Sie [diese Excel-Datei im Code verwenden](5115032.xlsm).

## **Überprüfen, ob VBA-Code in Node.js signiert ist**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## Konsolenausgabe

Unten ist die Konsolenausgabe des obigen Codes mithilfe der [Beispieldatei](5115032.xlsm), die über den Link bereitgestellt wird.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
