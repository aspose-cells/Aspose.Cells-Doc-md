---
title: Läsa och skriva DBF-filer
description: Aspose.Cells är ett C++-bibliotek för att arbeta med kalkylbladsfiler, som stöder läsning och skrivning av dBASE III- och IV-filer (DBF). Denna artikel förklarar hur man importerar data från och exporterar data till DBF-filer med Aspose.Cells, inklusive filformatdetaljer, stödda funktioner och steg-för-steg-exempel.
keywords: Aspose.Cells, C++-bibliotek, DBF, dBASE, läsa DBF, skriva DBF, importera DBF, exportera DBF, filformat, .dbf
type: docs
weight: 200
url: /sv/cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells ger fullständigt stöd för att läsa och skriva DBF-filer (dBASE). Du kan ladda befintliga dBASE III- och dBASE IV-filer till ett Workbook-objekt, manipulera data med det omfattande Aspose.Cells-API:et och spara arbetsboken tillbaka till DBF-formatet för användning med äldre databasapplikationer.

{{% /alert %}}

## **Introduktion**

DBF (DataBase File) är ett äldre databasfilformat som ursprungligen introducerades av dBASE i början av 1980-talet. Trots formatets ålder används DBF-filer fortfarande i stor utsträckning inom många branscher för att lagra strukturerade data, särskilt inom redovisning, GIS och andra specialiserade applikationer. Aspose.Cells låter dig integrera dessa äldre filer i moderna C++-kalkylbladsarbetsflöden sömlöst.

Biblioteket stöder både läsning och skrivning av DBF-filer, vilket ger dig möjlighet att:

- Importera data från befintliga DBF-filer till Aspose.Cells Workbook-objekt för vidare bearbetning eller konvertering till andra format.
- Skapa nya DBF-filer från grunden eller genom att omvandla data från andra kalkylbladsformat.
- Bibehålla fältdefinitioner, datatyper och poststrukturer vid överföring av data till och från DBF-formatet.

DBF-filer kan också öppnas direkt i Microsoft Excel och andra kalkylbladsapplikationer, vilket gör dem till en bekväm brygga mellan äldre system och moderna kalkylbladsverktyg.

## **DBF-versioner och funktioner som stöds**

Aspose.Cells stöder följande DBF-formatversioner:

- **dBASE III** — Den ursprungliga och mest stödda varianten av DBF-formatet.
- **dBASE IV** — En utökad version som stöder ytterligare datatyper och större fältstorlekar.

### Funktioner som stöds

Biblioteket ger omfattande stöd för följande operationer:

- Läsa DBF-data till ett Workbook-objekt, med alla poster och fältdefinitioner bevarade.
- Skriva arbetsboksdata tillbaka till DBF-format för export till dBASE-kompatibla applikationer.
- Hantera vanliga datatyper som används i DBF-filer, inklusive tecken-, numeriska-, datum- och logiska fält.
- Bevara fältdefinitioner som fältnamn, typ och längd under läs-/skrivoperationer.

### Begränsningar och överväganden

När du arbetar med DBF-filer, tänk på följande begränsningar:

- Det maximala antalet fält per fil är **128**.
- Den maximala poststorleken är **4000 byte**.
- Fältnamn är begränsade till **10 tecken**, måste vara i versaler och får inte innehålla mellanslag.
- Datumvärden i DBF-filer lagras i formatet `YYYYMMDD`.
- Teckenkodning kan variera beroende på källapplikationen (vanligtvis Windows-1252 eller OEM-kodtabeller).

## **Läsa en DBF-fil**

Aspose.Cells gör det enkelt att ladda data från en DBF-fil till ett Workbook-objekt. Biblioteket använder klassen `LoadOptions` för att ange källformatet, vilket säkerställer att data tolkas korrekt under laddningsprocessen.

### Läsa en DBF-fil med Aspose.Cells

