---
title: Travailler avec un moteur de calcul personnalisé pour GridJs
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/customcalculation/
description: Cet article explique comment utiliser le moteur de calcul personnalisé pour la bibliothèque Aspose.Cells.GridJs.
---
## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells.GridJs dispose d'un puissant moteur de calcul capable de calculer presque toutes les formules Excel Microsoft. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** qui a un**[Calculer (données GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** méthode. Cette méthode est appelée sur toutes vos formules. Dans cette méthode, nous capturons le**MYTESTFUNC** formule et multiplier par 2 pour sa première valeur de paramètre.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
