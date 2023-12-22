---
title: Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells
description: In questo articolo viene descritto come estendere il motore di calcolo predefinito implementando un motore di calcolo personalizzato utilizzando la libreria Aspose.Cells. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per implementare un motore di calcolo personalizzato e ottenere i risultati. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine
type: docs
weight: 80
url: /it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
##  **Implementare il motore di calcolo personalizzato**

Aspose.Cells dispone di un potente motore di calcolo in grado di calcolare quasi tutte le formule Excel di Microsoft. Nonostante ciò, ti consente anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Per implementare questa funzionalità vengono utilizzate le proprietà e le classi seguenti.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[Motore di calcolo astratto] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[CalculationData](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Il codice seguente implementa il motore di calcolo personalizzato. Implementa l'interfaccia**[Motore di calcolo astratto] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** che ha a**[Calcola(datiCalculationData)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** metodo. Questo metodo viene chiamato contro tutte le tue formule. All'interno di questo metodo, catturiamo il file**TODAY** funzione e aggiungere un giorno alla data del sistema. Pertanto, se la data corrente è 27/07/2023, il motore personalizzato calcolerà TODAY() come 28/07/2023.

###  **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

###  **Risultato**

Controlla l'output della console del codice di esempio riportato sopra, il valore (data e ora) di A1 con il motore personalizzato dovrebbe essere un giorno successivo rispetto al risultato senza motore personalizzato.

###  **Articolo correlato**

{{% alert color="primary" %}}

[Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
