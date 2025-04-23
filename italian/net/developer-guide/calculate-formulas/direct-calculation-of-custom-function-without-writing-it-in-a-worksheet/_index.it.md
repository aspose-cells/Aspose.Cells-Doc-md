---
title: Calcolo diretto di una funzione personalizzata senza scriverla in un foglio di lavoro
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per calcolare direttamente le funzioni personalizzate in Microsoft Excel senza scriverle nel foglio di lavoro. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per calcolare la funzione personalizzata e ottenere il risultato. Alla fine, salviamo il file Excel modificato sul disco.
keywords: Aspose.Cells, Excel, funzioni personalizzate, calcoli diretti, non c è bisogno di scrivere, fogli di lavoro
type: docs
weight: 90
url: /it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**

Questo argomento spiega come è possibile calcolare direttamente le funzioni personalizzate senza scriverle prima in un foglio di lavoro. Si prega di utilizzare il metodo [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) per questo scopo.

Si prega di vedere il seguente codice di esempio che illustra l'uso di questo metodo. Abbiamo utilizzato una funzione personalizzata chiamata MyCompany.CustomFunction() e ne calcoliamo il valore come "Aspose.Cells." e questo valore viene automaticamente concatenato con il valore della cella A1 che è "Benvenuto in " dall'interprete di calcolo e il valore calcolato finale ritorna come "Benvenuto in Aspose.Cells.".". Come si può vedere dal codice, non abbiamo scritto la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Output della console**

Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Articolo correlato**

{{% alert color="primary" %}}

[Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
