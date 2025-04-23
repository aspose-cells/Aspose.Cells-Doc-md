---
title: Ta bort namngivna områden med Node.js via C++
linktitle: Ta bort namngivna områden
type: docs
weight: 90
url: /sv/nodejs-cpp/Delete-named-ranges/
description: Du kan lära dig hur man tar bort definierade namn eller namngivna områden från Excel eller OpenOffice filer med Aspose.Cells for Node.js via C++.
---

## **Introduktion**
Om det finns för många definierade namn eller namngivna områden i Excel-filerna måste vi rensa några så att de inte längre refereras till.

## **Ta bort namngivet område i MS Excel**

För att ta bort ett namngivet område från Excel kan du följa dessa steg:
1. Öppna Microsoft Excel och öppna arbetsboken som innehåller det namngivna området.
2. Gå till fliken "Formler" i Excel-ribbonen.
3. Klicka på knappen "Namnhanterare" i gruppen "Definierade namn". Detta öppnar dialogrutan för Namnhanterare.
4. I dialogrutan för Namnhanterare väljer du det namngivna området du vill ta bort.
5. Klicka på knappen "Ta bort". Bekräfta borttagningen vid behov.
6. Klicka på knappen "Stäng" för att stänga dialogrutan för Namnhanterare.
7. Spara arbetsboken för att behålla ändringarna.

## **Tar bort namngivet område med Aspose.Cells for Node.js via C++**
Med Aspose.Cells for Node.js via C++ kan du ta bort namngivna områden eller definierade namn genom [text](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) eller [index](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) i listan.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Obs: om det definierade namnet hänvisas av formler kan det inte tas bort. Vi kan endast ta bort formeln för det definierade namnet.

## **Tar bort vissa namngivna områden**
När vi tar bort ett definierat namn måste vi kontrollera om det används av alla formler i filen.
För att förbättra prestandan vid borttagning av namngivna områden kan vi ta bort några samtidigt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Ta bort dubbla definierade namn**
Vissa Excel-filer blir korrupta eftersom några definierade namn är duplicerade. Därför kan vi ta bort dessa duplicerade namn för att reparera filen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



