---
title: Kopiera ark i arbetsbok
type: docs
weight: 40
url: /sv/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - Flytta eller kopiera ark i arbetsbok**
Nedan följer stegen för att kopiera och flytta kalkylblad i eller mellan arbetsböcker.

1. För att flytta eller kopiera ark inom eller mellan arbetsböcker, öppna arbetsboken som ska ta emot arken.
1. Växla till arbetsboken som innehåller de ark du vill flytta eller kopiera och välj sedan arken.
1.  På**Redigera** menyn, klicka**Flytta eller kopiera ark**.
1. I rutan Till bok klickar du på arbetsboken för att ta emot arken.
1.  För att flytta eller kopiera de markerade arken till en ny arbetsbok, klicka**ny bok**.
1.  I den**Före ark** klickar du på arket innan du vill infoga de flyttade eller kopierade arken.
1.  Om du vill kopiera arken istället för att flytta dem väljer du**Skapa en kopia** kryssruta.
## **Aspose.Cells - Kopiera ark i arbetsbok**
{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller en överbelastad metod, WorksheetCollection.addCopy(), som används för att lägga till ett kalkylblad till insamlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar källarkets index som en parameter. Den andra versionen tar namnet på källarbetsbladet.

Följande exempel visar hur man kopierar ett befintligt kalkylblad i en arbetsbok.

{{% /alert %}} 

Kopiera ark med Aspose.Cells

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Kopiera ark i arbetsbok**
{{% alert color="primary" %}} 

Workbook.cloneSheet() används för att kopiera ark med arbetsbok.

{{% /alert %}} 

Kopiera ark med Apache POI SS

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

 För mer information, besök[Kopiera och flytta arbetsblad](/cells/sv/java/copying-and-moving-worksheets).

{{% /alert %}}
