---
title: Smart Markörer i sidhuvuden och sidfötter | Aspose.Cells for Node.js via Java
linktitle: Smartmarkörer i sidhuvud och sidfot | Aspose.Cells for Node.js via Java
description: Placera Smart Marker-platshållare i sidhuvuden och sidfötter med dubbelvinkelparentes-syntax och WorkbookDesigner.setEnableHeaderFooterMarkers-växeln med JSON-datakällor samt binda bilder genom data-URI-värden i Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells for Node.js via Java, Smart Markörer, sidhuvuden, sidfötter, sidhuvud- och sidfotmarkörer, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, JSON-rader, databindning, bild, data-URI, JavaScript
type: docs
weight: 196
url: /sv/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Sidhuvuden och sidfötter innehåller ofta rapportmetadata som rapporttitel, rapportperiod, författare och avdelning. När denna information redan finns i den datakälla som används för att fylla arbetsboken, skapar manuell duplicering onödig repetition.  
Den klassiska Smart Marker-syntaksen, `&=Source.Field`, behandlas i kalkylbladets cellinnehåll. Om du placerar en klassisk markör i ett sidhuvud eller en sidfot via `PageSetup.setHeader` eller `PageSetup.setFooter` förblir den som bokstavlig text eftersom sidhuvuds- och sidfotssträngar inte ingår i kalkylbladets cellnät som skannas av `WorkbookDesigner.process()`.  
Från och med **Aspose.Cells for Node.js via Java 26.11** gör inställningen `WorkbookDesigner.setEnableHeaderFooterMarkers`, som är `false` som standard, så att `process()` löser platshållare skrivna som `<<Source.Field>>` i sidhuvuds- och sidfotssektionernas strängar. Anropa `designer.setEnableHeaderFooterMarkers(true)` innan du anropar `process()`. Platshållare i sidhuvuden och sidfötter använder samma datakälla som markörer i kalkylbladets kropp.  
Varje sidhuvud och varje sidfot innehåller tre adresserbara sektioner:
- Sektion `0` är vänstersektionen.
- Sektion `1` är mittsektionen.
- Sektion `2` är högersektionen.  
Använd `PageSetup.setHeader(int section, String value)` och `PageSetup.setFooter(int section, String value)` för att skriva dessa sektioner. Efter bearbetning använder du `PageSetup.getHeader(int section)` och `PageSetup.getFooter(int section)` för att hämta den färdiga texten.

{{% alert color="primary" %}}
En platshållare som `<<Source.Field>>` infogar fältvärdet som text i sektionens sträng. Bilder bindes med suffixet `(picture)` och ett data-URI-värde.
{{% /alert %}}

