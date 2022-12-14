---
title: Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro
type: docs
weight: 90
url: /it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**

 Questo argomento spiega come calcolare direttamente le funzioni personalizzate senza prima scriverle in un foglio di lavoro. Si prega di utilizzare il[**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)metodo per questo scopo.

Vedere il seguente codice di esempio che illustra l'utilizzo di questo metodo. Abbiamo utilizzato una funzione personalizzata denominata MyCompany.CustomFunction() e ne calcoliamo il valore come "Aspose.Cells". da noi stessi e quindi questo valore viene automaticamente concatenato con il valore della cella A1 che è "Welcome to " dal motore di calcolo e il valore finale calcolato ritorna come "Welcome to Aspose.Cells."". Come puoi vedere in un codice che abbiamo non ha scritto la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Uscita console**

Di seguito è riportato l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Articolo correlato**

{{% alert color="primary" %}}

[Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
