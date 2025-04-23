---
title: Hur man lägger till/infogar TextBox till arbetsblad med Node.js via C++
linktitle: Lägg till textfält i arbetsbladet
type: docs
weight: 10
url: /sv/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Hur man lägger till/infogar TextBox till arbetsblad i Aspose.Cells for Node.js via C++.
keywords: Lägg till/infoga Text Box TextBox arbetsblad Excel Aspose Node.js via C++
---

## Lägg till textfält i arbetsbladet i Excel

I Excel-programmet (version 07 och senare) finns två platser där du kan infoga text lådor. En i "infoga-former", den andra är på högra sidan av toppmenyn för "Infoga"-alternativet.

### metod ett:

![1](1.png)

### metod två:

![2](2.png)

## Hur man skapar

Du kan skapa textfält med horisontell eller vertikal text.

- Välj motsvarande alternativ (horisontell eller vertikal)
- Vänsterklicka på sidan
- Håll ner vänsterknappen och dra en distans på sidan
- Släpp vänsterknappen

Nu har du ett textfält.

## Lägg till Text Box till arbetsblad i Aspose.Cells for Node.js via C++

När du behöver massinlägga TextBox i kalkbladet är den manuella insättningsmetoden självklart ett katastrof. Om detta stör dig tror jag att detta dokument hjälper dig. [Aspose.Cells](https://products.aspose.com/cells/) ger dig ett API för att enkelt göra bulkinsättningar i din kod.

Följande provkod skapar en textruta.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Du kommer att få en fil som liknar [resultatfilen](result.xlsx). I filen kommer du se följande:

![](52449.png)

