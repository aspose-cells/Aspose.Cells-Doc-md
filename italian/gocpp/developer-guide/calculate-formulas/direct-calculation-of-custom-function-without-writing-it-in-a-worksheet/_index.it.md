---
title: Calcolo diretto di funzioni personalizzate senza scriverle in un foglio di lavoro con Golang tramite C++
linktitle: Calcolo diretto della funzione personalizzata
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per calcolare direttamente le funzioni personalizzate in Microsoft Excel senza scriverle nel foglio di lavoro. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per calcolare la funzione personalizzata e ottenere il risultato. Alla fine, salviamo il file Excel modificato sul disco.
keywords: Aspose.Cells, Excel, funzioni personalizzate, calcoli diretti, non c è bisogno di scrivere, fogli di lavoro
type: docs
weight: 90
url: /it/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**

Questo argomento spiega come calcolare direttamente le proprie funzioni personalizzate senza prima scriverle in un foglio di lavoro. Utilizzare il metodo [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/) a questo scopo.

Vedi il seguente esempio di codice che illustra l'uso di questo metodo. Abbiamo utilizzato una funzione personalizzata chiamata MyCompany::CustomFunction() e calcoliamo il suo valore come "Aspose.Cells." manually, e questo valore viene automaticamente concatenato con il valore della cella A1, che è "Benvenuto in ", tramite il motore di calcolo. Il valore finale calcolato viene restituito come "Benvenuto in Aspose.Cells.". Come puoi vedere nel codice, non abbiamo scritto la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

### **Esempio di programmazione**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **Output della console**

Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Articolo correlato**

{{% alert color="primary" %}}

[Implementa motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
