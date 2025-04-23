---
title: Obtenez une liste de polices utilisées dans une feuille de calcul ou un classeur
linktitle: Obtenez une liste de polices utilisées dans une feuille de calcul ou un classeur
description: Apprenez comment obtenir une liste de polices utilisées dans une feuille de calcul ou un classeur à l aide de Aspose.Cells for Node.js via C++. Cet article vous montrera comment récupérer les informations de police d un document.
keywords: Aspose.Cells, Node.js via C++, Feuille de calcul, Classeur, Police, Liste
type: docs
weight: 20
url: /fr/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Scénarios d'utilisation possibles**

Il est souvent nécessaire de connaître les polices utilisées dans votre classeur à des fins de rendu. Lorsque vous convertissez votre classeur en PDF ou image, Aspose.Cells exige que toutes les polices nécessaires soient installées sur votre système ou présentes dans votre **répertoire de polices**. Si Aspose.Cells ne parvient pas à trouver la police nécessaire, il essaie de la remplacer par une autre police appropriée présente sur votre système ou dans votre répertoire de polices et pouvant remplacer votre police actuelle. Cela entraîne non seulement un rendu indésirable des PDF ou images, mais cela prend également du temps de traitement pour trouver des polices adaptées.

Pour traiter de tels cas, vous devriez connaître quelles polices sont utilisées par votre classeur, puis soit installer ces polices sur votre système dans le cas d'un environnement Windows, soit les placer dans votre répertoire de polices dans le cas d'un environnement Windows ou Linux.

Aspose.Cells for Node.js via C++ fournit la méthode [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--) qui retourne la liste de toutes les polices utilisées dans votre classeur ou feuille de calcul.

## **Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur**

Le code d'exemple suivant charge le fichier Excel source et récupère la liste des polices utilisées à l'intérieur. Il contient une feuille de calcul factice avec quelques polices fictives ajoutées à des fins d'illustration. Lorsque le code imprime toutes les polices dans le classeur, il imprime également ces polices fictives. La capture d'écran suivante montre le [fichier Excel d'exemple](25395211.xlsx) et comment les polices fictives sont répertoriées.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


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
