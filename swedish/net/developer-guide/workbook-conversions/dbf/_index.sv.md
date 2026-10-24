---
title: Läsa och skriva DBF-filer
linktitle: Läsa och skriva DBF-filer
description: Aspose.Cells är ett .NET-bibliotek som stöder arbete med kalkylarksfiler samt läsning och skrivning av dBASE III- och dBASE IV-filer (DBF). Den här artikeln förklarar hur du importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive information om filformat, funktioner som stöds och steg-för-steg-exempel.
keywords: Aspose.Cells, .NET-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /sv/net/reading-and-writing-dbf-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells har fullständigt stöd för att läsa och skriva DBF-filer (dBASE). Du kan läsa in befintliga dBASE III- och dBASE IV-filer i ett Workbook-objekt, ändra data med hjälp av det omfattande API:et i Aspose.Cells och spara tillbaka arbetsboken i DBF-format för användning med äldre databasprogram.
{{% /alert %}}

## **Introduktion**
DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande allmänt i många branscher för att lagra strukturerad data, särskilt inom redovisning, GIS och andra specialiserade tillämpningar. Med Aspose.Cells kan du integrera dessa äldre filer sömlöst i moderna .NET-baserade arbetsflöden för kalkylarkshantering.
Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:
- Importera data från befintliga DBF-filer till Workbook-objekt i Aspose.Cells för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylarksformat.
- Behålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-format.
DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylarksprogram, vilket gör dem till en praktisk bro mellan äldre system och moderna kalkylarksverktyg.

## **DBF-versioner och funktioner som stöds**
Aspose.Cells stöder följande versioner av DBF-formatet:
- **dBASE III** – den ursprungliga och mest allmänt stödda varianten av DBF-formatet.
- **dBASE IV** – en utvidgad version som stöder ytterligare datatyper och större fältstorlekar.

### Funktioner som stöds
Biblioteket ger omfattande stöd för följande åtgärder:
- Läsa DBF-data till ett Workbook-objekt, där alla poster och fältdefinitioner bevaras.
- Skriva arbetsboksdata till DBF-format för export till program som är kompatibla med dBASE.
- Hantera vanliga datatyper som används i DBF-filer, inklusive teckenfält, numeriska fält, datumfält och logiska fält.
- Behålla fältdefinitioner såsom fältnamn, typ och längd vid läs- och skrivåtgärder.

### Begränsningar och överväganden
När du arbetar med DBF-filer bör du tänka på följande begränsningar:
- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste anges i versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodningen kan variera beroende på programmet som skapade filen (vanligtvis Windows-1252 eller OEM-kodsidor).

## **Läsa en DBF-fil**
Med Aspose.Cells är det enkelt att läsa in data från en DBF-fil i ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformaten, vilket säkerställer att data tolkas korrekt under inläsningen.

### Läsa en DBF-fil med Aspose.Cells
För att läsa en DBF-fil skapar du en `LoadOptions`-instans, anger egenskapen `LoadFormat` till `LoadFormat.Dbf` och skickar den tillsammans med filsökvägen till `Workbook`-konstruktorn. När filen har lästs in är data tillgängliga via samlingen `Worksheets`, där du kan iterera över celler, hämta värden eller ändra data efter behov.
Följande exempel visar hur du läser in en befintlig DBF-fil med Aspose.Cells, får åtkomst till det första kalkylarket och läser cellvärdena.

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
Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel behandlar DBF-filen som ett kalkylark och visar dess poster i tabellform. Detta är användbart för att snabbt verifiera data efter läsning eller skrivning med Aspose.Cells.
{{% /alert %}}

## **Skriva en DBF-fil**
Att skriva data till en DBF-fil följer samma mönster som att spara data i andra kalkylarksformat med Aspose.Cells. Du skapar eller läser in en Workbook, fyller kalkylarket med data och anropar sedan metoden `Save` med `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells
Följ de här stegen för att skapa en DBF-fil:
1. Skapa en ny `Workbook`-instans.
2. Hämta det första kalkylarket från samlingen `Worksheets`.
3. Fyll kalkylarket med data, inklusive rubriker i den första raden och poster i de efterföljande raderna.
4. Anropa metoden `Workbook.Save` och skicka filsökvägen samt `SaveFormat.Dbf` som parametrar.
Följande exempel visar hur du skapar en ny DBF-fil från grunden. Exemplet fyller ett kalkylark med data som innehåller olika datatyper (strängar, tal och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

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
// Ange kolumnbredder för bättre läsbarhet
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);
workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}
När du skriver data till en DBF-fil måste du se till att data uppfyller formatets begränsningar. Fältnamnen får vara högst 10 tecken långa och får inte innehålla mellanslag. Poster som totalt överstiger 4000 byte sparas inte korrekt. Datumvärdena bör vara giltiga och kunna representeras i formatet YYYYMMDD.
{{% /alert %}}

## **Överväganden om datatyper och formatering**
För att säkerställa att dataintegriteten bevaras är det viktigt att förstå hur datatyperna mappas mellan de två systemen.

### Mappning av celltyper till DBF-fälttyper
Cellvärden i Aspose.Cells konverteras automatiskt till lämpliga DBF-fälttyper vid sparning:
- **Strängar** mappas till teckenfält (C).
- **Numeriska värden** (heltal och decimaltal) mappas till numeriska fält (N).
- **Datumvärden** mappas till datumfält (D) i formatet `YYYYMMDD`.
- **Booleska värden** mappas till logiska fält (L).

### Teckenkodning
DBF-filer kan använda olika teckenkodningar beroende på vilket program som skapade dem. Aspose.Cells hanterar teckenkodningen automatiskt i de flesta fall, men om du får problem med att tecken visas kan du behöva kontrollera källfilens kodning.

### Regler för fältnamn
DBF-fältnamn måste följa följande regler:
- Maximal längd är 10 tecken.
- Måste börja med en bokstav.
- Får inte innehålla mellanslag eller specialtecken.
- Lagras med versaler oavsett om indatan använder versaler eller gemener.

### Verifiera resultatet
När du har skrivit en DBF-fil kan du verifiera resultatet genom att öppna filen i Microsoft Excel eller ett program som är kompatibelt med dBASE. Data bör visas i tabellform, med fältnamnen som kolumnrubriker och posterna ifyllda utifrån de data du har angett.

## **Konvertera mellan DBF och andra format**
Ett av de mest praktiska användningsområdena för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylarksformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett stort antal format kan du enkelt läsa in en DBF-fil och spara om den i ett annat format som stöds, eller omvänt.

{{< app/cells/assistant language="csharp" >}}