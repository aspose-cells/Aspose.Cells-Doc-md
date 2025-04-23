---
title: Sidinställningsfunktioner med Node.js via C++
linktitle: Siduppsättningsfunktioner
type: docs
weight: 60
url: /sv/nodejs-cpp/page-setup-features/
description: Utforska sidinställningsfunktioner med Aspose.Cells for Node.js via C++. Lär dig hur du konfigurerar sidans storlek, riktning och inställningar.
keywords: Sidinställningsfunktioner Node.js via C++, Konfigurera sidans storlek Node.js via C++, Riktning för sida inställningar Node.js via C++
---



## **Introduktion**
Med Aspose.Cells for Node.js via C++ kan du manipulera olika sidinställningsfunktioner för en Excel-arbetsbok. Dessa funktioner inkluderar att ställa in sidstorlek, orientering, marginaler och mer. Korrekt konfiguration av dessa funktioner möjliggör bättre utskrifts- och visningsupplevelse.

## **Ställa in sidstorlek och orientering**
Du kan ange sidans storlek och orientering för ett arbetsblad genom att använda `PageSetup`-klassen. Den ger olika egenskaper för att hantera sidans dimensioner och layout.

### **Exempel på kod**
Här är ett kodexempel som visar hur du ställer in sidans storlek och orientering.

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

## **Ställa in marginaler**
Du kan också ställa in marginalerna för sidan med samma `PageSetup`-klass. Marginalerna kan justeras för vänster, höger, topp och botten.

### **Exempel på kod**
Så här ställer du in marginalerna för ett arbetsblad.

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **Slutsats**
I denna dokumentation har du lärt dig hur du manipulerar sidinställningsfunktioner i Excel med hjälp av Aspose.Cells for Node.js via C++. Genom att använda `PageSetup`-klassen kan du kontrollera hur dina arbetsblad skrivs ut och visas, vilket förbättrar presentationen av information.

---
