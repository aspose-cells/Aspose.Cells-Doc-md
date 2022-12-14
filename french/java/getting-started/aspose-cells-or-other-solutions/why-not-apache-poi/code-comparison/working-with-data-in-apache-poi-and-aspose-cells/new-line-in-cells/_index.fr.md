---
title: Nouvelle ligne au Cells
type: docs
weight: 30
url: /fr/java/new-line-in-cells/
---
## **Aspose.Cells - Nouvelle ligne en Cells**
Pour s'assurer que le texte d'une cellule peut être lu, des sauts de ligne et des retours à la ligne explicites peuvent être appliqués. L'habillage du texte transforme une ligne en plusieurs dans une cellule, que les sauts de ligne explicites placent exactement là où vous le souhaitez.

Pour envelopper du texte dans une cellule, utilisez la méthode Style.setTextWrapped.

**Java**

{{< highlight "java" >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Nouvelle ligne en Cells**
CellStyle.setWrapText doit être vrai pour le texte enveloppé.

**Java**

{{< highlight "java" >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Sauts de ligne et retour à la ligne](/java/line-breaks-and-text-wrapping).

{{% /alert %}}
