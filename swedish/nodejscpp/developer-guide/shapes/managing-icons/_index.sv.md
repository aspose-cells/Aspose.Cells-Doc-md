---  
title: Lägg till ikoner i kalkblad med Node.js via C++  
linktitle: Hantera ikoner  
type: docs  
weight: 100  
url: /sv/nodejs-cpp/insert-svg-to-excel/  
---  

## Lägg till ikoner i kalkblad i Aspose.Cells for Node.js via C++

Om du behöver använda [Aspose.Cells](https://products.aspose.com/cells/) för att lägga till 'ikoner' i en Excelfil, kan detta dokument ge dig hjälp.

Gränssnittet för Excel som motsvarar infogning av ikoner är följande:

![](1.png)

- Välj positionen för ikonen som ska infogas i arbetsboken
- Vänsterklicka på *Infoga*->*Ikoner*
- I fönstret som öppnas väljer du ikonen i rutan med röd ram i figuren ovan
- Vänsterklicka *Infoga*, den kommer att infogas i Excel-filen.

Effekten är följande:

![](2.png)

Här har vi förberett *exempelkod* för att hjälpa dig att infoga ikoner med [Aspose.Cells](https://products.aspose.com/cells/). Det finns också en nödvändig [exempelfil](sample.xlsx) och en ikon [resursfil](icon.zip). Vi använde Excel-gränssnittet för att infoga en ikon med samma visningseffekt som [resursfilen](icon.zip) i [exempelfilen](sample.xlsx).

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

När du utför ovanstående kod i ditt projekt kommer du att få följande resultat:

![](3.png)  

{{< app/cells/assistant language="nodejs-cpp" >}}
