---
title: Konvertera sparkline till bild och HTML i Aspose.Cells for Java
linktitle: Convert Sparkline to Image and HTML
description: Lär dig hur du renderar Aspose.Cells sparklines till fristående bilder för inbäddning i celler och exporterar sparkline-rika kalkylblad till HTML med HtmlSaveOptions.
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är miniatyrdiagram som placeras inuti kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparkline-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `Cell.EmbeddedImage` som används i denna artikel är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**

Sparklines är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Medan Excel-användare ser dem på plats kräver många verkliga scenarier att en sparkline lämnar cellen — till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande, eller renderas som en del av en HTML-rapport som publiceras på webben.

Aspose.Cells stöder båda dessa operationer. Metoden `Sparkline.toImage` renderar en enskild sparkline till en ström, och de resulterande byten kan tilldelas till `Cell.EmbeddedImage` (via `setEmbeddedImage`) så att bilden lagras inuti en enda cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken — inklusive alla sparklines — till en självständig HTML-fil. Denna artikel går igenom båda arbetsflödena steg för steg.

## **Arbetsflöde 1 — Rendera sparklines till bilder och bädda in dem i celler**

I detta arbetsflöde kommer du att bygga ett kalkylblad som innehåller ett litet intervall av källvärden, koppla tre olika sparkline-grupper (Line, Column och Stacked/Win-Loss) till det intervallet, rendera varje grupp som en PNG, och skriva dessa PNG-byten till intilliggande celler som inbäddade bilder. Det slutliga resultatet är en enda `.xlsx`-fil som innehåller både de levande sparklines och deras renderade bildmotsvarigheter.

### **Steg-för-steg-instruktioner**

1. Definiera en arbetskatalog och se till att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturavläsningar).
4. Lägg till tre `SparklineGroup`-objekt i kalkylbladet genom att anropa `worksheet.getSparklineGroups().add(...)`:
   - En `SparklineType.LINE`-grupp förankrad vid `F1`, med dataintervall `A1:E1`.
   - En `SparklineType.COLUMN`-grupp förankrad vid `G1`, med dataintervall `A1:E1`.
   - En `SparklineType.STACKED`-grupp (vinst/förlust) förankrad vid `H1`, med dataintervall `A1:E1`.
5. Skapa en `ImageOrPrintOptions`-instans och anropa `setImageType(ImageType.PNG)` så att varje sparkline renderas som en transparent PNG.
6. För var och en av de tre grupperna, rendera dess enskilda sparkline med `group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)`, konvertera `ByteArrayOutputStream` till en `byte[]`, och tilldela arrayen via `worksheet.getCells().get("F2").setEmbeddedImage(...)`, `worksheet.getCells().get("G2").setEmbeddedImage(...)` respektive `worksheet.getCells().get("H2").setEmbeddedImage(...)`.
7. Anropa `workbook.save("output_with_sparklines.xlsx")` för att spara arbetsboken till disk.

```java
import com.aspose.cells.*;
import java.io.*;

// Skapa en ny arbetsbok och få åtkomst till det första kalkylbladet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Fylla i exempeldata i cellerna A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Lägg till en linje-sparkline-grupp förankrad vid F1 (kolumn 5, rad 0)
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// Lägg till en kolumn-sparkline-grupp förankrad vid G1 (kolumn 6, rad 0)
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// Lägg till en vinst/förlust (staplad) sparkline-grupp förankrad vid H1 (kolumn 7, rad 0)
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// Konfigurera bildalternativ för PNG-utdata
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// Konvertera linje-sparkline till bild och bädda in den i cell F2
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// Konvertera kolumn-sparkline till bild och bädda in den i cell G2
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Konvertera vinst/förlust-sparkline till bild och bädda in den i cell H2
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// Spara arbetsboken till disk
workbook.save("output_with_sparklines.xlsx");
```

Koden ovan skapar en arbetsbok där varje visuell representation av en sparkline dupliceras i två former: den levande, nativa sparkline som är förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna lagras inuti filen förblir arbetsboken ett enda fristående artefakt som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparkline-grupp som en PNG, konvertera `ByteArrayOutputStream` till en `byte[]`, och tilldela arrayen till egenskapen `EmbeddedImage` för målcellen via `setEmbeddedImage(byte[])` — det är tilldelningen som gör att bilden blir en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparkline-grupp är förankrad i en enskild cell kan du adressera den via indexeraren `group.getSparklines().get(0)` istället för att enumerera med en `for`-loop. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparkline per ankarcell". Att lagra bildbyten via `Cell.EmbeddedImage` (sätts via `setEmbeddedImage`) kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 — Exportera sparkline-kalkylbladet till HTML**

När arbetsboken innehåller levande sparklines (och eventuellt inbäddade bildmotsvarigheter) kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i detta arbetsflöde återanvänder du filen `output_with_sparklines.xlsx` som skapades i Arbetsflöde 1 och konverterar den till ett rent enkelsides-HTML-dokument.

### **Steg-för-steg-instruktioner**

1. Se till att filen `output_with_sparklines.xlsx` som skapades i Arbetsflöde 1 finns på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och anropa `setExportActiveWorksheetOnly(true)` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet istället för hela arbetsboken.
4. Anropa `workbook.save("sparklines.html", htmlOptions)` för att skriva HTML-utdata till disk.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

Koden ovan tar den sparkline-rika arbetsboken från Arbetsflöde 1 och förvandlar den till en portabel HTML-fil. Sparklines bevaras som inline SVG- eller PNG-renderingar i den genererade HTML-koden, beroende på exportläget, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att behöva Excel installerat. Genom att sätta `ExportActiveWorksheetOnly` till `true` via `setExportActiveWorksheetOnly(true)` undviker du att oavsiktligt publicera dolda blad eller hjälpdata — endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för finjustering av utdata, såsom `ExportHiddenWorksheet`, `ExportImagesAsBase64` och `Encoding`. Justera dessa efter behov för ditt distributionsmål.
{{% /alert %}}

## **API-sammanfattning**

Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells-API:er som arbetar tillsammans.

- `SparklineGroup` och samlingsaccessorn `worksheet.getSparklineGroups()` används för att deklarera typen (Line, Column, Stacked), dataintervallet och ankarcellen för varje sparkline-grupp. I denna artikel är varje grupp förankrad vid en enskild cell, så gruppen nås via `worksheet.getSparklineGroups().get(i)`.
- `Sparkline` och indexeraren `group.getSparklines().get(0)` returnerar den enskilda sparkline inuti en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen `for`-loop.
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparkline till en tillhandahållen `Stream`. Metoden returnerar `void`; du läser byten från strömmen efter anropet.
- `Cell.EmbeddedImage` är en `byte[]`-egenskap (tilldelas via `cell.setEmbeddedImage(byte[])`) som lagrar en bild inuti en enda cell. Den är tillgänglig i **Aspose.Cells 26.5 och senare** och är det rekommenderade sättet att göra en round-trip av en sparkline som renderats av `toImage` tillbaka in i samma arbetsbok.
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` när man genererar enkelsidesrapporter.
- `ImageOrPrintOptions.setImageType(ImageType)` finns i paketet `com.aspose.cells.drawing` och väljer bildformatet (till exempel `ImageType.PNG`) som används vid rendering med `toImage` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**

- [Sparklines in Aspose.Cells for Java](/cells/sv/java/sparkline/)
- [Inserting an Image into a Cell](/cells/sv/java/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Java](/cells/sv/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}