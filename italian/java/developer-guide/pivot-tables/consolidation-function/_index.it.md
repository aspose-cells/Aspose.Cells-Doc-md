---
title: Funzione di consolidamento
type: docs
weight: 20
url: /it/java/consolidation-function/
description: Applicare la funzione di consolidamento ai campi dati della tabella pivot.
---

## **funzione di consolidamento**

Aspose.Cells può essere utilizzato per applicare ConsolidationFunction ai campi dati (o campi di valore) della tabella pivot. In Microsoft Excel, è possibile fare clic con il pulsante destro del mouse sul campo di valore e quindi selezionare l'opzione **Impostazioni campo valore...** e quindi selezionare la scheda **Sommario valori per**. Da lì, è possibile selezionare qualsiasi ConsolidationFunction a propria scelta come Somma, Conteggio, Media, Massimo, Minimo, Prodotto, Conteggio univoco, ecc.

Aspose.Cells fornisce l'enumerazione [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) per supportare le seguenti funzioni di consolidamento.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **Applicazione della funzione di consolidamento ai campi dati della tabella pivot**

Il codice seguente applica la funzione di consolidamento **MEDIA** al primo campo dati (o campo valore) e la funzione di consolidamento **STD_DEV** al secondo campo dati (o campo valore).

Il file di origine e i file di output di esempio possono essere scaricati da qui per testare il codice di esempio:

[File Excel di origine](source.xlsx)

[File Excel di output](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

La funzione di consolidamento DistinctCount è supportata solo da Microsoft Excel 2013.

{{% /alert %}}

