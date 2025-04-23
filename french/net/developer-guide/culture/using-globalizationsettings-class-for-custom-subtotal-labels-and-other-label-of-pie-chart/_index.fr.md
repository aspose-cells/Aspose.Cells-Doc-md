---
title: Utilisation de la classe GlobalizationSettings pour les étiquettes de sous total personnalisées et d autres étiquettes de graphique circulaire
type: docs
weight: 70
url: /fr/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Scénarios d'utilisation possibles**

Les API Aspose.Cells ont exposé la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) afin de traiter les scénarios où l'utilisateur souhaite utiliser des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul. De plus, la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) peut également être utilisée pour modifier l'étiquette **Autre** du graphique circulaire lors du rendu de la feuille de calcul ou du graphique.

## **Introduction à la classe GlobalizationSettings**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) offre actuellement les 3 méthodes suivantes qui peuvent être substituées dans une classe personnalisée pour obtenir les étiquettes désirées pour les sous-totaux ou pour rendre un texte personnalisé pour l'étiquette **Autre** d'un graphique circulaire.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) : Obtient le nom total de la fonction.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) : Obtient le nom du total général de la fonction.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) : Obtient le nom des étiquettes "Autre" pour les graphiques circulaires.

### **Étiquettes personnalisées pour les sous-totaux**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) peut être utilisée pour personnaliser les étiquettes de sous-total en remplaçant les méthodes [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) comme démontré ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

Pour injecter des étiquettes personnalisées, il est nécessaire d'attribuer la propriété [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) à une instance de la classe **CustomSettings** définie ci-dessus avant d'ajouter les sous-totaux à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) fonctionne uniquement pour l'ajout de nouveaux sous-totaux. Si une feuille de calcul contient déjà des sous-totaux, leurs étiquettes ne peuvent pas être modifiées.

{{% /alert %}}

### **Texte personnalisé pour l'étiquette Autre du graphique circulaire**

La classe [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) offre la méthode [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) qui est utile pour donner une valeur personnalisée à l'étiquette "Autre" des graphiques circulaires. L'extrait suivant définit une classe personnalisée et substitue la méthode [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) pour obtenir une étiquette personnalisée basée sur l'identifiant de culture du système.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

L'extrait suivant charge une feuille de calcul existante contenant un graphique circulaire et rend le graphique en une image en utilisant la classe **CustomSettings** créée ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
