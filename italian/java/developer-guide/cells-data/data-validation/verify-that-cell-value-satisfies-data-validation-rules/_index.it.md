---
title: Verificare che il valore Cell soddisfi le regole di convalida dei dati
type: docs
weight: 90
url: /it/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di aggiungere regole di convalida dei dati alle celle del foglio di lavoro. Ad esempio, è possibile applicare una convalida decimale per limitare i numeri tra 10 e 20. Se viene inserito qualsiasi altro numero al di fuori di questo intervallo specificato, Microsoft Excel mostra un messaggio di errore e richiede all'utente di reinserire un numero dall'intervallo corretto. Se la copia dell'utente incolla un numero, ad esempio 3, nella cella, Excel non esegue il controllo di convalida o mostra un messaggio di errore.

{{% /alert %}}

## Verificare che il valore Cell soddisfi le regole di convalida dei dati

A volte è necessario verificare dinamicamente se un determinato valore soddisfa le regole di convalida dei dati applicate alla cella. A tale scopo, le API Aspose.Cells forniscono il[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) metodo. Se il valore in una cella non soddisfa la regola di convalida dei dati applicata a quella cella, restituisce**Falso** , altro**Vero**.

Il seguente file Excel di esempio Microsoft viene utilizzato con il codice di esempio riportato di seguito per testare il file[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) metodo. Come puoi vedere nell'istantanea che le celle**C1** ha**convalida dei dati decimali** applicato e accetterà solo valori**tra le 10 e le 20** . Ogni volta che il valore della cella è compreso tra 10 e 20,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) verrà restituito**Vero** , altrimenti tornerà**Falso**.

![cose da fare:immagine_alt_testo](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 Il codice di esempio seguente illustra come il[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) il metodo funziona. Innanzitutto, inserisce il valore 3 in C1. Poiché ciò non soddisfa la regola di convalida dei dati, il file[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) restituisce il metodo**Falso** . Quindi, inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di convalida dei dati, il[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) restituisce il metodo**Vero** . Allo stesso modo, ritorna**Falso** per valore 30.

## Java codice per verificare se un valore Cell soddisfa le regole di convalida dei dati

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Output della console generato dal codice di esempio

Ecco l'output della console generato quando il codice di esempio viene eseguito con il file Excel di esempio mostrato sopra.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
