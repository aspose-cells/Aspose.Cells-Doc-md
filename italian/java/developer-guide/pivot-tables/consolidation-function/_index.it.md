---
title: Funzione di consolidamento
type: docs
weight: 20
url: /it/java/consolidation-function/
description: Applicare ConsolidationFunction ai campi dati della tabella pivot.
---
## **Funzione di consolidamento**

 Aspose.Cells può essere utilizzato per applicare ConsolidationFunction ai campi dati (o campi valore) della tabella pivot. In Microsoft Excel, è possibile fare clic con il pulsante destro del mouse sul campo del valore e quindi selezionare**Impostazioni campo valore...** opzione e quindi selezionare la scheda**Riepiloga valori per**. Da lì, puoi selezionare qualsiasi ConsolidationFunction di tua scelta come Sum, Count, Average, Max, Min, Product, Distinct Count, ecc.

 Aspose.Cells fornisce[**Funzione di consolidamento**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) enumerazione per supportare le seguenti funzioni di consolidamento.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidamentoFunzione.MIN
- ConsolidationFunction.PRODUCT
- Funzione di consolidamento.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- Funzione di consolidamento.DISTINCT_COUNT

### **Applicazione di ConsolidationFunction ai campi dati della tabella pivot**

 Si applica il seguente codice**MEDIA** funzione di consolidamento al primo campo dati (o campo valore) e**STD_DEV** funzione di consolidamento al secondo campo dati (o campo valore).

Il file sorgente di esempio e i file di output possono essere scaricati da qui per testare il codice di esempio:

[File Excel di origine](source.xlsx)

[File Excel di output](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

La funzione di consolidamento DistinctCount è supportata solo da Microsoft Excel 2013.

{{% /alert %}}

