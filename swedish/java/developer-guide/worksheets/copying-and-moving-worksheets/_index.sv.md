---
title: Kopiera och Flytta Kalkylblad
type: docs
weight: 20
url: /sv/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med gemensam formatering och data. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det.

Aspose.Cells stöder kopiering och flyttning av kalkylblad inom eller mellan arbetsböcker. Kalkylblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta precision.

{{% /alert %}}

## **Flytta eller Kopiera Blad med Microsoft Excel**

Följande är stegen för att kopiera och flytta kalkylblad inom eller mellan arbetsböcker.

1. För att flytta eller kopiera blad till en annan arbetsbok, öppna arbetsboken som kommer ta emot bladen.
1. Byt till arbetsboken som innehåller bladen du vill flytta eller kopiera, och välj sedan bladen.
1. På **Redigera**-menyn klickar du på **Flytta eller Kopiera Blad**.
1. I rutan Till bok klickar du på arbetsboken som ska ta emot bladen.
1. För att flytta eller kopiera de valda bladen till en ny arbetsbok, klicka på **Ny bok**.
1. I rutan **Innan blad** klickar du på det blad innan vilket du vill infoga de flyttade eller kopierade bladen.
1. För att kopiera bladen istället för att flytta dem, markera kryssrutan **Skapa en kopia**.

## **Kopiera Kalkylblad inom en Arbetsbok**

Aspose.Cells tillhandahåller en överbelastad metod, [**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), som används för att lägga till ett kalkylblad i samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar indexet för källkalkylbladet som parameter. Den andra versionen tar namnet på källkalkylbladet.

Det följande exemplet visar hur man kopierar ett befintligt kalkylblad inom en arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Kopiera Kalkylblad mellan Arbetsböcker**

Aspose.Cells tillhandahåller en metod, [**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), som används för att kopiera data och formatering från ett källkalkylblad till ett annat kalkylblad inom eller mellan arbetsböckerna. Metoden tar källkalkylbladet objekt som parameter.

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Flytta Kalkylblad inom en Arbetsbok**

Aspose.Cells tillhandahåller en metod, [**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), används för att flytta ett kalkylblad till en annan plats i samma kalkylblad.

Det följande exemplet visar hur man flyttar ett kalkylblad till en annan plats inom arbetsboken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
