---
title: SmartMarker – rendering av arraydata i en enda cell | Aspose.Cells for JavaScript via C++
description: Lär dig hur du renderar arraydata till en enda cell med hjälp av attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for JavaScript via C++.
linktitle: SmartMarker – rendering av arraydata i en enda cell | Aspose.Cells
url: /sv/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, array i en enda cell, arrayrendering, mall
type: docs
weight: 195
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder rendering av arraydata till en enda cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur arrayelementen skiljs åt inom en enda cell, vilket ger flexibel formatering för rapporter och mallar.
{{% /alert %}}

## **Introduktion**
Smart Markers i Aspose.Cells är en kraftfull mallbaserad funktion som låter dig fylla kalkylbladsdata dynamiskt med hjälp av markörexpressioner som `&=DataSource.Field`. Markören placeras i en designarbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.
Som standard expanderar motorn arrayen och placerar varje element i en separat intilliggande cell – antingen horisontellt längs en rad eller vertikalt nedåt i en kolumn – när en Smart Marker refererar till en arrayegenskap (t.ex. `&=DataSource.Numbers`). Det här beteendet är praktiskt i många scenarier, men ibland är det bättre att rendera hela arrayen till en enda cell, där elementen sammanfogas och separeras med en avgränsare som du väljer.
Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inuti en Smart Marker-tag, tillgodoser exakt detta behov. Med dem kan du hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar direkt med arraydatakällor.

## **Varför den här funktionen behövs**

### **Standardbeteende för arrayutbredning**
När en Smart Marker refererar till en arrayegenskap expanderar Aspose.Cells som standard arrayen över flera celler. En markör som `&=Product.Tags` som tillämpas på en array med fyra strängar placerar exempelvis varje värde i sin egen cell, vilket flyttar annat mallinnehåll utåt och potentiellt bryter omsorgsfullt utformade rapportlayouter.

### **Begränsningar för användningsfall**
Det finns många praktiska scenarier där standardbeteendet för spridning är olämpligt:
- **Sammanfattningsrapporter** som kräver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade värden eller värden separerade med pipe-tecken inom en enda cell.
- **Filteretiketter eller statusindikatorer** som grupperar flera värden på ett ställe för att förbättra läsbarheten.
- **Nedströmspipelines** (CSV-export, PDF-rendering och massutskick) som förväntar sig ett enda konsoliderat värde per cell i stället för ett expanderat intervall.
- **Kompatibilitet mellan plattformar**, där vissa konsumenter inte kan hantera arrayer som sprids över flera celler.

### **Luckan som den fyller**
Utan en inbyggd mekanism skulle utvecklare behöva förbehandla data i JavaScript – sammanfoga arrayer till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna omvägning genom att hantera formateringen deklarativt inuti själva Smart Marker.

## **Funktionens fördelar**
Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:
- **Inneslutning i en enda cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouterna kompakta och förutsägbara.
- **Styrning av avgränsare**: Ange valfri avgränsningssträng – komma, semikolon, bindestreck, pipe-tecken, nyckelrad eller egen text.
- **Mallstyrd formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsreglerna ligger i Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre intilliggande mallinnehåll till andra rader eller kolumner.
- **Flexibla datatyper**: Fungerar med strängar, tal, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrade.

## **Så använder du funktionen**

### **Syntax för Smart Marker**
Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värdepar inom parenteserna i en vanlig Smart Marker. Den allmänna syntaxen är:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Markören består av följande delar:
- `&=DataSource.ArrayProperty` – den vanliga Smart Marker som refererar till arrayegenskapen i den bundna datakällan.
- `arrayasSingle=true` – instruerar motorn att rendera hela arrayen till en enda cell. Endast värdet `true` utlöser beteendet för en enda cell.
- `extraDelimiter=", "` – anger avgränsaren som placeras mellan arrayelementen. Värdet är en strängliteral; det kan vara tomt, ett tecken eller en sträng med flera tecken.

{{% alert color="primary" %}}
Attributet `extraDelimiter` accepterar valfri strängliteral, inklusive avgränsare med flera tecken, egen text eller escape-sekvenser som `\n` för utdata med nyckelradseparerade värden. Om arrayen är tom lämnas den resulterande cellen tom.
{{% /alert %}}

### **Steg-för-steg-arbetsflöde**
Arbetsflödet nedan beskriver hur du renderar en array till en enda cell med Smart Markers.
1. **Förbered datakällan**: Skapa ett objekt (eller en datastruktur) som exponerar en egenskap som returnerar en array. Egenskapen kan returnera en array med strängar, tal eller andra typer av värden som stöds.
2. **Skapa en designarbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en cell med en Smart Marker som refererar till arrayegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instantiera `WorkbookDesigner`**: Skapa ett `WorkbookDesigner`-objekt, koppla designarboken till det och bind datakällan med metoden `setDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `workbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med verkliga data.
5. **Spara resultatet**: Spara den resulterande arbetsboken på disk i XLSX eller i ett annat filformat som stöds.

### **Kodexempel 1 – grundläggande rendering av strängarray**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Kodexempel 2 – numerisk array med anpassad avgränsare**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Section 1: Default Smart Marker - values spread horizontally across cells
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Bind the data source and process Smart Markers
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Save the resulting workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Kodexempel 3 – jämförelse av standardbeteende och ArrayAsSingle-beteende**

### **Anmärkningar och bästa praxis**
Ha följande punkter i åtanke när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:
- Värdet för `extraDelimiter` behandlas som en strängliteral; escape alla specialtecken som mallprocessorn kan tolka.
- Attributet `arrayasSingle` accepterar ett booleskt värde (`true` / `false`). Endast `true` utlöser beteendet för en enda cell; alla andra värden återgår till standardbeteendet för spridning.
- Om arrayen är tom eller null lämnas cellen tom (eller innehåller en tom sträng, beroende på datatypen).
- Funktionen fungerar med både objektdatakällor och tabellariska datakällor där en kolumn kan delas upp i arrayer.
- För utdata med nyckelradseparerade värden använder du `\n` som avgränsarvärde.

## Relaterade artiklar

{{< app/cells/assistant language="javascript-cpp" >}}