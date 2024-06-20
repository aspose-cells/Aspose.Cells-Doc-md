---
title: Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells
description: Questo articolo descrive come estendere il motore di calcolo predefinito implementando un motore di calcolo personalizzato utilizzando la libreria Aspose.Cells. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per implementare un motore di calcolo personalizzato e ottenere i risultati. Alla fine, salviamo il file Excel modificato sul disco.
keywords: Aspose.Cells, Excel, Motore di calcolo personalizzato, estende il motore di calcolo predefinito
type: docs
weight: 80
url: /it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementare un Motore di Calcolo Personalizzato**

Aspose.Cells ha un potente motore di calcolo che può calcolare quasi tutte le formule di Microsoft Excel. Nonostante ciò, ti permette anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate nell'implementazione di questa funzionalità.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

Il seguente codice implementa il Motore di Calcolo Personalizzato. Implementa l'interfaccia [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) che ha un metodo [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate). Questo metodo viene chiamato per tutte le formule. All'interno di questo metodo, catturiamo la funzione **TODAY** e aggiungiamo un giorno alla data di sistema. Quindi, se la data corrente è il 27/07/2023, il motore personalizzato calcolerà TODAY() come 28/07/2023.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Risultato**

Si prega di controllare l'output della console del codice di esempio sopra, il valore (data ora) di A1 con il motore personalizzato dovrebbe essere un giorno dopo rispetto al risultato senza il motore personalizzato.

### **Articolo correlato**

{{% alert color="primary" %}}

[Calcolo diretto della funzione personalizzata senza scriverla in un foglio di calcolo](/cells/it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
