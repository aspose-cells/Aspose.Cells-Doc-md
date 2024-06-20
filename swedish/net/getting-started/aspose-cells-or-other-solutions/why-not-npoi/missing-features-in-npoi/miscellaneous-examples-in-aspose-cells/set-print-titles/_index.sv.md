---
title: Ange utskriftstitlar
type: docs
weight: 30
url: /sv/net/set-print-titles/
---

## **Aspose.Cells - Ange utskriftstitlar**
Aspose.Cells låter dig ange rad- och kolumnrubriker som ska upprepas på alla sidor av ett tryckt kalkylblad. För att göra det, använd [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-klassens egenskaper PrintTitleColumns och PrintTitleRows.

Rader eller kolumner som kommer att upprepas definieras genom att ange deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Ange utskriftstitlar** från någon av nedan nämnda sociala kodningsplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer detaljer, besök [Inställning av utskriftsalternativ](/cells/sv/net/setting-print-options/).

{{% /alert %}}
