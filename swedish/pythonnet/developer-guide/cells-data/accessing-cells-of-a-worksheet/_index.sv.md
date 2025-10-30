---
title: Åtkomst till kalkylbladets celler
type: docs
weight: 10
url: /sv/python-net/accessing-cells-of-a-worksheet/
description: Den här artikeln visar hur man får det maximala visningsområdet för arbetsbladet och får åtkomst till celler genom Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Hämta Cell objekt, Åtkomst till celler, Hur man får Cell objekt genom rad och kolumnindex för cellen, Hur man får Cell objekt genom cellindex i cellinsamlingen, Hur man får Cell objekt genom rad och kolumnindex för cellen, Få maximalt visningsområde för arbetsbladet. 
---

{{% alert color="primary" %}}

Vi vet att alla arbetsblad kan innehålla data som i grund och botten lagras i celler (med vilka ett arbetsblad är uppbyggt). En cell är en grundläggande del av ett arbetsblad som används för att konstruera hela arbetsbladet som en följd av rader och kolumner. Innan vi försöker komma åt data från ett arbetsblad, skulle vi behöva få åtkomst till dess celler. Så i det här ämnet kommer vi att diskutera några grundläggande tillvägagångssätt för att komma åt arbetsbladsceller vid körning genom Aspose.Cells för Python via .NET.

{{% /alert %}}

## **Hur man får åtkomst till celler**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Excelfil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) som tillåter åtkomst till varje arbetsblad i Excelfilen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) som representerar alla celler i arbetsbladet.

Vi kan använda [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-insamlingen för att komma åt celler i ett arbetsblad. Aspose.Cells för Python via .NET tillhandahåller tre grundläggande tillvägagångssätt för att komma åt celler i ett arbetsblad:

1. Genom att använda cellnamnet.
2. Genom att använda cellens rad- och kolumnindex.
3. Genom att använda en cellindex i [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen

**Viktigt:** Vi har nämnt att den 3:e metoden är den snabbaste och den 1:a metoden är den långsammaste. Skillnaden i prestanda mellan metoderna är mycket liten så oroa dig inte för prestandaförsämring, oavsett vilken metod du använder.

### **Hur man får Cell-objekt genom Cellnamn**

Utvecklare kan få åtkomst till en specifik cell genom att skicka dess cellnamn till [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen som en index.

Om du skapar ett tomt arbetsblad i början är antalet [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samling noll. När du använder den här metoden för att få åtkomst till en cell kontrolleras det om cellen finns i samlingen eller inte. Om ja, returnerar den cellobjektet i samlingen annars skapar den en ny [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-objekt, lägger till objektet i [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen och returnerar sedan objektet. Den här metoden är det enklaste sättet att få åtkomst till cellen om du är bekant med Microsoft Excel men det är det långsammaste som jämfört med andra metoder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **Hur man får Cell-objekt genom rad- och kolumnindex för cellen**

Utvecklare kan komma åt en specifik cell genom att skicka rad- och kolumnindex till [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassen.

Det här tillvägagångssättet fungerar på samma sätt som det första tillvägagångssättet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **Hur man får cellobjekt efter cellindex i cellsamlingen**

En cell kan också kommas åt genom att skicka cellens numeriska index till [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen.

Om du använder detta tillvägagångssätt för att komma åt celler kan ett undantag kastas om cellens numeriska index är utanför intervallet. Detta tillvägagångssätt är det snabbaste sättet att komma åt cellerna, men en viktig sak att veta är att om du använder detta tillvägagångssätt för att komma åt ett cellobjekt kan det numeriska indexet ändras efter att nya celler har lagts till i [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen. Cellobjekten i [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samlingen sorteras internt efter rad- och kolumnindex.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **Hur man får maximal visningsområde för arbetsblad**

Aspose.Cells för Python via .NET tillåter utvecklare att komma åt ett arbetsblads maximala visningsområde. Det maximala visningsområdet - intervallet av celler mellan den första och den sista cellen med innehåll - är användbart när du behöver kopiera, välja eller visa hela innehållet i ett arbetsblad i en bild.

Du kan komma åt ett arbetsblads maximala visningsområde med hjälp av [**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/). Följande exempelkod illustrerar hur du kommer åt [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/)-egenskapen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
