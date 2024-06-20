---
title: Skapar delsummer
type: docs
weight: 800
url: /sv/python-net/creating-subtotals/
description: Lär dig hur man skapar delsummer för eventuella återkommande värden i ett kalkylblad genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Tillämpa delsummor, Ange delsummor, Lägg till delsummor, Skapa delsummor, Hur man lägger till delsummor i ett kalkylblad 
---

{{% alert color="primary" %}}

Du kan automatiskt skapa delsummor för eventuella återkommande värden i ett kalkylblad. Aspose.Cells for Python via .NET tillhandahåller API-funktioner som hjälper dig att lägga till delsummor i kalkylblad programmatiskt.

{{% /alert %}}

## **Använda Microsoft Excel**

För att lägga till delsummer i Microsoft Excel:

1. Skapa en enkel datalista i det första arbetsbladet i arbetsboken (som visas i figuren nedan) och spara filen som Book1.xls.
1. Välj valfri cell i listan.
1. Från **Data**-menyn väljer du **Delsummer**. Delsummerdialogrutan visas. Ange vilken funktion som ska användas och var delsummer ska placeras.

## **Använda Aspose.Cells for Python via .NET API**

Aspose.Cells for Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen. Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad och andra objekt. Varje arbetsblad består av en [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samling. För att lägga till delsummer till ett arbetsblad, använd [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-klassens [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list)-metod. Ange metoden med parameter värden för att specificera hur delsumman ska beräknas och placeras.

I exemplen nedan har vi lagt till delsummor i det första kalkylbladet i mallfilen (Book1.xls) med hjälp av Aspose.Cells for Python via .NET API. När koden körs skapas ett kalkylblad med delsummor.

De kodsnuttar som följer visar hur man lägger till delsummor i ett kalkylblad med Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **Fortsatta ämnen**
- [Tillämpa delsumma och ändra riktningen för sammanfattande rader nedanför detaljer](/cells/sv/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
