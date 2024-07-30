---
title: Lavorare con il motore di calcolo personalizzato per GridJs
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: Questo articolo descrive come utilizzare il motore di calcolo personalizzato per la libreria Aspose.Cells.GridJs.
aliases:
  - /java/aspose-cells-gridjs/customcalculation/
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **Implementare un Motore di Calcolo Personalizzato**

Aspose.Cells.GridJs ha un potente motore di calcolo che può calcolare quasi tutte le formule di Microsoft Excel. Tuttavia, ti consente anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate nell'implementazione di questa funzionalità.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)

Il seguente codice implementa il motore di calcolo personalizzato. Implementa l'interfaccia [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine) che ha un metodo [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate). Questo metodo viene chiamato per tutte le formule. All'interno di questo metodo, catturiamo la formula **MYTESTFUNC** e moltiplichiamo per 2 il valore del suo primo parametro.

### **Esempio di programmazione**

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
