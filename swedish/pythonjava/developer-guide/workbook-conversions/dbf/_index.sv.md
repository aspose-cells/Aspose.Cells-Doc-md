---
title: Läsa och skriva DBF-filer
linktitle: Läsa och skriva
description: Aspose.Cells är ett Python via Java-bibliotek för att arbeta med kalkylbladsfiler, vilket stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive filformatdetaljer, stödda funktioner och steg-för-steg-exempel.
keywords: Aspose.Cells, Python via Java-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /sv/python-java/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder fullständigt stöd för att läsa och skriva DBF (dBASE)-filer. Du kan ladda befintliga dBASE III- och dBASE IV-filer till ett Workbook-objekt, manipulera data med hjälp av det rika Aspose.Cells-API:et och spara arbetsboken tillbaka till DBF-formatet för användning med äldre databasapplikationer.

{{% /alert %}}

## **Introduktion**

DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande i stor utsträckning inom många branscher för att lagra strukturerad data, särskilt inom redovisning, GIS och andra specialiserade applikationer. Aspose.Cells låter dig integrera dessa äldre filer i moderna Python via Java-kalkylbladsarbetsflöden sömlöst.

Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:

- Importera data från befintliga DBF-filer till Aspose.Cells Workbook-objekt för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylbladsformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer när data överförs till och från DBF-formatet.

DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsapplikationer, vilket gör dem till en bekväm brygga mellan äldre system och moderna kalkylbladsverktyg.

## **Stödda DBF-versioner och funktioner**

Aspose.Cells stöder följande DBF-formatversioner:

- **dBASE III** — Den ursprungliga och mest spridda varianten av DBF-formatet.
- **dBASE IV** — En utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Stödda funktioner

Biblioteket erbjuder omfattande stöd för följande operationer:

- Läsa DBF-data till ett Workbook-objekt, med alla poster och fältdefinitioner bevarade.
- Skriva arbetsboksdata tillbaka till DBF-format för export till dBASE-kompatibla applikationer.
- Hantera vanliga datatyper som används i DBF-filer, inklusive tecken-, numeriska-, datum- och logiska fält.
- Bevara fältdefinitioner som fältnamn, typ och längd under läs-/skrivoperationer.

### Begränsningar och överväganden

Tänk på följande begränsningar när du arbetar med DBF-filer:

- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste vara versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodning kan variera beroende på källapplikationen (vanligtvis Windows-1252 eller OEM-kodsidor).

## **Läsa en DBF-fil**

Aspose.Cells gör det enkelt att ladda data från en DBF-fil till ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt under laddningsprocessen.

### Läsa en DBF-fil med Aspose.Cells

För att läsa en DBF-fil måste du skapa en `LoadOptions`-instans, ställa in dess `LoadFormat`-egenskap till `LoadFormat.Dbf` och skicka den till `Workbook`-konstruktören tillsammans med filsökvägen. När den väl är laddad blir data åtkomlig via `Worksheets`-samlingen, där du kan iterera genom celler, extrahera värden eller manipulera data efter behov.

Följande exempel visar hur man laddar en befintlig DBF-fil i Aspose.Cells, kommer åt dess första kalkylblad och läser cellvärdena.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat

dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")

loadOptions = LoadOptions(LoadFormat.Dbf)

workbook = Workbook(filePath, loadOptions)

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

sb = []

maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()

for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")

print("".join(sb))

outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.Xlsx)

print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel kommer att behandla DBF-filen som ett kalkylblad och visa dess poster i en tabelllayout. Detta är användbart för att snabbt verifiera data efter att ha läst eller skrivit den med Aspose.Cells.

{{% /alert %}}

## **Skriva en DBF-fil**

Att skriva data till en DBF-fil följer ett liknande mönster som att spara andra kalkylbladsformat med Aspose.Cells. Du skapar eller laddar en Workbook, fyller kalkylbladet med data och anropar sedan `Save`-metoden medan du anger `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells

För att skapa en DBF-fil, följ dessa steg:

1. Skapa en ny `Workbook`-instans.
2. Hämta det första kalkylbladet från `Worksheets`-samlingen.
3. Fyll kalkylbladet med din data, inklusive rubriker i den första raden och poster i efterföljande rader.
4. Anropa metoden `Workbook.save` och skicka filsökvägen och `SaveFormat.Dbf` som parametrar.

Följande exempel visar hur man skapar en ny DBF-fil från grunden. Det fyller ett kalkylblad med exempeldata som innehåller olika datatyper (strängar, tal och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju

outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Kolumnrubriker
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")

# Datrad 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))

# Datrad 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))

# Datrad 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))

# Datrad 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))

# Datrad 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))

# Ställ in kolumnbredder för bättre läsbarhet
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)

workbook.save(filePath, SaveFormat.DBf)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

När du skriver data till en DBF-fil, se till att din data följer formatets begränsningar. Fältnamn bör inte vara längre än 10 tecken och bör inte innehålla mellanslag. Poster som överstiger 4000 byte totalt kommer inte att sparas korrekt. Datum bör vara giltiga datumvärden som kan representeras i formatet YYYYMMDD.

{{% /alert %}}

## **Överväganden för datatyp och formatering**

När data överförs mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyper mappas mellan de två systemen för att säkerställa dataintegritet.

### Celltyper till DBF-fälttyper

Aspose.Cells-cellvärden konverteras automatiskt till lämpliga DBF-fälttyper vid sparning:

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
- Lagras som versaler oavsett skiftläge som använts i indata.

### Verifiera utdata

Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller någon dBASE-kompatibel applikation. Datan bör visas i en tabelllayout med fältnamnen som kolumnrubriker, och posterna ifyllda enligt den data du angav.

## **Konvertera mellan DBF och andra format**

Ett av de mest praktiska användningsfallen för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylbladsformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett brett utbud av format kan du enkelt ladda en DBF-fil och spara om den i vilket annat stött format som helst, eller vice versa.

Du kan till exempel läsa en DBF-fil, tillämpa formatering eller beräkningar med Aspose.Cells-API:et och sedan spara resultatet som en XLSX-fil för distribution till användare som arbetar med moderna kalkylbladsapplikationer. Omvänt kan du ta data från en XLSX- eller CSV-fil och exportera den till DBF-format för integration med äldre system.



{{< app/cells/assistant language="python" >}}