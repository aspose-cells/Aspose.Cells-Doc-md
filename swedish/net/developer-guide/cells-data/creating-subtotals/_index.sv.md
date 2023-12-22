---
title: Skapa delsummor
type: docs
weight: 800
url: /sv/net/creating-subtotals/
description: Lär dig hur du skapar delsummor för återkommande värden i ett kalkylblad genom att använda Aspose.Cells for .NET API.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---
{{% alert color="primary" %}}

Du kan automatiskt skapa delsummor för alla återkommande värden i ett kalkylblad. Aspose.Cells tillhandahåller API-funktioner som hjälper dig att lägga till delsummor till kalkylark programmatiskt.

{{% /alert %}}

##  **Använder Microsoft Excel**

Så här lägger du till delsummor i Microsoft Excel:

1. Skapa en enkel datalista i det första kalkylbladet i arbetsboken (som visas i figuren nedan) och spara filen som Book1.xls.
1. Välj valfri cell i listan.
1.  Från**Data** menyn, välj *Delsummor**. Dialogrutan Delsummor kommer att visas. Definiera vilken funktion som ska användas och var delsummorna ska placeras.

##  **Använder Aspose.Cells API**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i Excel-filen.

Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad och andra objekt. Varje arbetsblad består av en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling. För att lägga till delsummor till ett kalkylblad, använd[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)klass'[**Delsumma**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)metod. Ange parametervärden till metoden för att specificera hur delsumman ska beräknas och placeras.

I exemplen nedan har vi lagt till delsummor till det första kalkylbladet i mallfilen (Book1.xls) med hjälp av Aspose.Cells API. När koden exekveras skapas ett kalkylblad med delsummor.

Kodavsnitten som följer visar hur man lägger till delsummor till ett kalkylblad med Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

##  **Förhandsämnen**
- [Tillämpa delsumma och ändra riktning på kontursammanfattningsraderna under detalj](/cells/sv/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
