---
title: Lavorare con un motore di calcolo personalizzato
type: docs
weight: 70
url: /it/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb, personalizzato, calcolo, CalculationEngine, GridAbstractCalculationEngine
description: Questo articolo introduce come utilizzare GridAbstractCalculationEngine per personalizzare il processo di calcolo in GridWeb.
---

## **Implementare un Motore di Calcolo Personalizzato**

Aspose.Cells.Gridweb dispone di un potente motore di calcolo che può calcolare quasi tutte le formule di Microsoft Excel. Tuttavia, consente anche di estendere il motore di calcolo predefinito che fornisce maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate nell'implementazione di questa funzionalità.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

Il seguente codice implementa il motore di calcolo personalizzato. Implementa l'interfaccia [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) che ha un metodo [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate). Questo metodo viene chiamato per tutte le formule. All'interno di questo metodo, catturiamo la formula **MYTESTFUNC** e moltiplichiamo per 2 il valore del suo primo parametro.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

