---
title: Dela upp Excel-filer i flera filer
linktitle: Dela upp Excel-filer i flera filer
description: Aspose.Cells for C++ är ett C++-bibliotek för att arbeta med kalkylbladsfiler, som stöder uppdelning av en enskild Excel-fil i flera filer. Den här artikeln introducerar hur man delar upp Excel-filer genom att kopiera varje kalkylblad till en separat arbetsbok och genom att kopiera specifika cellintervall till andra arbetsböcker.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, dela Excel-fil, kopiera kalkylblad, kopiera intervall, flera arbetsböcker, spara som separata filer
type: docs
weight: 195
url: /sv/cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder uppdelning av en enskild Excel-fil i flera filer. Det finns två huvudsakliga sätt att göra detta: (1) genom att kopiera varje kalkylblad i källarbetsboken till en ny arbetsbok och spara varje som en separat fil, och (2) genom att kopiera ett specifikt cellintervall från ett kalkylblad till en ny arbetsbok. Båda metoderna är användbara när du behöver distribuera delmängder av data, skapa mindre rapporter för olika mottagare, eller isolera data för individuell bearbetning.

## **Introduktion**
Det finns många verkliga scenarier där en utvecklare behöver dela upp en enskild Excel-fil i flera mindre filer. Till exempel kan en arbetsbok innehålla ett kalkylblad per avdelning, och varje avdelningschef behöver endast få sitt eget blad. I andra fall kanske du vill extrahera en viss tabell eller datablock från ett kalkylblad och skicka det som en fristående fil via e-post, utan att exponera resten av arbetsboken. Stora konsoliderade arbetsböcker kan också behöva delas upp i mindre bitar för enklare hantering, snabbare laddning eller vidare bearbetning av andra system.
Aspose.Cells erbjuder två flexibla metoder för denna uppgift. Den första metoden itererar genom varje kalkylblad i källarbetsboken och kopierar dess innehåll till en helt ny `Workbook`-instans, och sparar varje som en separat fil. Den andra metoden fokuserar på ett specifikt cellintervall inom ett kalkylblad och kopierar endast det intervallet till en ny arbetsbok. I båda fallen är det allmänna flödet detsamma: ladda källarbetsboken med klassen `Workbook`, få tillgång till relevant data via objekten `Worksheet` och `Cells`, överför innehållet till en destinations-`Workbook`, och spara sedan destinationen till disk.

## **Dela upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok**

### **Metodöversikt**
I denna metod öppnas källarbetsboken en gång, och sedan skapas en ny destinations-`Workbook` för varje `Worksheet` i dess `Worksheets`-samling. Innehållet i källkalkylbladet kopieras sedan till det första kalkylbladet i destinationsarbetsboken, och destinationsarbetsboken sparas som en fil vars namn härrör från källkalkylbladets namn. Resultatet är en utdatafil per kalkylblad, där varje utdatafil innehåller data från ett enda källblad.
Denna metod är rätt val när varje kalkylblad i din källarbetsbok representerar en logiskt oberoende informationsenhet (till exempel en avdelning, region, månad eller produktlinje) och du vill leverera eller bearbeta varje enhet för sig.

### **Steg**
Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok:
1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt och skicka filsökvägen till dess konstruktor.
2. Iterera genom samlingen `Workbook.Worksheets` med en `for`- eller `foreach`-loop så att varje `Worksheet` i källfilen bearbetas.
3. Inuti loopen, skapa en ny destinations-`Workbook`-instans (en tom arbetsbok) för det aktuella kalkylbladet.
4. Kopiera innehållet i källkalkylbladet till destinationskalkylbladet. Detta kan göras genom att iterera cellerna i källkalkylbladets `Cells`-samling och skriva deras värden till motsvarande celler i destinationskalkylbladet, eller genom att använda metoden `Cells.Copy` för att överföra ett helt intervall på en gång.
5. Konstruera en sökväg för utdatafil som innehåller källkalkylbladets namn (till exempel `dataDir + worksheet.Name + ".xls"`) så att varje genererad fil har ett unikt namn.
6. Anropa destinations-`Workbook.Save`-metoden för att skriva filen till disk.
7. Upprepa steg 3 till 6 för nästa kalkylblad tills alla kalkylblad har bearbetats.

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

Den förväntade utdata är en uppsättning nya filer i datakatalogen, en fil per kalkylblad från källarbetsboken. Varje fil är namngiven efter motsvarande källblad, och filen innehåller data (och valfritt formateringen) för det enskilda bladet.

## **Dela upp en Excel-fil genom att kopiera ett intervall till en ny arbetsbok**

### **Metodöversikt**
Ibland motsvarar inte datan du behöver dela upp ett helt kalkylblad utan snarare en specifik rektangulär region av ett kalkylblad, till exempel `A1:D10` eller ett namngivet intervall som representerar en viss tabell. I dessa fall är det ineffektivt att kopiera hela kalkylblad, och en mer precis metod krävs: identifiera källintervallet, kopiera endast det intervallet till en ny arbetsbok, och spara den nya filen.
Denna metod är idealisk när du vill extrahera en enskild tabell, rapportblock eller dataområde från ett större kalkylblad samtidigt som all orelaterat innehåll kasseras. Det är också användbart för att exportera användarvalda regioner av ett blad som fristående filer.

### **Steg**
Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera ett specifikt intervall till en ny arbetsbok:
1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt med filsökvägen.
2. Hämta mål-`Worksheet` som innehåller intervallet du vill kopiera, antingen via index (till exempel det första bladet) eller via namn från `Worksheets`-samlingen.
3. Identifiera intervallet som ska kopieras. Detta kan vara ett hårdkodat cellintervall som `A1:C10`, eller ett namngivet intervall som hämtas via `Worksheet.Cells`-samlingen, eller ett intervall som skapas via `Worksheet.Cells.CreateRange`.
4. Skapa en ny destinations-`Workbook`-instans.
5. Få tillgång till den första `Worksheet` i destinationsarbetsboken (standardbladet).
6. Kopiera källintervallet till destinationskalkylbladet, vanligtvis med början från cell `A1`. Metoden `Cells.Copy` på destinations-`Cells`-samlingen kan användas för att kopiera ett helt intervall, eller så kan du iterera genom källintervallets celler och skriva deras värden till destinationscellerna med `PutValue`. Valfria `CopyOptions` kan anges för att styra vad som överförs (endast värden, värden och stilar, formler, och så vidare).
7. Spara destinationsarbetsboken till en ny filsökväg på disk med metoden `Workbook.Save`.

### **Kodexempel**
Den förväntade utdata är en enda ny fil i datakatalogen som endast innehåller värdena (och valfritt formateringen) för det angivna intervallet extraherat från källarbetsboken. Destinationsfilen har ingen relation till annan data i källfilen; den innehåller bara det extraherade intervallet, med början från cell `A1` i sitt första kalkylblad.
{{% /alert %}}

## Relaterade artiklar
- [Lägg till filterfält i en pivottabell i Aspose.Cells for C++](/cells/sv/cpp/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for C++](/cells/sv/cpp/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/cpp/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for C++](/cells/sv/cpp/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="cpp" >}}