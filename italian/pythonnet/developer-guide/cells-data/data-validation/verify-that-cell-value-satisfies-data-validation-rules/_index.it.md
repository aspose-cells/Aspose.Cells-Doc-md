---
title: Verificare che il valore della cella soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Scopri come verificare che il valore della cella soddisfi le regole di convalida dei dati attraverso l API Aspose.Cells per Python via .NET..
keywords: Libreria Excel in Python, Ottieni il valore della convalida della cella in Python, Ottieni il valore della convalida della cella in Python, Verifica se un valore soddisfa le regole di convalida dei dati applicate alla cella in Python.
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di convalida dei dati alle celle. Ad esempio, una convalida decimale specifica che possono essere inseriti solo numeri compresi tra 10 e 20. Se un utente inserisce un numero diverso, Microsoft Excel visualizza un messaggio di errore e chiede loro di inserire un numero nell'intervallo corretto. Se si copia e incolla un numero, ad esempio 3, nella cella, Excel non esegue un controllo di convalida o mostra un messaggio di errore.

A volte è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella in modo programmatico. Nel caso sopra, ad esempio, l'ingresso dovrebbe fallire.

{{% /alert %}} 
## **Introduzione**
Aspose.Cells per Python via .NET fornisce il metodo [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) per convalidare i valori della cella in modo programmatico. Se il valore in una cella non soddisfa la regola di convalida dei dati applicata a quella cella, restituisce **False**, altrimenti **True**.

Il codice di esempio seguente illustra come funziona il metodo [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#). Prima, immette il valore 3 in C1. Poiché questo non soddisfa la regola di convalida dei dati, il metodo [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) restituisce **Falso**. Poi, immette il valore 15 in C1. Poiché questo valore soddisfa la regola di convalida dei dati, il metodo [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) restituisce **Vero**. Allo stesso modo, restituisce **Falso** per il valore 30.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **Output**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
