---
title: Restituzione di un intervallo di valori tramite ICustomFunction
type: docs
weight: 50
url: /it/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 Il[**IFunzione personalizzata**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) è deprecato dal rilascio di Aspose.Cells for Java 20.8. Si prega di utilizzare il[**Motore di calcolo astratto**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe. L'uso del[**Motore di calcolo astratto**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) classe è descritta nel seguente articolo.

[Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells fornisce[**IFunzione personalizzata**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)interfaccia utilizzata per implementare funzioni definite dall'utente o personalizzate che non sono supportate da Microsoft Excel come funzioni integrate.

 Principalmente quando si implementa il[**IFunzione personalizzata**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) metodo di interfaccia, è necessario restituire un singolo valore di cella. Ma a volte è necessario restituire un intervallo di valori. Questo articolo spiegherà come restituire l'intervallo di valori da[**IFunzione personalizzata**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Il codice seguente implementa[**IFunzione personalizzata**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)e restituisce l'intervallo di valori tramite il suo metodo.

 Crea una classe con una funzione*Calcola funzione personalizzata*. Questa classe implementa[**IFunzione personalizzata**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Ora usa la funzione sopra nel tuo programma

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
