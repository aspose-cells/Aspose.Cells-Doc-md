---
title: Konvertera Sparkline till bild och HTML i Aspose.Cells for Node.js via C++
linktitle: Convert Sparkline to Image and HTML
description: Lär dig hur du renderar Aspose.Cells sparklines till fristående bilder för inbäddning i celler och exporterar sparkline-rika kalkylblad till HTML med HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via C++, sparkline, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är miniatyrdiagram som placeras inuti kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparkline-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `cell.embeddedImage` som används i den här artikeln är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**

Sparklines är ett kompakt sätt att visualisera trender direkt inuti ett kalkylblad. Medan Excel-användare ser dem på plats kräver många verkliga scenarier att en sparkline lämnar cellen — till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande eller renderas som del av en HTML-rapport som publiceras på webben.

Aspose.Cells stöder båda dessa operationer. Metoden `Sparkline.toImage` renderar en enskild sparkline till en ström, och de resulterande byten kan tilldelas till `cell.embeddedImage` så att bilden lagras inuti en enskild cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken — inklusive alla sparklines — till en självständig HTML-fil. Den här artikeln går igenom båda arbetsflödena steg för steg.

## **Arbetsflöde 1 — Rendera sparklines till bilder och bädda in dem i celler**

I det här arbetsflödet kommer du att bygga ett kalkylblad som innehåller ett litet intervall av källvärden, koppla tre olika sparkline-grupper (Line, Column och Stacked/Win-Loss) till det intervallet, rendera varje grupp som en PNG och skriva dessa PNG-bytes till intilliggande celler som inbäddade bilder. Slutresultatet är en enda `.xlsx`-fil som innehåller både de levande sparklines och deras renderade bildmotsvarigheter.

### **Steg-för-steg-instruktioner**

1. Definiera en arbetskatalog och se till att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturavläsningar).
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.sparklineGroups.add(...)`:
   - En `SparklineType.Line`-grupp förankrad vid `F1`, med dataintervall `A1:E1`.
   - En `SparklineType.Column`-grupp förankrad vid `G1`, med dataintervall `A1:E1`.
   - En `SparklineType.Stacked`-grupp (vinst/förlust) förankrad vid `H1`, med dataintervall `A1:E1`.
5. Bygg en `ImageOrPrintOptions`-instans och ange dess `ImageType` till `ImageType.Png` så att varje sparkline renderas som en transparent PNG.
6. För var och en av de tre grupperna, rendera dess enskilda sparkline med `group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)`, konvertera strömmen till en `Buffer` (eller `Uint8Array`), och tilldela byten till `worksheet.cells["F2"].embeddedImage`, `worksheet.cells["G2"].embeddedImage` respektive `worksheet.cells["H2"].embeddedImage`.
7. Spara arbetsboken som `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Fyll i exempeldata i cellerna A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Lägg till en linjesparkline-grupp förankrad vid F1 (kolumn 5, rad 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Lägg till en kolumnsparkline-grupp förankrad vid G1 (kolumn 6, rad 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Lägg till en Vinst/Förlust (Staplad) sparkline-grupp förankrad vid H1 (kolumn 7, rad 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Konfigurera bildalternativ för PNG-utdata
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Konvertera linjesparkline till bild och bädda in den i cell F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// Konvertera kolumnsparkline till bild och bädda in den i cell G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// Konvertera Vinst/Förlust-sparkline till bild och bädda in den i cell H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// Spara arbetsboken till disk
workbook.save("output_with_sparklines.xlsx");
```

Koden ovan producerar en arbetsbok där varje visuell representation av en sparkline dupliceras i två former: den levande, nativa sparkline som är förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna finns inuti själva filen förblir arbetsboken ett enda självständigt artefakt som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparkline-grupp som en PNG, konvertera strömmen till en `Buffer` och tilldela arrayen till egenskapen `embeddedImage` för målcellen — det är tilldelningen som gör bilden till en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparkline-grupp är förankrad till en enda cell kan du adressera den genom indexeraren `group.sparklines[0]` istället för att räkna upp med `forEach`. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparkline per förankringscell". Att lagra bildbyten via `cell.embeddedImage` kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 — Exportera sparkline-kalkylbladet till HTML**

När arbetsboken väl innehåller levande sparklines (och eventuellt inbäddade bildmotsvarigheter) kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i det här arbetsflödet kommer du att återanvända filen `output_with_sparklines.xlsx` som producerades av arbetsflöde 1 och konvertera den till ett rent, ensidigt HTML-dokument.

### **Steg-för-steg-instruktioner**

1. Se till att filen `output_with_sparklines.xlsx` som producerades av arbetsflöde 1 är tillgänglig på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och ange dess egenskap `exportActiveWorksheetOnly` till `true` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet snarare än hela arbetsboken.
4. Anropa `workbook.save("sparklines.html", htmlOptions)` för att skriva HTML-utdata till disk.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Koden ovan tar den sparkline-rika arbetsboken från arbetsflöde 1 och förvandlar den till en portabel HTML-fil. Sparklines bevaras som inline SVG- eller PNG-renderingsar inuti den genererade HTML-koden, beroende på exportläget, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att behöva Excel installerat. Genom att sätta `exportActiveWorksheetOnly` till `true` undviker du att av misstag publicera dolda blad eller extra data — endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för finjustering av utdata, såsom `exportHiddenWorksheet`, `exportImagesAsBase64` och `encoding`. Justera dessa efter behov för ditt distributionsmål.
{{% /alert %}}

## **API-sammanfattning**

Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells-API:er som arbetar tillsammans.

- `SparklineGroup` och samlingsaccessorn `worksheet.sparklineGroups` används för att deklarera typen (Line, Column, Stacked), dataintervallet och förankringscellen för varje sparkline-grupp. I den här artikeln är varje grupp förankrad till en enda cell, så gruppen nås via `worksheet.sparklineGroups[i]`.
- `Sparkline` och indexeraren `group.sparklines[0]` returnerar den enskilda sparkline inuti en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen `forEach`-loop.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparkline till en angiven `Stream`. Metoden returnerar `void`; du läser byten från strömmen efter anropet.
- `cell.embeddedImage` är en `Buffer`- (eller `Uint8Array`-) egenskap som lagrar en bild inuti en enskild cell. Den är tillgänglig i **Aspose.Cells 26.5 och senare** och är det rekommenderade sättet att round-trip en sparkline renderad av `toImage` tillbaka till samma arbetsbok.
- `htmlSaveOptions.exportActiveWorksheetOnly` (en `bool`) begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` när man genererar ensidiga rapporter.
- `imageOrPrintOptions.imageType` finns i namnrymden `Aspose.Cells.Drawing` och väljer bildformatet (till exempel `ImageType.Png`) som används vid rendering med `toImage` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**

- [Sparklines i Aspose.Cells for Node.js via C++](/cells/sv/nodejs-cpp/sparkline/)
- [Infoga en bild i en cell](/cells/sv/nodejs-cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Node.js via C++](/cells/sv/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}