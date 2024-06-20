---
title: Imprimer des classeurs dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - Impression de classeurs**
Après avoir créé votre feuille de calcul, vous voudrez probablement en imprimer une copie papier pour vos besoins. Lors de l'impression, MS Excel suppose que vous souhaitez imprimer toute la zone de la feuille à moins que vous ne spécifiez votre sélection.

Impression de feuille de calcul

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Imprimer des classeurs** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Imprimer des classeurs](/cells/fr/net/printing-workbooks/).

{{% /alert %}}
