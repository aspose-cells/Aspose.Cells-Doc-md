---
title: Dela upp Excel-filer i flera filer
description: Aspose.Cells är ett C++-bibliotek för att arbeta med kalkylbladsfiler, som stöder uppdelning av en enskild Excel-fil i flera filer. Den här artikeln beskriver hur man delar upp Excel-filer genom att kopiera varje kalkylblad till en separat arbetsbok och genom att kopiera specifika cellintervall till andra arbetsböcker.
keywords: Aspose.Cells, C++ bibliotek, kalkylblad, dela upp Excel-fil, kopiera kalkylblad, kopiera intervall, flera arbetsböcker, spara som separata filer
type: docs
weight: 195
url: /sv/cpp/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells stöder uppdelning av en enskild Excel-fil i flera filer. Det finns två huvudsakliga sätt att göra detta: (1) genom att kopiera varje kalkylblad i källarbetsboken till en ny arbetsbok och spara varje som en separat fil, och (2) genom att kopiera ett specifikt cellintervall från ett kalkylblad till en ny arbetsbok. Båda metoderna är användbara när du behöver distribuera delmängder av data, skapa mindre rapporter för olika mottagare, eller isolera data för enskild bearbetning.

{{% /alert %}}

## **Introduktion**

Det finns många verkliga scenarier där en utvecklare behöver bryta upp en enskild Excel-fil i flera mindre filer. Till exempel kan en arbetsbok innehålla ett kalkylblad per avdelning, och varje avdelningschef behöver endast få sitt eget blad. I andra fall kanske du vill extrahera en viss tabell eller datablock från ett kalkylblad och skicka det som en fristående fil via e-post, utan att exponera resten av arbetsboken. Stora konsoliderade arbetsböcker kan också behöva delas upp i mindre bitar för enklare hantering, snabbare laddning, eller vidare bearbetning av andra system.

Aspose.Cells erbjuder två flexibla metoder för denna uppgift. Den första metoden itererar genom varje kalkylblad i källarbetsboken och kopierar dess innehåll till en helt ny `Workbook`-instans, och sparar varje arbetsbok som en separat fil. Den andra metoden fokuserar på ett specifikt cellintervall inom ett kalkylblad och kopierar endast det intervallet till en ny arbetsbok. I båda fallen är det allmänna flödet detsamma: ladda källarbetsboken med `Workbook`-klassen, få åtkomst till relevanta data genom `Worksheet`- och `Cells`-objekten, överför innehållet till en destinations-`Workbook`, och spara sedan destinationen till disk.

## **Dela upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok**

### **Metodöversikt**

I denna metod öppnas källarbetsboken en gång, och sedan skapas för varje `Worksheet` i dess `Worksheets`-samling en ny destinations-`Workbook`. Innehållet i kalkylbladet kopieras sedan till det första kalkylbladet i destinationsarbetsboken, och destinationsarbetsboken sparas som en fil vars namn härleds från källkalkylbladets namn. Resultatet är en utdatafil per kalkylblad, där varje utdatafil innehåller data från ett enda källblad.

Denna metod är det rätta valet när varje kalkylblad i din källarbetsbok representerar en logiskt oberoende informationsenhet (såsom en avdelning, region, månad, eller produktlinje) och du vill leverera eller bearbeta varje enhet för sig.

### **Steg**

Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok:

1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt och skicka filsökvägen till dess konstruktor.
2. Iterera genom `Workbook.Worksheets`-samlingen med en `for`- eller `foreach`-loop så att varje `Worksheet` i källfilen bearbetas.
3. Inne i loopen, skapa en ny destinations-`Workbook`-instans (en tom arbetsbok) för det aktuella kalkylbladet.
4. Lägg till ett nytt `Worksheet` i destinationsarbetsboken (eller använd det första standardkalkylbladet) och ge det ett meningsfullt namn, helst samma som källkalkylbladets `Name`-egenskap.
5. Kopiera innehållet i källkalkylbladet till destinationskalkylbladet. Detta kan göras genom att iterera cellerna i källkalkylbladets `Cells`-samling och skriva deras värden till motsvarande celler i destinationskalkylbladet, eller genom att använda `Cells.Copy`-metoden för att överföra ett helt intervall på en gång.
6. Konstruera en utdatafilsökväg som innehåller källkalkylbladets namn (till exempel `dataDir + worksheet.Name + ".xls"`) så att varje genererad fil har ett unikt namn.
7. Anropa destinations-`Workbook.Save`-metoden för att skriva filen till disk.
8. Upprepa steg 3 till 7 för nästa kalkylblad tills alla kalkylblad har bearbetats.

