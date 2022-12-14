---
title: Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut de Aspose.Cells
type: docs
weight: 80
url: /fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells dispose d'un puissant moteur de calcul capable de calculer la quasi-totalité des formules Excel Microsoft. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[Données de calcul] (https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** qui a un**[Calculer (données de calcul)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** méthode. Cette méthode est appelée sur toutes vos formules. Dans cette méthode, nous capturons le**Somme** formule et augmente sa valeur de 30. Ainsi, si la valeur calculée Aspose.Cells est de 20, notre moteur personnalisé la rendra de 50 en ajoutant 30.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Sortie console**

Voici la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **Article associé**

{{% alert color="primary" %}}

[Calcul direct de la fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
