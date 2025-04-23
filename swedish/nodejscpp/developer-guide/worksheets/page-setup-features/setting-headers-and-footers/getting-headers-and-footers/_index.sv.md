---
title: Hämtar rubriker eller sidfötter med Node.js via C++
linktitle: Att få headers eller footers
type: docs
weight: 30
url: /sv/nodejs-cpp/get-headers-or-footers/
description: Denna artikel förklarar hur man programmässigt hämtar rubriker och sidfötter från Excel eller OpenOffice filer med hjälp av Node.js via C++ API.
---

{{% alert color="primary" %}}

Headers och footers visas endast i vy för sidlayout, utskriftsvisning och på utskrifter. 

Du kan också använda dialogrutan Sidlayout om du vill visa headers eller footers för mer än ett kalkylblad åt gången. 

För andra bladtyper, såsom kalkylblad eller diagram, kan du infoga headers och footers endast genom att använda dialogrutan Sidlayout.

{{% /alert %}}

## **Hämta sidhuvuden och sidfötter i MS Excel**
1. Klicka på kalkylarket där du vill visa eller ändra sidhuvuden eller sidfötter.
2. På fliken Visa, i gruppen arbetsboksvisningar, klicka på Sidlayout.
   Excel visar kalkylarket i Sidlayoutvy.
3. För att visa eller redigera en sidhuvud eller sidfot, klicka i vänster-, mitt- eller höger sidhuvud- eller sidfotstextruta längst upp eller längst ned på kalkylarket (under Sidhuvud eller ovanför Sidfot).


## **Hämtar rubriker och sidfötter med Aspose.Cells for Node.js via C++**
Med [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) och [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-) metoder kan Node.js-utvecklare enkelt hämta rubriker eller sidfötter från filen.

1. Konstruera en arbetsbok för att öppna filen.
2. Hämta kalkylbladet där du vill hämta rubriker eller sidfot.
3. Hämta rubrik eller sidfot med ett specifikt avsnitts-ID.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Parera sidhuvuden och sidfötter till kommandolista**
Rubrik- eller sidfötters text kan innehålla specialkommandon, exempelvis en platshållare för sidnummer, aktuellt datum eller textformateringsattribut.

Specialkommandon representeras av en enda bokstav med en ledande och-symbol ("&").

Rubrik- och sidföttersträngarna konstrueras med ABNF-grammatik. Det är inte lätt att förstå utan en visare.

Aspose.Cells for Node.js via C++ tillhandahåller [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) metod för att tolka rubriker och sidfötter som kommando lista.

Följande kod visar hur man tolkar rubrik eller sidfot som kommando lista och bearbetar kommandon:

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
