---
title: Obtenez une liste de polices utilisées dans une feuille de calcul ou un classeur
description: Aspose.Cells est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul. Elle supporte l obtention d une liste de polices utilisées dans une feuille ou un classeur, permettant aux utilisateurs d obtenir des informations sur les polices utilisées dans un document. Cet article montrera comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour obtenir une liste de polices.
keywords: Aspose.Cells pour Python via .NET, Feuille de calcul, Classeur, Police, Liste
type: docs
weight: 20
url: /fr/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Scénarios d'utilisation possibles**

Il est souvent nécessaire de connaître les polices utilisées dans votre classeur pour des besoins de rendu. Lorsque vous convertissez votre classeur en PDF ou en image, Aspose.Cells pour Python via .NET nécessite que toutes les polices nécessaires soient installées sur votre système ou présentes dans votre **répertoire de polices**. Si Aspose.Cells pour Python via .NET ne parvient pas à trouver la police requise, il essaie de la remplacer par une autre police appropriée présente sur votre système ou dans votre répertoire de polices, ce qui peut conduire à un rendu indésirable du PDF ou des images, mais aussi augmenter le temps de traitement pour trouver des polices adaptées.

Pour faire face à de tels cas, il est important de savoir quelles polices sont utilisées dans votre classeur, puis d'installer ces polices sur votre système dans le cas de l'environnement Windows ou de les placer dans votre répertoire de polices dans le cas de l'environnement Windows ou Linux.

Aspose.Cells pour Python via .NET fournit la méthode [**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts) qui retourne la liste de toutes les polices utilisées dans votre classeur ou feuille de calcul.

## **Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur**

Le code d'exemple suivant charge le fichier Excel source et récupère la liste des polices utilisées à l'intérieur. Il contient une feuille de calcul factice avec quelques polices fictives ajoutées à des fins d'illustration. Lorsque le code imprime toutes les polices dans le classeur, il imprime également ces polices fictives. La capture d'écran suivante montre le [fichier Excel d'exemple](25395211.xlsx) et comment les polices fictives sont répertoriées.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

## **Sortie console**

Voici la sortie de la console du code d'échantillon ci-dessus lorsqu'il est exécuté avec le fichier Excel d'exemple donné (25395211.xlsx).

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}

