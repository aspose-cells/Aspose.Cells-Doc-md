---
title: Konvertera sparkline till bild och HTML i Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: Lär dig hur du renderar Aspose.Cells sparklines till fristående bilder för cellinbäddning och exporterar sparkline-rika kalkylblad till HTML med HtmlSaveOptions i Python via .NET.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, rendera sparkline, konvertera sparkline till bild, exportera sparkline till HTML
type: docs
weight: 120
url: /sv/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Sparklines är miniatyrdiagram som placeras inuti kalkylbladsceller. Aspose.Cells låter dig extrahera varje sparkline som en fristående bild (för inbäddning i en annan cell eller en extern rapport) och även exportera hela det sparkline-rika kalkylbladet till HTML för webbläsarbaserad distribution. Egenskapen `cell.embedded_image` som används i den här artikeln är tillgänglig i **Aspose.Cells 26.5 och senare**.
{{% /alert %}}

## **Introduktion**

Sparklines är ett kompakt sätt att visualisera trender direkt i ett kalkylblad. Medan Excel-användare ser dem på plats kräver många verkliga scenarier att en sparkline lämnar cellen — till exempel för att bäddas in i en annan cell som en statisk bild, bifogas till ett automatiserat e-postmeddelande eller renderas som en del av en HTML-rapport som publiceras på webben.

Aspose.Cells stöder båda dessa åtgärder. Metoden `sparkline.to_image` renderar en enskild sparkline till en ström, och de resulterande bytena kan tilldelas till `cell.embedded_image` så att bilden lagras inuti en enda cell i arbetsboken. Separat låter `HtmlSaveOptions` dig konvertera hela arbetsboken — inklusive sparklines — till en självständig HTML-fil. Den här artikeln går igenom båda arbetsflödena från början till slut.

## **Arbetsflöde 1 — Rendera sparklines till bilder och bädda in dem i celler**

I det här arbetsflödet kommer du att bygga ett kalkylblad som innehåller ett litet intervall källvärden, koppla tre olika sparkline-grupper (linje, kolumn och staplad/vinst-förlust) till det intervallet, rendera varje grupp som en PNG, och skriva dessa PNG-byten till intilliggande celler som inbäddade bilder. Det slutliga resultatet är en enda `.xlsx`-fil som innehåller både de levande sparklines och deras renderade bildmotsvarigheter.

### **Steg-för-steg-instruktioner**

1. Definiera en arbetskatalog och se till att den finns på disk.
2. Skapa en ny `Workbook` och hämta en referens till det första `Worksheet`.
3. Fyll cellerna `A1` till `E1` med fem numeriska exempelvärden (till exempel daglig försäljning eller temperaturavläsningar).
4. Lägg till tre `SparklineGroup`-objekt till kalkylbladet genom att anropa `worksheet.sparkline_groups.add(...)`:
   - En `SparklineType.LINE`-grupp förankrad vid `F1`, med dataintervall `A1:E1`.
   - En `SparklineType.COLUMN`-grupp förankrad vid `G1`, med dataintervall `A1:E1`.
   - En `SparklineType.STACKED`-grupp (vinst/förlust) förankrad vid `H1`, med dataintervall `A1:E1`.
5. Bygg en `ImageOrPrintOptions`-instans och ställ in dess `image_type` till `ImageType.PNG` så att varje sparkline renderas som en transparent PNG.
6. För var och en av de tre grupperna, rendera dess enskilda sparkline med `group.sparklines[0].to_image(memory_stream, image_options)`, konvertera `BytesIO`-strömmen till ett `bytes`-objekt, och tilldela arrayen till `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` respektive `worksheet.cells["H2"].embedded_image`.
7. Spara arbetsboken som `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# Skapa en ny arbetsbok och kom åt det första arbetsbladet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fyll i exempeldata i cellerna A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Lägg till en linje-sparkline-grupp förankrad vid F1 (kolumn 5, rad 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Lägg till en kolumn-sparkline-grupp förankrad vid G1 (kolumn 6, rad 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Lägg till en vinst/förlust (staplad) sparkline-grupp förankrad vid H1 (kolumn 7, rad 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Konfigurera bildalternativ för PNG-utdata
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Konvertera linje-sparkline till bild och bädda in den i cell F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Konvertera kolumn-sparkline till bild och bädda in den i cell G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Konvertera vinst/förlust-sparkline till bild och bädda in den i cell H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Spara arbetsboken till disk
workbook.save("output_with_sparklines.xlsx")
```

