---
title: Restituzione di un Intervallo di Valori utilizzando ICustomFunction
type: docs
weight: 270
url: /it/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

Il [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) è deprecato dal rilascio di Aspose.Cells for Java 20.8. Si prega di utilizzare la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine). L'uso della classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) è descritto nell'articolo seguente.

[Restituzione di un Intervallo di Valori utilizzando AbstractCalculationEngine](/cells/it/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells fornisce l'interfaccia [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) che viene utilizzata per implementare funzioni definite dall'utente o personalizzate non supportate da Microsoft Excel come funzioni integrate.

Principalmente quando si implementa il metodo dell'interfaccia [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction), è necessario restituire un singolo valore di cella. Ma a volte è necessario restituire un intervallo di valori. Questo articolo spiegherà come restituire l'intervallo di valori da [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Restituire una gamma di valori utilizzando ICustomFunction**

Il codice seguente implementa [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) e restituisce l'intervallo di valori tramite il suo metodo. Si prega di controllare il [file excel di output](5472922.xlsx) e il [pdf](5472925.pdf) generati con il codice per il riferimento.

Crea una classe con una funzione *CalculateCustomFunction*. Questa classe implementa [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Ora utilizza la funzione sopra nel tuo programma

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
