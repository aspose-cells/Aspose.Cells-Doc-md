---
title: Infoga en bild i en cell
linktitle: Infoga en bild i en cell
description: Aspose.Cells är ett .NET-bibliotek för arbete med kalkylarksfiler. Den här artikeln förklarar hur du anpassar en bild exakt till en enda cell, antingen genom att placera en flytande bild över cellen eller genom att bädda in bilden direkt i cellen.
keywords: Aspose.Cells, NET-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder två olika sätt att koppla en bild till en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellområde, medan en inbäddad bild lagras inuti själva cellen och automatiskt skalas efter cellens visningsyta. Välj den metod som bäst matchar dina layoutkrav.

## **Introduktion**
Att anpassa en bild exakt till en enda cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, personalkataloger, instrumentpaneler eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kanske du vill ha en ren, cellbunden bild som håller sig justerad med cellen som äger den.
Aspose.Cells stöder detta scenario på två kompletterande sätt:
- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess `Placement` till `MoveAndSize`, och justera dess fästceller (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bildbytes till cellens `EmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsyta och följer med cellen.
Resten av denna artikel går igenom båda metoderna, förklarar de relevanta API:erna och visar hur de används i kod.

## **Metod 1: Placera en bild över en cell**
En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om den inte tillhör någon enskild cell är den förankrad i ett cellområde. Bildens fästceller — dess övre vänstra och nedre högra hörn — bestämmer dess visuella omfattning på kalkylbladet. Som standard spänner en nybildad bild över flera celler.
För att få en flytande bild att täcka **exakt en cell** behöver du:
1. Lägga till bilden med `Worksheet.Pictures.Add(int row, int column, Stream stream)`, vilket förankrar den nya bilden i den givna cellen.
2. Ange de fyra fästegenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Sätta `Picture.Placement` till `PlacementType.MoveAndSize` så att bilden flyttas och ändras storlek tillsammans med den underliggande cellen när användaren ändrar kolumnbredd eller radhöjd.

### **Förankra bilden till en enskild cell**
Bildens fäste definieras av fyra nollbaserade indexegenskaper:
- `Picture.UpperLeftRow` — radindex för bildens övre kant.
- `Picture.UpperLeftColumn` — kolumnindex för bildens vänstra kant.
- `Picture.LowerRightRow` — radindex för bildens nedre kant. För att bildens nedre kant ska hamna längst ner i rad `r`, ange detta till `r + 1`.
- `Picture.LowerRightColumn` — kolumnindex för bildens högra kant. För att bildens högra kant ska hamna till höger om kolumn `c`, ange detta till `c + 1`.

{{% alert color="primary" %}}
Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Avvikelser med ett på det nedre högra fästet är den vanligaste källan till bilder som ser ut att överlappa in i en intilliggande cell.

### **Styra placeringsbeteendet**
`Picture.Placement` är en uppräkning av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellsbild är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och ändras storlek tillsammans med sin underliggande cell, vilket bevarar den exakta passformen.

### **Steg-för-steg-instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.Worksheets[0]`.
3. Öppna bildfilen från disk till en `FileStream` med ett `using`-block så att strömmen kasseras korrekt.
4. Anropa `worksheet.Pictures.Add(5, 2, stream)` för att lägga till en bild förankrad i cell C6. Fånga den returnerade `Picture`-referensen.
5. Ange de fyra fästkoordinaterna så att bilden endast täcker cell C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Sätt `picture.Placement = PlacementType.MoveAndSize` för att hålla bilden justerad med C6 när kolumnen eller raden storleksändras.
7. Lägg eventuellt till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken på disk som en `.xlsx`-fil.
Följande kod demonstrerar det kompletta tillvägagångssättet.

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
Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder: egenskapen `Cell.EmbeddedImage`. Genom att tilldela bildbytes till denna egenskap fästs bilden vid själva cellen, som om den vore inline-innehåll.

### **Hur inbäddade bilder fungerar**
- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga fästkoordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad eller användas i andra cellnivåoperationer.
Detta gör `Cell.EmbeddedImage` till det mest kortfattade alternativet när ditt mål helt enkelt är "en bild som lever inuti denna cell".

### **Steg-för-steg-instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.Worksheets[0]`.
3. Läs bildfilen från disk till en `byte[]`-array (till exempel genom att använda `File.ReadAllBytes`).
4. Hämta en referens till målcellen — antingen via `worksheet.Cells["C6"]` eller `worksheet.Cells[5, 2]`.
5. Tilldela byte-arrayen till cellens `EmbeddedImage`-egenskap.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken på disk som en `.xlsx`-fil.
Följande kod demonstrerar det kompletta tillvägagångssättet.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Hämta målcellen C6
var cell = worksheet.Cells["C6"];
// Läs bildfilen till en byte-array
byte[] imageData = File.ReadAllBytes("logo.png");
// Bädda in bilden direkt i cellen
cell.EmbeddedImage = imageData;
// Valfritt: justera radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
worksheet.Cells.SetColumnWidth(2, 30);   // Kolumn C (index 2)
worksheet.Cells.SetRowHeight(5, 100);     // Rad 6 (index 5)
// Spara den resulterande arbetsboken som en .xlsx-fil
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Välja rätt metod**
Båda metoderna ger en bild som passar inuti en enskild cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:
- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lagervisning, eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du kräver äldre kompatibilitet med kod som redan arbetar med `PictureCollection`.
  - Du behöver beräkna fästkoordinater dynamiskt baserat på kalkylbladets layout.
- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha den enklaste möjliga infogningen av en bild i en cell.
  - Bilden ska följa med cellen som annat cellinnehåll.
  - Du inte behöver manipulera bilden som en form.
{{% /alert %}}

{{% /alert %}}

## Relaterade artiklar
- [Excel-kamera i Aspose.Cells for .NET](/cells/sv/net/excel-camera/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for .NET](/cells/sv/net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for .NET](/cells/sv/net/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/net/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for .NET](/cells/sv/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}