Koden ovan producerar en arbetsbok där varje visuell representation av en sparkline dupliceras i två former: den levande, nativa sparkline som är förankrad vid rad 1, och en statisk PNG-bild inbäddad direkt i en intilliggande cell på rad 2. Eftersom bilderna lever inuti filen själv förblir arbetsboken ett enda självständigt objekt som kan e-postas eller arkiveras utan att de inbäddade bildreferenserna bryts. Rendera varje sparkline-grupp som en PNG, konvertera `BytesIO`-strömmen till ett `bytes`-objekt, och tilldela bytena till egenskapen `embedded_image` för målcellen — det är tilldelningen som gör bilden till en del av cellens lagrade innehåll.

{{% alert color="primary" %}}
Eftersom varje sparkline-grupp är förankrad till en enda cell kan du adressera den via indexeraren `group.sparklines[0]` istället för att räkna upp med en `for`-loop. Detta håller renderingskoden kort och matchar det typiska mönstret "en sparkline per ankarcell". Att lagra bildbytena via `cell.embedded_image` kräver Aspose.Cells 26.5 eller senare.
{{% /alert %}}

## **Arbetsflöde 2 — Exportera sparkline-kalkylbladet till HTML**

När arbetsboken innehåller levande sparklines (och eventuellt inbäddade bildmotsvarigheter) kan hela kalkylbladet publiceras på webben genom att spara det som HTML. Klassen `HtmlSaveOptions` exponerar de reglage du behöver för att styra denna export; i det här arbetsflödet kommer du att återanvända filen `output_with_sparklines.xlsx` som producerades av arbetsflöde 1 och konvertera den till ett rent HTML-dokument med en sida.

### **Steg-för-steg-instruktioner**

1. Se till att filen `output_with_sparklines.xlsx` som producerades av arbetsflöde 1 är tillgänglig på disk i din arbetskatalog.
2. Ladda den filen i en ny `Workbook`-instans.
3. Instansiera `HtmlSaveOptions` och ställ in egenskapen `export_active_worksheet_only` till `True` så att den resulterande HTML-filen endast innehåller det aktiva kalkylbladet snarare än hela arbetsboken.
4. Anropa `workbook.save("sparklines.html", html_options)` för att skriva HTML-utdata till disk.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Koden ovan tar den sparkline-rika arbetsboken från arbetsflöde 1 och förvandlar den till en portabel HTML-fil. Sparklines bevaras som inline SVG- eller PNG-renderings inuti den genererade HTML:en, beroende på exportläget, så slutanvändare kan se trenderna i vilken modern webbläsare som helst utan att Excel behöver vara installerat. Genom att ställa in `export_active_worksheet_only` till `True` undviker du att av misstag publicera dolda blad eller extra data — endast det kalkylblad som för närvarande är synligt för användaren exporteras.

{{% alert color="primary" %}}
Klassen `HtmlSaveOptions` erbjuder ytterligare egenskaper för finjustering av utdata, såsom `export_hidden_worksheet`, `export_images_as_base64` och `encoding`. Justera dessa efter behov för ditt distributionsmål.
{{% /alert %}}

## **API-sammanfattning**

Arbetsflödena ovan förlitar sig på en liten uppsättning Aspose.Cells-API:er som arbetar tillsammans.

- `SparklineGroup` och samlingsaccessorn `worksheet.sparkline_groups` används för att deklarera typen (linje, kolumn, staplad), dataintervallet och ankarcellen för varje sparkline-grupp. I den här artikeln är varje grupp förankrad till en enda cell, så gruppen nås via `worksheet.sparkline_groups[i]`.
- `Sparkline` och indexeraren `group.sparklines[0]` returnerar den enskilda sparkline inuti en grupp. Eftersom varje grupp i exemplet innehåller exakt en sparkline krävs ingen `for`-loop.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` är renderingsmetoden som skriver en bild av sparkline till en tillhandahållen ström. Metoden returnerar `None`; du läser bytena från strömmen efter anropet.
- `cell.embedded_image` är en `bytes`-egenskap som lagrar en bild inuti en enda cell. Den är tillgänglig i **Aspose.Cells 26.5 och senare** och är det rekommenderade sättet att round-trippa en sparkline som renderats av `to_image` tillbaka till samma arbetsbok.
- `html_save_options.export_active_worksheet_only` (en `bool`) begränsar HTML-export till det aktiva kalkylbladet. Det är en av de mest använda egenskaperna på `HtmlSaveOptions` vid generering av rapporter med en sida.
- `image_or_print_options.image_type` finns i namnrymden `aspose.cells.drawing` och väljer bildformatet (till exempel `ImageType.PNG`) som används vid rendering med `to_image` och vid utskrift av kalkylblad till bilder.

## **Relaterade artiklar**

- [Sparklines i Aspose.Cells for Python via .NET](/cells/sv/python-net/sparkline/)
- [Infoga en bild i en cell](/cells/sv/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/sv/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}