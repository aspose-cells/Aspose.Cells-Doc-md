---
title: Dela upp Excel-filer i flera filer
description: Aspose.Cells är ett Java-bibliotek för arbete med kalkylarksfiler, som stöder uppdelning av en enskild Excel-fil i flera filer. Den här artikeln beskriver hur man delar upp Excel-filer genom att kopiera varje kalkylblad till en separat arbetsbok och genom att kopiera specifika cellintervall till andra arbetsböcker.
linktitle: Dela upp Excel-filer i flera
keywords: Aspose.Cells, Java-bibliotek, kalkylark, dela Excel-fil, kopiera kalkylblad, kopiera intervall, flera arbetsböcker, spara som separata filer
type: docs
weight: 195
url: /sv/java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder uppdelning av en enskild Excel-fil i flera filer. Det finns två primära sätt att göra detta: (1) genom att kopiera varje kalkylblad i källarbetsboken till en ny arbetsbok och spara varje som en separat fil, och (2) genom att kopiera ett specifikt cellintervall från ett kalkylblad till en ny arbetsbok. Båda metoderna är användbara när du behöver distribuera delmängder av data, skapa mindre rapporter för olika mottagare, eller isolera data för individuell bearbetning.

## **Introduktion**
Det finns många verkliga scenarier där en utvecklare behöver dela upp en enskild Excel-fil i flera mindre filer. Till exempel kan en arbetsbok innehålla ett kalkylblad per avdelning, och varje avdelningschef behöver bara få sitt eget blad. I andra fall kanske du vill extrahera en viss tabell eller datablock från ett kalkylblad och skicka den som en fristående fil via e-post, utan att exponera resten av arbetsboken. Stora konsoliderade arbetsböcker kan också behöva delas upp i mindre bitar för enklare hantering, snabbare laddning, eller vidarebearbetning av andra system.
Aspose.Cells erbjuder två flexibla metoder för denna uppgift. Den första metoden itererar genom varje kalkylblad i källarbetsboken och kopierar dess innehåll till en helt ny `Workbook`-instans, och sparar varje som en separat fil. Den andra metoden fokuserar på ett specifikt cellintervall i ett kalkylblad och kopierar bara det intervallet till en ny arbetsbok. I båda fallen är det allmänna flödet detsamma: ladda källarbetsboken med hjälp av `Workbook`-klassen, få åtkomst till relevant data genom `Worksheet`- och `Cells`-objekten, överför innehållet till en destinations-`Workbook`, och spara sedan destinationen till disk.

## **Dela upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok**

### **Metodöversikt**
I denna metod öppnas källarbetsboken en gång, och sedan skapas en ny destinations-`Workbook` för varje `Worksheet` i dess `Worksheets`-samling. Innehållet i källkalkylbladet kopieras sedan till det första kalkylbladet i destinationsarbetsboken, och destinationsarbetsboken sparas som en fil vars namn härleds från källkalkylbladets namn. Resultatet är en utdatafil per kalkylblad, där varje utdatafil innehåller data från ett enda källblad.
Denna metod är rätt val när varje kalkylblad i din källarbetsbok representerar en logiskt oberoende informationsenhet (till exempel en avdelning, region, månad eller produktlinje) och du vill leverera eller bearbeta varje enhet separat.

### **Steg**
Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera varje kalkylblad till en ny arbetsbok:
1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt och skicka filsökvägen till dess konstruktor.
2. Iterera genom `Workbook.Worksheets`-samlingen med hjälp av en `for`- eller `foreach`-loop så att varje `Worksheet` i källfilen bearbetas.
3. Inne i loopen, skapa en ny destinations-`Workbook`-instans (en tom arbetsbok) för det aktuella kalkylbladet.
5. Kopiera innehållet i källkalkylbladet till destinationskalkylbladet. Detta kan göras genom att iterera cellerna i källkalkylbladets `Cells`-samling och skriva deras värden till motsvarande celler i destinationskalkylbladet, eller genom att använda `Cells.copy`-metoden för att överföra ett helt intervall på en gång.
6. Konstruera en utdatafilsökväg som inkluderar källkalkylbladets namn (till exempel, `dataDir + worksheet.getName() + ".xls"`) så att varje genererad fil har ett unikt namn.
7. Anropa destinations-`Workbook.save`-metoden för att skriva filen till disk.
8. Upprepa steg 3 till 7 för nästa kalkylblad tills alla kalkylblad har bearbetats.

### **Kodexempel**

```java
import com.aspose.cells.*;
String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}
```

Den förväntade utdatan är en uppsättning nya filer i datakatalogen, en fil per kalkylblad från källarbetsboken. Varje fil är namngiven efter sitt motsvarande källblad, och filen innehåller data (och valfritt formatering) från det enskilda bladet.

## **Dela upp en Excel-fil genom att kopiera ett intervall till en ny arbetsbok**

### **Metodöversikt**
Ibland motsvarar inte datan du behöver dela upp ett helt kalkylblad utan snarare en specifik rektangulär region av ett kalkylblad, såsom `A1:D10` eller ett namngivet intervall som representerar en viss tabell. I dessa fall är det slösaktigt att kopiera hela kalkylblad, och en mer precis metod krävs: identifiera källintervallet, kopiera bara det intervallet till en ny arbetsbok, och spara den nya filen.
Denna metod är idealisk när du vill extrahera en enskild tabell, rapportblock eller dataområde från ett större kalkylblad medan du kasserar all orelaterat innehåll. Det är också användbart för att exportera användarvalda regioner av ett blad som fristående filer.

### **Steg**
Följande steg beskriver hur man delar upp en Excel-fil genom att kopiera ett specifikt intervall till en ny arbetsbok:
1. Öppna käll-Excel-filen genom att instansiera ett `Workbook`-objekt med filsökvägen.
2. Hämta mål-`Worksheet` som innehåller intervallet du vill kopiera, antingen via index (till exempel det första bladet) eller via namn från `Worksheets`-samlingen.
3. Identifiera intervallet som ska kopieras. Detta kan vara ett hårdkodat cellintervall såsom `A1:C10`, eller ett namngivet intervall erhållet genom `Worksheet.Cells`-samlingen, eller ett intervall skapat via `Worksheet.Cells.createRange`.
4. Skapa en ny destinations-`Workbook`-instans.
5. Få åtkomst till den första `Worksheet` i destinationsarbetsboken (standardbladet).
6. Kopiera källintervallet till destinationskalkylbladet, vanligtvis med början från cell `A1`. `Cells.copy`-metoden på destinations-`Cells`-samlingen kan användas för att kopiera ett helt intervall, eller så kan du iterera genom källintervallets celler och skriva deras värden till destinationscellerna med `putValue`. Valfria `CopyOptions` kan tillhandahållas för att styra vad som överförs (endast värden, värden och stilar, formler, och så vidare).
7. Spara destinationsarbetsboken till en ny filsökväg på disk med hjälp av `Workbook.save`-metoden.

### **Kodexempel**
Den förväntade utdatan är en enskild ny fil i datakatalogen som endast innehåller värdena (och valfritt formateringen) av det angivna intervallet extraherat från källarbetsboken. Destinationsfilen har ingen relation till någon annan data i källfilen; den innehåller bara det extraherade intervallet, med början från cell `A1` i sitt första kalkylblad.
{{% /alert %}}

## Relaterade artiklar
- [Lägg till filterfält i en pivottabell i Aspose.Cells for Java](/cells/sv/java/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for Java](/cells/sv/java/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/java/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Java](/cells/sv/java/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}