---
title: Skapar delsummer
type: docs
weight: 50
url: /sv/java/creating-subtotals/
---

{{% alert color="primary" %}}

Du kan automatiskt skapa delsummer för alla upprepningsvärden i ett kalkylblad. Aspose.Cells tillhandahåller API-funktioner som hjälper dig lägga till delsummor i kalkylblad programmatiskt.

{{% /alert %}}

## **Använda Microsoft Excel**

För att skapa delsummor i Microsoft Excel:

1. Skapa en enkel datalista i det första arbetsbladet i arbetsboken (som visas i figuren nedan) och spara filen som Book1.xls.
1. Välj valfri cell i listan.
1. Från **Data**-menyn väljer du **Delsummor**.
   Dialogrutan Delsummor visas. Definiera vilken funktion som ska användas och var delsummorna ska placeras.

   **Välja ett datintervall för att lägga till delsummor**

![todo:image_alt_text](creating-subtotals_1.png)

**Dialogruta för delsummer** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Använda Aspose.Cells API**

Aspose.Cells tillhandahåller en klass, {0 som representerar en Microsoft Excel-fil. {1}klassen innehåller en {2}som ger åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klassen. Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad och andra objekt. Varje kalkylblad består av en [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling. För att skapa delsummor i ett kalkylblad, använd [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)klassens subtotal-metod. Ange lämpliga värden för metodens parametrar för att få önskat resultat.

Exemplet nedan visar hur du skapar delsummor i det första kalkylbladet i mallfilen (Book1.xls) med Aspose.Cells API.

När koden körs skapas ett kalkylblad med delsummor.

**Tillämpa delsummor** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
