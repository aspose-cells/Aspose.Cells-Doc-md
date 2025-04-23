---
title: Skapar delsummer
type: docs
weight: 800
url: /sv/nodejs-cpp/creating-subtotals/
description: Lär dig hur man skapar delsumma för vilka som helst återkommande värden i ett kalkylblad genom att använda API n Aspose.Cells for Node.js via C++.
keywords: Applicera delsummer, Ange delsummer, Lägg till delsummer, Skapa delsummer, Hur man lägger till delsummer till ett arbetsblad 
---

{{% alert color="primary" %}}

Du kan automatiskt skapa delsumma för vilka som helst återkommande värden i ett kalkylblad. Aspose.Cells for Node.js via C++ erbjuder API-funktioner som hjälper dig att lägga till delsumma till kalkylblad programkodsmässigt.

{{% /alert %}}

## **Använda Microsoft Excel**

För att lägga till delsummer i Microsoft Excel:

1. Skapa en enkel datalista i det första arbetsbladet i arbetsboken (som visas i figuren nedan) och spara filen som Book1.xls.
1. Välj valfri cell i listan.
1. Från **Data**-menyn väljer du **Delsummer**. Delsummerdialogrutan visas. Ange vilken funktion som ska användas och var delsummer ska placeras.

## **Använda API:n Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) samling som ger tillgång till varje arbetsblad i Excel-filen.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. Klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad och andra objekt. Varje arbetsblad består av en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling. För att lägga till delsummer till ett arbetsblad, använd [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-klassens [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-)-metod. Ange metoden med parameter värden för att specificera hur delsumman ska beräknas och placeras.

I exemplen nedan har vi lagt till delsumma till det första arbetsbladet i [mallfilen](book1.xlsx) med hjälp av API:n Aspose.Cells for Node.js via C++. När koden körs skapas ett arbetsblad med delsumma.

Följande kodbitar visar hur man lägger till delsumma till ett arbetsblad med Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

