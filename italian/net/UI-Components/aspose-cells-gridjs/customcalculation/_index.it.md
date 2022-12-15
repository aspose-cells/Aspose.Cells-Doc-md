---
title: Utilizzo del motore di calcolo personalizzato per GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/customcalculation/
description: Questo articolo descrive come utilizzare il motore di calcolo personalizzato per la libreria Aspose.Cells.GridJs.
---
## **Implementa il motore di calcolo personalizzato**

Aspose.Cells.GridJs ha un potente motore di calcolo in grado di calcolare quasi tutte le formule di Microsoft Excel. Nonostante ciò, ti consente anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate per implementare questa funzionalità.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

Il codice seguente implementa il motore di calcolo personalizzato. Implementa l'interfaccia**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** che ha un**[Calcola(dati GridCalculationData)](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** metodo. Questo metodo viene chiamato contro tutte le tue formule. All'interno di questo metodo, acquisiamo il file**MYTESTFUNC** formula e moltiplicare per 2 per il suo primo valore di parametro .

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
