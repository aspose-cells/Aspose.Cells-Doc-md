---
title: Impression de cahiers d'exercices au Aspose.Cells
type: docs
weight: 20
url: /fr/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells - Impression de cahiers**
Après avoir fini de créer votre feuille de calcul, vous souhaiterez probablement imprimer une copie papier de la feuille selon vos besoins. Lorsque vous imprimez, MS Excel suppose que vous souhaitez imprimer toute la zone de la feuille de calcul, sauf si vous spécifiez votre sélection.

Feuille de travail d'impression

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
## **Télécharger le code d'exécution**
 Télécharger**Impression de classeurs** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Impression de classeurs](/cells/fr/net/printing-workbooks/).

{{% /alert %}}
