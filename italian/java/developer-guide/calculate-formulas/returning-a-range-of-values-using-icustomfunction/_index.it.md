---
title: Restituzione di un intervallo di valori tramite ICustomFunction
type: docs
weight: 270
url: /it/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 Il[**IFunzione personalizzata**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) è deprecato dal rilascio di Aspose.Cells for Java 20.8. Si prega di utilizzare il[**Motore di calcolo astratto**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) classe. L'uso del[**Motore di calcolo astratto**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) classe è descritta nel seguente articolo.

[Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells fornisce[**IFunzione personalizzata**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)interfaccia utilizzata per implementare funzioni definite dall'utente o personalizzate che non sono supportate da Microsoft Excel come funzioni predefinite.

 Principalmente quando si implementa il[**IFunzione personalizzata**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) metodo di interfaccia, è necessario restituire un singolo valore di cella. Ma a volte è necessario restituire un intervallo di valori. Questo articolo spiegherà come restituire l'intervallo di valori da[**IFunzione personalizzata**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Restituzione di un intervallo di valori tramite ICustomFunction**

 Il codice seguente implementa[**IFunzione personalizzata**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) e restituisce l'intervallo di valori tramite il suo metodo. Si prega di controllare[file excel di output](5472922.xlsx) e[PDF](5472925.pdf) generato con il codice per riferimento.

Crea una classe con una funzione*Calcola funzione personalizzata*. Questa classe implementa[**IFunzione personalizzata**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Ora usa la funzione sopra nel tuo programma.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
