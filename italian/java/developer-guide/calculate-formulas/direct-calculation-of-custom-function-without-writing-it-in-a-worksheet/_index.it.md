---
title: Calcolo diretto di una funzione personalizzata senza scriverla in un foglio di lavoro
type: docs
weight: 650
url: /it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

Questo articolo spiega come è possibile calcolare direttamente le funzioni personalizzate senza scriverle prima in un foglio di lavoro. Si prega di utilizzare il metodo [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) per questo scopo.

{{% /alert %}} 
## **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**
Si prega di vedere il seguente codice di esempio che illustra l'uso di questo metodo. Abbiamo utilizzato una funzione personalizzata chiamata *MyCompany.CustomFunction()* e calcoliamo il suo valore come "Aspose.Cells." da soli e poi questo valore viene automaticamente concatenato con il valore della cella A1 che è "Benvenuti in " dal motore di calcolo e il valore calcolato finale restituisce "Benvenuti in Aspose.Cells.". Come si vede dal codice, non abbiamo scritto la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Output della console**
Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Articolo correlato**
{{% alert color="primary" %}} 

- [Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
