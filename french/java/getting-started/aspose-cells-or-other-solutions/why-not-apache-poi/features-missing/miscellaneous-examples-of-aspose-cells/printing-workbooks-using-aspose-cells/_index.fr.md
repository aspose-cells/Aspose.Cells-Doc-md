---
title: Impression de classeurs à l aide de Aspose.Cells
type: docs
weight: 20
url: /fr/java/printing-workbooks-using-aspose-cells/
---

## **Aspose.Cells - Impression de classeurs**
Après avoir créé votre feuille de calcul, vous voudrez probablement en imprimer une copie papier pour vos besoins. Lors de l'impression, MS Excel suppose que vous souhaitez imprimer toute la zone de la feuille à moins que vous ne spécifiez votre sélection.

Impression de feuille de calcul

**Java**

{{< highlight java >}}

 //Instantiate a new workbook

Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions

ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}

Impression de classeur

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Impression de classeurs](/cells/fr/java/printing-workbooks).

{{% /alert %}}
