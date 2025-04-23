---
title: Implementera 1904 datumsystem med Node.js via C++
description: Aspose.Cells är ett Node.js bibliotek för att arbeta med kalkylbladsfiler. Det stöder implementeringen av 1904 datumsystemet, vilket gör det möjligt för användare att beräkna och formatera baserat på datumet 1 januari 1904. Den här artikeln beskriver hur du implementerar 1904 datumsystemet med Aspose.Cells biblioteket.
keywords: Aspose.Cells, 1904 datumsystem, kalkylblad, beräkning, formatering, Node.js via C++
type: docs
weight: 7000
url: /sv/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel stöder två datumssystem: 1900-datumssystemet (standard datumssystem som implementerats i Excel för Windows) och 1904-datumssystemet. 1904-datumssystemet används vanligtvis för att säkerställa kompatibilitet med Macintosh Excel-filer och är det förvalda systemet om du använder Excel för Macintosh. Du kan ställa in 1904-datumssystemet för Excel-filer med Aspose.Cells for Node.js via C++. 

{{% /alert %}} 

För att implementera 1904-datumssystemet i Microsoft Excel (t.ex. Microsoft Excel 2003):

1. Från menyn **Verktyg** väljer du **Alternativ** och väljer fliken **Beräkning**.
1. Välj alternativet **1904 datumssystem**.
1. Klicka på **OK**.

|**Välja 1904-datumssystem i Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Se följande kodexempel om hur du uppnår detta med Aspose.Cells API:erna.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
