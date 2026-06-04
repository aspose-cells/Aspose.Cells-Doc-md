---
title: Läsa och skriva DBF-filer
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylbladsfiler, vilket stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive information om filformat, funktioner som stöds och steg-för-steg-exempel.
keywords: Aspose.Cells, .NET library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf
type: docs
weight: 200
url: /sv/net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder fullständigt stöd för läsning och skrivning av DBF-filer (dBASE). Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, manipulera data med hjälp av det omfattande Aspose.Cells-API:et, och spara arbetsboken tillbaka till DBF-formatet för användning med äldre databasprogram.

{{% /alert %}}

## **Introduktion**

DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande i stor utsträckning inom många branscher för lagring av strukturerad data, särskilt inom redovisning, GIS och andra specialiserade tillämpningar. Aspose.Cells låter dig sömlöst integrera dessa äldre filer i moderna .NET-kalkylbladsarbetsflöden.

Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:

- Importera data från befintliga DBF-filer till Aspose.Cells Workbook-objekt för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylbladsformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-formatet.

DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsprogram, vilket gör dem till en bekväm brygga mellan äldre system och moderna kalkylbladsverktyg.

## **DBF-versioner och funktioner som stöds**

Aspose.Cells stöder följande DBF-formatversioner:

- **dBASE III** — Den ursprungliga och mest stödda varianten av DBF-formatet.
- **dBASE IV** — En utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Funktioner som stöds

Biblioteket erbjuder omfattande stöd för följande operationer:

- Läsa DBF-data till ett Workbook-objekt, där alla poster och fältdefinitioner bevaras.
- Skriva arbetsboksdata tillbaka till DBF-format för export till dBASE-kompatibla program.
- Hantera vanliga datatyper som används i DBF-filer, inklusive tecken-, numeriska-, datum- och logiska fält.
- Bevara fältdefinitioner som fältnamn, typ och längd vid läsning/skrivning.

### Begränsningar och överväganden

Tänk på följande begränsningar när du arbetar med DBF-filer:

- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste vara versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodning kan variera beroende på källprogrammet (vanligtvis Windows-1252 eller OEM-kodtabeller).

## **Läsa en DBF-fil**

Aspose.Cells gör det enkelt att läsa in data från en DBF-fil till ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt under inläsningen.

### Läsa en DBF-fil med Aspose.Cells

För att läsa en DBF-fil behöver du skapa en `LoadOptions`-instans, ange egenskapen `LoadFormat` till `LoadFormat.Dbf` och skicka den till `Workbook`-konstruktören tillsammans med filsökvägen. När data har lästs in blir de åtkomliga via samlingen `Worksheets`, där du kan iterera genom celler, extrahera värden eller manipulera data efter behov.

Följande exempel visar hur man läsa in en befintlig DBF-fil i Aspose.Cells, komma åt det första kalkylbladet och läsa cellvärdena.

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;

string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");

LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.Worksheets[0];

Cells cells = worksheet.Cells;

StringBuilder sb = new StringBuilder();

int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}

Console.WriteLine(sb.ToString());

string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);

Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel behandlar DBF-filen som ett kalkylblad och visar dess poster i en tabellayout. Detta är användbart för att snabbt verifiera data efter att ha läst eller skrivit den med Aspose.Cells.

{{% /alert %}}

## **Skriva en DBF-fil**

Att skriva data till en DBF-fil följer ett liknande mönster som att spara i vilket annat kalkylbladsformat som helst med Aspose.Cells. Du skapar eller läser in en Workbook, fyller kalkylbladet med data och anropar sedan metoden `Save` med `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells

Följ dessa steg för att skapa en DBF-fil:

1. Skapa en ny `Workbook`-instans.
2. Hämta det första kalkylbladet från samlingen `Worksheets`.
3. Fyll kalkylbladet med din data, inklusive rubriker på den första raden och poster på efterföljande rader.
4. Anropa metoden `Workbook.Save` med filsökvägen och `SaveFormat.Dbf` som parametrar.

Följande exempel visar hur man skapar en ny DBF-fil från grunden. Det fyller ett kalkylblad med exempeldata som innehåller olika datatyper (strängar, tal och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

```csharp
using System;
using System.IO;
using Aspose.Cells;

string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");

if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;

// Kolumnrubriker
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");

// Datarad 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));

// Datarad 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));

// Datarad 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));

// Datarad 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));

// Datarad 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));

// Ställ in kolumnbredder för bättre läsbarhet
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

När du skriver data till en DBF-fil ska du se till att dina data följer formatets begränsningar. Fältnamn bör inte vara längre än 10 tecken och får inte innehålla mellanslag. Poster som överstiger 4000 byte totalt kommer inte att sparas korrekt. Datum bör vara giltiga datumvärden som kan representeras i formatet YYYYMMDD.

{{% /alert %}}

## **Överväganden om datatyper och formatering**

När data överförs mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyper mappas mellan de två systemen för att säkerställa dataintegritet.

### Celltyper till DBF-fälttyper

Aspose.Cells cellvärden konverteras automatiskt till lämpliga DBF-fälttyper vid sparande:

- **Strängar** mappas till teckenfält (C).
- **Numeriska värden** (heltal och decimaler) mappas till numeriska fält (N).
- **Datumvärden** mappas till datumfält (D) i formatet `YYYYMMDD`.
- **Booleska värden** mappas till logiska fält (L).

### Teckenkodning

DBF-filer kan använda olika teckenkodningar beroende på programmet som skapade dem. Aspose.Cells hanterar teckenkodning transparent i de flesta fall, men om du stöter på problem med teckenvisningen kan du behöva verifiera källfilens teckenkodning.

### Regler för fältnamn

DBF-fältnamn måste följa följande regler:

- Maximal längd på 10 tecken.
- Måste börja med en bokstav.
- Får inte innehålla mellanslag eller specialtecken.
- Lagras som versaler oavsett skiftläge som används vid inmatning.

### Verifiera utdata

Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller annat dBASE-kompatibelt program. Data ska visas i en tabellayout med fältnamnen som kolumnrubriker, och posterna ifyllda enligt den data du angav.

## **Konvertera mellan DBF och andra format**

Ett av de mest praktiska användningsfallen för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylbladsformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett brett utbud av format kan du enkelt läsa in en DBF-fil och spara om den i valfritt annat format som stöds, eller vice versa.

Du kan till exempel läsa en DBF-fil, tillämpa formatering eller beräkningar med hjälp av Aspose.Cells-API:et och sedan spara resultatet som en XLSX-fil för distribution till användare som arbetar med moderna kalkylbladsprogram. Omvänt kan du ta data från en XLSX- eller CSV-fil och exportera den till DBF-format för integration med äldre system.



{{< app/cells/assistant language="csharp" >}}