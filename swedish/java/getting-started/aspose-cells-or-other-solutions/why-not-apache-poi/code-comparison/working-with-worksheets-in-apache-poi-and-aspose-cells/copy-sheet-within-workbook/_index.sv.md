---
title: Kopiera kalkylblad inom arbetsbok
type: docs
weight: 40
url: /sv/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - Flytta eller kopiera ark inom arbetsboken**
Följande är stegen för att kopiera och flytta kalkylblad inom eller mellan arbetsböcker.

1. För att flytta eller kopiera ark inom eller mellan arbetsböcker, öppna arbetsboken som kommer att ta emot arken.
1. Byt till arbetsboken som innehåller bladen du vill flytta eller kopiera, och välj sedan bladen.
1. På **Redigera**-menyn klickar du på **Flytta eller Kopiera Blad**.
1. I rutan Till bok klickar du på arbetsboken som ska ta emot bladen.
1. För att flytta eller kopiera de valda bladen till en ny arbetsbok, klicka på **Ny bok**.
1. I rutan **Innan blad** klickar du på det blad innan vilket du vill infoga de flyttade eller kopierade bladen.
1. För att kopiera ark istället för att flytta dem, markera kryssrutan **Skapa en kopia**.
## **Aspose.Cells - Kopiera kalkylblad inom arbetsbok**
{{% alert color="primary" %}} 

Aspose.Cells tillhandahåller en överbelastad metod, WorksheetCollection.addCopy(), som används för att lägga till ett kalkylblad i samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar parametern för källkalkylbladets index. Den andra versionen tar källkalkylbladets namn.

Det följande exemplet visar hur man kopierar ett befintligt kalkylblad inom en arbetsbok.

{{% /alert %}} 

Kopiera ark med hjälp av Aspose.Cells

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Kopiera kalkylblad inom arbetsbok**
{{% alert color="primary" %}} 

Workbook.cloneSheet() används för att kopiera ark inom arbetsbok.

{{% /alert %}} 

Kopiera ark med hjälp av Apache POI SS

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

För mer information, besök [Kopiera och flytta arbetsblad](/cells/sv/java/copying-and-moving-worksheets)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
