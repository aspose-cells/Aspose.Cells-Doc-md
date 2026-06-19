---
title: Infoga en bild i en cell
description: Aspose.Cells är ett Node.js via C++-bibliotek för att arbeta med kalkylbladsfiler. Denna artikel förklarar hur man anpassar en bild exakt till en enda cellstorlek med två olika metoder: att placera en flytande bild över cellen, eller att bädda in bilden direkt i cellen.
keywords: Aspose.Cells, Node.js via C++-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/nodejs-cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder två olika sätt att associera en bild med en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och automatiskt skalas för att passa cellens visningsyta. Välj den metod som bäst passar dina layoutkrav.

{{% /alert %}}

## **Introduktion**

Att anpassa en bild exakt till en enda cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, medarbetarkataloger, instrumentpaneler eller inventeringslistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kanske du vill ha en ren, cellbunden bild som håller sig justerad med den cell som äger den.

Aspose.Cells stöder detta scenario på två kompletterande sätt:

- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess `placement` till `MoveAndSize`, och justera dess förankringsceller (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bilddata till cellens `embeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsyta och följer med cellen.

Resten av denna artikel går igenom båda metoderna, förklarar de relevanta API:erna och visar hur de används i kod.

## **Metod 1: Placera en bild över en cell**

En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om den inte är en del av någon enskild cell, är den förankrad till ett cellintervall. Bildens förankringsceller — dess övre vänstra och nedre högra hörn — bestämmer dess visuella utsträckning på kalkylbladet. Som standard spänner en nyligen tillagd bild över flera celler.

För att få en flytande bild att täcka **exakt en cell** måste du:

1. Lägga till bilden med `worksheet.pictures.add(row, column, stream)`, vilket förankrar den nya bilden till den givna cellen.
2. Ange de fyra förankringsegenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ange `picture.placement` till `PlacementType.MoveAndSize` så att bilden flyttas och storleksändras tillsammans med den underliggande cellen när användaren ändrar kolumnbredd eller radhöjd.

### **Förankra bilden till en enskild cell**

Bildens förankring definieras av fyra nollbaserade indexegenskaper:

- `picture.upperLeftRow` — radindex för bildens övre kant.
- `picture.upperLeftColumn` — kolumnindex för bildens vänstra kant.
- `picture.lowerRightRow` — radindex för bildens nedre kant. För att bildens nedre kant ska hamna längst ner på rad `r`, ange detta till `r + 1`.
- `picture.lowerRightColumn` — kolumnindex för bildens högra kant. För att bildens högra kant ska hamna till höger om kolumn `c`, ange detta till `c + 1`.

Till exempel, för att anpassa bilden exakt till cell **C6** (radindex `5`, kolumnindex `2`), ange `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6` och `lowerRightColumn = 3`.

{{% alert color="primary" %}}

Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel på den nedre högra förankringen är den vanligaste källan till att bilder verkar överlappa in i en intilliggande cell.

{{% /alert %}}

### **Styra placeringsbeteendet**

`picture.placement` är en enum av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellbild är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och storleksändras tillsammans med sin underliggande cell, vilket bevarar den exakta passformen.

### **Steg-för-steg-instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.worksheets[0]`.
3. Öppna bildfilen från disk till en ström, och se till att strömmen stängs korrekt efter användning.
4. Anropa `worksheet.pictures.add(5, 2, stream)` för att lägga till en bild förankrad till cell C6. Fånga den returnerade `Picture`-referensen.
5. Ange de fyra förankringskoordinaterna så att bilden endast täcker cell C6: `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Ange `picture.placement = PlacementType.MoveAndSize` för att hålla bilden justerad med C6 när kolumnen eller raden storleksändras.
7. Valfritt kan du lägga till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Metod 2: Bädda in en bild direkt i en cell**

Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder: egenskapen `cell.embeddedImage`. Att tilldela bilddata till denna egenskap fäster bilden till själva cellen, som om den vore inline-innehåll.

### **Hur inbäddade bilder fungerar**

- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga förankringskoordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad, eller användas i andra cellnivåoperationer.

Detta gör `cell.embeddedImage` till det mest koncisa alternativet när ditt mål helt enkelt är "en bild som lever inuti denna cell".

### **Steg-för-steg-instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.worksheets[0]`.
3. Läs bildfilen från disk till en Buffer eller byte-array med Node.js filsystems-API:er (till exempel, `fs.readFileSync`).
4. Hämta en referens till målcellen — antingen via `worksheet.cells["C6"]` eller `worksheet.cells[5, 2]`.
5. Tilldela byte-arrayen till cellens `embeddedImage`-egenskap.
6. Valfritt kan du justera radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```javascript
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

Båda metoderna producerar en bild som passar inuti en enskild cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:

- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lagervisning eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver äldre kompatibilitet med kod som redan arbetar med bildsamlingen.
  - Du behöver beräkna förankringskoordinater dynamiskt baserat på kalkylbladets layout.

- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha det enklaste möjliga infogandet av en bild i en cell.
  - Bilden ska följa med cellen som vilket annat cellinnehåll som helst.
  - Du inte behöver manipulera bilden som en form.

{{% alert color="primary" %}}

Båda metoderna kan samexistera i samma arbetsbok. Du kan placera flytande bilder över en uppsättning celler och bädda in bilder direkt i andra celler, eftersom de två mekanismerna använder olika lagringslager i filen.

{{% /alert %}}

## **Relaterade artiklar**

- [Hur man infogar bild i cell](/cells/sv/nodejs-cpp/how-to-place-image-to-cell/)
- [Lägg till bildhyperlänkar](/cells/sv/nodejs-cpp/add-image-hyperlinks/)
- [Ladda en webbbild från en URL till ett Excel-kalkylblad](/cells/sv/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipulera position, storlek och designdiagram](/cells/sv/nodejs-cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="javascript" >}}