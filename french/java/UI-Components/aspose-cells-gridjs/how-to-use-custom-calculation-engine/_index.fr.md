---
title: Travailler avec un moteur de calcul personnalisé pour GridJs
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: Cet article décrit comment utiliser le moteur de calcul personnalisé pour la bibliothèque Aspose.Cells.GridJs.
aliases:
  - /java/aspose-cells-gridjs/customcalculation/
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells.GridJs dispose d'un puissant moteur de calcul qui peut calculer presque toutes les formules Microsoft Excel. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre une plus grande puissance et flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)

Le code suivant met en œuvre le moteur de calcul personnalisé. Il implémente l'interface [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine) qui a une méthode [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate). Cette méthode est appelée pour toutes vos formules. À l'intérieur de cette méthode, nous capturons la formule **MYTESTFUNC** et multiplions par 2 pour sa première valeur de paramètre.

### **Exemple de programmation**

```JAVA
class MyCalculation : GridAbstractCalculationEngine
        {
           public override void calculate(GridCalculationData data)
            {
                if (!"MYTESTFUNC".Equals(data.FunctionName.ToUpper()))
                {
                    return;
                }
                data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));
            }
        }
// in the startup.cs when you do initialization ,set the CalculateEngine		
  MyCalculation ce = new MyCalculation();
  GridJsWorkbook.CalculateEngine = ce;

```
