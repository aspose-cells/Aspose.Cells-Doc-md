---
title: Åtkomst till Cells i ett arbetsblad
type: docs
weight: 10
url: /sv/net/accessing-cells-of-a-worksheet/
description: Den här artikeln visar hur du får det maximala visningsintervallet för kalkylblad och åtkomstceller via Aspose.Cells for .NET API.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

Vi vet att alla kalkylblad kan innehålla data som i princip lagras i celler (som ett kalkylblad är uppbyggt av). En cell är en grundläggande del av ett kalkylblad som används för att konstruera hela kalkylbladet som en sekvens av rader och kolumner. Innan vi försöker komma åt data från ett kalkylblad skulle vi behöva få tillgång till dess celler. Så i det här ämnet kommer vi att diskutera några grundläggande metoder för att komma åt kalkylbladsceller vid körning med Aspose.Cells.

{{% /alert %}}

##  **Så här kommer du åt Cells**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling som representerar alla celler i kalkylbladet.

 Vi kan använda[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling för att komma åt celler i ett kalkylblad. Aspose.Cells tillhandahåller tre grundläggande metoder för att komma åt celler i ett kalkylblad:

1. Använder cellnamnet.
1. Använda en cells rad- och kolumnindex.
1.  Använda ett cellindex i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling

**VIKTIG:**Vi har nämnt att den tredje inflygningen är den snabbaste och den första är den långsammaste. Prestandaskillnaden mellan tillvägagångssätten är mycket liten, så oroa dig inte för prestandaförsämring, vilket tillvägagångssätt du än använder.

###  **Hur man får Cell Objekt av Cell Namn**

 Utvecklare kan komma åt vilken specifik cell som helst genom att skicka dess cellnamn till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass som ett index.

 Om du skapar ett tomt kalkylblad i början kommer antalet[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samlingen är noll. När du använder det här tillvägagångssättet för att komma åt en cell, kommer den att kontrollera om denna cell finns i samlingen eller inte. Om ja, returnerar den cellobjektet i samlingen annars skapar den ett nytt[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objekt, lägger till objektet till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling och returnerar sedan objektet. Detta tillvägagångssätt är det enklaste sättet att komma åt cellen om du är bekant med Microsoft Excel, men det är det långsammaste sättet jämfört med andra metoder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **Hur man får Cell objekt efter rad och kolumn Index för Cell**

 Utvecklare kan komma åt vilken specifik cell som helst genom att skicka indexen för dess rad och kolumn till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass.

Detta tillvägagångssätt fungerar på samma sätt som det första tillvägagångssättet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **Så här får du Cell Objekt av Cell Index i Cells samling**

 En cell kan också nås genom att skicka cellens numeriska index till[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling.

Om du använder det här tillvägagångssättet för att komma åt celler kan ett undantag skapas om cellens numeriska index ligger utanför intervallet. Detta tillvägagångssätt är det snabbaste för att komma åt cellerna men en viktig sak att veta är att om du använder den här metoden för att komma åt ett cellobjekt, kan det numeriska indexet ändras efter att nya celler läggs till i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling. Cellobjekten i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samlingen är internt sorterad efter rad- och kolumnindex.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **Så här får du maximalt visningsområde för arbetsblad**

Aspose.Cells tillåter utvecklare att komma åt ett kalkylblads maximala visningsområde. Det maximala visningsintervallet - cellintervallet mellan den första och sista cellen med innehåll - är användbart när du behöver kopiera, markera eller visa hela innehållet i ett kalkylblad i en bild.

Du kan komma åt ett kalkylblads maximala visningsområde med[**Arbetsblad.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . Följande exempelkod illustrerar hur du kommer åt[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
