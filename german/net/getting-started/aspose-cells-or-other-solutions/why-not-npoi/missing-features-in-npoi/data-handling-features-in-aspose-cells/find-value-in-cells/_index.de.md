---
title: Wert in Zellen finden
type: docs
weight: 20
url: /de/net/find-value-in-cells/
---

## **Aspose.Cells - Wert in Zellen finden**
In Microsoft Excel können Benutzer nach Zellen suchen, die bestimmte Daten enthalten. Beispielsweise öffnet das Klicken auf **Bearbeiten** und dann auf **Suchen** den Suchdialog. Benutzer geben einen Wert ein und klicken auf **OK**, um danach zu suchen. Excel markiert übereinstimmende Felder.

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
## **Laufenden Code herunterladen**
Laden Sie **Wert in Zellen finden** von einer der unten aufgeführten sozialen Code-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Daten finden oder suchen](/cells/de/net/find-or-search-data/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
