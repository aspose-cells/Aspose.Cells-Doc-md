---
title: Infoga bakgrundsbild i Excel med Node.js via C++
linktitle: Infoga bakgrundsbild i Excel
type: docs
weight: 90
url: /sv/nodejs-cpp/insert-background-image-to-excel/
description: "Hur man infogar bakgrundsbild i Excel med Aspose.Cells for Node.js via C++."
---

{{% alert color="primary" %}} 

Du kan göra ett kalkylblad mer lockande genom att lägga till en bild som bakgrund. Denna funktion kan vara ganska effektiv om du har en speciell företagsgrafik som lägger till en antydan till bakgrunden utan att dölja data på bladet. Du kan ange bakgrundsbild för ett blad med Aspose.Cells API.

{{% /alert %}} 

## **Ange bakgrund på kalkylblad i Microsoft Excel**

För att ange ett kalkylblads bakgrundsbild i Microsoft Excel (t.ex. Microsoft Excel 2019):

1. Från menyn **Sidlayout**, hitta alternativet **Sidlayout** och klicka sedan på alternativet **Bakgrund**.
1. Välj en bild för att sätta kalkylbladets bakgrundsbild.

   **Ange en ark-bakgrund**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Ställa in bladbakgrund med Aspose.Cells for Node.js via C++**

Koden nedan ställer in en bakgrundsbild med en bild från en ström.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## Relaterade artiklar

- [Arbeta med bakgrund i ODS-filer](/cells/sv/nodejs-cpp/working-with-background-in-ods-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
