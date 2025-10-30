---
title: Åtkomst till kalkylbladets celler
type: docs
weight: 10
url: /sv/nodejs-cpp/accessing-cells-of-a-worksheet/
description: Denna artikel visar hur man får den maximala visningsintervallet för ett arbetsblad och tillgång till celler via Aspose.Cells for Node.js via C++ API.
keywords: Få Cell objekt, Åtkomst till celler, Få maximalt visningsområde på arbetsbladet. 
---

{{% alert color="primary" %}}

Vi vet att alla arbetsblad kan innehålla data som huvudsakligen lagras i celler (som ett arbetsblad är uppbyggt av). En cell är en grundläggande del av ett arbetsblad som används för att konstruera hela arbetsbladet som en sekvens av rader och kolumner. Innan vi försöker få åtkomst till data från ett arbetsblad, behöver vi få tillgång till dess celler. Så i detta ämne diskuterar vi några grundläggande metoder för att tillgå arbetsbladets celler vid körning med Aspose.Cells for Node.js via C++.

{{% /alert %}}

## **Hur man får åtkomst till celler**

Aspose.Cells for Node.js via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen ger en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling som representerar alla celler i arbetsbladet.

Vi kan använda [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen för att komma åt celler i ett arbetsblad. Aspose.Cells for Node.js via C++ tillhandahåller tre grundläggande metoder för att komma åt celler i ett arbetsblad:

1. Genom att använda cellnamnet.
2. Genom att använda cellens rad- och kolumnindex.
3. Genom att använda en cellindex i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen

**Viktigt:** Vi har nämnt att den 3:e metoden är den snabbaste och den 1:a metoden är den långsammaste. Skillnaden i prestanda mellan metoderna är mycket liten så oroa dig inte för prestandaförsämring, oavsett vilken metod du använder.

### **Hur man får Cell-objekt genom Cellnamn**

Utvecklare kan få åtkomst till en specifik cell genom att skicka dess cellnamn till [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen som en index.

Om du skapar ett tomt arbetsblad i början är antalet [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling noll. När du använder den här metoden för att få åtkomst till en cell kontrolleras det om cellen finns i samlingen eller inte. Om ja, returnerar den cellobjektet i samlingen annars skapar den en ny [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-objekt, lägger till objektet i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen och returnerar sedan objektet. Den här metoden är det enklaste sättet att få åtkomst till cellen om du är bekant med Microsoft Excel men det är det långsammaste som jämfört med andra metoder.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **Hur man får Cell-objekt genom rad- och kolumnindex för cellen**

Utvecklare kan komma åt en specifik cell genom att skicka rad- och kolumnindex till [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen.

Det här tillvägagångssättet fungerar på samma sätt som det första tillvägagångssättet.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **Hur man får cellobjekt efter cellindex i cellsamlingen**

En cell kan också kommas åt genom att skicka cellens numeriska index till [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen.

Om du använder detta tillvägagångssätt för att komma åt celler kan ett undantag kastas om cellens numeriska index är utanför intervallet. Detta tillvägagångssätt är det snabbaste sättet att komma åt cellerna, men en viktig sak att veta är att om du använder detta tillvägagångssätt för att komma åt ett cellobjekt kan det numeriska indexet ändras efter att nya celler har lagts till i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen. Cellobjekten i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen sorteras internt efter rad- och kolumnindex.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **Hur man får maximal visningsområde för arbetsblad**

Aspose.Cells for Node.js via C++ för Node.js via C++ låter utvecklare komma åt ett arbetsblads maximala visningsområde. Det maximala visningsområdet - intervallet av celler mellan den första och sista cellen med innehåll - är användbart när du behöver kopiera, välja eller visa hela innehållet i ett arbetsblad i en bild.

Du kan komma åt ett arbetsblads maximala visningsområde med hjälp av [**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--). Följande exempelkod illustrerar hur du kommer åt [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--)-egenskapen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
