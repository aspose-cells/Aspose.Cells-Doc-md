---
title: Kopiera och Flytta Kalkylblad
type: docs
weight: 20
url: /sv/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

Ibland behöver du ett antal kalkylblad med gemensam formatering och data. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det.

Aspose.Cells stöder kopiering och flyttning av kalkylblad inom eller mellan arbetsböcker. Kalkylblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta precision.

{{% /alert %}} 
## **Flytta eller Kopiera Blad med Microsoft Excel**
Följande är stegen som är involverade i att kopiera och flytta kalkylblad inom eller mellan arbetsböcker.

1. Öppna arbetsboken som kommer att ta emot kalkylbladen.
1. Byt till arbetsboken som innehåller bladen du vill flytta eller kopiera, och välj sedan bladen.
1. På **Redigera**-menyn klickar du på **Flytta eller kopiera kalkylblad**.
1. I rutan Till bok klickar du på arbetsboken som ska ta emot bladen.
1. För att flytta eller kopiera de valda kalkylbladen till en ny arbetsbok, klicka på **ny bok**.
1. I rutan **Före kalkylblad** klickar du på kalkylarket före vilket du vill infoga de flyttade eller kopierade kalkylbladen.
1. För att kopiera kalkylbladen istället för att flytta dem väljer du kryssrutan **Skapa en kopia**.
### **Kopiera Kalkylblad inom en Arbetsbok**
Aspose.Cells tillhandahåller en överbelastad [WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) metoden som används för att kopiera ett befintligt kalkylblad. En version av metoden tar indexet för källkalkylbladet som parameter. Den andra versionen tar namnet på källkalkylbladet.

Det följande exemplet visar hur man kopierar ett befintligt kalkylblad inom en arbetsbok.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Kopiera Kalkylblad mellan Arbetsböcker**
Aspose.Cells tillhandahåller [Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) metoden som används för att kopiera kalkylblad till andra arbetsböcker. Metoden tar källkalkylbladsobjektet som parameter.

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Flytta Kalkylblad inom en Arbetsbok**
Aspose.Cells tillhandahåller [Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) metoden som används för att flytta ett kalkylblad till en annan plats i samma kalkylblad.

Det följande exemplet visar hur man flyttar ett kalkylblad till en annan plats inom arbetsboken.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
