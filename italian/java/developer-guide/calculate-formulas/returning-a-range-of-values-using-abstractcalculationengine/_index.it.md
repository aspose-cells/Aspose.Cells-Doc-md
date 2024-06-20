---
title: Restituzione di un Intervallo di Valori utilizzando l AbstractCalculationEngine
type: docs
weight: 275
url: /it/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) che viene utilizzata per implementare funzioni utente o personalizzate non supportate da Microsoft Excel come funzioni integrate.

Questo articolo spiegherà come restituire l'intervallo di valori da [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

Il seguente codice dimostra l'uso del [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) e restituisce l'intervallo di valori tramite il suo metodo.

Creare una classe con una funzione *CalcolaFunzionePersonalizzata*. Questa classe estende [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Ora utilizza la funzione sopra nel tuo programma

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
