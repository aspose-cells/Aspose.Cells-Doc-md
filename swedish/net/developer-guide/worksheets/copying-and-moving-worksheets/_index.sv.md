---
title: Kopiera och Flytta Kalkylblad
type: docs
weight: 10
url: /sv/net/copying-and-moving-worksheets/
description: Den här artikeln innehåller exempelkod och beskriver hur du kan kopiera och flytta arksidor programmatiskt både inom en Excel arbetsbok och mellan Excel arbetsböcker med hjälp av C# API eller .NET bibliotek.
keywords: kopiera arksida c#, flytta arksida c#
---

{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med gemensam formatering och data. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det.

Aspose.Cells stöder kopiering och flyttning av kalkylblad inom eller mellan arbetsböcker. Kalkylblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta precision.

{{% /alert %}}

## **Flytta eller Kopiera Blad med Microsoft Excel**

Följande steg är inblandade för att kopiera och flytta arksidor inom eller mellan arbetsböcker i Microsoft Excel.

1. För att flytta eller kopiera blad till en annan arbetsbok, öppna arbetsboken som kommer ta emot bladen.
1. Byt till arbetsboken som innehåller bladen du vill flytta eller kopiera, och välj sedan bladen.
1. På **Redigera**-menyn klickar du på **Flytta eller Kopiera Blad**.
1. I dialogrutan **Till bok** klicka på arbetsboken som ska ta emot sidorna.
1. För att flytta eller kopiera de valda sidorna till en ny arbetsbok, klicka på **Ny bok**.
1. I rutan **Innan blad** klickar du på det blad innan vilket du vill infoga de flyttade eller kopierade bladen.
1. För att kopiera bladen istället för att flytta dem, markera kryssrutan **Skapa en kopia**.

### **Kopiera Arksidor inom en Arbetsbok med Aspose.Cells**

Aspose.Cells tillhandahåller en överbelastad metod, [**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index), som används för att lägga till ett kalkylblad i samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar indexet för källkalkylbladet som parameter. Den andra versionen tar namnet på källkalkylbladet.

Det följande exemplet visar hur man kopierar ett befintligt kalkylblad inom en arbetsbok.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **Kopiera Kalkylblad mellan Arbetsböcker**

Aspose.Cells tillhandahåller en metod, [**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) som används för att kopiera data och formatering från ett källkalkylblad till ett annat kalkylblad inom eller mellan arbetsböcker. Metoden tar källkalkylbladsobjektet som parameter.

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **Flytta Kalkylblad inom en Arbetsbok**

Aspose.Cells erbjuder en metod [**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto) som används för att flytta ett kalkylblad till en annan plats i samma kalkylblad. Metoden tar målkalkylbladets index som parameter.

Det följande exemplet visar hur man flyttar ett kalkylblad till en annan plats inom arbetsboken.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
