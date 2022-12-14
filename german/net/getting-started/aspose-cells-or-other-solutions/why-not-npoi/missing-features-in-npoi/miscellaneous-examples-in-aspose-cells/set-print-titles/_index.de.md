---
title: Drucktitel festlegen
type: docs
weight: 30
url: /de/net/set-print-titles/
---
## **Aspose.Cells - Drucktitel festlegen**
Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften festzulegen, die auf allen Seiten eines gedruckten Arbeitsblatts wiederholt werden sollen. Verwenden Sie dazu die[Seiteneinrichtung](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)Klasse PrintTitleColumns- und PrintTitleRows-Eigenschaften.

Die Zeilen oder Spalten, die wiederholt werden, werden durch die Übergabe ihrer Zeilen- oder Spaltennummern definiert. Beispielsweise werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

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
## **Laufcode herunterladen**
 Download**Drucktitel festlegen** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Druckoptionen einstellen](/cells/de/net/setting-print-options/).

{{% /alert %}}
