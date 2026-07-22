---
title: Läsa och skriva DBF-filer
linktitle: Läsa och skriva
description: Aspose.Cells är ett bibliotek för Python via .NET för att arbeta med kalkylbladsfiler, vilket stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Den här artikeln förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive filformatdetaljer, stödda funktioner och stegvisa exempel.
keywords: Aspose.Cells, Python via .NET-bibliotek, DBF, dBASE, läs DBF, skriv DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /sv/python-net/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells har fullt stöd för att läsa och skriva DBF-filer (dBASE). Du kan ladda befintliga dBASE III- och dBASE IV-filer till ett Workbook-objekt, manipulera data med hjälp av det omfattande Aspose.Cells-API:et och spara arbetsboken tillbaka till DBF-format för användning med äldre databasapplikationer.

{{% /alert %}}

## **Introduktion**

DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande i stor utsträckning inom många branscher för att lagra strukturerad data, särskilt inom redovisning, GIS och andra specialiserade tillämpningar. Aspose.Cells gör att du sömlöst kan integrera dessa äldre filer i moderna Python via .NET-kalkylbladsarbetsflöden.

Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:

- Importera data från befintliga DBF-filer till Aspose.Cells Workbook-objekt för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylbladsformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-formatet.

DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsapplikationer, vilket gör dem till en praktisk brygga mellan äldre system och moderna kalkylbladsverktyg.

## **DBF-versioner och funktioner som stöds**

Aspose.Cells stöder följande versioner av DBF-formatet:

- **dBASE III** — Den ursprungliga och mest allmänt stödda varianten av DBF-formatet.
- **dBASE IV** — En utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Funktioner som stöds

Biblioteket erbjuder omfattande stöd för följande operationer:

- Läsa DBF-data till ett Workbook-objekt, med alla poster och fältdefinitioner bevarade.
- Skriva arbetsboksdata tillbaka till DBF-format för export till dBASE-kompatibla applikationer.
- Hantera vanliga datatyper som används i DBF-filer, inklusive tecken-, numeriska-, datum- och logiska fält.
- Bevara fältdefinitioner såsom fältnamn, typ och längd vid läs/skriv-operationer.

### Begränsningar och överväganden

Tänk på följande begränsningar när du arbetar med DBF-filer:

- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste vara versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `ÅÅÅÅMMDD`.
- Teckenkodning kan variera beroende på källapplikationen (vanligtvis Windows-1252 eller OEM-kodtabeller).

## **Läsa en DBF-fil**

Aspose.Cells gör det enkelt att läsa in data från en DBF-fil till ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt under inläsningsprocessen.

### Läsa en DBF-fil med Aspose.Cells

För att läsa en DBF-fil behöver du skapa en `LoadOptions`-instans, ange dess `load_format`-egenskap till `LoadFormat.DBF` och skicka den till `Workbook`-konstruktorn tillsammans med filsökvägen. När den är laddad blir data åtkomlig via samlingen `worksheets`, där du kan iterera genom celler, extrahera värden eller manipulera data efter behov.

Följande exempel visar hur man läser in en befintlig DBF-fil i Aspose.Cells, kommer åt dess första kalkylblad och läser cellvärdena.

```python
import os
import aspose.cells as ac

data_dir = "Data/"
file_path = os.path.join(data_dir, "example.dbf")

load_options = ac.LoadOptions(ac.LoadFormat.DBF)

workbook = ac.Workbook(file_path, load_options)

worksheet = workbook.worksheets[0]

cells = worksheet.cells

lines = []

max_row = cells.max_data_row
max_col = cells.max_data_column

for i in range(max_row + 1):
    line_parts = []
    for j in range(max_col + 1):
        cell = cells[i, j]
        value = cell.string_value
        line_parts.append("|" + value)
    line_parts.append("|")
    lines.append("".join(line_parts))

result = "\n".join(lines) + ("\n" if lines else "")
print(result)

output_path = os.path.join(data_dir, "output.xlsx")
workbook.save(output_path, ac.SaveFormat.XLSX)

print("DBF file loaded successfully. Converted XLSX saved at: " + output_path)
```

{{% alert color="primary" %}}

Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel behandlar DBF-filen som ett kalkylblad och visar dess poster i en tabellayout. Detta är användbart för att snabbt verifiera data efter att ha läst eller skrivit den med Aspose.Cells.

{{% /alert %}}

## **Skriva en DBF-fil**

Att skriva data till en DBF-fil följer ett liknande mönster som att spara andra kalkylbladsformat med Aspose.Cells. Du skapar eller laddar en Workbook, fyller kalkylbladet med data och anropar sedan metoden `save` medan du anger `SaveFormat.DBF` som målformat.

### Skriva en DBF-fil med Aspose.Cells

För att skapa en DBF-fil, följ dessa steg:

