---
title: Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur
type: docs
weight: 20
url: /fr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Scénarios d'utilisation possibles**

 Il est souvent nécessaire de connaître les polices utilisées dans votre classeur à des fins de rendu. Lorsque vous convertissez votre classeur en PDF ou en image, Aspose.Cells nécessite que toutes les polices nécessaires soient installées sur votre système ou présentes dans votre**répertoire des polices**Si Aspose.Cells ne parvient pas à trouver la police nécessaire, il essaie de la remplacer par une autre police appropriée présente sur votre système ou dans votre répertoire de polices et peut remplacer votre police actuelle. Cela entraîne non seulement un rendu indésirable des PDF ou des images, mais prend également du temps de traitement pour trouver les polices appropriées.

Afin de traiter de tels cas, vous devez savoir quelles polices sont utilisées par votre classeur, puis installez ces polices sur votre système dans le cas d'un environnement Windows ou placez-les dans votre répertoire de polices dans le cas d'un environnement Windows ou Linux.

 Aspose.Cells fournit le[Classeur.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()) qui renvoie la liste de toutes les polices utilisées dans votre classeur ou feuille de calcul.

## **Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur**

 L'exemple de code suivant charge le fichier Excel source et récupère la liste des polices utilisées à l'intérieur. Il contient une feuille de calcul factice dans laquelle des polices factices ont été ajoutées à des fins d'illustration. Lorsque le code imprime toutes les polices à l'intérieur du classeur, il imprime également ces polices factices. La capture d'écran suivante montre le[exemple de fichier excel](sampleGetFonts.xlsx)et comment les polices factices sont répertoriées.

![tâche : image_autre_texte](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Sortie console**

 Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le donné[exemple de fichier excel](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
