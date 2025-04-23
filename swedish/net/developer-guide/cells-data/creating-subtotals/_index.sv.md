---
title: Skapar delsummer
type: docs
weight: 800
url: /sv/net/creating-subtotals/
description: Lär dig hur du skapar delsummer för vilka återkommande värden som helst i en kalkyl genom att använda Aspose.Cells for .NET API.
keywords: Applicera delsummer, Ange delsummer, Lägg till delsummer, Skapa delsummer, Hur man lägger till delsummer till ett arbetsblad 
---

{{% alert color="primary" %}}

Du kan automatiskt skapa delsummer för vilka återkommande värden som helst i en kalkyl. Aspose.Cells tillhandahåller API-funktioner som hjälper dig att lägga till delsummer till kalkylblad programmatiskt.

{{% /alert %}}

## **Använda Microsoft Excel**

För att lägga till delsummer i Microsoft Excel:

1. Skapa en enkel datalista i det första arbetsbladet i arbetsboken (som visas i figuren nedan) och spara filen som Book1.xls.
1. Välj valfri cell i listan.
1. Från **Data**-menyn väljer du **Delsummer**. Delsummerdialogrutan visas. Ange vilken funktion som ska användas och var delsummer ska placeras.

## **Använda Aspose.Cells API**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som tillåter åtkomst till varje arbetsblad i Excel-filen.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad och andra objekt. Varje arbetsblad består av en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling. För att lägga till delsummer till ett arbetsblad, använd [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-klassens [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index)-metod. Ange metoden med parameter värden för att specificera hur delsumman ska beräknas och placeras.

I exemplen nedan har vi lagt till delsummer i det första arbetsbladet i mallfilen (Book1.xls) med hjälp av Aspose.Cells API. När koden körs skapas ett arbetsblad med delsummor.

De kodsnuttar som följer visar hur man lägger till delsummer till ett arbetsblad med Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Fortsatta ämnen**
- [Tillämpa delsumma och ändra riktningen för sammanfattande rader nedanför detaljer](/cells/sv/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
{{< app/cells/assistant language="csharp" >}}
