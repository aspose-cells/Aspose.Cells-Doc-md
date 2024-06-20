---
title: Restituzione di un Intervallo di Valori utilizzando l AbstractCalculationEngine
description: Questo articolo introduce un motore di calcolo astratto che restituisce un intervallo di valori in Microsoft Excel utilizzando la libreria Aspose.Cells. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per ottenere un intervallo di valori e restituire il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, un motore di calcolo astratto che restituisce una serie di valori
type: docs
weight: 55
url: /it/net/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) che viene utilizzata per implementare funzioni utente o personalizzate non supportate da Microsoft Excel come funzioni integrate.

Questo articolo spiegherà come restituire l'intervallo di valori da [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

Il seguente codice dimostra l'uso della classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) e restituisce l'intervallo di valori tramite il suo metodo.

Creare una classe con una funzione *CalculateCustomFunction*. Questa classe implementa [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Ora utilizza la funzione sopra nel tuo programma.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
