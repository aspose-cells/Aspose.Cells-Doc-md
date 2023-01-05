---
title: Utilizzo del motore di calcolo personalizzato
type: docs
weight: 70
url: /it/net/working-with-custom-calculation-engine/
---
## **Implementa il motore di calcolo personalizzato**

Aspose.Cells.Gridweb ha un potente motore di calcolo in grado di calcolare quasi tutte le formule Excel Microsoft. Nonostante ciò, ti consente anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate per implementare questa funzionalità.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

Il codice seguente implementa il motore di calcolo personalizzato. Implementa l'interfaccia**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** che ha un**[Calcola(dati GridCalculationData)](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** metodo. Questo metodo viene chiamato contro tutte le tue formule. All'interno di questo metodo, acquisiamo il file**MYTESTFUNC** formula e moltiplicare per 2 per il suo primo valore di parametro .

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

