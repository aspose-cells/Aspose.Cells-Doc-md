---
title: Restituzione di un Intervallo di Valori utilizzando ICustomFunction
description: Questo articolo descrive come utilizzare la libreria Aspose.Cells per restituire un intervallo di valori con ICustomFunction in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per ottenere un intervallo di valori e restituire il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, ICustomFunction, restituisce una serie di valori
type: docs
weight: 50
url: /it/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

Il [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) è deprecato dal rilascio di Aspose.Cells for Java 20.8. Si prega di utilizzare la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine). L'uso della classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) è descritto nell'articolo seguente.

[Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells fornisce l'interfaccia [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) che viene utilizzata per implementare funzioni definite dall'utente o personalizzate non supportate da Microsoft Excel come funzioni integrate.

Principalmente quando si implementa il metodo dell'interfaccia [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction), è necessario restituire un singolo valore di cella. Ma a volte è necessario restituire un intervallo di valori. Questo articolo spiegherà come restituire l'intervallo di valori da [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

Il codice seguente implementa [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) e restituisce l'intervallo di valori tramite il suo metodo.

Creare una classe con una funzione *CalculateCustomFunction*. Questa classe implementa [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Ora utilizza la funzione sopra nel tuo programma.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
