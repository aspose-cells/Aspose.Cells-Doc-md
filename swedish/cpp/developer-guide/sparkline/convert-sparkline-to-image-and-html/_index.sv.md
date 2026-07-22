---
title: Konvertera sparkline till bild och HTML i Aspose.Cells for C++
linktitle: Convert Sparkline to Image and HTML
description: Lär dig hur du renderar Aspose.Cells-sparklines till fristående bilder för inbäddning i celler och exporterar sparkline-rika kalkylblad till HTML med HtmlSaveOptions.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är miniatyrdiagram placerade inne i kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparkline-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `Cell.EmbeddedImage` som används i den här artikeln är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**

Sparklines är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Medan Excel-användare ser dem på plats kräver många verkliga scenarier att en sparkline lämnar cellen – till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande eller renderas som en del av en HTML-rapport som publiceras på webben.

Aspose.Cells stödjer båda dessa operationer. Metoden `Sparkline.ToImage` renderar en enskild sparkline till en ström, och de resulterande bytena kan tilldelas till `Cell.EmbeddedImage` så att bilden lagras i en enskild cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken – inklusive sparklines – till en självständig HTML-fil. Den här artikeln går igenom båda arbetsflödena steg för steg.

## **Arbetsflöde 1 – Rendera sparklines till bilder och bädda in dem i celler**

I det här arbetsflödet kommer du att bygga ett kalkylblad som innehåller ett litet intervall av källvärden, koppla tre olika sparkline-grupper (linje, kolumn och staplade/vinst-förlust) till det intervallet, rendera varje grupp som en PNG, och skriva dessa PNG-byten i intilliggande celler som inbäddade bilder. Det slutliga resultatet är en enda `.xlsx`-fil som innehåller både de levande sparklines och deras renderade bildmotsvarigheter.

### **Steg-för-steg-instruktioner**

1. Definiera en arbetskatalog och se till att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturavläsningar).
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.SparklineGroups.Add(...)`:
   - En `SparklineType.Line`-grupp förankrad vid `F1`, med dataområde `A1:E1`.
   - En `SparklineType.Column`-grupp förankrad vid `G1`, med dataområde `A1:E1`.
   - En `SparklineType.Stacked` (vinst/förlust)-grupp förankrad vid `H1`, med dataområde `A1:E1`.
5. Bygg en `ImageOrPrintOptions`-instans och ställ in dess `ImageType` till `ImageType.Png` så att varje sparkline renderas som en transparent PNG.
6. För var och en av de tre grupperna, rendera dess enskilda sparkline med `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, konvertera `MemoryStream` till en `Vector<uint8_t>`, och tilldela arrayen till `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` respektive `worksheet.Cells["H2"].EmbeddedImage`.
7. Spara arbetsboken som `output_with_sparklines.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);

    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);

    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);

    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);

    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);

    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);

    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);

    workbook.Save(u"output_with_sparklines.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

Koden ovan producerar en arbetsbok där varje visuell representation av en sparkline dupliceras i två former: den levande, nativa sparkline förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna finns i själva filen förblir arbetsboken ett enda självständigt objekt som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparkline-grupp som en PNG, konvertera `MemoryStream` till en `Vector<uint8_t>`, och tilldela arrayen till egenskapen `EmbeddedImage` för målcellen – det är tilldelningen som gör bilden till en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparkline-grupp är förankrad till en enskild cell kan du adressera den via indexeraren `group.Sparklines[0]` istället för att räkna upp med `foreach`. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparkline per förankringscell". Att lagra bildbyten via `Cell.EmbeddedImage` kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 – Exportera sparkline-kalkylbladet till HTML**

När arbetsboken innehåller levande sparklines (och valfritt inbäddade bildmotsvarigheter), kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i detta arbetsflöde kommer du att återanvända filen `output_with_sparklines.xlsx` som producerades av arbetsflöde 1 och konvertera den till ett rent HTML-dokument med en sida.

### **Steg-för-steg-instruktioner**

1. Se till att filen `output_with_sparklines.xlsx` som producerades av arbetsflöde 1 är tillgänglig på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och ställ in dess egenskap `ExportActiveWorksheetOnly` till `true` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet snarare än hela arbetsboken.
4. Anropa `workbook.Save("sparklines.html", htmlOptions)` för att skriva HTML-utdata till disk.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Koden ovan tar den sparkline-rika arbetsboken från arbetsflöde 1 och förvandlar den till en portabel HTML-fil. Sparklines bevaras som inline SVG- eller PNG-renderingar i den genererade HTML:en, beroende på exportläge, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att behöva ha Excel installerat. Genom att ställa in `ExportActiveWorksheetOnly` till `true` undviker du att oavsiktligt publicera dolda blad eller hjälpdata – endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för finjustering av utdata, såsom `ExportHiddenWorksheet`, `ExportImagesAsBase64` och `Encoding`. Justera dessa efter behov för ditt distributionsmål.
{{% /alert %}}

## **API-sammanfattning**

Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells-API:er som arbetar tillsammans.

- `SparklineGroup` och samlingsaccessorn `worksheet.SparklineGroups` används för att deklarera typen (linje, kolumn, staplade), dataområdet och förankringscellen för varje sparkline-grupp. I den här artikeln är varje grupp förankrad till en enskild cell, så gruppen nås via `worksheet.SparklineGroups[i]`.
- `Sparkline` och indexeraren `group.Sparklines[0]` returnerar den enskilda sparkline inom en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen `foreach`-loop.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparkline till en angiven `Stream`. Metoden returnerar `void`; du läser byten från strömmen efter anropet.
- `Cell.EmbeddedImage` är en `Vector<uint8_t>`-egenskap som lagrar en bild i en enskild cell. Den är tillgänglig i **Aspose.Cells 26.5 och senare** och är det rekommenderade sättet att round-trippa en sparkline renderad av `ToImage` tillbaka till samma arbetsbok.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (en `bool`) begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` när man genererar ensides-rapporter.
- `ImageOrPrintOptions.ImageType` finns i namnrymden `Aspose.Cells.Drawing` och väljer bildformatet (till exempel `ImageType.Png`) som används vid rendering med `ToImage` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**

- [Sparklines i Aspose.Cells for C++](/cells/sv/cpp/sparkline/)
- [Infoga en bild i en cell](/cells/sv/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/sv/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}