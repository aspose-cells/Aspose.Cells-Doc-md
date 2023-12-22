---
title: Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine
description: Questo articolo introduce un motore di calcolo astratto che restituisce un intervallo di valori in Microsoft Excel utilizzando la libreria Aspose.Cells. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo utilizzare i metodi forniti da Aspose.Cells per ottenere un intervallo di valori e restituire il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, an abstract calculation engine that returns a series of values
type: docs
weight: 55
url: /it/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce[**Motore di calcolo astratto**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe utilizzata per implementare funzioni definite dall'utente o personalizzate che non sono supportate da Microsoft Excel come funzioni integrate.

 Questo articolo spiegherà come restituire l'intervallo di valori da[**Motore di calcolo astratto**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

 Il codice seguente illustra l'uso di[**Motore di calcolo astratto**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) class e restituisce l'intervallo di valori tramite il suo metodo.

Crea una classe con una funzione *CalculateCustomFunction*. Questa classe implementa[**Motore di calcolo astratto**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Ora usa la funzione sopra nel tuo programma

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
