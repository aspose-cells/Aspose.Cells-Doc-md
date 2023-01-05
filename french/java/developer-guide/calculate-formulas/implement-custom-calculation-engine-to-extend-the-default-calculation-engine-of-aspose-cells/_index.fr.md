---
title: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells
type: docs
weight: 590
url: /fr/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells dispose d'un puissant moteur de calcul capable de calculer la quasi-totalité des formules Excel Microsoft. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [RésuméCalculMoteur](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculDonnées](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implémenter un moteur de calcul personnalisé**
Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface[RésuméCalculMoteur](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) qui n'a qu'une seule méthode[calculer (données CalculData)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Cette méthode est appelée sur toutes vos formules. Dans cette méthode, nous capturons le**SOMME** formule et augmente sa valeur de 30. Ainsi, si la valeur calculée Aspose.Cells est de 20, notre moteur personnalisé la rendra de 50 en ajoutant 30.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **Sortie console**
Voici la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **Article associé**
{{% alert color="primary" %}} 

- [Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
