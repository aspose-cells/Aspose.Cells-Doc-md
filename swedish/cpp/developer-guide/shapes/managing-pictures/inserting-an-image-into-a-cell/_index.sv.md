---
title: Infoga en bild i en cell
linktitle: Infoga en bild i en cell
description: Aspose.Cells är ett C++-bibliotek för att arbeta med kalkylarksfiler. Den här artikeln förklarar hur man anpassar en bild exakt till en enskild cell, antingen genom att placera en flytande bild över cellen eller genom att bädda in bilden direkt i cellen.
keywords: Aspose.Cells, C++-bibliotek, kalkylark, infoga bild, bädda in bild, bild i cell, anpassa bild till cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /sv/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells erbjuder två olika sätt att koppla en bild till en enskild cell. En flytande bild är en form på kalkylbladets ritlager som visuellt överlagrar ett cellintervall, medan en inbäddad bild lagras inuti själva cellen och skalas automatiskt efter cellens visningsyta. Välj det tillvägagångssätt som bäst matchar dina layoutkrav.

## **Introduktion**
Att anpassa en bild exakt till en enskild cell är ett vanligt krav när man utformar kalkylblad som fungerar som visuella rapporter, produktkataloger, medarbetarkataloger, dashboards eller inventarielistor. Istället för att sträcka ut en bild över många celler eller placera den löst på ett kalkylblad kanske du vill ha en ren, cellbunden bild som håller sig justerad med den cell som äger den.
Aspose.Cells stödjer detta scenario på två kompletterande sätt:
- **Tillvägagångssätt 1 — Placera en flytande bild över en cell.** Lägg till en `Picture` i kalkylbladet, ange dess `Placement` till `MoveAndSize`, och justera dess ankarceller (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) så att bilden täcker exakt en cell.
- **Tillvägagångssätt 2 — Bädda in en bild direkt i en cell.** Tilldela bildbytes till cellens `EmbeddedImage`-egenskap. Bilden skalas automatiskt för att passa cellens visningsyta och följer med cellen.
Resten av denna artikel går igenom båda tillvägagångssätten, förklarar de relevanta API:erna och visar hur man använder dem i kod.

## **Tillvägagångssätt 1: Placera en bild över en cell**
En flytande bild är ett `Picture`-objekt som lever på kalkylbladets ritlager. Även om den inte tillhör någon enskild cell är den förankrad vid ett cellintervall. Bildens ankarceller — dess övre vänstra och nedre högra hörn — avgör dess visuella omfattning på kalkylbladet. Som standard spänner en nyligen tillagd bild över flera celler.
För att få en flytande bild att täcka **exakt en cell** behöver du:
1. Lägg till bilden med `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)`, vilket förankrar den nya bilden vid den givna cellen.
2. Ange de fyra ankaregenskapsvärdena så att bildens begränsningsrektangel sammanfaller med målcellen.
3. Ange `Picture.Placement` till `PlacementType.MoveAndSize` så att bilden flyttas och storleksändras tillsammans med den underliggande cellen när användaren ändrar kolumnbredden eller radhöjden.

### **Förankra bilden vid en enskild cell**
Bildens ankare definieras av fyra nollbaserade indexegenskaper:
- `Picture.UpperLeftRow` — radindex för bildens övre kant.
- `Picture.UpperLeftColumn` — kolumnindex för bildens vänstra kant.
- `Picture.LowerRightRow` — radindex för bildens nedre kant. För att bildens nedre kant ska hamna längst ned i rad `r` anger du detta till `r + 1`.
- `Picture.LowerRightColumn` — kolumnindex för bildens högra kant. För att bildens högra kant ska hamna till höger om kolumn `c` anger du detta till `c + 1`.

{{% alert color="primary" %}}
Rad- och kolumnindex i Aspose.Cells är **nollbaserade**. Cell C6 har radindex 5 och kolumnindex 2. Off-by-one-fel på det nedre högra ankaret är den vanligaste källan till bilder som ser ut att överlappa in i en intilliggande cell.