## **Aktivera sidhuvud-/sidfot-markörer med JSON-raddata**
Använd följande sekvens för att lösa platshållare i sidhuvud och sidfot med JSON-raddata i **Aspose.Cells for Node.js via Java 26.11**:
1. Skapa en `Workbook` och hämta dess första `Worksheet` med `workbook.getWorksheets().get(0)`.
2. Skriv `<<Source.Field>>`-platshållare i önskade sidhuvuds- och sidfotssektioner med `PageSetup.setHeader` och `PageSetup.setFooter`.
3. Förbered raddata som en JSON-array av radobjekt och välj ett källnamn som matchar källprefixet som används av platshållarna. Till exempel stödjer en källa med namn `node` platshållare som `<<node.Name>>`. Vanliga JavaScript-objekt och -arrayer som skickas till `setDataSource` bindas inte på denna plattform – JSON är det stödjade tabellformatet.
4. Skapa en `WorkbookDesigner` för arbetsboken.
5. Anropa `designer.setEnableHeaderFooterMarkers(true)` innan du bearbetar.
6. Bifoga JSON-data med `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')`.
7. Anropa `designer.process()`.
8. Efter bearbetning finns platshållarna inte längre i sidhuvuds- eller sidfotstexten. Använd `getHeader` och `getFooter` för att hämta de färdiga sektionernas strängar.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **Använd en JSON-datakälla**
När rapportdata redan finns tillgänglig som JSON kan ett `setJsonDataSource`-anrop mata alla markörstilar. Anropa `WorkbookDesigner.setJsonDataSource(String name, String json)` för att bifoga källan.  
`name`-argumentet är källnamnet som används av platshållarna. Till exempel stödjer namnet `node` platshållare som `<<node.Company>>` och `<<node.Title>>`.  
Skicka raddata direkt till `setJsonDataSource`:
- En radarray, såsom en JSON-array som innehåller en eller flera radobjekt, stöds.
- Ett enskilt radobjekt kan också skickas direkt.
- Omge inte raderna med ett namngivet toppnivå-nyckel som `{"rows":[...]}`. Detta omslag är inte den förväntade radorienterade indatan för detta arbetsflöde.  
En JSON-källa kan fylla båda markörstilarna under samma `process()`-anrop. Den kan lösa en klassisk `&=`-markör i en cell i kalkylbladet och dubbelvinkelparentes-platshållare `<<>>` i sidhuvuds- och sidfotssektioner. Du måste fortfarande anropa `designer.setEnableHeaderFooterMarkers(true)` för att platshållarna i sidhuvud och sidfot ska lösas.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **Växling och flerrads-källsemantik**
`setEnableHeaderFooterMarkers` är `false` som standard, och inställningen styr endast sidhuvuds- och sidfot-platshållarna `<<Source.Field>>`. När växeln är avstängd löser `process()` fortfarande klassiska `&=`-kroppsmarkörer, men en `<<Source.Field>>`-platshållare i ett sidhuvud eller en sidfot förblir bokstavlig text.  
En sidhuvuds- eller sidfotssektion är en sträng, inte ett repeterande band. Om datakällan innehåller flera rader ger den första raden värden för sidhuvudet och sidfoten. När de har lösts blir värdena vanlig text i sidhuvudet eller sidfoten. De finns kvar i arbetsboken efter att du anropar `save` och är närvarande när du laddar den sparade arbetsboken igen.  
Följande exempel skapar två arbetsböcker med samma flerrads-JSON-källa för att jämföra beteendet när växeln är avstängd respektive påslagen. `plainDesigner` lämnar platshållaren oförändrad, medan `enabledDesigner` löser den med hjälp av den första raden.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **Binda en bild i ett sidhuvud eller en sidfot**
Suffixet `(picture)` binder en bild i en sidhuvuds- eller sidfotssektion. Skriv `<<node.logo(picture)>>` där bilden ska visas och ange fältvärdet som en data-URI — prefixet `data:image/png;base64,` följt av Base64-texten för bildens byte. En ren Base64-sträng utan `data:`-prefixet bäddar inte in en bild.  
Efter `process()`:
1. Platshållaren ersätts med `&G`, den standardiserade bildkoden för sidhuvud och sidfot. Eftersom markören blir en kod i sektionens sträng kan den placeras i längre text, exempelvis `Logo: <<node.logo(picture)>>`.
2. Bild-bytena bäddas in i arbetsboken som en mediakomponent knuten till ritlagret för sidhuvud/sidfötter i det kalkylbladet, så bilden skrivs ut tillsammans med sidhuvudet eller sidfoten.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

Den utskrivna `&G` är bildkoden som Excel tolkar vid rendering av sidhuvudet — `logo.png`-byten finns nu i `HeaderFooterPicture.xlsx`, och bilden skrivs ut i stället för koden.  
För att använda Smart Markörer i sidhuvud och sidfot, skriv `<<Source.Field>>`-platshållare i vänster-, mitten- och högersektionerna för sidhuvud eller sidfot med `setHeader` och `setFooter`. Anropa `designer.setEnableHeaderFooterMarkers(true)` innan du anropar `process()`, och tillhandahåll värden via `designer.setJsonDataSource(name, json)`. Läs de färdiga sektionerna med `getHeader` och `getFooter`. Samma datakälla kan fylla både kroppens markörer och platshållare i sidhuvud eller sidfot i ett enda bearbetningspass. Lägg till suffixet `(picture)` med ett data-URI-värde för att binda en bild i en sektion.

## Relaterade artiklar
- [SmartMarker Enskild Cell-Array-Rendering](/cells/sv/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}