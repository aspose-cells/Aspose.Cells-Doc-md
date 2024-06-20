---
title: Inställningar för arbetsbok
type: docs
weight: 250
url: /sv/net/aspose-cells-gridweb/aspose-cells-gridweb/workbook-settings/
description: Den här artikeln beskriver arbetsboksinställningarna i GridWeb.
keywords: GridWeb, inställningar
---


Det finns några inställningar vi kan ange genom att ange GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/GridWorkbookSettings)

| **Namn** | **Beskrivning** |
| :- | :- |
|MaxIteration |Får eller ställer in det maximala antalet iterationer för att lösa en cirkulär referens, standardvärdet är 100. |
|Iteration | Får eller ställer in om använda iteration för att lösa cirkulära referenser. |
|ForceFullCalculate | Får eller ställer in om fullständigt beräknar varje gång när en beräkning utlöses. |
|CreateCalcChain | Hämtar eller anger om beräknade formler ska skapas. Standard är falskt. |
|ReCalculateOnOpen | Hämtar eller anger om alla formler ska räknas om vid öppning av filen. |
|PrecisionAsDisplayed | Sant om beräkningar i arbetsboken kommer att göras med endast precisionen av siffrorna som de visas |
|Date1904 | Hämtar eller anger ett värde som representerar om arbetsboken använder det 1904 datum systemet. |
|CheckCustomNumberFormat | Hämtar eller anger om kontroll av anpassat nummerformat när inställning av Style.Custom. |
|Author | Hämtar och anger författaren av filen. |



Till exempel, följande kod ställer ReCalculateOnOpen till falskt för att stoppa beräkningen vid öppning av filen :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-ReCalculateOnOpen.cs" >}}

 följande kod ställer in författaren för filen :

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "GridWorkbookSettings-Author.cs" >}}


