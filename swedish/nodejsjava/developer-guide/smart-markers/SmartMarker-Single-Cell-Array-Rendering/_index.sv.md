---
title: SmartMarker – rendering av en array i en enda cell | Aspose.Cells for Node.js via Java
linktitle: SmartMarker – rendering av en array i en enda cell | Aspose.Cells for Node.js via Java
description: Lär dig hur du renderar arraydata till en enda cell med hjälp av attributen `arrayassingle` och `arraydelimiter` för Smart Marker i Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, Smart Markers, arrayassingle, arraydelimiter, array i en enda cell, arrayrendering, mall
type: docs
weight: 195
url: /sv/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kan rendera en array som datakälla till en enda cell med Smart Markers. Attributet `arrayassingle` inaktiverar standardbeteendet där elementen sprids ett i taget, och attributet `arraydelimiter` anger avgränsaren mellan de sammanfogade elementen – en komma som standard, eller ett valfritt enskilt tecken eller en sträng med flera tecken i citattecken som du anger.
{{% /alert %}}

## **Introduktion**
Smart Markers i Aspose.Cells är en mallbaserad funktion som via marköruttryck som `&=DataSource.Field` dynamiskt fyller kalkylblad med data. Markören placeras i en arbetsbok för design. När mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.

Som standard expanderar motorn arrayen när en Smart Marker refererar till ett arrayfält, till exempel `&=Product.Tags` som är bundet till en array med fyra värden. Varje element placeras då i sin egen cell, så att värdena sprids lodrätt nedåt i kolumnen under markören. Det här beteendet är praktiskt i många sammanhang, men i vissa situationer är det bättre att rendera hela arrayen till en enda cell och sammanfoga elementen med en avgränsare som du väljer.

Attributen `arrayassingle` och `arraydelimiter`, som skrivs inom parenteserna i en Smart Marker i formatet `name:value`, tar precis hand om det här behovet. De gör att du kan hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar direkt med arraydatakällor.

## **Varför den här funktionen behövs**

### **Standardbeteende vid spridning av arrayer**
När en Smart Marker refererar till ett arrayfält expanderar Aspose.Cells som standard arrayen över flera celler. En markör som `&=Product.Tags`, kopplad till en array med fyra värden, placerar exempelvis varje värde i sin egen cell under markören, vilket förskjuter annat mallinnehåll och kan bryta noggrant utformade rapportlayouter.

### **Begränsningar i användningsfall**
Det finns många praktiska situationer där standardspridningen är olämplig:
- **Sammanfattningsrapporter** som kräver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade värden eller värden åtskilda med ett vertikalstreck i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för att förbättra läsbarheten.
- **Nedströmsflöden** (CSV-export, PDF-rendering och sammanslagning av brev) som förväntar sig ett enda samlat värde per cell i stället för ett expanderat intervall.
- **Kompatibilitet mellan plattformar**, där vissa mottagare inte kan hantera arrayer som sprids över flera celler.

### **Luckan som den fyller**
Utan en inbyggd mekanism skulle utvecklare behöva förbehandla data i JavaScript – sammanfoga arrayer till strängar med avgränsare innan de kopplas till `WorkbookDesigner`. Detta duplicerar logiken, komplicerar datamodellerna och ökar risken för fel. Attributen `arrayassingle` och `arraydelimiter` eliminerar behovet av denna lösning genom att hantera formateringen deklarativt i Smart Marker-taggen.

## **Fördelar med funktionen**
Att använda attributen `arrayassingle` och `arraydelimiter` i dina Smart Markers ger flera fördelar:
- **Innehåll i en enda cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Kontroll av avgränsare**: Ange den avgränsare du vill använda – en komma, ett semikolon, en bindestreck, ett vertikalstreck eller en sträng med flera tecken i citattecken, till exempel `" | "`.
- **Mallstyrd formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsreglerna anges i Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre intilliggande mallinnehåll till andra rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängarrayer som tillhandahålls som JSON-rader, inklusive numeriska värden som återges som strängar.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera utan ändringar.

## **Så använder du den här funktionen**

### **Syntax för Smart Marker**
Attributen `arrayassingle` och `arraydelimiter` följer den attributgrammatik som Aspose.Cells använder, i formatet `name:value`, inom parenteserna i en vanlig Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Markören består av följande delar:
- `&=DataSource.ArrayField` – den vanliga Smart Marker som refererar till arrayfältet i den bundna datakällan.
- `arrayassingle:true` – instruerar motorn att rendera hela arrayen till en enda cell i stället för att sprida elementen.
- `arraydelimiter:;` – valfritt; anger avgränsaren mellan arrayelementen. När den utelämnas används ett komma.

