---
title: Kopiera och flytta arbetsblad
type: docs
weight: 10
url: /sv/cpp/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Ibland behöver du ett antal kalkylblad med vanlig formatering och data. Om du till exempel arbetar med kvartalsbudgetar kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett ark och sedan kopiera det.

Aspose.Cells stöder kopiering och flyttning av kalkylblad inom eller mellan arbetsböcker. Ett kalkylblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta precision.

{{% /alert %}} 
##  **Flytta eller kopiera ark med Microsoft Excel**
Följande är stegen för att kopiera och flytta kalkylblad i eller mellan arbetsböcker i Microsoft Excel.

1. För att flytta eller kopiera ark till en annan arbetsbok, öppna arbetsboken som ska ta emot arken.
1. Växla till arbetsboken som innehåller de ark du vill flytta eller kopiera och välj sedan arken.
1.  På**Redigera** menyn, klicka på *Flytta eller kopiera blad**.
1.  den**Att boka** klickar du på arbetsboken för att ta emot arken.
1. För att flytta eller kopiera de markerade arken till en ny arbetsbok, klicka på *Ny bok**.
1.  den**Före ark** klickar du på arket innan du vill infoga de flyttade eller kopierade arken.
1.  Om du vill kopiera arken istället för att flytta dem väljer du**Skapa en kopia** kryssruta.
###  **Kopiera arbetsblad i en arbetsbok med Aspose.Cells**
 Aspose.Cells tillhandahåller en överbelastad metod[AddCopy()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/addcopy/)som används för att lägga till ett kalkylblad till samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar källarkets index som en parameter. Den andra versionen tar namnet på källarbetsbladet. Följande exempel visar hur man kopierar ett befintligt kalkylblad i en arbetsbok.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-CopyWorksheetsWithinWorkbook-new.cpp" >}}
###  **Flytta kalkylblad i arbetsboken**
 Aspose.Cells tillhandahåller en metod[MoveTo()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/moveto/)som används för att flytta ett kalkylblad till en annan plats i samma kalkylblad. Metoden tar målkalkylbladets index som en parameter. Följande exempel visar hur du flyttar ett kalkylblad till en annan plats i arbetsboken.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-CopyingAndMovingWorksheets-MoveWorksheetsWithinWorkbook-new.cpp" >}}
