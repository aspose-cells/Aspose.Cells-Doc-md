---
title: Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells
type: docs
weight: 80
url: /it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **Implementa il motore di calcolo personalizzato**

Aspose.Cells ha un potente motore di calcolo in grado di calcolare quasi tutte le formule di Microsoft Excel. Nonostante ciò, ti consente anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate per implementare questa funzionalità.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[Dati di calcolo](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Il codice seguente implementa il motore di calcolo personalizzato. Implementa l'interfaccia**[AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** che ha un**[Calcola (dati dati di calcolo)](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** metodo. Questo metodo viene chiamato contro tutte le tue formule. All'interno di questo metodo, acquisiamo il file**Somma** formula e ne aumenta il valore di 30. Quindi, se il valore calcolato Aspose.Cells è 20, il nostro motore personalizzato lo renderà 50 aggiungendo 30.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Uscita console**

Ecco l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **Articolo correlato**

{{% alert color="primary" %}}

[Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
