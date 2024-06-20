---
title: Åtkomst till kalkylbladets celler
type: docs
weight: 10
url: /sv/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Vi vet att alla kalkylblad kan innehålla data som i huvudsak lagras i celler (med vilka ett kalkylblad är uppbyggt). En cell är en grundläggande del av ett kalkylblad som används för att konstruera hela kalkylbladet som en sekvens av rader och kolumner. Innan vi försöker få åtkomst till data från ett kalkylblad skulle vi behöva få åtkomst till dess celler. Så i det här ämnet kommer vi att diskutera några grundläggande tillvägagångssätt för att få åtkomst till kalkylbladets celler vid runtime med hjälp av Aspose.Cells.

{{% /alert %}} 
## **Åtkomst till celler**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) innehåller en samling [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller en samling [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) som representerar alla celler i kalkylbladet.

Vi kan använda [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen för att få åtkomst till celler i ett kalkylblad. Aspose.Cells tillhandahåller olika grundläggande tillvägagångssätt för att få åtkomst till celler:

1. [Använda cellnamn](/cells/sv/java/accessing-cells-of-a-worksheet/).
1. [Använda rad- och kolumnindex](/cells/sv/java/accessing-cells-of-a-worksheet/).
### **Användning av cellnamn**
Utvecklare kan få åtkomst till en specifik cell genom att ange dess cellnamn till [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen i klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Om du skapar ett tomt kalkylblad i början är antalet [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen noll. När du använder det här tillvägagångssättet för att få åtkomst till en cell kommer den att kontrollera om den här cellen finns i samlingen eller inte. Om ja returnerar den cellobjektet i samlingen annars skapar den en ny [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-objekt, lägger till objektet i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen och returnerar sedan objektet. Det här tillvägagångssättet är det enklaste sättet att få åtkomst till cellen om du är bekant med Microsoft Excel men det är långsammare än andra tillvägagångssätt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Användning av rad- och kolumnindex för cellen**
Utvecklare kan få åtkomst till en specifik cell genom att ange rad- och kolumnindex för cellen till [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen i klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Det här tillvägagångssättet fungerar på samma sätt som det första tillvägagångssättet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Relaterade artiklar**
{{% alert color="primary" %}} 

- [Namngivna områden](/cells/sv/java/named-ranges/)

{{% /alert %}} 
## **Åtkomst till kalkylbladets maximala visningsområde**
Aspose.Cells tillåter utvecklare att få åtkomst till ett kalkylblads maximala visningsområde. Det maximala visningsområdet - området av celler mellan den första och den sista cellen med innehåll - är användbart när du behöver kopiera, välja eller visa hela innehållet i ett kalkylblad i en bild.

Du kan få åtkomst till ett kalkylblads maximala visningsområde genom att använda [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

I följande figur är det valda kalkylbladets maximala visningsområde A1:G15.

**Visar det maximala visningsområdet för detta kalkylblad** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

Följande exempelkod illustrerar hur man får åtkomst till egenskapen [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange). Koden genererar följande utmatning.

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
