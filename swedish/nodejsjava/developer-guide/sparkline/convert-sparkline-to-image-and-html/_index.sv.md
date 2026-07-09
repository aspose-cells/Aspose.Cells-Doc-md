---
title: Konvertera sparkline till bild och HTML i Aspose.Cells for Node.js via Java
linktitle: Convert Sparkline to Image and HTML
description: Lär dig hur du renderar Aspose.Cells sparklines till fristående bilder för inbäddning i celler och exporterar sparkline-rika kalkylblad till HTML med HtmlSaveOptions.
keywords: Aspose.Cells, Node.js via Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är miniatyrdiagram placerade i kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparkline-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `Cell.EmbeddedImage` som används i denna artikel är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**

Sparklines är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Medan Excel-användare ser dem på plats kräver många verkliga scenarier att en sparkline lämnar cellen — till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande, eller renderas som en del av en HTML-rapport som publiceras på webben.

Aspose.Cells stöder båda dessa operationer. Metoden `Sparkline.toImage` renderar en enskild sparkline till en ström, och de resulterande bytena kan tilldelas till `Cell.EmbeddedImage` så att bilden lagras i en enskild cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken — sparklines och allt — till en självständig HTML-fil. Den här artikeln går igenom båda arbetsflödena steg för steg.

## **Arbetsflöde 1 — Rendera sparklines till bilder och bädda in dem i celler**

I detta arbetsflöde kommer du att bygga ett kalkylblad som innehåller ett litet intervall av källvärden, koppla tre olika sparkline-grupper (Line, Column och Stacked/Win-Loss) till det intervallet, rendera varje grupp som en PNG, och skriva dessa PNG-byten till intilliggande celler som inbäddade bilder. Det slutliga resultatet är en enda `.xlsx`-fil som innehåller både de levande sparklines och deras renderade bildmotsvarigheter.

### **Steg-för-steg-instruktioner**

1. Definiera en arbetskatalog och se till att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska provvärden (till exempel daglig försäljning eller temperaturavläsningar).
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.sparklineGroups.add(...)`:
   - En `SparklineType.Line`-grupp förankrad vid `F1`, med dataintervall `A1:E1`.
   - En `SparklineType.Column`-grupp förankrad vid `G1`, med dataintervall `A1:E1`.
   - En `SparklineType.Stacked` (vinst/förlust)-grupp förankrad vid `H1`, med dataintervall `A1:E1`.
5. Skapa en `ImageOrPrintOptions`-instans och ställ in dess `ImageType` till `ImageType.Png` så att varje sparkline renderas som en transparent PNG.
6. För vardera av de tre grupperna, rendera dess enda sparkline med hjälp av `group.sparklines[0].toImage(outputStream, imageOptions)`, konvertera `ByteArrayOutputStream` till en `byte[]`, och tilldela arrayen till `worksheet.cells.get("F2").setEmbeddedImage(...)`, `worksheet.cells.get("G2").setEmbeddedImage(...)`, respektive `worksheet.cells.get("H2").setEmbeddedImage(...)`.
7. Spara arbetsboken som `output_with_sparklines.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Fylla i exempeldata i cellerna A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Lägg till en linje-sparkline-grupp förankrad vid F1 (kolumn 5, rad 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// Lägg till en kolumn-sparkline-grupp förankrad vid G1 (kolumn 6, rad 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// Lägg till en vinst/förlust (staplad) sparkline-grupp förankrad vid H1 (kolumn 7, rad 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// Konfigurera bildalternativ för PNG-utdata
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// Konvertera linje-sparkline till bild och bädda in den i cell F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Konvertera kolumn-sparkline till bild och bädda in den i cell G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Konvertera vinst/förlust-sparkline till bild och bädda in den i cell H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Spara arbetsboken till disk
workbook.save("output_with_sparklines.xlsx");
```

Koden ovan producerar en arbetsbok där varje visuell representation av en sparkline dupliceras i två former: den levande, nativa sparkline som är förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna lever i själva filen förblir arbetsboken ett enda självständigt objekt som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparkline-grupp som en PNG, konvertera `ByteArrayOutputStream` till en `byte[]`, och tilldela arrayen till egenskapen `setEmbeddedImage` för målcellen — det är tilldelningen som gör att bilden blir en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparkline-grupp är förankrad i en enskild cell kan du adressera den via indexeraren `group.sparklines[0]` istället för att räkna upp med `forEach`. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparkline per ankarcell". Att lagra bildbytena via `Cell.EmbeddedImage` kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 — Exportera sparkline-kalkylbladet till HTML**

När arbetsboken innehåller levande sparklines (och valfritt inbäddade bildmotsvarigheter) kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i detta arbetsflöde kommer du att återanvända filen `output_with_sparklines.xlsx` som producerades av Arbetsflöde 1 och konvertera den till ett rent HTML-dokument med en sida.

### **Steg-för-steg-instruktioner**

1. Se till att filen `output_with_sparklines.xlsx` som producerades av Arbetsflöde 1 är tillgänglig på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och ställ in dess egenskap `ExportActiveWorksheetOnly` till `true` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet snarare än hela arbetsboken.
4. Anropa `workbook.save("sparklines.html", htmlOptions)` för att skriva HTML-utdata till disk.

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Koden ovan tar den sparkline-rika arbetsboken från Arbetsflöde 1 och gör om den till en portabel HTML-fil. Sparklines bevaras som inline SVG- eller PNG-renderingar i den genererade HTML:en, beroende på exportläget, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att behöva ha Excel installerat. Genom att ställa in `ExportActiveWorksheetOnly` till `true` undviker du att av misstag publicera dolda blad eller extra data — endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för finjustering av utdata, såsom `ExportHiddenWorksheet`, `ExportImagesAsBase64` och `Encoding`. Justera dessa efter behov för ditt distributionsmål.
{{% /alert %}}

## **API-sammanfattning**

Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells-API:er som arbetar tillsammans.

- `SparklineGroup` och samlingsåtkomsten `worksheet.sparklineGroups` används för att deklarera typen (Line, Column, Stacked), dataintervallet och ankarcellen för varje sparkline-grupp. I denna artikel är varje grupp förankrad i en enskild cell, så gruppen nås via `worksheet.sparklineGroups[i]`.
- `Sparkline` och indexeraren `group.sparklines[0]` returnerar den enskilda sparkline i en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen `forEach`-loop.
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparkline till en tillhandahållen `OutputStream`. Metoden returnerar `void`; du läser bytena från strömmen efter anropet.
- `Cell.EmbeddedImage` är en `byte[]`-egenskap som lagrar en bild i en enskild cell. Den är tillgänglig i **Aspose.Cells 26.5 och senare** och är det rekommenderade sättet att rundgångslagra en sparkline som renderats av `toImage` tillbaka i samma arbetsbok.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (en `boolean`) begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` när man genererar ensidesrapporter.
- `ImageOrPrintOptions.ImageType` finns i namnrymden `com.aspose.cells.drawing` och väljer bildformatet (till exempel `ImageType.Png`) som används vid rendering med `toImage` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**

- [Sparklines i Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/sparkline/)
- [Infoga en bild i en cell](/cells/sv/nodejs-java/inserting-an-image-into-a-cell/)
- [SmartMarker-rendering av enstaka cellmatris | Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}