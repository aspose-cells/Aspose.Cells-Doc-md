---
title: Smart Markers i sidhuvud och sidfot | Aspose.Cells .NET
linktitle: Smartmarkörer i sidhuvud och sidfot | Aspose.Cells
description: Placera Smart Marker-platshållare i sidhuvud och sidfot med dubbelvinkelparentessyntax och WorkbookDesigner.EnableHeaderFooterMarkers-omkopplaren med DataTable- eller JSON-datakällor, samt bind bilder via data-URI i Aspose.Cells for .NET.
keywords: Aspose.Cells, Smart Markers, sidhuvuden, sidfötter, sidhuvud-sidfot-markörer, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, databindning, bild, data-URI, C#
type: docs
weight: 196
url: /sv/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Sidhuvud och sidfot innehåller ofta rapportmetadata såsom rapporttitel, rapportperiod, författare och avdelning. När denna information redan finns i datakällan som används för att fylla arbetsboken, skapar manuell upprepning onödig duplicering.  
Klassisk Smart Marker-syntax, `&=Source.Field`, behandlas i kalkylbladets cellinnehåll. Om du placerar en klassisk markör i ett sidhuvud eller en sidfot via `PageSetup.SetHeader` eller `PageSetup.SetFooter` förblir den bokstavlig text eftersom sidhuvud- och sidfotsträngarna inte ingår i kalkylbladets cellrutnät som skannas av `WorkbookDesigner.Process()`.  
Från och med **Aspose.Cells for .NET 26.11** gör `WorkbookDesigner.EnableHeaderFooterMarkers`-omkopplaren, som är `false` som standard, att `Process()` löser platshållare skrivna som `<<Source.Field>>` i sidhuvud- och sidfot-sektionens strängar — sätt den till `true` innan du anropar `Process()`. Sidhuvud- och sidfot-platshållare använder samma datakälla som kroppens markörer.  
Varje sidhuvud och sidfot innehåller tre adresserbara sektioner:
- Sektion `0` är den vänstra sektionen.
- Sektion `1` är den centrala sektionen.
- Sektion `2` är den högra sektionen.  
Använd `PageSetup.SetHeader(int section, string value)` och `PageSetup.SetFooter(int section, string value)` för att skriva dessa sektioner. Efter bearbetning, använd `PageSetup.GetHeader(int section)` och `PageSetup.GetFooter(int section)` för att hämta den färdiga texten.

{{% alert color="primary" %}}
En platshållare som `<<Source.Field>>` infogar fältvärdet som text i sektionens sträng. Bilder bindas med suffixet `(picture)` och ett data-URI-värde.  
{{% /alert %}}