{{% alert color="warning" %}}
Skriv attribut i formatet `name:value` (ett kolon, inte ett likhetstecken) och separera flera attribut med ett komma **utan mellanrum**. Ett mellanrum efter kommat gör att det tolkade värdet förskjuts ett tecken – `(arrayassingle:true, arraydelimiter:;)` skulle använda den felaktiga avgränsaren `:;` i stället för `;`.
{{% /alert %}}

### **Former för avgränsare**
- Ett enskilt tecken skrivs direkt efter kolonet: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- En avgränsare med flera tecken skrivs i dubbla citattecken: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Arbetsflöde steg för steg**
Det följande arbetsflödet beskriver hur du renderar en array till en enda cell med Smart Markers.
1. **Förbered datakällan**: Lägg upp varje post som ett JSON-objekt där ett fält innehåller en array, till exempel `{"Tags": ["C#", "Aspose"]}`. Vanliga JavaScript-objekt och arrayer som skickas till `setDataSource` binds inte på den här plattformen – JSON-rader är det tabellformat som stöds.
2. **Skapa en arbetsbok för design**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en cell med en Smart Marker som refererar till arrayfältet och har attributet `arrayassingle`. Lägg även till `arraydelimiter` när en anpassad avgränsare behövs.
3. **Instantiera `WorkbookDesigner`**: Skapa en `WorkbookDesigner` för arbetsboken och koppla dina JSON-rader med `setJsonDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `workbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med verkliga data.
5. **Spara resultatet**: Spara den resulterande arbetsboken på disk i XLSX eller ett annat filformat som stöds.

### **Kodexempel 1 – Grundläggande rendering av en strängarray**

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

Exemplet skriver ut det sammanfogade värdet av hela arrayen. De fyra taggarna placeras i en cell och åtskils med standardkomman:

```
C#,Aspose,SmartMarker,Excel
```

### **Kodexempel 2 – Numeriska värden med en anpassad avgränsare**

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

När poängen tillhandahålls som JSON-strängar visas talen i det sammanfogade resultatet utan decimaler:

```
95-88-76-100-67
```

{{% alert color="note" %}}
JSON-tal som behandlas av Java-motorn kommer fram som dubbelvärden, så `[95, 88]` skulle sammanfogas till `95.0-88.0`. Sätt citattecken runt talen i JSON-raderna när du vill att de sammanfogade värdena ska visas som exakta heltal.
{{% /alert %}}

### **Kodexempel 3 – Jämförelse av standardrendering och rendering i en enda cell**

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

Standardmarkören placerar ett element i varje cell nedåt i kolumn B, medan `arrayassingle`-markören sammanfogar samma array till en enda cell i kolumn C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Anteckningar och bästa praxis**
Beakta följande punkter när du arbetar med attributen `arrayassingle` och `arraydelimiter`:
- Attributvärden anges i formatet `name:value`. En form med likhetstecken, såsom `arrayassingle=true`, känns inte igen och återgår tyst till standardbeteendet för spridning.
- Separera attribut med ett komma utan mellanrum; ett mellanrum efter kommat gör att det tolkade avgränsarvärdet förskjuts ett tecken (se varningen ovan).
- Värdet för `arraydelimiter` kan vara ett enskilt tecken som skrivs direkt efter kolonet eller en sträng med flera tecken i dubbla citattecken.
- När `arraydelimiter` utelämnas åtskils elementen med ett komma.
- Använd radobjekt med `setJsonDataSource` för arrayfält; vanliga JavaScript-objekt och arrayer som skickas till `setDataSource` binds inte på den här plattformen.
- JSON-tal kommer fram som dubbelvärden via Java-motorn (`95` sammanfogas som `95.0`); sätt citattecken runt numeriska värden i JSON-raderna när du vill att heltalen ska visas exakt.
- Placera en Smart Marker i en cell som är tillräckligt bred för att visa den resulterande sammanfogade strängen; annars kan innehållet, beroende på formateringen, visas i angränsande celler.

## Relaterade artiklar
- [Lägg till filterfält i en pivottabell i Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/add-page-field-in-pivot-table/)
- [Tillämpa format på pivottabeller i Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/apply-style-to-pivot-table/)
- [Ändra layouten för sidfält i en pivottabell](/cells/sv/nodejs-java/change-page-field-layout/)
- [Konvertera en sparkline till bild och HTML i Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}