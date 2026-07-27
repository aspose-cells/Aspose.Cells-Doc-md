---
title: Funzione di consolidamento
type: docs
weight: 20
url: /it/net/consolidation-function/
---

## **funzione di consolidamento**

Aspose.Cells può essere utilizzato per applicare ConsolidationFunction ai campi dati (o campi di valore) della tabella pivot. In Microsoft Excel, è possibile fare clic con il pulsante destro del mouse sul campo di valore e quindi selezionare l'opzione **Impostazioni campo valore...** e quindi selezionare la scheda **Sommario valori per**. Da lì, è possibile selezionare qualsiasi ConsolidationFunction a propria scelta come Somma, Conteggio, Media, Massimo, Minimo, Prodotto, Conteggio univoco, ecc.

Aspose.Cells fornisce l'enumerazione [**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) per supportare le seguenti funzioni di consolidamento.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

### **Applicazione della funzione di consolidamento ai campi dati della tabella pivot**

Il seguente codice applica la funzione di consolidamento **Media** al primo campo dati (o campo valore) e la funzione di consolidamento **ConteggioDistinto** al secondo campo dati (o campo valore).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

La funzione di consolidamento DistinctCount è supportata solo da Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
