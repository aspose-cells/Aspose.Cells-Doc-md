---
title: Seiten Setup Funktionen mit Node.js über C++
linktitle: Seiteneinrichtungsfunktionen
type: docs
weight: 60
url: /de/nodejs-cpp/page-setup-features/
description: Erforschen Sie die Seiten Setup Funktionen mit Aspose.Cells for Node.js via C++. Lernen Sie, wie Sie Seitendimensionen, Ausrichtungen und Einstellungen konfigurieren.
keywords: Seiten Setup Funktionen Node.js über C++, Seitendimensionen konfigurieren Node.js über C++, Seitenorientierungsoptionen Node.js über C++
---



## **Einführung**
 Mit Aspose.Cells for Node.js via C++ können Sie verschiedene Seiten-Setup-Funktionen einer Excel-Arbeitsmappe manipulieren. Dazu gehören das Einstellen der Seitengröße, Ausrichtung, Ränder und mehr. Eine richtige Konfiguration verbessert Druck- und Anzeigeerfahrung.

## ** Seitengröße und Ausrichtung einstellen**
 Sie können die Seitengröße und Ausrichtung eines Arbeitsblatts mit der `PageSetup`-Klasse festlegen. Diese bietet verschiedenste Eigenschaften zur Verwaltung von Seitendimensionen und Layout.

### **Beispielcode**
 Hier ist ein Beispielcode, der zeigt, wie man die Seitengröße und Ausrichtung festlegt.

```javascript
const { Workbook } = require("aspose.cells");

// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size

// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation

// Save the workbook
workbook.save("PageSetupExample.xlsx");
```

## **Ränder einstellen**
 Sie können auch die Ränder für die Seite mit derselben `PageSetup`-Klasse festlegen. Die Ränder können für links, rechts, oben und unten angepasst werden.

### **Beispielcode**
 So können Sie die Ränder eines Arbeitsblatts festlegen.

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **Fazit**
 In diesem Dokument haben Sie gelernt, wie man Seiteneinrichtungsfunktionen in Excel mit Aspose.Cells for Node.js via C++ manipuliert. Durch die effektive Nutzung der `PageSetup`-Klasse können Sie steuern, wie Ihre Arbeitsblätter gedruckt und angezeigt werden, was die Präsentation verbessert.

---
