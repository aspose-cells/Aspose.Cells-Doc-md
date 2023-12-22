---
title: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells
description: Cet article décrit comment étendre le moteur de calcul par défaut en implémentant un moteur de calcul personnalisé à l'aide de la bibliothèque Aspose.Cells. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour implémenter un moteur de calcul personnalisé et obtenir les résultats. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **Implémenter un moteur de calcul personnalisé**

Aspose.Cells dispose d'un puissant moteur de calcul capable de calculer presque toutes les formules Excel Microsoft. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées dans l'implémentation de cette fonctionnalité.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** qui a un**[Calculer (données CalculationData)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** méthode. Cette méthode est appelée contre toutes vos formules. Dans cette méthode, nous capturons le**TODAY** fonction et ajoutez un jour à la date du système. Ainsi, si la date actuelle est le 27/07/2023, alors le moteur personnalisé calculera TODAY() comme étant le 28/07/2023.

###  **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **Résultat**

Veuillez vérifier la sortie de la console de l'exemple de code ci-dessus, la valeur (date et heure) de A1 avec moteur personnalisé doit être un jour plus tard que le résultat sans moteur personnalisé.

###  **Article associé**

{{% alert color="primary" %}}

[Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
