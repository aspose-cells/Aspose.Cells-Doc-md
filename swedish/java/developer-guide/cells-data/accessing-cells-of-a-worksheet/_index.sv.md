---
title: Åtkomst till Cells i ett arbetsblad
type: docs
weight: 10
url: /sv/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Vi vet att alla kalkylblad kan innehålla data som i princip lagras i celler (som ett kalkylblad är uppbyggt av). En cell är en grundläggande del av ett kalkylblad som används för att konstruera hela kalkylbladet som en sekvens av rader och kolumner. Innan vi försöker komma åt data från ett kalkylblad skulle vi behöva få tillgång till dess celler. Så i det här ämnet kommer vi att diskutera några grundläggande metoder för att komma åt kalkylbladsceller vid körning med Aspose.Cells.

{{% /alert %}} 
## **Tillgång till Cells**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling som representerar alla celler i kalkylbladet.

 Vi kan använda[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling för att komma åt celler i ett kalkylblad. Aspose.Cells tillhandahåller olika grundläggande metoder för åtkomst till celler:

1. [Använder cellnamn](/cells/sv/java/accessing-cells-of-a-worksheet/).
1. [Använder rad- och kolumnindex](/cells/sv/java/accessing-cells-of-a-worksheet/).
### **Använder Cell Namn**
 Utvecklare kan komma åt vilken specifik cell som helst genom att skicka dess cellnamn till[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass.

 Om du skapar ett tomt kalkylblad i början kommer antalet[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samlingen är noll. När du använder det här tillvägagångssättet för att komma åt en cell, kommer den att kontrollera om denna cell finns i samlingen eller inte. Om ja, returnerar den cellobjektet i samlingen annars skapar den ett nytt[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) objekt, lägger till objektet till[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling och returnerar sedan objektet. Detta tillvägagångssätt är det enklaste sättet att komma åt cellen om du är bekant med Microsoft Excel, men det är långsammare än andra metoder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Använda rad- och kolumnindex för Cell**
 Utvecklare kan komma åt vilken specifik cell som helst genom att skicka indexen för dess rad och kolumn till[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass.

Detta tillvägagångssätt fungerar på samma sätt som det första tillvägagångssättet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **relaterade artiklar**
{{% alert color="primary" %}} 

- [Namngivna Ranges](/cells/sv/java/named-ranges/)

{{% /alert %}} 
## **Få åtkomst till maximalt visningsområde för arbetsblad**
Aspose.Cells tillåter utvecklare att komma åt ett kalkylblads maximala visningsområde. Det maximala visningsintervallet - cellintervallet mellan den första och sista cellen med innehåll - är användbart när du behöver kopiera, markera eller visa hela innehållet i ett kalkylblad i en bild.

 Du kan komma åt ett kalkylblads maximala visningsområde med[Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

I följande figur är det valda arbetsbladets maximala visningsområde A1:G15.

**Visar det maximala visningsintervallet för detta kalkylblad** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

 Följande exempelkod illustrerar hur du kommer åt[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)fast egendom. Koden genererar följande utdata.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
