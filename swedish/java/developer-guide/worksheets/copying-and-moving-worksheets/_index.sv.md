---
title: Kopiera och flytta arbetsblad
type: docs
weight: 20
url: /sv/java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med vanlig formatering och data. Om du till exempel arbetar med kvartalsbudgetar kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett ark och sedan kopiera det.

Aspose.Cells stöder kopiering och flyttning av kalkylblad inom eller mellan arbetsböcker. Arbetsblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta precision.

{{% /alert %}}

## **Flytta eller kopiera ark med Microsoft Excel**

Nedan följer stegen för att kopiera och flytta kalkylblad i eller mellan arbetsböcker.

1. För att flytta eller kopiera ark till en annan arbetsbok, öppna arbetsboken som ska ta emot arken.
1. Växla till arbetsboken som innehåller de ark du vill flytta eller kopiera och välj sedan arken.
1.  På**Redigera** menyn, klicka**Flytta eller kopiera ark**.
1. I rutan Till bok klickar du på arbetsboken för att ta emot arken.
1.  För att flytta eller kopiera de markerade arken till en ny arbetsbok, klicka**ny bok**.
1.  I den**Före ark** klickar du på arket innan du vill infoga de flyttade eller kopierade arken.
1.  Om du vill kopiera arken istället för att flytta dem väljer du**Skapa en kopia** kryssruta.

## **Kopiera arbetsblad i en arbetsbok**

 Aspose.Cells tillhandahåller en överbelastad metod,[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), som används för att lägga till ett kalkylblad till samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar källarkets index som en parameter. Den andra versionen tar namnet på källarbetsbladet.

Följande exempel visar hur man kopierar ett befintligt kalkylblad i en arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Kopiera arbetsblad mellan arbetsböcker**

 Aspose.Cells tillhandahåller en metod,[**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), används för att kopiera data och formatering från ett källark till ett annat kalkylblad inom eller mellan arbetsböckerna. Metoden tar källarksobjektet som en parameter.

Följande exempel visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

Följande exempel visar hur man kopierar ett kalkylblad från en arbetsbok till en annan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Flytta kalkylblad i arbetsboken**

 Aspose.Cells tillhandahåller en metod,[**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), används för att flytta ett kalkylblad till en annan plats i samma kalkylblad.

Följande exempel visar hur du flyttar ett kalkylblad till en annan plats i arbetsboken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