1. Skapa en ny `Workbook`-instans.
2. Kom åt det första kalkylbladet från samlingen `worksheets`.
3. Fyll kalkylbladet med dina data, inklusive rubriker i den första raden och poster i efterföljande rader.
4. Anropa metoden `Workbook.save` och skicka filsökvägen och `SaveFormat.DBF` som parametrar.

Följande exempel visar hur man skapar en ny DBF-fil från grunden. Det fyller ett kalkylblad med exempeldata som innehåller olika datatyper (strängar, tal och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

```python
from datetime import datetime

outputDir = r"C:\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Kolumnrubriker
cells[0, 0].put_value("ID")
cells[0, 1].put_value("Name")
cells[0, 2].put_value("Department")
cells[0, 3].put_value("Salary")
cells[0, 4].put_value("HireDate")

# Datarad 1
cells[1, 0].put_value(101)
cells[1, 1].put_value("John Smith")
cells[1, 2].put_value("Engineering")
cells[1, 3].put_value(75000.50)
cells[1, 4].put_value(datetime(2020, 3, 15))

# Datarad 2
cells[2, 0].put_value(102)
cells[2, 1].put_value("Jane Doe")
cells[2, 2].put_value("Marketing")
cells[2, 3].put_value(68000.75)
cells[2, 4].put_value(datetime(2019, 7, 22))

# Datarad 3
cells[3, 0].put_value(103)
cells[3, 1].put_value("Bob Johnson")
cells[3, 2].put_value("Finance")
cells[3, 3].put_value(82000.00)
cells[3, 4].put_value(datetime(2021, 1, 10))

# Datarad 4
cells[4, 0].put_value(104)
cells[4, 1].put_value("Alice Brown")
cells[4, 2].put_value("Human Resources")
cells[4, 3].put_value(71000.25)
cells[4, 4].put_value(datetime(2018, 11, 5))

# Datarad 5
cells[5, 0].put_value(105)
cells[5, 1].put_value("Charlie Wilson")
cells[5, 2].put_value("Operations")
cells[5, 3].put_value(79500.80)
cells[5, 4].put_value(datetime(2022, 5, 30))

# Ställ in kolumnbredder för bättre läsbarhet
worksheet.cells.set_column_width(0, 8)
worksheet.cells.set_column_width(1, 20)
worksheet.cells.set_column_width(2, 20)
worksheet.cells.set_column_width(3, 12)
worksheet.cells.set_column_width(4, 14)

workbook.save(filePath, ac.SaveFormat.Dbf)
```

{{% alert color="primary" %}}

När du skriver data till en DBF-fil, se till att dina data följer formatets begränsningar. Fältnamn bör inte vara längre än 10 tecken och bör inte innehålla mellanslag. Poster som överstiger totalt 4000 byte kommer inte att sparas korrekt. Datum bör vara giltiga datumvärden som kan representeras i formatet ÅÅÅÅMMDD.

{{% /alert %}}

## **Överväganden gällande datatyper och formatering**

Vid överföring av data mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyper mappas mellan de två systemen för att säkerställa dataintegritet.

### Celltyper till DBF-fälttyper

Aspose.Cells cellvärden konverteras automatiskt till lämpliga DBF-fälttyper vid sparande:

- **Strängar** mappas till teckenfält (C).
- **Numeriska värden** (heltal och decimaler) mappas till numeriska fält (N).
- **Datumvärden** mappas till datumfält (D) i formatet `ÅÅÅÅMMDD`.
- **Booleska värden** mappas till logiska fält (L).

### Kodning

DBF-filer kan använda olika teckenkodningar beroende på applikationen som skapade dem. Aspose.Cells hanterar kodning transparent i de flesta fall, men om du stöter på problem med teckenvisningen kan du behöva verifiera kodningen av källfilen.

### Regler för fältnamn

DBF-fältnamn måste följa följande regler:

- Maximal längd på 10 tecken.
- Måste börja med en bokstav.
- Får inte innehålla mellanslag eller specialtecken.
- Lagras som versaler oavsett vilken skiftläge som används i inmatningen.

### Verifiering av utdata

Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller någon dBASE-kompatibel applikation. Data bör visas i en tabellayout med fältnamnen som kolumnrubriker, och posterna ifyllda enligt den data du angav.

## **Konvertera mellan DBF och andra format**

Ett av de mest praktiska användningsfallen för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylbladsformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett brett utbud av format kan du enkelt läsa in en DBF-fil och spara om den i valfritt annat stött format, eller vice versa.

Du kan till exempel läsa en DBF-fil, tillämpa formatering eller beräkningar med Aspose.Cells-API:et och sedan spara resultatet som en XLSX-fil för distribution till användare som arbetar med moderna kalkylbladsapplikationer. Omvänt kan du hämta data från en XLSX- eller CSV-fil och exportera den till DBF-format för integration med äldre system.



{{< app/cells/assistant language="python" >}}