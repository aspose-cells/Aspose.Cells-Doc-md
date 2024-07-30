---
title: Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage
type: docs
weight: 850
url: /fr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Scénarios d'utilisation possibles**
Lorsque vous copiez des lignes ou une plage contenant des graphiques vers une nouvelle feuille de calcul, la source de données du graphique ne change pas. Par exemple, si la source de données du graphique est =Feuil1!$A$1:$B$4, alors après avoir copié des lignes ou une plage vers une nouvelle feuille de calcul, la source de données restera la même, c'est-à-dire =Feuil1!$A$1:$B$4. Elle fait toujours référence à l'ancienne feuille de calcul, à savoir Feuil1. C'est également le comportement de Microsoft Excel. Mais si vous souhaitez qu'elle fasse référence à la nouvelle feuille de calcul de destination, veuillez utiliser la propriété CopyOptions.ReferToDestinationSheet et la définir sur true lors de l'appel de la méthode Cells.CopyRows(). Maintenant, si votre feuille de calcul de destination est DestSheet, la source de données de votre graphique changera de =Feuil1!$A$1:$B$4 à =DestSheet!$A$1:$B$4.
## **Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage**
Le code d'exemple suivant explique l'utilisation de la propriété CopyOptions.ReferToDestinationSheet lors de la copie de lignes ou d'une plage contenant un graphique vers une nouvelle feuille de calcul. Le code utilise le [fichier Excel d'exemple](5472284.xlsx) et génère le [fichier Excel de sortie](5472283.xlsx). La capture d'écran montre que la source de données du graphique dans le [fichier Excel de sortie](5472283.xlsx) fait maintenant référence à DestSheet au lieu de Feuil1.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






