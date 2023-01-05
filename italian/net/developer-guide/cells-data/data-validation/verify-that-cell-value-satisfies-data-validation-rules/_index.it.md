---
title: Verificare che il valore Cell soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di convalida dei dati alle celle. Ad esempio, una convalida decimale specifica che è possibile immettere solo numeri compresi tra 10 e 20. Se un utente inserisce un numero diverso. Microsoft Excel mostra un messaggio di errore e richiede di inserire un numero nell'intervallo corretto. Se copi e incolli un numero, ad esempio 3, nella cella, Excel non esegue un controllo di convalida o mostra un messaggio di errore.

volte, è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella a livello di codice. Nel caso precedente, ad esempio, la voce dovrebbe fallire.

{{% /alert %}} 
## **introduzione**
 Aspose.Cells fornisce il[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodo per convalidare i valori delle celle a livello di codice. Se il valore in una cella non soddisfa la regola di convalida dei dati applicata a quella cella, restituisce**Falso** , altro**Vero**.

 Il codice di esempio seguente illustra come il[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodo funziona. Innanzitutto, inserisce il valore 3 in C1. Poiché ciò non soddisfa la regola di convalida dei dati, il file[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodo restituisce**Falso** . Quindi, inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di convalida dei dati, il[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodo restituisce**Vero** . Allo stesso modo, ritorna**Falso** per valore 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Produzione**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