## **Aktivera Sidhuvud-/Sidfot-markörer med en DataTable**
Använd följande sekvens för att lösa sidhuvud- och sidfot-platshållare med en `DataTable` i **Aspose.Cells for .NET 26.11**:
1. Skapa ett `Workbook` och hämta dess första `Worksheet` på index `0`.
2. Skriv `<<Source.Field>>`-platshållare i önskade sidhuvud- och sidfot-sektioner med `PageSetup.SetHeader` och `PageSetup.SetFooter`.
3. Skapa en `DataTable` vars tabellnamn matchar källprefixet som används av platshållarna. Till exempel stödjer en tabell med namnet `node` platshållare som `<<node.Name>>`.
4. Skapa en `WorkbookDesigner` för arbetsboken.
5. Sätt `designer.EnableHeaderFooterMarkers` till `true` före bearbetning.
6. Koppla tabellen med `designer.SetDataSource(table)`.
7. Anropa `designer.Process()`.
8. Efter bearbetning finns inte längre platshållarna i sidhuvud- eller sidfotstexten. Använd `GetHeader` och `GetFooter` för att hämta de färdiga sektionsträngarna.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **Använd en JSON-datakälla**
Du kan använda JSON istället för en `DataTable` när rapportdata redan finns i JSON-format. Anropa `WorkbookDesigner.SetJsonDataSource(string name, string json)` för att koppla källan.  
Argumentet `name` har samma roll som `DataTable`-namnet. Till exempel stödjer namnet `node` platshållare som `<<node.Company>>` och `<<node.Title>>`.  
Leverera raddata direkt till `SetJsonDataSource`:
- En radarray, såsom en JSON-array som innehåller ett eller flera radobjekt, stöds.
- Ett enskilt radobjekt kan också skickas direkt.
- Vikla inte in raderna under en namngiven toppnyckel som `{"rows":[...]}`. Detta omslag är inte det förväntade rad-orienterade inmatningsformatet för detta arbetsflöde.  
En JSON-källa kan fylla båda markörstilarna under samma `Process()`-anrop. Den kan lösa en klassisk `&=`-markör i en kalkylbladscell och dubbelvinkelparentes-`<<>>`-platshållare i sidhuvud- och sidfot-sektioner. Du måste fortfarande aktivera `EnableHeaderFooterMarkers` för att sidhuvud- och sidfot-platshållarna ska lösas.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **Omkopplare och flerrads-källsemantik**
`EnableHeaderFooterMarkers` är `false` som standard, och omkopplaren styr endast sidhuvud- och sidfot-`<<Source.Field>>`-platshållarna. När omkopplaren är av, löser `Process()` fortfarande klassiska `&=`-kroppsmarkörer, men en `<<Source.Field>>`-platshållare i ett sidhuvud eller en sidfot förblir bokstavlig text.  
En sidhuvud- eller sidfot-sektion är en enda sträng, inte ett repeterande band. Om datakällan innehåller flera rader, ger den första raden sidhuvud- och sidfot-värdena. När de har lösts blir värdena vanlig sidhuvud- eller sidfot-text. De finns kvar i arbetsboken efter att du anropat `Save` och är närvarande när du laddar den sparade arbetsboken igen.  
Följande exempel skapar två arbetsböcker baserade på samma flerrads-`DataTable` för att jämföra beteendet när omkopplaren är av respektive på. `plainDesigner` lämnar platshållaren oförändrad, medan `enabledDesigner` löser den med den första raden.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **Binda en bild i ett sidhuvud eller en sidfot**
Suffixet `(picture)` binder en bild i en sidhuvud- eller sidfot-sektion. Skriv `<<node.logo(picture)>>` där bilden ska visas, och ange fältvärdet som en data-URI — prefixet `data:image/png;base64,` följt av Base64-texten för bildens byte. En ren Base64-sträng utan `data:`-prefixet bäddar inte in en bild.  
Efter `Process()`:
1. Platshållaren ersätts med `&G`, den standardiserade sidhuvud- och sidfot-bildkoden. Eftersom markören blir kod i sektionens sträng kan den finnas i längre text, exempelvis `Logo: <<node.logo(picture)>>`.
2. Bildens byte bäddas in i arbetsboken som en mediedel kopplad till sidhuvud-/sidfot-ritningslagret i det kalkylbladet, så bilden skrivs ut med sidhuvudet eller sidfoten.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

Den skrivna `&G` är bildkoden som Excel tolkar vid rendering av sidhuvudet — `logo.png`-bytena finns nu i `HeaderFooterPicture.xlsx`, och bilden skrivs ut i stället för koden.  
För att använda sidhuvud- och sidfot-Smart Markers, skriv `<<Source.Field>>`-platshållare i den vänstra, centrala och högra sidhuvud- eller sidfot-sektionen med `SetHeader` och `SetFooter`. Sätt `EnableHeaderFooterMarkers` till `true` på `WorkbookDesigner` innan du anropar `Process()`, och leverera värden via antingen `SetDataSource(DataTable)` eller `SetJsonDataSource`. Läs de färdiga sektionerna med `GetHeader` och `GetFooter`. Samma datakälla kan fylla både kroppens markörer och sidhuvud- eller sidfot-platshållare i ett bearbetningssteg. Lägg till suffixet `(picture)` med ett data-URI-värde för att binda en bild i en sektion.

## Relaterade artiklar
- [SmartMarker enkelcell-arrayrendering](/cells/sv/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}