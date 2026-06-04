---
title: Läsa och skriva DBF-filer
description: Aspose.Cells for Node.js via C++ är ett bibliotek för att arbeta med kalkylbladsfiler, vilket stöder läsning och skrivning av dBASE III och IV (DBF)-filer. Denna artikel förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive detaljer om filformat, stödda funktioner och steg-för-steg-exempel.
keywords: Aspose.Cells, Node.js via C++, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /sv/nodejs-cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder fullt stöd för att läsa och skriva DBF (dBASE)-filer. Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera datan med hjälp av det omfattande Aspose.Cells-API:et, och spara arbetsboken tillbaka till DBF-formatet för användning med äldre databasapplikationer.

{{% /alert %}}

## **Introduktion**

DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande i stor utsträckning inom många branscher för att lagra strukturerad data, särskilt inom redovisning, GIS och andra specialiserade applikationer. Aspose.Cells låter dig integrera dessa äldre filer i moderna Node.js via C++ kalkylbladsarbetsflöden sömlöst.

Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:

- Importera data från befintliga DBF-filer till Aspose.Cells Workbook-objekt för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylbladsformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-formatet.

DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsapplikationer, vilket gör dem till en praktisk brygga mellan äldre system och moderna kalkylbladsverktyg.

## **Stödda DBF-versioner och funktioner**

Aspose.Cells stöder följande DBF-formatversioner:

- **dBASE III** — Den ursprungliga och mest spridda varianten av DBF-formatet.
- **dBASE IV** — En utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Stödda funktioner

Biblioteket erbjuder omfattande stöd för följande operationer:

- Läsa DBF-data till ett Workbook-objekt, med alla poster och fältdefinitioner bevarade.
- Skriva arbetsboksdata tillbaka till DBF-format för export till dBASE-kompatibla applikationer.
- Hantera vanliga datatyper som används i DBF-filer, inklusive tecken-, numeriska-, datum- och logiska fält.
- Bevara fältdefinitioner såsom fältnamn, typ och längd under läs-/skrivoperationer.

### Begränsningar och överväganden

När du arbetar med DBF-filer bör du tänka på följande begränsningar:

- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 bytes**.
- Fältnamn är begränsade till **10 tecken**, måste vara versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodning kan variera beroende på källapplikationen (vanligtvis Windows-1252 eller OEM-kodtabeller).

## **Läsa en DBF-fil**

Aspose.Cells gör det enkelt att läsa in data från en DBF-fil till ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att datan tolkas korrekt under inläsningsprocessen.

### Läsa en DBF-fil med Aspose.Cells

För att läsa en DBF-fil behöver du skapa en `LoadOptions`-instans, ange dess `LoadFormat`-egenskap till `LoadFormat.Dbf`, och skicka den till `Workbook`-konstruktören tillsammans med filsökvägen. När den är inläst blir datan tillgänglig via `Worksheets`-samlingen, där du kan iterera genom celler, extrahera värden eller manipulera datan efter behov.

Följande exempel visar hur man läser in en befintlig DBF-fil i Aspose.Cells, kommer åt dess första kalkylblad och läser cellvärdena.

```javascript
let sb = "";

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

for (let i = 0; i <= maxRow; i++)
{
    for (let j = 0; j <= maxCol; j++)
    {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        sb += "|" + value;
    }
    sb += "|" + "\n";
}

console.log(sb);

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel kommer att behandla DBF-filen som ett kalkylblad och visa dess poster i en tabelllayout. Detta är användbart för att snabbt verifiera datan efter att ha läst eller skrivit den med Aspose.Cells.

{{% /alert %}}

## **Skriva en DBF-fil**

Att skriva data till en DBF-fil följer ett liknande mönster som att spara något annat kalkylbladsformat med Aspose.Cells. Du skapar eller läser in en Workbook, fyller kalkylbladet med data, och anropar sedan `save`-metoden medan du anger `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells

För att skapa en DBF-fil, följ dessa steg:

1. Skapa en ny `Workbook`-instans.
2. Hämta det första kalkylbladet från `Worksheets`-samlingen.
3. Fyll kalkylbladet med din data, inklusive rubriker i den första raden och poster i efterföljande rader.
4. Anropa `workbook.save`-metoden, och skicka filsökvägen och `SaveFormat.Dbf` som parametrar.

Följande exempel visar hur man skapar en ny DBF-fil från grunden. Det fyller ett kalkylblad med exempeldata som innehåller olika datatyper (strängar, tal och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");
const fs = require("fs");

const outputDir = "C:\\Output\\";
const filePath = path.join(outputDir, "output.dbf");

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Kolumnrubriker
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// Datrad 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));

// Datrad 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));

// Datrad 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));

// Datrad 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));

// Datrad 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));

// Ställ in kolumnbredder för bättre läsbarhet
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}

När du skriver data till en DBF-fil, se till att din data följer formatets begränsningar. Fältnamn bör inte vara längre än 10 tecken och bör inte innehålla mellanslag. Poster som överstiger 4000 bytes totalt kommer inte att sparas korrekt. Datum bör vara giltiga datumvärden som kan representeras i formatet YYYYMMDD.

{{% /alert %}}

## **Överväganden för datatyper och formatering**

Vid överföring av data mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyper mappas mellan de två systemen för att säkerställa dataintegritet.

### Celltyper till DBF-fälttyper

Aspose.Cells cellvärden konverteras automatiskt till lämpliga DBF-fälttyper vid sparande:

- **Strängar** mappas till teckenfält (C).
- **Numeriska värden** (heltal och decimaler) mappas till numeriska fält (N).
- **Datumvärden** mappas till datumfält (D) i formatet `YYYYMMDD`.
- **Booleska värden** mappas till logiska fält (L).

### Kodning

DBF-filer kan använda olika teckenkodningar beroende på applikationen som skapade dem. Aspose.Cells hanterar kodning transparent i de flesta fall, men om du stöter på problem med teckenvisning kan du behöva verifiera kodningen av källfilen.

### Regler för fältnamn

DBF-fältnamn måste följa följande regler:

- Maximal längd på 10 tecken.
- Måste börja med en bokstav.
- Får inte innehålla mellanslag eller specialtecken.
- Lagras som versaler oavsett vilken skiftläge som användes vid inmatning.

### Verifiera utdata

Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller någon dBASE-kompatibel applikation. Datan bör visas i en tabelllayout med fältnamnen som kolumnrubriker, och posterna ifyllda enligt den data du angav.

## **Konvertera mellan DBF och andra format**

Ett av de mest praktiska användningsområdena för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylbladsformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett brett utbud av format kan du enkelt läsa in en DBF-fil och spara om den i vilket annat format som helst som stöds, eller vice versa.

Du kan till exempel läsa en DBF-fil, tillämpa formatering eller beräkningar med Aspose.Cells-API:et, och sedan spara resultatet som en XLSX-fil för distribution till användare som arbetar med moderna kalkylbladsapplikationer. Omvänt kan du hämta data från en XLSX- eller CSV-fil och exportera den till DBF-format för integration med äldre system.



{{< app/cells/assistant language="javascript" >}}