---
title: Dela upp Excel-filer i flera filer
linktitle: Dela upp Excel-filer
description: Aspose.Cells är ett Python via Java-bibliotek för att arbeta med kalkylarksfiler, som stöder delning av en enda Excel-fil i flera filer. Den här artikeln beskriver hur man delar upp Excel-filer genom att kopiera varje kalkylblad till en separat arbetsbok och genom att kopiera specifika cellintervall till andra arbetsböcker.
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylark, dela Excel-fil, kopiera kalkylblad, kopiera intervall, flera arbetsböcker, spara som separata filer
type: docs
weight: 195
url: /sv/python-java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder delning av en enda Excel-fil i flera filer. Det finns två primära sätt att göra detta: (1) genom att kopiera varje kalkylblad i källarbetsboken till en ny arbetsbok och spara varje som en separat fil, och (2) genom att kopiera ett specifikt cellintervall från ett kalkylblad till en ny arbetsbok. Båda metoderna är användbara när du behöver distribuera delmängder av data, skapa mindre rapporter för olika mottagare, eller isolera data för individuell bearbetning.

{{% /alert %}}

## **Introduktion**

Det finns många verkliga scenarier där en utvecklare behöver dela upp en enda Excel-fil i flera mindre filer. En arbetsbok kan till exempel innehålla ett kalkylblad per avdelning, och varje avdelningschef behöver bara få sitt eget blad. I andra fall kanske du vill extrahera en specifik tabell eller datablock från ett kalkylblad och skicka det som en fristående fil via e-post, utan att exponera resten av arbetsboken. Stora konsoliderade arbetsböcker kan också behöva delas upp i mindre bitar för enklare hantering, snabbare laddning, eller vidare bearbetning av andra system.

Aspose.Cells erbjuder två flexibla metoder för denna uppgift. Den första metoden itererar genom varje kalkylblad i källarbetsboken och kopierar dess innehåll till en helt ny `Workbook`-instans, och sparar varje som en separat fil. Den andra metoden fokuserar på ett specifikt cellintervall inom ett kalkylblad och kopierar endast det intervallet till en ny arbetsbok. I båda fallen är det allmänna flödet detsamma: ladda källarbetsboken med hjälp av `Workbook`-klassen, kom åt relevant data genom `Worksheet`- och `Cells`-objekten, överför innehållet till en destinations-`Workbook`, och spara sedan destinationen till disk.

## **Dela upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok**

### **Metodöversikt**

I denna metod öppnas källarbetsboken en gång, och sedan skapas en ny destinations-`Workbook` för varje `Worksheet` i dess `Worksheets`-samling. Innehållet i källkalkylbladet kopieras sedan till det första kalkylbladet i destinationsarbetsboken, och destinationsarbetsboken sparas som en fil vars namn härleds från källkalkylbladets namn. Resultatet är en utdatafil per kalkylblad, där varje utdatafil innehåller data från ett enda källblad.

Denna metod är rätt val när varje kalkylblad i din källarbetsbok representerar en logiskt oberoende informationsenhet (till exempel en avdelning, region, månad eller produktlinje) och du vill leverera eller bearbeta varje enhet separat.

### **Steg**

Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok:

1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt och skicka filsökvägen till dess konstruktor.
2. Iterera genom `Workbook.Worksheets`-samlingen med hjälp av en `for`- eller `foreach`-loop så att varje `Worksheet` i källfilen bearbetas.
3. Inuti loopen, skapa en ny destinations-`Workbook`-instans (en tom arbetsbok) för det aktuella kalkylbladet.
4. Lägg till ett nytt `Worksheet` i destinationsarbetsboken (eller använd det första standardkalkylbladet) och tilldela det ett meningsfullt namn, helst detsamma som källkalkylbladets `Name`-egenskap.
5. Kopiera innehållet i källkalkylbladet till destinationskalkylbladet. Detta kan göras genom att iterera cellerna i källkalkylbladets `Cells`-samling och skriva deras värden till motsvarande celler i destinationskalkylbladet, eller genom att använda `Cells.copy`-metoden för att överföra ett helt intervall på en gång.
6. Konstruera en utdatafilsökväg som innehåller källkalkylbladets namn (till exempel `dataDir + worksheet.Name + ".xls"`) så att varje genererad fil har ett unikt namn.
7. Anropa destinations-`Workbook.save`-metoden för att skriva filen till disk.
8. Upprepa steg 3 till 7 för nästa kalkylblad tills alla kalkylblad har bearbetats.

