---
title: Finden Sie Wert in Cells
type: docs
weight: 20
url: /de/net/find-value-in-cells/
---
## **Aspose.Cells - Wert finden in Cells**
In Microsoft Excel können Benutzer nach Zellen suchen, die bestimmte Daten enthalten. Klicken zum Beispiel**Bearbeiten**und dann**Finden**öffnet den Suchdialog. Der Benutzer gibt einen Wert ein und klickt**OK**danach zu suchen. Excel hebt übereinstimmende Felder hervor.

**C#**

{{< highlight "cs" >}}

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
## **Laufcode herunterladen**
 Download**Finden Sie Wert in Cells** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Daten finden oder suchen](/cells/de/net/find-or-search-data/).

{{% /alert %}}
