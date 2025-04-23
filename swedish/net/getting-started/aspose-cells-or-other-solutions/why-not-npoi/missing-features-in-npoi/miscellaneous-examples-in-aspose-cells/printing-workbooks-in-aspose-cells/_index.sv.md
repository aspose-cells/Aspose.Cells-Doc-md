---
title: Skriva ut arbetsböcker i Aspose.Cells
type: docs
weight: 20
url: /sv/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - Skriv ut arbetsböcker**
När du har skapat din kalkylblad vill du förmodligen skriva ut en papperskopia av kalkylarket enligt ditt behov. När du skriver ut antar MS Excel att du vill skriva ut hela kalkylbladsområdet om du inte specificerar ditt urval.

Utskrift av kalkylblad

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
## **Ladda ned körbar kod**
Ladda ner **Skriva ut arbetsböcker** från någon av nedan nämnda sociala kodningsplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer information, besök [Skriva ut arbetsböcker](/cells/sv/net/printing-workbooks/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
