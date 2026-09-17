---
title: Infoga en bild i en cell
linktitle: Infoga en bild i en cell
description: Aspose.Cells är ett Node.js via Java-bibliotek för arbete med kalkylbladsfiler. Den här artikeln förklarar hur man passar in en bild exakt i en enda cell, antingen genom att placera en flytande bild över cellen eller genom att bädda in bilden direkt i cellen.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/nodejs-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder två olika sätt att koppla en bild till en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och automatiskt skalas för att passa cellens visningsyta. Välj det tillvägagångssätt som bäst matchar dina layoutkrav.
{{% /alert %}}

## **Introduktion**
Att passa in en bild exakt i en enda cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, personalkataloger, dashboards eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kanske du vill ha en ren, cellbunden bild som håller sig inriktad med cellen som äger den.
Aspose.Cells stöder detta scenario på två kompletterande sätt:
- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess `Placement` till `MoveAndSize`, och justera dess ankarceller (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bildbytes till cellens `EmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsyta och följer med cellen.
Resten av den här artikeln går igenom båda metoderna, förklarar de relevanta API:erna och visar hur man använder dem i kod.

## **Metod 1: Placera en bild över en cell**
En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om det inte är en del av någon enskild cell är det förankrat till ett cellintervall. Bildens ankarceller — dess övre vänstra och nedre högra hörn — avgör dess visuella omfattning på kalkylbladet. Som standard sträcker sig en nyligen tillagd bild över flera celler.
För att få en flytande bild att täcka **exakt en cell** måste du:
1. Lägg till bilden med `worksheet.getPictures().add(int row, int column, InputStream stream)`, vilket förankrar den nya bilden till den angivna cellen.
2. Ange de fyra ankaregenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ange `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` så att bilden flyttas och storleksändras med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden till en enskild cell**
Bildens ankare definieras av fyra nollbaserade indexegenskaper:
- `picture.setUpperLeftRow(int)` — radindexet för bildens övre kant.
- `picture.setUpperLeftColumn(int)` — kolumnindexet för bildens vänstra kant.
- `picture.setLowerRightRow(int)` — radindexet för bildens nedre kant. För att få bildens nedre kant att sitta vid botten av rad `r`, ange detta till `r + 1`.
- `picture.setLowerRightColumn(int)` — kolumnindexet för bildens högra kant. För att få bildens högra kant att sitta vid höger om kolumn `c`, ange detta till `c + 1`.

{{% alert color="primary" %}}
Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel på det nedre högra ankaret är den vanligaste källan till bilder som verkar överlappa in i en intilliggande cell.

### **Styra placeringsbeteendet**
`Picture.Placement` är en enum av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellsbild är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och storleksändras tillsammans med sin underliggande cell och bevarar den exakta passningen.

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Kom åt målets `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Öppna bildfilen från disk till en `InputStream` (till exempel genom att använda `FileInputStream`) så att strömmen stängs korrekt.
4. Anropa `worksheet.getPictures().add(5, 2, stream)` för att lägga till en bild förankrad till cell C6. Fånga den returnerade `Picture`-referensen.
5. Ange de fyra ankarkoordinaterna så att bilden bara täcker cell C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Ange `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` för att hålla bilden inriktad med C6 när kolumnen eller raden storleksändras.
7. Lägg valfritt till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.
Följande kod demonstrerar det fullständiga tillvägagångssättet.

```javascript
const AsposeCells = require("aspose.cells-node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Metod 2: Bädda in en bild direkt i en cell**
Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder, egenskapen `Cell.EmbeddedImage`. Genom att tilldela bildbytes till den här egenskapen bifogas bilden till själva cellen, som om den vore inline-innehåll.

### **Hur inbäddade bilder fungerar**
- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga ankarkoordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad, eller användas i andra cellnivåoperationer.
Detta gör `Cell.EmbeddedImage` till det mest kortfattade alternativet när ditt mål helt enkelt är "en bild som lever inuti den här cellen".

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Kom åt målets `Worksheet` från `workbook.getWorksheets().get(0)`.
3. Läs bildfilen från disk till en byte-array (till exempel genom att använda `Files.readAllBytes` från `java.nio.file.Files`).
4. Få en referens till målcellen — antingen genom `worksheet.getCells().get("C6")` eller `worksheet.getCells().get(5, 2)`.
5. Tilldela byte-arrayen till cellens `EmbeddedImage`-egenskap via `cell.setEmbeddedImage(bytes)`.
6. Justera valfritt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.
Följande kod demonstrerar det fullständiga tillvägagångssättet.

```javascript
const AsposeCells = require("aspose.cells-node");
const fs = require("fs");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Hämta målcellen C6
var cell = worksheet.getCells().get("C6");
// Läs bildfilen till en byte-array
var imageData = fs.readFileSync("logo.png");
// Bädda in bilden direkt i cellen
cell.setEmbeddedImage(imageData);
// Justera valfritt radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
worksheet.getCells().setColumnWidth(2, 30);   // Kolumn C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Rad 6 (index 5)
// Spara den resulterande arbetsboken som en .xlsx-fil
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Välja rätt metod**
Båda metoderna producerar en bild som passar inuti en enda cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:
- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lagerordning eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver äldre kompatibilitet med kod som redan fungerar med `PictureCollection`.
  - Du behöver beräkna ankarkoordinater dynamiskt baserat på kalkylbladets layout.
- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha den enklaste möjliga infogningen av en bild i en cell.
  - Bilden ska följa med cellen som vilket annat cellinnehåll som helst.
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}