---
title: Skapa delsummor
type: docs
weight: 50
url: /sv/java/creating-subtotals/
---
{{% alert color="primary" %}}

Du kan automatiskt skapa delsummor för alla återkommande värden i ett kalkylblad. Aspose.Cells tillhandahåller API-funktioner som hjälper dig att lägga till delsummor till kalkylprogram programmatiskt.

{{% /alert %}}

## **Använder Microsoft Excel**

Så här skapar du delsummor i Microsoft Excel:

1. Skapa en enkel datalista i det första kalkylbladet i arbetsboken (som visas i figuren nedan) och spara filen som Book1.xls.
1. Välj valfri cell i listan.
1.  Från**Data** menyn, välj**Delsummor**.
 Dialogrutan Delsummor visas. Definiera vilken funktion som ska användas och var delsummorna ska placeras.

   **Välja ett dataintervall för att lägga till delsummor**

![todo:image_alt_text](creating-subtotals_1.png)

**Dialogrutan Delsumma** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Använder Aspose.Cells API**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass. Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad och andra objekt. Varje arbetsblad består av en[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. För att skapa delsummor i ett kalkylblad, använd[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)klassens subtotalmetod. Ange lämpliga värden för parametrarna för metoden för att få det resultat du vill ha.

Exemplet nedan visar hur man skapar delsummor i det första kalkylbladet i mallfilen (Book1.xls) med Aspose.Cells API.

När koden körs skapas ett kalkylblad med delsummor.

**Tillämpa delsummor** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
