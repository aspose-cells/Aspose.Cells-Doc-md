---
title: Åtkomst till kalkylbladets celler
type: docs
weight: 10
url: /sv/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Vi vet att alla kalkylblad kan innehålla data som i huvudsak lagras i celler (med vilka ett kalkylblad är uppbyggt). En cell är en grundläggande del av ett kalkylblad som används för att konstruera hela kalkylbladet som en sekvens av rader och kolumner. Innan vi försöker få åtkomst till data från ett kalkylblad skulle vi behöva få åtkomst till dess celler. Så i det här ämnet kommer vi att diskutera några grundläggande tillvägagångssätt för att få åtkomst till kalkylbladets celler vid runtime med hjälp av Aspose.Cells.

{{% /alert %}} 
## **Åtkomst till celler**
Aspose.Cells tillhandahåller en klass [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling som representerar alla celler i kalkylbladet.

Vi kan använda [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen för att nå celler i ett kalkylblad. Aspose.Cells tillhandahåller tre grundläggande tillvägagångssätt för att nå celler i ett kalkylblad:

1. Genom att använda cellnamn.
2. Genom att använda cellens rad- och kolumnindex.
1. Använda en cellindex i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen.

{{% alert color="primary" %}} 

1. Genom att använda en cellindex i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen

{{% /alert %}} 
### **Användning av cellnamn**
Vi har nämnt att det tredje tillvägagångssättet är det snabbaste och det första tillvägagångssättet är det långsammaste. Skillnaden i prestanda mellan tillvägagångssätten är mycket liten så oroa dig inte för prestandaförsämring, oavsett vilket tillvägagångssätt du använder.

Om du skapar en tom kalkylblad i början är räkningen av [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) kollektionen noll. När du använder detta tillvägagångssätt för att komma åt en cell, kommer den att kontrollera om denna cell finns i samlingen eller inte. Om ja, returnerar den cellobjektet i samlingen annars skapar den en ny [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) objekt, lägger till objektet i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen och returnerar sedan det objektet. Detta tillvägagångssätt är det enklaste sättet att komma åt cellen om du är bekant med Microsoft Excel men det är det långsammaste som jämfört med andra tillvägagångssätt.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **Användning av rad- och kolumnindex för cellen**
Utvecklare kan komma åt vilken specifik cell som helst genom att skicka in indexen för dess rad och kolumn till [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen av [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. Detta tillvägagångssätt fungerar på samma sätt som det första tillvägångssättet.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **Åtkomst till kalkylbladets maximala visningsområde**
Aspose.Cells tillåter utvecklare att komma åt ett kalkylblads maximala visningsområde. Det maximala visningsområdet - området för celler mellan den första och sista cellen med innehåll - är användbart när du behöver kopiera, välja eller visa hela innehållet på ett kalkylblad i en bild.

Du kan komma åt ett kalkylblads maximala visningsområde med hjälp av [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) metoden i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
