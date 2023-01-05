---
title: Ställ in utskriftsrubriker
type: docs
weight: 30
url: /sv/net/set-print-titles/
---
## **Aspose.Cells - Ställ in trycktitlar**
Aspose.Cells låter dig ange rad- och kolumnrubriker som ska upprepas på alla sidor i ett utskrivet kalkylblad. För att göra det, använd[Utskriftsformat](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)klass PrintTitleColumns och PrintTitleRows egenskaper.

Raderna eller kolumnerna som kommer att upprepas definieras genom att skicka deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Ställ in utskriftsrubriker** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Ställa in utskriftsalternativ](/cells/sv/net/setting-print-options/).

{{% /alert %}}
