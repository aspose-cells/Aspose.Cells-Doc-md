---
title: Travailler avec un moteur de calcul personnalisé
type: docs
weight: 70
url: /fr/net/working-with-custom-calculation-engine/
---
## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells.Gridweb dispose d'un puissant moteur de calcul capable de calculer la quasi-totalité des formules Excel Microsoft. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** qui a un**[Calculer (données GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** méthode. Cette méthode est appelée sur toutes vos formules. Dans cette méthode, nous capturons le**MYTESTFUNC** formule et multiplier par 2 pour sa première valeur de paramètre.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

