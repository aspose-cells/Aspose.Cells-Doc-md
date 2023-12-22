---
title: Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro
description: Questo articolo illustra come utilizzare la libreria Aspose.Cells per calcolare direttamente le funzioni personalizzate in Microsoft Excel senza scrivere la funzione in un foglio di lavoro. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo utilizzare i metodi forniti da Aspose.Cells per calcolare la funzione personalizzata e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
##  **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**

 Questo argomento spiega come calcolare direttamente le funzioni personalizzate senza prima scriverle in un foglio di lavoro. Si prega di utilizzare il[**Worksheet.CalculateFormula(formula stringa, opzioni CalculationOptions)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)metodo a questo scopo.

Consultare il seguente codice di esempio che illustra l'utilizzo di questo metodo. Abbiamo utilizzato una funzione personalizzata denominata MyCompany.CustomFunction() e calcoliamo il suo valore come "Aspose.Cells". da noi stessi e quindi questo valore viene automaticamente concatenato con il valore della cella A1 che è "Benvenuto a " dal motore di calcolo e il valore finale calcolato restituisce "Benvenuto a Aspose.Cells."". Come puoi vedere in un codice che abbiamo non è stata scritta la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

###  **Esempio di programmazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

###  **Uscita della console**

Di seguito è riportato l'output della console del codice di esempio riportato sopra.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

###  **Articolo correlato**

{{% alert color="primary" %}}

[Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
