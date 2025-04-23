---
title: Unicode Zusatzzeichen im Ausgabepdf durch Aspose.Cells for Node.js via C++ rendern
linktitle: Unicode Supplementary Zeichen im Ausgabe PDF durch Aspose.Cells rendern
type: docs
weight: 350
url: /de/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Erfahren Sie, wie Unicode Zusatzzeichen im Ausgabepdf mit Aspose.Cells for Node.js via C++ gerendert werden. 
---

{{% alert color="primary" %}}

Normale Unicode-Zeichen sind 2 Byte lang, während Unicode-Supplementary-Zeichen 4 Byte lang sind. Aspose.Cells unterstützt jetzt das Rendern dieser 4-Byte-Unicode-Zeichen.

Im Unicode-Standard für Zeichen handelt es sich bei den Supplementary-Zeichen um Zeichen, denen die Codepunkte von U+10000 bis U+10FFFF zugewiesen sind. Mit anderen Worten, dies sind die Unicode-Zeichen größer als U+FFFF.

- In UTF-8 sind diese Zeichen jeweils 4 Bytes lang.
- In UTF-16 benötigen diese Zeichen 2 Ersatzzeichen (16-Bit-Einheiten).

{{% /alert %}}

## Unicode-Zusatzzeichen im Ausgabepdf durch Aspose.Cells for Node.js via C++ rendern

Das folgende Bildschirmfoto zeigt, wie Aspose.Cells die [Quelldatei Excel](5115563.xlsx) in das [Ausgabepdf](5115564.pdf) gerendert hat. Wie Sie sehen können, wurden alle drei Unicode-Zusatzzeichen exakt so gerendert, wie es Microsoft Excel tut.

![todo:image_alt_text](output.png)

## Beispielcode

Sie können diesen Beispiellcode verwenden, um die [Quellexceldatei](5115563.xlsx) in die [Ausgabepdf](5115564.pdf) zu konvertieren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
