---
title: Lire et manipuler des graphiques Excel 2016
type: docs
weight: 20
url: /fr/cpp/read-and-manipulate-excel-2016-charts/
---
## **Scénarios d'utilisation possibles**
Aspose.Cells prend en charge la lecture et la manipulation des graphiques Microsoft Excel 2016 qui ne sont pas présents dans Microsoft Excel 2013 ou les versions antérieures.
## **Lire et manipuler des graphiques Excel 2016**
 L'exemple de code suivant charge le[exemple de fichier Excel](66519072.xlsx) qui contient des graphiques Excel 2016 dans la première feuille de calcul. Il lit tous les graphiques un par un et change son titre en fonction de son type de graphique. La capture d'écran suivante montre l'exemple de fichier Excel avant l'exécution du code. Comme vous pouvez le voir, le titre du graphique est le même pour tous les graphiques.

![tâche : image_autre_texte](read-and-manipulate-excel-2016-charts_1.png)

 La capture d'écran suivante montre le[fichier Excel de sortie](66519073.xlsx) après l'exécution du code. Comme vous pouvez le voir, le titre du graphique est modifié en fonction de son type de graphique.

![tâche : image_autre_texte](read-and-manipulate-excel-2016-charts_2.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-ReadAndManipulateExcel2016Charts.cpp" >}}
## **Sortie console**
Voici la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec l'exemple de fichier Excel fourni.

{{< highlight "java" >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}
