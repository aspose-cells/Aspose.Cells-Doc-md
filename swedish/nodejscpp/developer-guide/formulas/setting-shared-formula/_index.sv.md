---
title: Ställa in delad formel med Node.js via C++
linktitle: Ange Delad Formel
type: docs
weight: 10
url: /sv/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Om du vill lägga till en funktion i ett kalkylblad som ska göra vissa beräkningar förklarar den här artikeln hur du gör detta med Aspose.Cells for Node.js via C++.

{{% /alert %}}

## Ställa in delad formel med Aspose.Cells for Node.js via C++

Anta att du har ett kalkylblad fyllt med data i det format som liknar det följande exempelkalkylbladet.

|**Inmatningsfil med en kolumn data**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Du vill lägga till en funktion i B2 som kommer att beräkna momsen för den första dataraden. Skatten är **9%**. Formeln som beräknar momsen är: **"=A2*0.09"**. Den här artikeln förklarar hur man tillämpar denna formel med Aspose.Cells.

Aspose.Cells låter dig ange en formel med hjälp av [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) egenskap. Det finns två alternativ för att lägga till formler till de andra cellerna (B3, B4, B5, etc.) i kolumnen.

 Antingen gör du vad du gjorde för den första cellen, effektivt ställer in formeln för varje cell, och uppdaterar cellreferensen därefter (A3*0,09, A4*0,09, A5*0,09 och så vidare). Detta kräver att cellreferenserna för varje rad uppdateras. Det kräver också att Aspose.Cells analyserar varje formel individuellt, vilket kan ta tid för stora kalkylblad och komplexa formler. Det lägger också till extra kodrader även om loopar kan minska detta något.

Ett annat tillvägagångssätt är att använda en **delad formel**. Med en delad formel uppdateras formlerna automatiskt för cellreferenser i varje rad så att momsen beräknas korrekt. [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) metoden är mer effektiv än det första tillvägagångssättet.

Följande exempel visar hur du använder den.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
