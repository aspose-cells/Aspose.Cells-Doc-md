---
title: Infoga en bild i en cell
description: Aspose.Cells är ett C++-bibliotek för att arbeta med kalkylarksfiler. Den här artikeln förklarar hur man anpassar en bild exakt till en enskild cells storlek med hjälp av två olika metoder, placera en flytande bild över cellen, eller bädda in bilden direkt i cellen.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder två olika sätt att associera en bild med en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och skalas automatiskt till cellens visningsområde. Välj den metod som bäst motsvarar dina layoutkrav.

{{% /alert %}}

## **Introduktion**

Att anpassa en bild exakt till en enskild cell är ett vanligt krav vid utformning av kalkylblad som fungerar som visuella rapporter, produktkataloger, medarbetarkataloger, instrumentpaneler eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kanske du vill ha en ren, cellbunden bild som håller sig justerad med cellen som äger den.

Aspose.Cells stöder det här scenariot på två kompletterande sätt:

- **Metod 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess `Placement` till `MoveAndSize`, och justera dess förankringsceller (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) så att bilden täcker exakt en cell.
- **Metod 2 — Bädda in en bild direkt i en cell.** Tilldela bildbytes till cellens `EmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsområde och följer med cellen.

Resten av den här artikeln går igenom båda metoderna, förklarar relevanta API:er och visar hur man använder dem i kod.

## **Metod 1: Placera en bild över en cell**

En flytande bild är ett `Picture`-objekt som finns på kalkylbladets ritlager. Även om det inte tillhör någon enskild cell, är det förankrat till ett cellintervall. Bildens förankringsceller — dess övre vänstra och nedre högra hörn — bestämmer dess visuella omfattning på kalkylbladet. Som standard spänner en nyligen tillagd bild över flera celler.

För att få en flytande bild att täcka **exakt en cell** behöver du:

1. Lägg till bilden med `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, vilket förankrar den nya bilden till den givna cellen.
2. Ange de fyra förankringsegenskaperna så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ange `Picture.Placement` till `PlacementType.MoveAndSize` så att bilden flyttas och storleksändras tillsammans med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden till en enskild cell**

Bildens förankring definieras av fyra nollbaserade indexegenskaper:

- `Picture.UpperLeftRow` — radindex för bildens övre kant.
- `Picture.UpperLeftColumn` — kolumnindex för bildens vänstra kant.
- `Picture.LowerRightRow` — radindex för bildens nedre kant. För att bildens nedre kant ska ligga längst ner på rad `r`, ange detta till `r + 1`.
- `Picture.LowerRightColumn` — kolumnindex för bildens högra kant. För att bildens högra kant ska ligga till höger om kolumn `c`, ange detta till `c + 1`.

Till exempel, för att anpassa bilden exakt i cell **C6** (radindex `5`, kolumnindex `2`), ange `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` och `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel i den nedre högra förankringen är den vanligaste källan till bilder som verkar överlappa in i en intilliggande cell.

{{% /alert %}}

### **Styra placeringsbeteendet**

`Picture.Placement` är en enum av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellsbild är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och storleksändras tillsammans med sin underliggande cell, vilket bevarar den exakta passformen.

### **Steg-för-steg-instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.Worksheets[0]`.
3. Läs bildfilen från disk till en `Vector<uint8_t>`-bytebuffert så att bildbyten är tillgängliga för API:et.
4. Anropa `worksheet.Pictures.Add(5, 2, imageData)` för att lägga till en bild förankrad till cell C6. Fånga den returnerade `Picture`-referensen.
5. Ange de fyra förankringskoordinaterna så att bilden endast täcker cell C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Ange `picture.Placement = PlacementType.MoveAndSize` för att hålla bilden justerad med C6 när kolumnen eller raden ändras.
7. Lägg eventuellt till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();

    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));

    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);

    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Metod 2: Bädda in en bild direkt i en cell**

Aspose.Cells exponerar också en enklare mekanism för cellbundna bilder: egenskapen `Cell.EmbeddedImage`. Genom att tilldela bildbytes till den här egenskapen bifogas bilden till själva cellen, som om den vore inline-innehåll.

### **Så här fungerar inbäddade bilder**

- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga förankringskoordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad eller användas i andra cellnivåoperationer.

Detta gör `Cell.EmbeddedImage` till det mest koncisa alternativet när ditt mål helt enkelt är "en bild som lever inuti den här cellen".

### **Steg-för-steg-instruktioner**

1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.Worksheets[0]`.
3. Läs bildfilen från disk till en `Vector<uint8_t>`-bytearray.
4. Hämta en referens till målcellen — antingen via `worksheet.Cells["C6"]` eller `worksheet.Cells[5, 2]`.
5. Tilldela bytearrayen till cellens `EmbeddedImage`-egenskap.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.

Följande kod demonstrerar hela metoden.

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(u"C6");

    // Läs bildfilen till en byte-array
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // Konvertera std::vector till Aspose::Cells::Vector med pekare+storlek-konstruktorn
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // Bädda in bilden direkt i cellen
    cell.SetEmbeddedImage(imageData);

    // Justera valfritt radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
    worksheet.GetCells().SetColumnWidth(2, 30);   // Kolumn C (index 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Rad 6 (index 5)

    // Spara den resulterande arbetsboken som en .xlsx-fil
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Välja rätt metod**

Båda metoderna producerar en bild som passar inuti en enskild cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:

- **Använd en flytande bild (Metod 1) när:**
  - Du behöver finare kontroll över placering, lagerordning eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan väljas, omordnas eller grupperas med andra former.
  - Du behöver äldre kompatibilitet med kod som redan fungerar med `PictureCollection`.
  - Du behöver beräkna förankringskoordinater dynamiskt baserat på kalkylbladets layout.

- **Använd en inbäddad bild (Metod 2) när:**
  - Du vill ha den enklaste möjliga infogningen av en bild i en cell.
  - Bilden ska följa med cellen som allt annat cellinnehåll.
  - Du inte behöver manipulera bilden som en form.

{{% alert color="primary" %}}

Båda metoderna kan samexistera i samma arbetsbok. Du kan placera flytande bilder över en uppsättning celler och bädda in bilder direkt i andra celler, eftersom de två mekanismerna använder olika lagringslager i filen.

{{% /alert %}}

## **Relaterade artiklar**

- [Hur man infogar bild i cell](/cells/sv/cpp/how-to-place-image-to-cell/)
- [Lägg till bildhyperlänkar](/cells/sv/cpp/add-image-hyperlinks/)
- [Ladda en webbbild från en URL till ett Excel-kalkylblad](/cells/sv/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipulera position, storlek och designdiagram](/cells/sv/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}