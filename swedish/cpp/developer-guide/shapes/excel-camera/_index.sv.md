---
title: Excel Camera i Aspose.Cells for C++
linktitle: Excel Camera i Aspose.Cells for C++
description: Lär dig hur du använder Excel Camera i Aspose.Cells for C++ för att skapa en dynamisk bild kopplad till ett cellintervall som uppdateras med källdatan och bevarar all källformatering.
keywords: Aspose.Cells, C++, Excel Camera, dynamisk bild, länkad bild, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /sv/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera är ett kalkylbladsobjekt som renderar en levande bild av ett cellintervall och flyter på ritlagret som en vanlig bild. Aspose.Cells stöder två skapandelägen, en dynamisk bild som uppdateras automatiskt när källdatan ändras och en statisk bild som tar en engångssnapshot av ett intervall. Den här artikeln går igenom båda metoderna så att du kan välja den som passar din layout.

## **Vad är Excel Camera?**
Excel Camera är i princip ett bildobjekt förankrat vid en specifik rad och kolumn på kalkylbladets ritlager. Till skillnad från en vanlig infogad bild är kameran kopplad till ett källintervall via en A1-formel som t.ex. `"A1:F10"`. Närhelst en cell inom det intervallet ändras, uppdateras kamerans bild automatiskt för att återspegla det nya innehållet. Kameran bevarar all formatering av källområdet — kanter, bakgrundsfärger, typsnitt och talformat — så allt som är synligt i cellerna visas också i kamerans bild. Detta gör kameran särskilt användbar för dashboards, sammanfattningar, sidopaneler och rapportlayouter där du vill ha en synlig förhandsvisning av ett avlägset område utan att behöva scrolla eller upprepa data. Två varningar gäller: du måste anropa `UpdateSelectedValue()` innan du sparar arbetsboken, och filen kommer att exporteras till HTML eller PDF, eftersom dessa format förlitar sig på inbäddade bilddata snarare än en live-omräkning.

## **Metod 1 — Lägg till en dynamisk kamerabild**
Den dynamiska kameran är den vanligaste metoden och ligger närmast Excels inbyggda kameraverktyg. Den fungerar genom att lägga till en bild utan initialt bildinnehåll och sedan tilldela den en `Formula` som refererar till källintervallet. När formeln har tilldelats, uppdaterar ett anrop till `UpdateSelectedValue()` den inbäddade bilddatan så att den är synkroniserad med cellerna den speglar. Kameran implementeras inte genom en dedikerad klass — den byggs helt på den vanliga `Picture`-typen.
De viktigaste API:erna är:
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — lägger till en bild förankrad vid given rad och kolumn. Om du skickar en tom `Vector<uint8_t>()` skapas en tom bild som fungerar som platshållare för en dynamisk kamera. Metoden returnerar indexet för den nya bilden.
- `worksheet.GetPictures().Get(int index)` — hämtar en specifik `Picture` från samlingen efter index.
- `Picture.SetFormula(U16String value)` — anger A1-referensen till det källintervall som kameran speglar, till exempel `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` — uppdaterar den inbäddade bilddatan från cellerna som refereras av `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` MÅSTE anropas innan du sparar när utdata är HTML eller PDF; annars kommer den exporterade filen inte att innehålla bilddata och kameran visas tom i den renderade utdata.
{{% /alert %}}

Följande kod skapar en arbetsbok, lägger till en tom bild förankrad vid rad 10 kolumn 6, kopplar den till källintervallet `A1:F10` via egenskapen `Formula`, uppdaterar den inbäddade bilddatan och sparar arbetsboken.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Dynamisk kamera: lägg till en tom bild, länka den via formel till A1:F10, uppdatera sedan
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Metod 2 — Lägg till en statisk kamerabild**
Den statiska kameran är i princip en engångsrenderad förhandsvisning av ett cellintervall. Istället för att upprätthålla en live-länk renderar du intervallet till en `Vector<uint8_t>`-bytebuffert en gång och skickar den bufferten direkt till `Pictures.Add(row, col, data)`. Bildinnehållet är då fast vid skapandetillfället och uppdateras inte automatiskt när källceller ändras.
De viktigaste API:erna är:
- `Cells.CreateRange(U16String address)` — bygger ett `Range`-objekt från en A1-adress som t.ex. `U16String("A1:F10")`.
- `Range.ToImage(ImageOrPrintOptions options)` — renderar intervallet till en `Vector<uint8_t>`-bytebuffert. Om du skickar `nullptr` används standardrenderingsalternativ; överlagringar finns för finare kontroll över utdata.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — lägger till bilden förankrad vid given rad och kolumn, denna gång genom att skicka bytebufferten som produceras av `Range.ToImage`.
Följande kod skapar en arbetsbok, bygger ett `Range` för `A1:F10`, renderar det till bildbytes via `Range.ToImage(nullptr)`, lägger till bilden förankrad vid rad 10 kolumn 6 och sparar arbetsboken.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Statisk kamera: bygg Range, rendera till bytes, lägg till som bild
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Välja mellan dynamisk och statisk**
- **Dynamisk kamera:** uppdateras vid varje omräkning, stöder HTML- och PDF-export efter `UpdateSelectedValue()`, och bevarar live-länkbeteendet under filens livstid.
- **Statisk kamera:** en engångsrendering som aldrig uppdateras, användbar när du vill ha en fast visuell snapshot inbäddad vid byggtiden snarare än en live-spegling av datan.
Aspose.Cells stöder både en dynamisk, automatisk uppdaterande kamera byggd på `Picture.Formula` plus `UpdateSelectedValue()` och en statisk engångskamera byggd på `Range.ToImage` plus `Vector<uint8_t>`. Välj den dynamiska metoden när din utdata behöver hålla sig synkroniserad med källcellerna, och välj den statiska metoden när du bara behöver en fast visuell snapshot vid byggtiden.

{{< app/cells/assistant language="cpp" >}}