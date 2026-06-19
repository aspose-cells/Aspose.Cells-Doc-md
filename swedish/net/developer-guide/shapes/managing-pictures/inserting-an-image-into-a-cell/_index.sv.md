---
title: Infoga en bild i en cell
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylbladsfiler. Den här artikeln förklarar hur man anpassar en bild exakt till en enda cellstorlek med två olika metoder: placera en flytande bild över cellen, eller bädda in bilden direkt i cellen.
keywords: Aspose.Cells, NET library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder två olika sätt att koppla en bild till en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och skalas automatiskt efter cellens visningsområde. Välj den metod som bäst matchar dina layoutkrav.

{{% /alert %}}

## **Introduktion**

Att anpassa en bild exakt till en enskild cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, medarbetarkataloger, instrumentpaneler eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad, kanske du vill ha en ren, cellbunden bild som håller sig justerad med den cell som äger den.

Aspose.Cells stöder detta scenario på två kompletterande sätt:

- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess `Placement` till `MoveAndSize`, och justera dess ankarceller (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bilddata till cellens `EmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsområde och följer med cellen.

Resten av den här artikeln går igenom båda metoderna, förklarar de relevanta API:erna och visar hur man använder dem i kod.

## **Metod 1: Placera en bild över en cell**

En flytande bild är ett `Picture`-objekt som lever på kalkylbladets ritlager. Även om den inte är en del av någon enskild cell, är den förankrad till ett cellintervall. Bildens ankarceller — dess övre vänstra och nedre högra hörn — bestämmer dess visuella omfattning på kalkylbladet. Som standard spänner en nyligen tillagd bild över flera celler.

För att få en flytande bild att täcka **exakt en cell** måste du:

1. Lägg till bilden med `Worksheet.Pictures.Add(int row, int column, Stream stream)`, vilket förankrar den nya bilden till den angivna cellen.
2. Ange de fyra ankaregenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ange `Picture.Placement` till `PlacementType.MoveAndSize` så att bilden flyttas och storleksändras med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden till en enskild cell**

Bildens ankare definieras av fyra nollbaserade indexegenskaper:

- `Picture.UpperLeftRow` — radindexet för bildens övre kant.
- `Picture.UpperLeftColumn` — kolumnindexet för bildens vänstra kant.
- `Picture.LowerRightRow` — radindexet för bildens nedre kant. För att bildens nedre kant ska ligga längst ner på rad `r`, ange detta till `r + 1`.
- `Picture.LowerRightColumn` — kolumnindexet för bildens högra kant. För att bildens högra kant ska ligga till höger om kolumn `c`, ange detta till `c + 1`.

Till exempel, för att anpassa bilden exakt till cell **C6** (radindex `5`, kolumnindex `2`), ange `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` och `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel på det nedre högra ankaret är den vanligaste källan till bilder som verkar överlappa in i en intilliggande cell.

{{% /alert %}}

### **Styra placeringsbeteende**

`Picture.Placement` är en uppräkning av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellsbild är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och storleksändras tillsammans med sin underliggande cell, vilket bevarar den exakta passformen.

### **Stegvisa instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.Worksheets[0]`.
3. Öppna bildfilen från disk till en `FileStream` med ett `using`-block så att strömmen kasseras på rätt sätt.
4. Anropa `worksheet.Pictures.Add(5, 2, stream)` för att lägga till en bild förankrad till cell C6. Spara den returnerade `Picture`-referensen.
5. Ange de fyra ankarpositionerna så att bilden bara täcker cell C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Ange `picture.Placement = PlacementType.MoveAndSize` för att hålla bilden justerad med C6 när kolumnen eller raden ändras i storlek.
7. Lägg eventuellt till exempeltext i omgivande celler för att demonstrera att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}

workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Metod 2: Bädda in en bild direkt i en cell**

Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder: egenskapen `Cell.EmbeddedImage`. Att tilldela bilddata till denna egenskap fäster bilden vid själva cellen, som om den vore inline-innehåll.

### **Hur inbäddade bilder fungerar**

- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga ankarpositioner eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad, eller användas i andra cellnivåoperationer.

Detta gör `Cell.EmbeddedImage` till det mest kortfattade alternativet när ditt mål helt enkelt är "en bild som lever inuti denna cell".

### **Stegvisa instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.Worksheets[0]`.
3. Läs bildfilen från disk till en `byte[]`-array (till exempel genom att använda `File.ReadAllBytes`).
4. Hämta en referens till målcellen — antingen via `worksheet.Cells["C6"]` eller `worksheet.Cells[5, 2]`.
5. Tilldela byte-arrayen till cellens `EmbeddedImage`-egenskap.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Hämta målcellen C6
var cell = worksheet.Cells["C6"];

// Läs bildfilen till en byte-array
byte[] imageData = File.ReadAllBytes("logo.png");

// Bädda in bilden direkt i cellen
cell.EmbeddedImage = imageData;

// Justera eventuellt radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
worksheet.Cells.SetColumnWidth(2, 30);   // Kolumn C (index 2)
worksheet.Cells.SetRowHeight(5, 100);     // Rad 6 (index 5)

// Spara den resulterande arbetsboken som en .xlsx-fil
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Välja rätt metod**

Båda metoderna producerar en bild som passar inuti en enskild cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:

- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lagerordning eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver äldre kompatibilitet med kod som redan arbetar med `PictureCollection`.
  - Du behöver beräkna ankarpositioner dynamiskt baserat på kalkylbladets layout.

- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha den enklaste möjliga infogningen av en bild i en cell.
  - Bilden ska följa med cellen som allt annat cellinnehåll.
  - Du behöver inte manipulera bilden som en form.

{{% alert color="primary" %}}

Båda metoderna kan samexistera i samma arbetsbok. Du kan placera flytande bilder över en uppsättning celler och bädda in bilder direkt i andra celler, eftersom de två mekanismerna använder olika lagringslager i filen.

{{% /alert %}}

## **Relaterade artiklar**

- [Hur man infogar bild i cell](/cells/sv/net/how-to-place-image-to-cell/)
- [Hur man anpassar bild till cellbredd och -höjd](/cells/sv/net/how-to-fit-image-to-cell-width-height/)
- [Lägg till bildhyperlänkar](/cells/sv/net/add-image-hyperlinks/)
- [Ladda en webbild från en URL till ett Excel-kalkylblad](/cells/sv/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipulera position, storlek och designdiagram](/cells/sv/net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="csharp" >}}