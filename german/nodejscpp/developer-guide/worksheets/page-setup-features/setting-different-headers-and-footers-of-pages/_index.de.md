---
title: Verschiedene Kopf und Fußzeilen für verschiedene Seiten mit Node.js über C++ einstellen
linktitle: Setzen von verschiedenen Kopf und Fußzeilen für verschiedene Seiten
type: docs
weight: 35
url: /de/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Dieser Artikel bietet Beispielcode, der zeigt, wie man programmgesteuert Kopf und Fußzeilen der Seiteneinrichtung eines Excel Arbeitsblatts mit Aspose.Cells for Node.js via C++ festlegt. Legen Sie Kopf und Fußzeilen für erste, ungerade und gerade Seiten fest.
keywords: Kopf und Fußzeilen auf der ersten Seite in Excel mit Node.js über C++ festlegen, Kopf und Fußzeilen ungerader Seiten in Excel mit Node.js über C++, Kopf und Fußzeilen gerader Seiten in Excel mit Node.js über C++ festlegen
---

{{% alert color="primary" %}}

MS Excel unterstützt das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten seit Excel 2007.
 Aspose.Cells for Node.js via C++ unterstützt die gleiche Funktion.

{{% /alert %}}

## **Setzen verschiedener Kopf- und Fußzeilen in MS Excel**

**![Setzen verschiedener Kopf- und Fußzeilen](difpage.png)**

1. Klicken Sie auf **Seitenlayout > Drucktitel > Kopf-/Fußzeile**.
1. Überprüfen Sie **Unterschiedliche ungerade und gerade Seiten** oder **Unterschiedliche erste Seite**.
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

## ** Verschiedene Kopf- und Fußzeilen mit Aspose.Cells for Node.js via C++ einstellen**

Aspose.Cells verhält sich genauso wie Excel.
1. Setzt die Flags [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) und [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
