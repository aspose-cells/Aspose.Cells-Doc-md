---
title: Verificare che il valore Cell soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Scopri come verificare che il valore Cell soddisfi le regole di convalida dei dati tramite Aspose.Cells for .NET API..
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di convalida dei dati alle celle. Ad esempio, una convalida decimale specifica che possono essere immessi solo numeri compresi tra 10 e 20. Se un utente inserisce un numero diverso. Microsoft Excel mostra un messaggio di errore e richiede di inserire un numero nell'intervallo corretto. Se copi e incolli un numero, ad esempio 3, nella cella, Excel non esegue un controllo di convalida né mostra un messaggio di errore.

A volte è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella a livello di codice. Nel caso precedente, ad esempio, l'inserimento dovrebbe fallire.

{{% /alert %}} 
##  **introduzione**
 Aspose.Cells fornisce il[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)metodo per convalidare i valori delle celle a livello di codice. Se il valore in una cella non soddisfa la regola di convalida dei dati applicata a quella cella, restituisce *False**, altrimenti *True**.

 Il seguente codice di esempio illustra come[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) il metodo funziona. Per prima cosa inserisce il valore 3 in C1. Poiché ciò non soddisfa la regola di convalida dei dati, il file[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) il metodo restituisce**Falso**. Quindi inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di convalida dei dati, il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) restituisce **True**. Allo stesso modo, restituisce **False** per valore 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **Produzione**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
