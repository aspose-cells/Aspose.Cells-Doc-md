---
title: Verificare che il valore della cella soddisfi le regole di convalida dei dati
type: docs
weight: 90
url: /it/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di aggiungere regole di convalida dei dati alle celle del foglio di lavoro. Ad esempio, può essere applicata una convalida decimale per limitare i numeri tra 10 e 20. Se viene inserito qualsiasi altro numero al di fuori di questo intervallo specificato, Microsoft Excel mostra un messaggio di errore e richiede all'utente di reinserire un numero dall'intervallo corretto. Se l'utente copia e incolla un numero, ad es. 3, nella cella, Excel non esegue il controllo di convalida o mostra un messaggio di errore.

{{% /alert %}}

Verifica che il valore della cella soddisfi le regole di convalida dei dati

A volte è necessario verificare dinamicamente se un dato valore soddisfa le regole di convalida dei dati applicate alla cella. A questo scopo, le API di Aspose.Cells forniscono il metodo [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Se il valore in una cella non soddisfa la regola di convalida dei dati applicata a quella cella, restituisce **Falso**, altrimenti **Vero**.

Il file di esempio di seguito di Microsoft Excel viene usato con il codice di esempio sottostante per testare il metodo [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Come puoi vedere nello snapshot, le celle C1 hanno la convalida dei dati decimali applicata e accetteranno solo valori tra 10 e 20. Ogni volta che il valore della cella è compreso tra 10 e 20, il metodo [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) restituirà **Vero**, altrimenti restituirà **Falso**.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

Il seguente esempio di codice illustra come funziona il metodo [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--). Per prima cosa, immette il valore 3 in C1. Poiché ciò non soddisfa la regola di convalida dei dati, il metodo [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) restituisce **Falso**. Poi, immette il valore 15 in C1. Poiché questo valore soddisfa la regola di convalida dei dati, il metodo [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) restituisce **Vero**. Allo stesso modo, restituisce **Falso** per il valore 30.

Codice Java per verificare se un valore della cella soddisfa le regole di convalida dei dati

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Output della console generato dall'esempio di codice

Ecco l'output della console generato quando il codice di esempio viene eseguito con il file Excel di esempio mostrato sopra.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
