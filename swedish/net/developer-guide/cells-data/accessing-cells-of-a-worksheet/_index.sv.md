---
title: Åtkomst till kalkylbladets celler
type: docs
weight: 10
url: /sv/net/accessing-cells-of-a-worksheet/
description: Denna artikel visar hur man får det maximala visningsområdet för arbetsblad och får åtkomst till celler via Aspose.Cells for .NET API et.
keywords: Få Cell objekt, Åtkomst till celler, Få maximalt visningsområde på arbetsbladet. 
---

{{% alert color="primary" %}}

Vi vet att alla kalkylblad kan innehålla data som i huvudsak lagras i celler (med vilka ett kalkylblad är uppbyggt). En cell är en grundläggande del av ett kalkylblad som används för att konstruera hela kalkylbladet som en sekvens av rader och kolumner. Innan vi försöker få åtkomst till data från ett kalkylblad skulle vi behöva få åtkomst till dess celler. Så i det här ämnet kommer vi att diskutera några grundläggande tillvägagångssätt för att få åtkomst till kalkylbladets celler vid runtime med hjälp av Aspose.Cells.

{{% /alert %}}

## **Hur man får åtkomst till celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling som representerar alla celler i arbetsbladet.

Vi kan använda [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen för att få åtkomst till celler i ett arbetsblad. Aspose.Cells tillhandahåller tre grundläggande metoder för att få åtkomst till celler i ett arbetsblad:

1. Genom att använda cellnamnet.
2. Genom att använda cellens rad- och kolumnindex.
3. Genom att använda en cellindex i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen

**Viktigt:** Vi har nämnt att den 3:e metoden är den snabbaste och den 1:a metoden är den långsammaste. Skillnaden i prestanda mellan metoderna är mycket liten så oroa dig inte för prestandaförsämring, oavsett vilken metod du använder.

### **Hur man får Cell-objekt genom Cellnamn**

Utvecklare kan få åtkomst till en specifik cell genom att skicka dess cellnamn till [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen som en index.

Om du skapar ett tomt arbetsblad i början är antalet [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling noll. När du använder den här metoden för att få åtkomst till en cell kontrolleras det om cellen finns i samlingen eller inte. Om ja, returnerar den cellobjektet i samlingen annars skapar den en ny [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-objekt, lägger till objektet i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen och returnerar sedan objektet. Den här metoden är det enklaste sättet att få åtkomst till cellen om du är bekant med Microsoft Excel men det är det långsammaste som jämfört med andra metoder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Hur man får Cell-objekt genom rad- och kolumnindex för cellen**

Utvecklare kan komma åt en specifik cell genom att skicka rad- och kolumnindex till [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen.

Det här tillvägagångssättet fungerar på samma sätt som det första tillvägagångssättet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Hur man får cellobjekt efter cellindex i cellsamlingen**

En cell kan också kommas åt genom att skicka cellens numeriska index till [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen.

Om du använder detta tillvägagångssätt för att komma åt celler kan ett undantag kastas om cellens numeriska index är utanför intervallet. Detta tillvägagångssätt är det snabbaste sättet att komma åt cellerna, men en viktig sak att veta är att om du använder detta tillvägagångssätt för att komma åt ett cellobjekt kan det numeriska indexet ändras efter att nya celler har lagts till i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen. Cellobjekten i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samlingen sorteras internt efter rad- och kolumnindex.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Hur man får maximal visningsområde för arbetsblad**

Aspose.Cells tillåter utvecklare att få åtkomst till ett kalkylblads maximala visningsområde. Det maximala visningsområdet - området av celler mellan den första och den sista cellen med innehåll - är användbart när du behöver kopiera, välja eller visa hela innehållet i ett kalkylblad i en bild.

Du kan komma åt ett arbetsblads maximala visningsområde med hjälp av [**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange). Följande exempelkod illustrerar hur du kommer åt [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)-egenskapen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