### **Kodexempel**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

dataDir = "data/"
workbook = Workbook(dataDir + "book1.xls")

for i in range(workbook.getWorksheets().getCount()):
    sourceSheet = workbook.getWorksheets().get(i)
    sheetName = sourceSheet.getName()
    
    destWorkbook = Workbook()
    destIndex = destWorkbook.getWorksheets().add()
    destSheet = destWorkbook.getWorksheets().get(destIndex)
    destSheet.setName(sheetName)
    
    destSheet.copy(sourceSheet)
    
    destFile = dataDir + sheetName + ".xls"
    destWorkbook.save(destFile, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

Det förväntade resultatet är en uppsättning nya filer i datakatalogen, en fil per kalkylblad från källarbetsboken. Varje fil är namngiven efter motsvarande källblad, och filen innehåller data (och valfritt formateringen) från det enskilda bladet.

## **Dela upp en Excel-fil genom att kopiera ett intervall till en ny arbetsbok**

### **Metodöversikt**

Ibland motsvarar inte datan du behöver dela ett helt kalkylblad utan snarare en specifik rektangulär region av ett kalkylblad, såsom `A1:D10` eller ett namngivet intervall som representerar en viss tabell. I dessa fall är det slösaktigt att kopiera hela kalkylblad, och en mer exakt metod krävs: identifiera källintervallet, kopiera endast det intervallet till en ny arbetsbok, och spara den nya filen.

Denna metod är idealisk när du vill extrahera en enskild tabell, rapportblock eller dataområde från ett större kalkylblad samtidigt som du kasserar allt orelaterat innehåll. Det är också användbart för att exportera användarvalda regioner av ett blad som fristående filer.

### **Steg**

Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera ett specifikt intervall till en ny arbetsbok:

1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt med filsökvägen.
2. Hämta mål-`Worksheet` som innehåller intervallet du vill kopiera, antingen via index (till exempel det första bladet) eller via namn från `Worksheets`-samlingen.
3. Identifiera intervallet som ska kopieras. Detta kan vara ett hårdkodat cellintervall som `A1:C10`, eller ett namngivet intervall som erhålls genom `Worksheet.Cells`-samlingen, eller ett intervall skapat via `Worksheet.Cells.createRange`.
4. Skapa en ny destinations-`Workbook`-instans.
5. Kom åt den första `Worksheet` i destinationsarbetsboken (standardbladet).
6. Kopiera källintervallet till destinationskalkylbladet, vanligtvis med början från cell `A1`. `Cells.copy`-metoden på destinations-`Cells`-samlingen kan användas för att kopiera ett helt intervall, eller så kan du iterera genom källintervallets celler och skriva deras värden till destinationscellerna med `putValue`. Valfria `CopyOptions` kan tillhandahållas för att styra vad som överförs (endast värden, värden och stilar, formler, och så vidare).
7. Spara destinationsarbetsboken till en ny filsökväg på disk med hjälp av `Workbook.save`-metoden.

### **Kodexempel**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# Definiera datakatalogen och filsökvägarna
dataDir = "data/"
sourcePath = dataDir + "book1.xls"
outputPath = dataDir + "outputrange.xls"

# Öppna källans Excel-fil
sourceWorkbook = Workbook(sourcePath)

# Hämta det första kalkylbladet från källarboken
sourceWorksheet = sourceWorkbook.getWorksheets().get(0)

# Definiera källans cellområde A1:C10 (10 rader, 3 kolumner som börjar vid rad 0, kol 0)
sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3)

# Skapa en ny destinationsarbetsbok
destWorkbook = Workbook()

# Få åtkomst till det första kalkylbladet i destinationsarbetsboken
destWorksheet = destWorkbook.getWorksheets().get(0)

# Skapa destinationsområdet vid A1 med samma dimensioner som källans område
destRange = destWorksheet.getCells().createRange(0, 0, 10, 3)

# Kopiera källans område till destinationsområdet
destRange.copy(sourceRange)

# Spara destinationsarbetsboken till en ny .xls-fil
destWorkbook.save(outputPath, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

Det förväntade resultatet är en enda ny fil i datakatalogen som endast innehåller värdena (och valfritt formateringen) för det angivna intervallet som extraherats från källarbetsboken. Destinationsfilen har ingen relation till någon annan data i källfilen; den innehåller bara det extraherade intervallet, med början vid cell `A1` i dess första kalkylblad.



{{< app/cells/assistant language="python" >}}