---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells for Node.js via C++
description: Lär dig hur du renderar arraydata i en enda cell med attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, Node.js library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
url: /sv/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells stöder rendering av arraydata i en enda cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur arrayelement separeras inom en enda cell, vilket ger flexibel formatering för rapporter och mallar.

{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla kalkylbladsdata med marköruttryck som `&=DataSource.Field`. Markören placeras i en designarbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.

Som standard, när en Smart Marker refererar till en arrayegenskap (till exempel `&=DataSource.Numbers`), expanderar motorn arrayen och placerar varje element i en separat intilliggande cell — antingen horisontellt över en rad eller vertikalt nedför en kolumn. Även om detta beteende är bekvämt i många scenarier finns det situationer där du skulle föredra att rendera hela arrayen i en enda cell, med elementen sammanfogade och separerade med en avgränsare du väljer.

Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inuti en Smart Marker-tagg, uppfyller exakt detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar naturligt med arraydatakällor.

## **Varför denna funktion behövs**

### **Standardbeteende för arrayspridning**

När en Smart Marker refererar till en arrayegenskap expanderar Aspose.Cells arrayen över flera celler som standard. Till exempel kommer en markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden att placera varje värde i sin egen cell, vilket skjuter ut annat mallinnehåll och potentiellt bryter noggrant utformade rapportlayouter.

### **Begränsningar i användningsfall**

Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:

- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller pipe-separerade värden inom en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, dokumentkoppling) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformskompatibilitet**, där vissa konsumenter inte tolererar arrayer som sprider sig över flera celler.

### **Glappet det fyller**

Utan en inbyggd mekanism skulle utvecklare tvingas förbehandla data i JavaScript — sammanfoga arrayer till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt inuti själva Smart Markern.

## **Funktionsfördelar**

Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:

- **Encellinneslutning**: Alla arrayelement renderas i exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange valfri separatorsträng du vill — komma, semikolon, bindestreck, pipe, nyrad eller annan anpassad text.
- **Malldriven formatering**: Ingen ytterligare kod krävs för att förbehandla datan; formateringsregler finns inuti Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre ut intilliggande mallinnehåll till olika rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, nummer, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **Hur man använder denna funktion**

### **Smart Marker-syntax**

Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en standard Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören är sammansatt av följande delar:

- `&=DataSource.ArrayProperty` — den standard Smart Marker som refererar till arrayegenskapen på den bundna datakällan.
- `arrayasSingle=true` — instruerar motorn att rendera hela arrayen i en enda cell. Endast värdet `true` utlöser encellsbeteendet.
- `extraDelimiter=", "` — definierar separatorn som placeras mellan arrayelement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken eller en sträng med flera tecken.

{{% alert color="primary" %}}

Attributet `extraDelimiter` accepterar valfri strängliteral, inklusive avgränsare med flera tecken, anpassad text eller escape-sekvenser som `\n` för nyradsseparerad utdata. Om arrayen är tom lämnas den resulterande cellen tom.

{{% /alert %}}

### **Steg-för-steg-arbetsflöde**

Följande arbetsflöde beskriver hur man renderar en array i en enda cell med Smart Markers.

1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en array. Egenskapen kan returnera `string[]`, `int[]` eller annan arraytyp som stöds.
2. **Skapa en designarbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smart Marker-cell som refererar till arrayegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, bifoga designarbetsboken till det och bind din datakälla med metoden `setDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `workbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med riktig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller annat filformat som stöds.

### **Kodexempel 1 — Grundläggande strängarray-rendering**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Kodexempel 2 — Numerisk array med anpassad avgränsare**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **Kodexempel 3 — Jämförelse av standard- vs. ArrayAsSingle-beteende**

```javascript
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Sektion 1: Standard Smart Marker - värden sprids horisontellt över celler
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// Sektion 2: Ny encellrendering med arrayasSingle och extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// Bind datakällan och bearbeta Smart Markers
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// Spara den resulterande arbetsboken
workbook.save("output_comparison.xlsx");
```

### **Anteckningar och bästa praxis**

Tänk på följande punkter när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:

- Värdet `extraDelimiter` behandlas som en strängliteral; escape:a alla specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett booleskt värde (`true` / `false`). Endast `true` utlöser encellsbeteendet; alla andra värden faller tillbaka till standardspridningsbeteendet.
- Om arrayen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatypen).
- Funktionen fungerar med objektdatakällor såväl som `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i arrayer.
- För nyradsseparerad utdata kan du använda `\n` eller `os.EOL` som avgränsarvärde.
- Placera Smart Markern i en cell som har tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spilla över i intilliggande celler beroende på formatet.

## **Relaterade artiklar**

- [Slå ihop och dela celler](/cells/sv/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}