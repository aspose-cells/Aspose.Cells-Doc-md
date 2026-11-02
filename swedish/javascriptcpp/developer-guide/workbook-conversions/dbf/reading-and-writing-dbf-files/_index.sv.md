---
title: Läsa och skriva DBF-filer
linktitle: Läsa och skriva DBF-filer
description: Aspose.Cells är ett JavaScript via C++-bibliotek för arbete med kalkylarksfiler, som stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur du importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive detaljer om filformatet, funktioner som stöds och steg-för-steg-exempel.
keywords: Aspose.Cells, JavaScript via C++-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /sv/javascript-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells har fullt stöd för läsning och skrivning av DBF-filer (dBASE). Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett `Workbook`-objekt, manipulera data med hjälp av det funktionsrika API:et i Aspose.Cells och spara arbetsboken tillbaka i DBF-format för användning med äldre databasprogram.
{{% /alert %}}

## **Introduktion**
DBF (databasfil) är ett äldre databasfilformat som introducerades ursprungligen av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande allmänt i många branscher för att lagra strukturerad data, särskilt inom bokföring, GIS och andra specialiserade tillämpningar. Aspose.Cells låter dig sömlöst integrera dessa äldre filer i moderna kalkylarksflöden.
Biblioteket stöder både läsning och skrivning av DBF-filer och ger dig följande möjligheter:
- Importera data från befintliga DBF-filer till `Workbook`-objekt i Aspose.Cells för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att transformera data från andra kalkylarksformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer vid dataöverföring till och från DBF-formatet.
DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylarksapplikationer, vilket gör dem till en bekväm brygga mellan äldre system och moderna kalkylarksverktyg.

## **DBF-versioner och funktioner som stöds**
Aspose.Cells stöder följande versioner av DBF-formatet:
- **dBASE III** – den ursprungliga och mest använda varianten av DBF-formatet.
- **dBASE IV** – en utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Funktioner som stöds
Biblioteket erbjuder omfattande stöd för följande åtgärder:
- Läsa in DBF-data i ett `Workbook`-objekt, med alla poster och fältdefinitioner bevarade.
- Skriva tillbaka arbetsbokens data till DBF-format för export till dBASE-kompatibla applikationer.
- Hantera vanliga datatyper som används i DBF-filer, inklusive teckenfält, numeriska fält, datumfält och logiska fält.
- Bevara fältdefinitioner som fältnamn, typ och längd vid läs- och skrivåtgärder.

### Begränsningar och överväganden
När du arbetar med DBF-filer bör du beakta följande begränsningar:
- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste anges med versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodningen kan variera beroende på programmet som skapade filen (vanligtvis Windows-1252 eller OEM-kodssidor).

## **Läsa en DBF-fil**
Aspose.Cells gör det enkelt att läsa in data från en DBF-fil i ett `Workbook`-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt när de läses in.

### Läsa en DBF-fil med Aspose.Cells
För att läsa en DBF-fil skapar du en `LoadOptions`-instans, anger egenskapen `loadFormat` till `LoadFormat.Dbf` och passerar den till `Workbook`-konstruktorn tillsammans med filsökvägen. När filen har lästs in kan du komma åt data via samlingen `Worksheets`, där du kan iterera genom celler, extrahera värden eller manipulera data efter behov.
Följande exempel visar hur du läser in en befintlig DBF-fil i Aspose.Cells, får åtkomst till det första kalkylbladet och läser cellvärdena.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel behandlar DBF-filen som ett kalkylark och visar dess poster i tabellform. Detta är användbart för att snabbt verifiera data efter läsning eller skrivning med Aspose.Cells.
{{% /alert %}}

## **Skriva en DBF-fil**
Att skriva data till en DBF-fil följer samma mönster som att spara data i något annat kalkylarksformat med Aspose.Cells. Du skapar eller läser in ett `Workbook`-objekt, fyller kalkylbladet med data och anropar sedan metoden `save` samtidigt som du anger `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells
För att skapa en DBF-fil följer du dessa steg:
1. Skapa en ny `Workbook`-instans.
2. Få åtkomst till det första kalkylbladet i samlingen `Worksheets`.
3. Fyll kalkylbladet med data, inklusive rubriker i den första raden och poster i efterföljande rader.
4. Anropa metoden `Workbook.save` och skicka filsökvägen och `SaveFormat.Dbf` som parametrar.
Följande exempel visar hur du skapar en ny DBF-fil från grunden. Exemplet fyller ett kalkylark med exempeldata som innehåller olika datatyper (strängar, tal och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Kolumnrubriker
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // Datarad 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // Datarad 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // Datarad 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // Datarad 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // Datarad 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // Ange kolumnbredder för bättre läsbarhet
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
När du skriver data till en DBF-fil måste du säkerställa att data uppfyller formatets begränsningar. Fältnamn bör vara högst 10 tecken och får inte innehålla mellanslag. Poster som totalt överstiger 4000 byte sparas inte korrekt. Datumvärden bör vara giltiga och kunna representeras i formatet YYYYMMDD.
{{% /alert %}}

## **Överväganden kring datatyper och formatering**
När data överförs mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyperna mappas mellan de två systemen, så att dataintegriteten säkerställs.

### Från celltyper till DBF-fälttyper
Cellvärden i Aspose.Cells konverteras automatiskt till lämpliga DBF-fälttyper vid sparande:
- **Strängar** mappas till teckenfält (C).
- **Numeriska värden** (heltal och decimaltal) mappas till numeriska fält (N).
- **Datumvärden** mappas till datumfält (D) i formatet `YYYYMMDD`.
- **Booleska värden** mappas till logiska fält (L).

### Teckenkodning
DBF-filer kan använda olika teckenkodningar beroende på vilket program som skapade dem. Aspose.Cells hanterar teckenkodningen automatiskt i de flesta fall, men om tecken visas fel kan du behöva kontrollera källfilens teckenkodning.

### Regler för fältnamn
DBF-fältnamn måste följa följande regler:
- Högst 10 tecken.
- Måste börja med en bokstav.
- Får inte innehålla mellanslag eller specialtecken.
- Lagras med versaler oavsett skiftläget i indatavärdena.

### Verifiering av resultatet
Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller någon dBASE-kompatibel applikation. Data bör visas i tabellform, där fältnamnen är kolumnrubriker och posterna visar de data du har angett.

## **Konvertering mellan DBF och andra format**
Ett av de mest praktiska användningsområdena för läsning och skrivning av DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylarksformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett stort antal format kan du enkelt läsa in en DBF-fil och spara om den i ett annat format som stöds, eller omvändt.

{{< app/cells/assistant language="javascript-cpp" >}}