### **Styra placeringsbeteende**
`Picture.Placement` är en uppräkning av typen `PlacementType` som styr hur bilden beter sig när användaren ändrar storlek på raden eller kolumnen under den. Det rekommenderade värdet för en encellsbild är `PlacementType.MoveAndSize`, vilket gör att bilden flyttas och storleksändras tillsammans med sin underliggande cell, vilket bevarar den exakta passformen.

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.GetWorksheets().Get(0]`.
3. Läs bildfilen från disk till en `Vector<uint8_t>`-bytebuffert så att bildbytesna är tillgängliga för API:et.
4. Anropa `worksheet.Pictures.Add(5, 2, imageData)` för att lägga till en bild förankrad vid cell C6. Fånga den returnerade `Picture`-referensen.
5. Ange de fyra ankarkoordinaterna så att bilden endast täcker cell C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Ange `picture.Placement = PlacementType.MoveAndSize` för att hålla bilden justerad med C6 när kolumnen eller raden storleksändras.
7. Lägg eventuellt till exempeltext i omgivande celler för att visa att endast cell C6 innehåller bilden.
8. Spara arbetsboken till disk som en `.xlsx`-fil.
Följande kod demonstrerar hela tillvägagångssättet.

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

## **Tillvägagångssätt 2: Bädda in en bild direkt i en cell**
Aspose.Cells erbjuder också en enklare mekanism för cellbundna bilder: egenskapen `Cell.EmbeddedImage`. Genom att tilldela bildbytes till denna egenskap bifogas bilden till själva cellen, som om den vore inline-innehåll.

### **Hur inbäddade bilder fungerar**
- Bilden lagras som en del av cellinnehållet snarare än som en form på ritlagret.
- Bilden skalas automatiskt för att passa inuti cellens renderade gränser. Inga ankarkoordinater eller placeringsinställningar krävs.
- Cellen förblir en riktig cell med en riktig adress som kan refereras av formler, sorteras som en del av en rad eller användas i andra cellnivåoperationer.
Detta gör `Cell.EmbeddedImage` till det mest koncisa alternativet när ditt mål helt enkelt är "en bild som lever inuti denna cell".

### **Stegvisa instruktioner**
1. Skapa en ny `Workbook` (eller öppna en befintlig).
2. Hämta målets `Worksheet` från `workbook.GetWorksheets().Get(0]`.
3. Läs bildfilen från disk till en `Vector<uint8_t>`-bytearray.
4. Hämta en referens till målcellen — antingen via `worksheet.GetCells().Get("C6"]` eller `worksheet.GetCells().Get(5, 2]`.
5. Tilldela bytearrayen till cellens `EmbeddedImage`-egenskap.
6. Justera eventuellt radhöjden och kolumnbredden för målraden och målkolumnen för att ge den inbäddade bilden ett mer framträdande utseende.
7. Spara arbetsboken till disk som en `.xlsx`-fil.
Följande kod demonstrerar hela tillvägagångssättet.

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
    // Konvertera std::vector till Aspose::Cells::Vector med pekar- och storlekskonstruktor
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());
    // Bädda in bilden direkt i cellen
    cell.SetEmbeddedImage(imageData);
    // Valfritt: justera radhöjd och kolumnbredd så att den inbäddade bilden syns bättre
    worksheet.GetCells().SetColumnWidth(2, 30);   // Kolumn C (index 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Rad 6 (index 5)
    // Spara den resulterande arbetsboken som en .xlsx-fil
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Välja rätt tillvägagångssätt**
Båda tillvägagångssätten producerar en bild som passar inuti en enskild cell, men de skiljer sig åt i hur bilden lagras och hur den beter sig:
- **Använd en flytande bild (Tillvägagångssätt 1) när:**
  - Du behöver finare kontroll över placering, lagervisning eller justering med andra ritobjekt.
  - Du vill att bilden ska bete sig som en form som kan markeras, omordnas eller grupperas med andra former.
  - Du kräver äldre kompatibilitet med kod som redan arbetar med `PictureCollection`.
  - Du behöver beräkna ankarkoordinater dynamiskt baserat på kalkylbladets layout.
- **Använd en inbäddad bild (Tillvägagångssätt 2) när:**
  - Du vill ha den enklaste möjliga infogningen av en bild i en cell.
  - Bilden ska följa med cellen som annat cellinnehåll.
  - Du inte behöver manipulera bilden som en form.
{{% /alert %}}

{{% /alert %}}

## Relaterade artiklar
- [Excel-kamera i Aspose.Cells for C++](/cells/sv/cpp/excel-camera/)
- [Lägg till filterfält i en pivottabell i Aspose.Cells for C++](/cells/sv/cpp/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for C++](/cells/sv/cpp/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/cpp/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for C++](/cells/sv/cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="cpp" >}}