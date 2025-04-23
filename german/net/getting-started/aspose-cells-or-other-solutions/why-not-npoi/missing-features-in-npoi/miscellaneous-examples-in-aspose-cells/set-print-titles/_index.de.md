---
title: Drucktitel festlegen
type: docs
weight: 30
url: /de/net/set-print-titles/
---

## **Aspose.Cells - Drucktitel festlegen**
Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts zu wiederholen. Verwenden Sie dazu die Klasse [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) und die Eigenschaften PrintTitleColumns und PrintTitleRows.

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

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
## **Laufenden Code herunterladen**
Laden Sie **Drucktitel festlegen** von einer der unten aufgeführten sozialen Code-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Druckoptionen festlegen](/cells/de/net/setting-print-options/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