### **Kodexempel**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "data/";
    Workbook wb(U16String((dataDir + "book1.xls").c_str()));

    int sheetCount = wb.GetWorksheets().GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet sourceSheet = wb.GetWorksheets().Get(i);
        U16String sheetName = sourceSheet.GetName();

        Workbook destWorkbook;
        int destIndex = destWorkbook.GetWorksheets().Add();
        Worksheet destSheet = destWorkbook.GetWorksheets().Get(destIndex);
        destSheet.SetName(sheetName);

        destSheet.Copy(sourceSheet);

        std::string destFile = dataDir + sheetName.ToUtf8() + ".xls";
        destWorkbook.Save(U16String(destFile.c_str()), SaveFormat::Excel97To2003);
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Den förväntade utdatan är en uppsättning nya filer i datakatalogen, en fil per kalkylblad från källarbetsboken. Varje fil är namngiven efter sitt motsvarande källblad, och filen innehåller data (och valfritt formateringen) från det enskilda bladet.

## **Dela upp en Excel-fil genom att kopiera ett intervall till en ny arbetsbok**

### **Metodöversikt**

Ibland motsvarar inte datan du behöver dela upp ett helt kalkylblad, utan snarare en specifik rektangulär region av ett kalkylblad, såsom `A1:D10` eller ett namngivet intervall som representerar en viss tabell. I dessa fall är det slösaktigt att kopiera hela kalkylblad, och en mer precis metod krävs: identifiera källintervallet, kopiera endast det intervallet till en ny arbetsbok, och spara den nya filen.

Denna metod är idealisk när du vill extrahera en enskild tabell, rapportblock, eller dataområde från ett större kalkylblad samtidigt som du kasserar allt orelaterat innehåll. Det är också användbart för att exportera användarvalda regioner av ett blad som fristående filer.

### **Steg**

Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera ett specifikt intervall till en ny arbetsbok:

1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt med filsökvägen.
2. Hämta målets `Worksheet` som innehåller intervallet du vill kopiera, antingen via index (till exempel det första bladet) eller via namn från `Worksheets`-samlingen.
3. Identifiera intervallet som ska kopieras. Detta kan vara ett hårdkodat cellintervall såsom `A1:C10`, eller ett namngivet intervall som erhålls genom `Worksheet.Cells`-samlingen, eller ett intervall som skapas via `Worksheet.Cells.CreateRange`.
4. Skapa en ny destinations-`Workbook`-instans.
5. Få åtkomst till det första `Worksheet` i destinationsarbetsboken (standardbladet).
6. Kopiera källintervallet till destinationskalkylbladet, vanligtvis med början från cell `A1`. `Cells.Copy`-metoden på destinations-`Cells`-samlingen kan användas för att kopiera ett helt intervall, eller så kan du iterera genom källintervallets celler och skriva deras värden till destinationscellerna med `PutValue`. Valfria `CopyOptions` kan tillhandahållas för att kontrollera vad som överförs (endast värden, värden och stilar, formler, och så vidare).
7. Spara destinationsarbetsboken till en ny filsökväg på disk med `Workbook.Save`-metoden.

### **Kodexempel**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Definiera datakatalogen och filsökvägarna
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // Öppna källans Excel-fil
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // Hämta det första kalkylbladet från källans arbetsbok
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // Definiera källans cellområde A1:C10 (10 rader, 3 kolumner med start på rad 0, kol 0)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Skapa en ny destinationsarbetsbok
    Workbook destWorkbook;

    // Kom åt det första kalkylbladet i destinationsarbetsboken
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // Skapa destinationsområdet vid A1 med samma dimensioner som källans område
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Kopiera källans område till destinationsområdet
    destRange.Copy(sourceRange);

    // Spara destinationsarbetsboken till en ny .xls-fil
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Den förväntade utdatan är en enskild ny fil i datakatalogen som endast innehåller värdena (och valfritt formateringen) för det angivna intervallet som extraherats från källarbetsboken. Destinationsfilen har ingen relation till annan data i källfilen; den innehåller bara det extraherade intervallet, med början från cell `A1` i sitt första kalkylblad.

## **Relaterade artiklar**

- [Kopiera rader och kolumner](/cells/sv/cpp/copying-rows-and-columns/)
- [Sammanfoga och dela celler](/cells/sv/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}