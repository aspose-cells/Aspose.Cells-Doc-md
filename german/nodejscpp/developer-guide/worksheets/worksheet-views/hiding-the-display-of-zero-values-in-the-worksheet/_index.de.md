---
title: Ausblenden der Anzeige von Nullwerten im Arbeitsblatt mit Node.js via C++
linktitle: Ausblenden der Anzeige von Nullwerten im Arbeitsblatt
type: docs
weight: 50
url: /de/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Dieser Artikel zeigt Ihnen Beispielcode, wie Sie Nullwerte in einer Excel Tabelle programmgesteuert mit der Node.js Bibliothek via C++ ausblenden.
keywords: Nullwerte im Excel Arbeitsblatt in Node.js via C++ ausblenden
---

{{% alert color="primary" %}} 

Manchmal müssen Sie Nullwerte in einer Tabelle ausblenden. Es könnte eine persönliche Vorliebe oder ein Formatierungsstandard sein.

{{% /alert %}} 

Um Nullwerte in einem Arbeitsblatt in Microsoft Excel zu verstecken (z. B. Microsoft Excel 2003):

1. Wählen Sie im Menü **Extras** die Option **Optionen** und dann den Tab **Ansicht** aus.
1. Deaktivieren Sie die Option **Nullwerte**.
1. Klicken Sie auf **OK**.

Bitte sehen Sie sich den folgenden Beispielcode an, der das Ausblenden von Nullen mit Aspose.Cells for Node.js via C++ demonstriert.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
