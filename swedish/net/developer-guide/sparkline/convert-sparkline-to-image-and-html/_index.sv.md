---
title: Konvertera Sparkline till bild och HTML i Aspose.Cells for .NET
linktitle: Convert Sparkline to Image and HTML
description: Lär dig hur du renderar Aspose.Cells-sparklines till fristående bilder för inbäddning i celler och exporterar sparkline-rika kalkylblad till HTML med HtmlSaveOptions.
keywords: Aspose.Cells, .NET, sparkline, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är miniatyrdiagram som placeras inuti kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparkline-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `Cell.EmbeddedImage` som används i denna artikel är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**

Sparklines är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Även om Excel-användare ser dem på plats, kräver många verkliga scenarier att en sparkline lämnar cellen – till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande, eller renderas som en del av en HTML-rapport som publiceras på webben.

Aspose.Cells stöder båda dessa operationer. Metoden `Sparkline.ToImage` renderar en enskild sparkline till en ström, och de resulterande bytes kan tilldelas till `Cell.EmbeddedImage` så att bilden lagras i en enda cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken – inklusive sparklines – till en självständig HTML-fil. Den här artikeln går igenom båda arbetsflödena steg för steg.

## **Arbetsflöde 1 — Rendera sparklines till bilder och bädda in dem i celler**

I detta arbetsflöde kommer du att bygga ett kalkylblad som innehåller ett litet intervall av källvärden, koppla tre olika sparkline-grupper (Line, Column och Stacked/Win-Loss) till det intervallet, rendera varje grupp som en PNG, och skriva dessa PNG-bytes till intilliggande celler som inbäddade bilder. Slutresultatet är en enda `.xlsx`-fil som innehåller både de levande sparklines och deras renderade bildmotsvarigheter.

### **Stegvisa instruktioner**

1. Definiera en arbetskatalog och se till att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturmätningar).
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.SparklineGroups.Add(...)`:
   - En `SparklineType.Line`-grupp förankrad vid `F1`, med dataområde `A1:E1`.
   - En `SparklineType.Column`-grupp förankrad vid `G1`, med dataområde `A1:E1`.
   - En `SparklineType.Stacked`-grupp (vinst/förlust) förankrad vid `H1`, med dataområde `A1:E1`.
5. Skapa en `ImageOrPrintOptions`-instans och sätt dess `ImageType` till `ImageType.Png` så att varje sparkline renderas som en transparent PNG.
6. För var och en av de tre grupperna, rendera dess enskilda sparkline med `group.Sparklines[0].ToImage(memoryStream, imageOptions)`, konvertera `MemoryStream` till en `byte[]`, och tilldela arrayen till `worksheet.Cells["F2"].EmbeddedImage`, `worksheet.Cells["G2"].EmbeddedImage` respektive `worksheet.Cells["H2"].EmbeddedImage`.
7. Spara arbetsboken som `output_with_sparklines.xlsx`.



```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// Skapa en ny arbetsbok och öppna det första kalkylbladet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Fylla i exempeldata i cellerna A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Lägg till en linje-sparkline-grupp förankrad vid F1 (kolumn 5, rad 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// Lägg till en kolumn-sparkline-grupp förankrad vid G1 (kolumn 6, rad 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// Lägg till en Vinst/Förlust (Staplad) sparkline-grupp förankrad vid H1 (kolumn 7, rad 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// Konfigurera bildalternativ för PNG-utdata
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// Konvertera linje-sparkline till bild och bädda in den i cell F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// Konvertera kolumn-sparkline till bild och bädda in den i cell G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// Konvertera Vinst/Förlust-sparkline till bild och bädda in den i cell H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// Spara arbetsboken till disk
workbook.Save("output_with_sparklines.xlsx");
```

Koden ovan skapar en arbetsbok där varje visuell representation av en sparkline dupliceras i två former: den levande, nativa sparklinen förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna lever inuti filen själv förblir arbetsboken ett enda självständigt objekt som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparkline-grupp som en PNG, konvertera `MemoryStream` till en `byte[]`, och tilldela arrayen till `EmbeddedImage`-egenskapen för målcellen – det är tilldelningen som gör bilden till en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparkline-grupp är förankrad till en enda cell kan du adressera den via indexeraren `group.Sparklines[0]` istället för att räkna upp med `foreach`. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparkline per förankringscell". Att lagra bildbyteen via `Cell.EmbeddedImage` kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 — Exportera sparkline-kalkylbladet till HTML**

När arbetsboken innehåller levande sparklines (och eventuellt inbäddade bildmotsvarigheter) kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i detta arbetsflöde återanvänder du filen `output_with_sparklines.xlsx` som skapades av Arbetsflöde 1 och konverterar den till ett rent ensidigt HTML-dokument.

### **Stegvisa instruktioner**

1. Se till att filen `output_with_sparklines.xlsx` som skapades av Arbetsflöde 1 är tillgänglig på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och sätt dess `ExportActiveWorksheetOnly`-egenskap till `true` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet snarare än hela arbetsboken.
4. Anropa `workbook.Save("sparklines.html", htmlOptions)` för att skriva HTML-utdata till disk.



```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

Koden ovan tar den sparkline-rika arbetsboken från Arbetsflöde 1 och förvandlar den till en portabel HTML-fil. Sparklines bevaras som inline SVG- eller PNG-renderingar inuti den genererade HTML-koden, beroende på exportläget, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att behöva ha Excel installerat. Genom att sätta `ExportActiveWorksheetOnly` till `true` undviker du att av misstag publicera dolda blad eller extra data – endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för finjustering av utdata, såsom `ExportHiddenWorksheet`, `ExportImagesAsBase64` och `Encoding`. Justera dessa efter behov för ditt driftsättningsmål.
{{% /alert %}}

## **API-sammanfattning**

Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells API:er som arbetar tillsammans.

- `SparklineGroup` och samlingsåtkomsten `worksheet.SparklineGroups` används för att deklarera typen (Line, Column, Stacked), dataområdet och förankringscellen för varje sparkline-grupp. I denna artikel är varje grupp förankrad till en enda cell, så gruppen nås via `worksheet.SparklineGroups[i]`.
- `Sparkline` och indexeraren `group.Sparklines[0]` returnerar den enskilda sparklinen inuti en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen `foreach`-loop.
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparklinen till en angiven `Stream`. Metoden returnerar `void`; du läser byteen från strömmen efter anropet.
- `Cell.EmbeddedImage` är en `byte[]`-egenskap som lagrar en bild i en enda cell. Den är tillgänglig i **Aspose.Cells 26.5 och senare** och är det rekommenderade sättet att överföra en sparkline som renderats av `ToImage` tillbaka till samma arbetsbok.
- `HtmlSaveOptions.ExportActiveWorksheetOnly` (en `bool`) begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` vid generering av ensidiga rapporter.
- `ImageOrPrintOptions.ImageType` finns i namnrymden `Aspose.Cells.Drawing` och väljer bildformatet (till exempel `ImageType.Png`) som används vid rendering med `ToImage` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**

- [Sparklines in Aspose.Cells for .NET](/cells/sv/net/sparkline/)
- [Inserting an Image into a Cell](/cells/sv/net/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells .NET](/cells/sv/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}