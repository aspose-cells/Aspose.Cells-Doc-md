---
title: Utilisation de la classe GlobalizationSettings pour les étiquettes de sous-total personnalisées et une autre étiquette de graphique à secteurs
type: docs
weight: 50
url: /fr/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Scénarios d'utilisation possibles**
 Aspose.Cells Les API ont exposé le[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) classe afin de gérer les scénarios dans lesquels l'utilisateur souhaite utiliser des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul. De plus, le[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)la classe peut également être utilisée pour modifier la**Autre** étiquette pour le graphique à secteurs lors du rendu de la feuille de calcul ou du graphique.
## **Introduction à la classe GlobalizationSettings**
 La[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) propose actuellement les 3 méthodes suivantes qui peuvent être remplacées dans une classe personnalisée pour obtenir les étiquettes souhaitées pour les sous-totaux ou pour afficher le texte personnalisé pour le**Autre** étiquette d'un graphique à secteurs.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Obtient le nom total de la fonction.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) : obtient le nom du total général de la fonction.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) : obtient le nom des étiquettes "Autre" pour les graphiques à secteurs.
### **Étiquettes personnalisées pour les sous-totaux**
 La[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) peut être utilisée pour personnaliser les étiquettes de sous-total en remplaçant la[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) méthodes comme démontré ci-dessus.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Afin d'injecter des étiquettes personnalisées, il est nécessaire d'attribuer le[WorkbookSettings.GlobalizationSettingsWorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) propriété à une instance de*Paramètres personnalisés*classe définie ci-dessus avant d'ajouter les sous-totaux à la feuille de calcul.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

 La[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)la classe ne fonctionne que pour ajouter de nouveaux sous-totaux. Si une feuille de calcul contient déjà des sous-totaux, leurs libellés ne peuvent pas être modifiés.

{{% /alert %}} 
### **Texte personnalisé pour une autre étiquette de graphique à secteurs**
 La[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) la classe offre le[obtenirAutreNom](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ) qui est utile pour attribuer une valeur personnalisée à l'étiquette "Autre" des graphiques à secteurs. L'extrait de code suivant définit une classe personnalisée et remplace le[obtenirAutreNom](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) pour obtenir une étiquette personnalisée basée sur la langue par défaut définie pour JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 L'extrait de code suivant charge une feuille de calcul existante contenant un graphique à secteurs et affiche le graphique sous forme d'image tout en utilisant le*Paramètres personnalisés*classe créée ci-dessus.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


 Voici l'image résultante lorsque les paramètres régionaux de la machine sont définis sur France. Comme vous pouvez le voir, le libellé "Autre" a été traduit en "Autre" tel que défini dans*Paramètres personnalisés*classer.

![tâche : image_autre_texte](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