För att läsa en DBF-fil behöver du skapa en `LoadOptions`-instans, ange dess `LoadFormat`-egenskap till `LoadFormat.Dbf` och skicka den till `Workbook`-konstruktören tillsammans med filsökvägen. När den väl är laddad blir data tillgänglig via `Worksheets`-samlingen, där du kan iterera genom celler, extrahera värden eller manipulera data efter behov.

Följande exempel visar hur man laddar en befintlig DBF-fil i Aspose.Cells, kommer åt dess första kalkylblad och läser cellvärdena.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Du kan öppna DBF-filer direkt i Microsoft Excel genom att välja filen i dialogrutan Öppna. Excel behandlar DBF-filen som ett kalkylblad och visar dess poster i en tabellayout. Detta är användbart för att snabbt verifiera data efter att ha läst eller skrivit data med Aspose.Cells.

{{% /alert %}}

## **Skriva en DBF-fil**

Att skriva data till en DBF-fil följer ett liknande mönster som att spara i andra kalkylbladsformat med Aspose.Cells. Du skapar eller laddar en Workbook, fyller kalkylbladet med data och anropar sedan `Save`-metoden medan du anger `SaveFormat.Dbf` som målformat.

### Skriva en DBF-fil med Aspose.Cells

För att skapa en DBF-fil, följ dessa steg:

1. Skapa en ny `Workbook`-instans.
2. Öppna det första kalkylbladet från `Worksheets`-samlingen.
3. Fyll kalkylbladet med dina data, inklusive rubriker i den första raden och poster i efterföljande rader.
4. Anropa metoden `Workbook.Save`, och skicka filsökvägen och `SaveFormat.Dbf` som parametrar.

Följande exempel visar hur man skapar en ny DBF-fil från grunden. Det fyller ett kalkylblad med exempeldata som innehåller olika datatyper (strängar, tal och datum) för att illustrera hur fälttyper hanteras vid export till DBF-formatet.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Kolumnrubriker
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // Datrad 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // Datrad 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // Datrad 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // Datrad 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // Datrad 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // Ställ in kolumnbredder för bättre läsbarhet
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

När du skriver data till en DBF-fil, se till att dina data följer formatets begränsningar. Fältnamn bör inte vara längre än 10 tecken och bör inte innehålla mellanslag. Poster som överstiger 4000 byte totalt kommer inte att sparas korrekt. Datum bör vara giltiga datumvärden som kan representeras i formatet YYYYMMDD.

{{% /alert %}}

## **Överväganden för datatyper och formatering**

Vid överföring av data mellan Aspose.Cells och DBF-formatet är det viktigt att förstå hur datatyper mappas mellan de två systemen för att säkerställa dataintegritet.

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
- Lagras som versaler oavsett vilken skiftläge som använts vid inmatning.

### Verifiera utdata

Efter att ha skrivit en DBF-fil kan du verifiera resultatet genom att öppna den i Microsoft Excel eller någon dBASE-kompatibel applikation. Data bör visas i en tabellayout med fältnamnen som kolumnrubriker, och posterna ifyllda enligt det data du angav.

## **Konvertera mellan DBF och andra format**

Ett av de mest praktiska användningsfallen för att läsa och skriva DBF-filer med Aspose.Cells är att konvertera data mellan DBF-formatet och moderna kalkylbladsformat som XLSX, XLS eller CSV. Eftersom Aspose.Cells stöder ett brett utbud av format kan du enkelt ladda en DBF-fil och spara om den i något annat format som stöds, eller vice versa.

Du kan till exempel läsa en DBF-fil, tillämpa formatering eller beräkningar med Aspose.Cells-API:et och sedan spara resultatet som en XLSX-fil för distribution till användare som arbetar med moderna kalkylbladsapplikationer. Omvänt kan du ta data från en XLSX- eller CSV-fil och exportera data till DBF-format för integration med äldre system.



{{< app/cells/assistant language="cpp" >}}