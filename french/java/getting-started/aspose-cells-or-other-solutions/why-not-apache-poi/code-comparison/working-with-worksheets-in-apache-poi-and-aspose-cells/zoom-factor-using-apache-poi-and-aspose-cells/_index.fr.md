---
title: Facteur de zoom utilisant Apache POI et Aspose.Cells
type: docs
weight: 70
url: /fr/java/zoom-factor-using-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Facteur de zoom**
Microsoft Excel fournit une fonctionnalité qui permet aux utilisateurs de définir le facteur de zoom ou d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes.

Aspose.Cells fournit une classe, Workbook, qui représente un fichier Excel Microsoft. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la méthode setZoom de la classe Worksheet.

**Java**

{{< highlight "java" >}}

 Worksheet worksheet = worksheets.get(0);

//Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Facteur de zoom**
Apache POI fournit la fonction de zoom de la méthode Sheet.setZoom().

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.createSheet("new sheet");

sheet1.setZoom(3,4);   // 75 percent magnification

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/zoomfactor)
