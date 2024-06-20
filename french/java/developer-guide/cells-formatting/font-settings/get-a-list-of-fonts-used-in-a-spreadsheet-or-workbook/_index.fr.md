---
title: Obtenez une liste de polices utilisées dans une feuille de calcul ou un classeur
type: docs
weight: 20
url: /fr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Scénarios d'utilisation possibles**

Il est souvent nécessaire de connaître les polices de caractères utilisées dans votre classeur à des fins de rendu. Lorsque vous convertissez votre classeur en PDF ou en image, Aspose.Cells nécessite que toutes les polices nécessaires soient installées sur votre système ou présentes dans votre **répertoire de polices**. Si Aspose.Cells est incapable de trouver la police nécessaire, il essaie de la remplacer par une autre police appropriée présente sur votre système ou dans votre répertoire de polices et peut substituer votre police réelle. Cela se traduit non seulement par un rendu indésirable de PDF ou d'images, mais prend également du temps de traitement pour trouver des polices appropriées.

Pour faire face à de tels cas, vous devez savoir quelles polices sont utilisées dans votre classeur, puis installer ces polices sur votre système en cas d'environnement Windows ou les placer dans votre répertoire de polices en cas d'environnement Windows ou Linux.

Aspose.Cells fournit la méthode [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--) qui retourne la liste de toutes les polices utilisées dans votre classeur ou votre feuille de calcul.

## **Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur**

Le code d'exemple suivant charge le fichier excel source et récupère la liste des polices utilisées à l'intérieur. Il a une feuille de calcul factice contenant quelques polices factices ajoutées à des fins d'illustration. Lorsque le code imprime toutes les polices dans le classeur, il imprime également ces polices factices. La capture d'écran suivante montre le [fichier excel d'exemple](sampleGetFonts.xlsx) et comment les polices factices sont répertoriées.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](sampleGetFonts.xlsx) fourni.

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
