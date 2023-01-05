---
title: Drucken von Arbeitsmappen unter Aspose.Cells
type: docs
weight: 20
url: /de/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells – Drucken von Arbeitsmappen**
Nachdem Sie mit der Erstellung Ihrer Tabelle fertig sind, möchten Sie wahrscheinlich eine Hardcopy der Tabelle für Ihren Bedarf ausdrucken. Wenn Sie drucken, geht MS Excel davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben Ihre Auswahl an.

Arbeitsblatt drucken

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Create an object for ImageOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Get the first worksheet

Worksheet sheet = workbook.Worksheets[0];

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.ToPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Drucken von Arbeitsmappen** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Drucken von Arbeitsmappen](/cells/de/net/printing-workbooks/).

{{% /alert %}}
