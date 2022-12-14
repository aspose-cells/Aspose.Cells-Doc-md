---
title: Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur
type: docs
weight: 20
url: /fr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Scénarios d'utilisation possibles**

Il est souvent nécessaire de connaître les polices utilisées dans votre classeur à des fins de rendu. Lorsque vous convertissez votre classeur en PDF ou en image, Aspose.Cells nécessite que toutes les polices nécessaires soient installées sur votre système ou présentes dans votre**répertoire des polices**Si Aspose.Cells ne parvient pas à trouver la police nécessaire, il essaie de la remplacer par une autre police appropriée présente sur votre système ou dans votre répertoire de polices et peut remplacer votre police actuelle. Cela entraîne non seulement un rendu indésirable des PDF ou des images, mais prend également du temps de traitement pour trouver les polices appropriées.

Pour faire face à de tels cas, vous devez savoir quelles polices sont utilisées par votre classeur, puis installez ces polices sur votre système dans le cas d'un environnement Windows ou placez-les dans votre répertoire de polices dans le cas d'un environnement Windows ou Linux.

 Aspose.Cells fournit le**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**méthode qui renvoie la liste de toutes les polices utilisées dans votre classeur ou feuille de calcul.

## **Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur**

 L'exemple de code suivant charge le fichier Excel source et récupère la liste des polices utilisées à l'intérieur. Il contient une feuille de calcul factice dans laquelle des polices factices ont été ajoutées à des fins d'illustration. Lorsque le code imprime toutes les polices à l'intérieur du classeur, il imprime également ces polices factices. La capture d'écran suivante montre le[exemple de fichier excel](25395211.xlsx)et comment les polices factices sont répertoriées.

![tâche : image_autre_texte](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **Sortie console**

 Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le donné[exemple de fichier excel](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0]]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

{{< /highlight >}}
