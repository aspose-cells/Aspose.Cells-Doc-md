---
title: Utilisation de la classe GlobalizationSettings pour les étiquettes de sous-total personnalisées et une autre étiquette de graphique à secteurs
type: docs
weight: 70
url: /fr/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Scénarios d'utilisation possibles**

 Aspose.Cells Les API ont exposé le[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)classe afin de gérer les scénarios dans lesquels l'utilisateur souhaite utiliser des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul. De plus, le[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) la classe peut également être utilisée pour modifier la**Autre** étiquette pour le graphique à secteurs lors du rendu de la feuille de calcul ou du graphique.

## **Introduction à la classe GlobalizationSettings**

 Le[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) propose actuellement les 3 méthodes suivantes qui peuvent être remplacées dans une classe personnalisée pour obtenir les étiquettes souhaitées pour les sous-totaux ou pour afficher le texte personnalisé pour le**Autre** étiquette d'un graphique à secteurs.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Obtient le nom total de la fonction.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Obtient le nom du total général de la fonction.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Obtient le nom des libellés "Autre" pour les graphiques à secteurs.

### **Étiquettes personnalisées pour les sous-totaux**

 Le[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)peut être utilisée pour personnaliser les étiquettes de sous-total en remplaçant la[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)méthodes comme démontré ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 Afin d'injecter des étiquettes personnalisées, il est nécessaire d'attribuer le[**WorkbookSettings.GlobalizationSettingsWorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) propriété à une instance de**Paramètres personnalisés**classe définie ci-dessus avant d'ajouter les sous-totaux à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

 Le[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)la classe ne fonctionne que pour ajouter de nouveaux sous-totaux. Si une feuille de calcul contient déjà des sous-totaux, leurs libellés ne peuvent pas être modifiés.

{{% /alert %}}

### **Texte personnalisé pour une autre étiquette de graphique à secteurs**

 Le[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) offres de cours[**ObtenirAutreNom**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)méthode qui est utile pour donner une valeur personnalisée à l'étiquette "Autre" des graphiques à secteurs. L'extrait de code suivant définit une classe personnalisée et remplace le[**ObtenirAutreNom**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)méthode pour obtenir une étiquette personnalisée basée sur l'identifiant de culture du système.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 L'extrait de code suivant charge une feuille de calcul existante contenant un graphique à secteurs et affiche le graphique sous forme d'image tout en utilisant le**Paramètres personnalisés**classe créée ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
