---
title: Hitta värde i celler
type: docs
weight: 20
url: /sv/net/find-value-in-cells/
---

## **Aspose.Cells - Hitta värde i celler**
I Microsoft Excel kan användare söka efter celler som innehåller specifik data. Till exempel, att klicka på **Redigera** och sedan **Sök** öppnar sökdialogen. Användarna anger ett värde och klickar på **OK** för att söka efter det. Excel markerar matchande fält.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Hitta värde i celler** från någon av nedan nämnda sociala kodningsplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer information, besök [Hitta eller sök data](/cells/sv/net/find-or-search-data/).

{{% /alert %}}
