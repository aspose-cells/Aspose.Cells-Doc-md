---
title: Imprimer des classeurs dans xlsx4j
type: docs
weight: 30
url: /fr/java/printing-workbooks-in-xlsx4j/
---

## **Aspose.Cells - Impression de classeurs**
Après avoir créé votre feuille de calcul, vous voudrez probablement en imprimer une copie papier pour vos besoins. Lors de l'impression, MS Excel suppose que vous souhaitez imprimer toute la zone de la feuille à moins que vous ne spécifiez votre sélection.

**Imprimer la feuille de calcul**

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

**Imprimer le classeur**

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Impression des classeurs](/cells/fr/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
