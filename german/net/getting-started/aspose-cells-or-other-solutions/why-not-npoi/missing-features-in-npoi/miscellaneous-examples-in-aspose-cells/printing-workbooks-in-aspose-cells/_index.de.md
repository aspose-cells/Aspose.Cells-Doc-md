---
title: Arbeitsmappen drucken in Aspose.Cells
type: docs
weight: 20
url: /de/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - Arbeitsmappen drucken**
Nachdem Sie Ihre Arbeitsmappe erstellt haben, möchten Sie wahrscheinlich eine gedruckte Version des Blatts für Ihre Zwecke haben. Beim Drucken geht MS Excel davon aus, dass Sie den gesamten Arbeitsblattbereich drucken möchten, es sei denn, Sie geben Ihre Auswahl an.

Arbeitsblatt drucken

**C#**

{{< highlight cs >}}

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
## **Laufenden Code herunterladen**
Laden Sie **Arbeitsmappen drucken** von einer der unten aufgeführten sozialen Code-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Arbeitsmappen drucken](/cells/de/net/printing-workbooks/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
