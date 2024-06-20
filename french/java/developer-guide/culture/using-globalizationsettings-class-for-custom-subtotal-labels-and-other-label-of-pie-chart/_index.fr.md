---
title: Utilisation de la classe GlobalizationSettings pour les étiquettes de sous total personnalisées et d autres étiquettes de graphique circulaire
type: docs
weight: 50
url: /fr/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Scénarios d'utilisation possibles**
Les API Aspose.Cells ont exposé la classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) afin de gérer les scénarios où l'utilisateur souhaite utiliser des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul. De plus, la classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) peut également être utilisée pour modifier l'étiquette **Autre** du graphique circulaire lors du rendu de la feuille de calcul ou du graphique.
## **Introduction à la classe GlobalizationSettings**
La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) offre actuellement les 3 méthodes suivantes qui peuvent être remplacées par une classe personnalisée pour obtenir les étiquettes souhaitées pour les sous-totaux ou pour rendre un texte personnalisé pour l'étiquette **Autre** d'un graphique circulaire.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Obtient le nom total de la fonction.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): Obtient le nom de grand total de la fonction.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): Obtient le nom des étiquettes "Autres" pour les graphiques circulaires.
### **Étiquettes personnalisées pour les sous-totaux**
La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) peut être utilisée pour personnaliser les étiquettes de sous-total en remplaçant les méthodes [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) comme démontré ci-dessous.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Pour injecter des étiquettes personnalisées, il est nécessaire d'attribuer la propriété [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) à une instance de la classe *CustomSettings* définie ci-dessus avant d'ajouter les sous-totaux à la feuille de calcul.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) ne fonctionne que pour l'ajout de nouveaux sous-totaux. Si une feuille de calcul contient déjà des sous-totaux, leurs étiquettes ne peuvent pas être modifiées.

{{% /alert %}} 
### **Texte personnalisé pour l'étiquette Autre du graphique circulaire**
La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) propose la méthode [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) qui est utile pour donner une valeur personnalisée à l'étiquette "Autre" des graphiques circulaires. L'extrait suivant définit une classe personnalisée et remplace la méthode [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) pour obtenir une étiquette personnalisée en fonction de la langue par défaut définie pour la JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


L'extrait suivant charge une feuille de calcul existante contenant un graphique circulaire et rend le graphique sous forme d'image tout en utilisant la classe *CustomSettings* créée précédemment.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Voici l'image résultante lorsque le paramètre régional de la machine est défini sur la France. Comme vous pouvez le voir, l'étiquette "Autre" a été traduite en "Autre" comme défini dans la classe *CustomSettings*.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
