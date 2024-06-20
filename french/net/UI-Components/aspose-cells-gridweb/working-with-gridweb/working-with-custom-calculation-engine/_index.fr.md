---
title: Travailler avec un moteur de calcul personnalisé
type: docs
weight: 70
url: /fr/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb, personnalisé, calcul, CalculationEngine, GridAbstractCalculationEngine
description: Cet article présente comment utiliser GridAbstractCalculationEngine pour personnaliser le processus de calcul dans GridWeb.
---

## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells.Gridweb dispose d'un moteur de calcul puissant qui peut calculer presque toutes les formules de Microsoft Excel. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

Le code suivant met en œuvre le moteur de calcul personnalisé. Il implémente l'interface [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) qui a une méthode [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate). Cette méthode est appelée pour toutes vos formules. À l'intérieur de cette méthode, nous capturons la formule **MYTESTFUNC** et multiplions par 2 pour sa première valeur de paramètre.

### **Exemple de programmation**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

