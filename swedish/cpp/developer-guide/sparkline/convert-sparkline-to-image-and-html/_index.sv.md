---
title: Konvertera Sparkline till bild och HTML i Aspose.Cells for C++
linktitle: Konvertera Sparkline till bild och HTML i Aspose.Cells for C++
description: Lär dig hur du renderar Aspose.Cells sparklines till fristående bilder för inbäddning i celler och exporterar sparkline-rika kalkylblad till HTML med HtmlSaveOptions.
keywords: Aspose.Cells, C++, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är miniatyrdiagram placerade i kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparkline-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `Cell.EmbeddedImage` som används i denna artikel är tillgänglig i **Aspose.Cells 26.5 och senare**.

## **Introduktion**
Sparklines är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Medan Excel-användare ser dem på plats, kräver många verkliga situationer att en sparkline lämnar cellen — till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande eller renderas som en del av en HTML-rapport som publiceras på webben.
Aspose.Cells stöder båda dessa operationer. Metoden `Sparkline.ToImage` renderar en enskild sparkline till en `Vector<uint8_t>`-bytearray, och de resulterande byten kan tilldelas till `Cell.EmbeddedImage` så att bilden lagras i en enda cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken — sparklines och allt — till en fristående HTML-fil. Denna artikel går igenom båda arbetsflödena steg för steg.

## **Arbetsflöde 1 — Rendera sparklines till bilder och bädda in dem i celler**
I detta arbetsflöde kommer du att bygga ett kalkylblad som innehåller ett litet intervall av källvärden, koppla tre olika sparkline-grupper (Line, Column och Stacked/Win-Loss) till det intervallet, rendera varje grupp som en PNG och skriva dessa PNG-bytes till intilliggande celler som inbäddade bilder. Slutresultatet är en enda `.xlsx`-fil som innehåller både de levande sparklines och deras renderade bildmotsvarigheter.

### **Steg-för-steg-instruktioner**
1. Definiera en arbetskatalog och säkerställ att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturavläsningar).
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.SparklineGroups.Add(...)`:
   - En `SparklineType.Line`-grupp förankrad vid `F1`, med dataintervall `A1:E1`.
   - En `SparklineType.Column`-grupp förankrad vid `G1`, med dataintervall `A1:E1`.
   - En `SparklineType.Stacked` (vinst/förlust)-grupp förankrad vid `H1`, med dataintervall `A1:E1`.
5. Bygg en `ImageOrPrintOptions`-instans och sätt dess `ImageType` till `ImageType.Png` så att varje sparkline renderas som en transparent PNG.
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

Koden ovan producerar en arbetsbok där varje visuell representation av en sparkline dupliceras i två former: den levande, nativa sparkline som är förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna lever inuti filen förblir arbetsboken ett enda fristående dokument som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparkline-grupp som en PNG — `Sparkline.ToImage(ImageOrPrintOptions)` returnerar bildbyten direkt som en `Vector<uint8_t>` — och tilldela arrayen till egenskapen `EmbeddedImage` för målcellen — det är tilldelningen som gör bilden till en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparkline-grupp är förankrad till en enda cell kan du adressera den via indexeraren `group.Sparklines[0]` istället för att enumerera med `foreach`. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparkline per ankarcell". Att lagra bildbyten via `Cell.EmbeddedImage` kräver Aspose.Cells 26.5 eller senare.

## **Arbetsflöde 2 — Exportera sparkline-kalkylbladet till HTML**
När arbetsboken innehåller levande sparklines (och eventuellt inbäddade bildmotsvarigheter) kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i detta arbetsflöde återanvänder du filen `output_with_sparklines.xlsx` som producerades av Arbetsflöde 1 och konverterar den till ett rent, ensidigt HTML-dokument.

### **Steg-för-steg-instruktioner**
1. Säkerställ att filen `output_with_sparklines.xlsx` som producerades av Arbetsflöde 1 finns på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och sätt dess egenskap `ExportActiveWorksheetOnly` till `true` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet snarare än hela arbetsboken.
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

Koden ovan tar den sparkline-rika arbetsboken från Arbetsflöde 1 och förvandlar den till en portabel HTML-fil. Sparklines bevaras som inline SVG- eller PNG-renderings i den genererade HTML-koden, beroende på exportläget, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att behöva ha Excel installerat. Genom att sätta `ExportActiveWorksheetOnly` till `true` undviker du att av misstag publicera dolda blad eller hjälpdata — endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för finjustering av utdata, såsom `ExportHiddenWorksheet`, `ExportImagesAsBase64` och `Encoding`. Justera dessa efter behov för ditt driftsättningsmål.

## **API-sammanfattning**
Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells-API:er som arbetar tillsammans.
- `SparklineGroup` och samlingsåtkomsten `worksheet.SparklineGroups` används för att deklarera typen (Line, Column, Stacked), dataintervallet och ankarcellen för varje sparkline-grupp. I denna artikel är varje grupp förankrad till en enda cell, så gruppen nås via `worksheet.SparklineGroups[i]`.
- `Sparkline` och indexeraren `group.Sparklines[0]` returnerar den enskilda sparkline inuti en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen `foreach`-loop.
- `Sparkline.ToImage(ImageOrPrintOptions)` är renderingsmetoden som returnerar en bild av sparkline direkt som en `Vector<uint8_t>`-bytearray.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (en `bool`) begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` när man genererar ensidiga rapporter.
- `ImageOrPrintOptions.ImageType` finns i namespacet `Aspose.Cells.Drawing` och väljer bildformatet (till exempel `ImageType.Png`) som används vid rendering med `ToImage` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**
- [Sparklines i Aspose.Cells for C++](/cells/sv/cpp/sparkline/)
- [Infoga en bild i en cell](/cells/sv/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker-rendering av enskild cellmatris | Aspose.Cells for C++](/cells/sv/cpp/SmartMarker-Single-Cell-Array-Rendering/)
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}