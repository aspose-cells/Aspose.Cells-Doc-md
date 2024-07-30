---
title: Kopiera och Flytta Kalkylblad
type: docs
weight: 10
url: /sv/python-net/copying-and-moving-worksheets/
description: Denna artikel inkluderar exempelkod och beskriver hur man kopierar och flyttar arkmallar programmatiskt både inom en Excel arbetsbok och mellan Excel arböcker med Aspose.Cells för Python API via .NET.
keywords: Python Excel Library, Python kopiera arkmall, Python flytta arkmall, Python kopiera arkmallar mellan arbetsböcker, Python flytta arkmallar inom en arbetsbok, Python kopiera arkmallar mellan arbetsböcker, Python kopiera arkmallar inom en arbetsbok.
---

{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med gemensam formatering och data. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det.

Aspose.Cells for Python via .NET stöder kopiering och flyttning av arkmallar inom eller mellan arbetsböcker. Arbetsblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta precision.

{{% /alert %}}

## **Hur man flyttar eller kopierar ark med hjälp av Microsoft Excel**

Följande steg är inblandade för att kopiera och flytta arksidor inom eller mellan arbetsböcker i Microsoft Excel.

1. För att flytta eller kopiera blad till en annan arbetsbok, öppna arbetsboken som kommer ta emot bladen.
1. Byt till arbetsboken som innehåller bladen du vill flytta eller kopiera, och välj sedan bladen.
1. På **Redigera**-menyn klickar du på **Flytta eller Kopiera Blad**.
1. I dialogrutan **Till bok** klicka på arbetsboken som ska ta emot sidorna.
1. För att flytta eller kopiera de valda sidorna till en ny arbetsbok, klicka på **Ny bok**.
1. I rutan **Innan blad** klickar du på det blad innan vilket du vill infoga de flyttade eller kopierade bladen.
1. För att kopiera bladen istället för att flytta dem, markera kryssrutan **Skapa en kopia**.

## **Hur man kopierar kalkylblad inom en arbetsbok med Aspose.Cells för Python Excel Library**

Aspose.Cells for Python via .NET tillhandahåller en överbelastad metod, [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str), som används för att lägga till ett kalkylblad i samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar indexet för källkalkylbladet som parameter. Den andra versionen tar namnet på källkalkylbladet.

Det följande exemplet visar hur man kopierar ett befintligt kalkylblad inom en arbetsbok.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Hur man kopierar kalkylblad mellan arbetsböcker**

Aspose.Cells for Python via .NET tillhandahåller en metod, [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet) använd för att kopiera data och formatering från ett källkalkylblad till ett annat kalkylblad inom eller mellan arbetsböcker. Metoden tar källkalkylbladsobjektet som parameter.

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Hur man flyttar kalkylblad inom arbetsboken**

Aspose.Cells for Python via .NET tillhandahåller en metod [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) som används för att flytta ett kalkylblad till en annan plats i samma kalkylblad. Metoden tar målkalkylbladets index som parameter.

Det följande exemplet visar hur man flyttar ett kalkylblad till en annan plats inom arbetsboken.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
