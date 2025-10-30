---
title: Ställa in olika headers och footers för olika sidor med Node.js via C++
linktitle:  Inställ olika sidhuvuden och sidfötter för olika sidor 
type: docs
weight: 35
url: /sv/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Denna artikel visar exempel på kod som visar hur man programmässigt ställer in headers och footers för Excel arbetsbladets Siduppställning med hjälp av Aspose.Cells for Node.js via C++. Ställ in headers och footers för första, udda och jämna sidor.
keywords: ställer in excel header footer första sidan Node.js via C++, ställer in excel header footer udda sidor Node.js via C++, ställer in excel header footer jämna sidor Node.js via C++
---

{{% alert color="primary" %}}

MS Excel stöder att ställa in olika rubriker och fotnoter för första sidan, udda sidor och jämna sidor sedan Excel 2007.
Aspose.Cells for Node.js via C++ stöder samma funktion.

{{% /alert %}}

## **Inställning av olika sidhuvuden och sidfötter i MS Excel**

**![Inställning av olika sidhuvuden och sidfötter](difpage.png)**

1. Klicka på **Sidlayout > Sidhuvud/fot > Sidhuvud/sidfot**.
1. Kontrollera **Different Odd and Even Pages** eller **Different first page**.
1. Ange olika sidhuvuden och sidfötter.

## **Ställa in olika headers och footers med Aspose.Cells for Node.js via C++**

Aspose.Cells beter sig på samma sätt som Excel.
1. Sätter flaggorna [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) och [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. Ange olika sidhuvuden och sidfötter.
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
{{< app/cells/assistant language="nodejs-cpp" >}}
