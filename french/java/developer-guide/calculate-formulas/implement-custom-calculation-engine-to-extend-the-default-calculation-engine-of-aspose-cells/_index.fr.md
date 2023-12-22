---
title: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells
type: docs
weight: 590
url: /fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells dispose d'un puissant moteur de calcul capable de calculer presque toutes les formules Excel Microsoft. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées dans l'implémentation de cette fonctionnalité.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [RésuméCalculMoteur](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Données de calcul](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **Implémenter un moteur de calcul personnalisé**
Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface[RésuméCalculMoteur](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) qui n'a qu'une seule méthode[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Cette méthode est appelée contre toutes vos formules. Dans cette méthode, nous capturons le**TODAY** fonction et ajoutez un jour à la date du système. Ainsi, si la date actuelle est le 27/07/2023, alors le moteur personnalisé calculera TODAY() comme étant le 28/07/2023.

###  **Exemple de programmation**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **Résultat**

Veuillez vérifier la sortie de la console de l'exemple de code ci-dessus, la valeur (date et heure) de A1 avec moteur personnalisé doit être un jour plus tard que le résultat sans moteur personnalisé.

###  **Article associé**
{{% alert color="primary" %}} 

- [Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
