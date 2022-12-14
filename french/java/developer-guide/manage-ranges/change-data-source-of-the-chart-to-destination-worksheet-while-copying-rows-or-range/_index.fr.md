---
title: Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage
type: docs
weight: 850
url: /fr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Scénarios d'utilisation possibles**
Lorsque vous copiez des lignes ou une plage contenant des graphiques dans une nouvelle feuille de calcul, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est =Sheet1!$A$1:$B$4, puis après avoir copié des lignes ou une plage dans une nouvelle feuille de calcul, la source de données restera la même, c'est-à-dire =Sheet1!$A$1:$B$4. Il fait toujours référence à l'ancienne feuille de calcul, c'est-à-dire Sheet1. C'est également le comportement Excel Microsoft. Mais si vous voulez qu'il se réfère à la nouvelle feuille de calcul de destination, veuillez utiliser la propriété CopyOptions.ReferToDestinationSheet et définissez-la sur true lors de l'appel de la méthode Cells.CopyRows(). Maintenant, si votre feuille de calcul de destination est DestSheet, la source de données de votre graphique passera de =Sheet1!$A$1:$B$4 à =DestSheet!$A$1:$B$4.
## **Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage**
L'exemple de code suivant explique l'utilisation de la propriété CopyOptions.ReferToDestinationSheet lors de la copie de lignes ou d'une plage contenant un graphique dans une nouvelle feuille de calcul. Le code utilise le[exemple de fichier excel](5472284.xlsx) et génère le[fichier excel de sortie](5472283.xlsx) . La capture d'écran montre que la source de données du graphique dans[fichier excel de sortie](5472283.xlsx) fait désormais référence à DestSheet au lieu de Sheet1.

![tâche : image_autre_texte](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






