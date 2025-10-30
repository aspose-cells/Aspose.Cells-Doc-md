---
title: Verificare che il valore della cella soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Impara come verificare se il valore di una cella soddisfa le regole di validazione dei dati tramite l’API Aspose.Cells for Node.js via C++.
keywords: Ottieni il valore di validazione della cella Node.js tramite C++, Verifica se un valore soddisfa le regole di validazione dei dati applicate alla cella Node.js tramite C++, Verifica se un valore soddisfa le regole di validazione dei dati applicate alla cella Node.js tramite C++
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di validazione dei dati alle celle. Ad esempio, una validazione decimale specifica che possono essere inseriti solo numeri tra 10 e 20. Se l'utente inserisce un numero diverso, Excel mostra un messaggio di errore e invita a inserire un numero nel range corretto. Se si copia e incolla un numero, per esempio 3, nella cella, Excel non esegue un controllo di validazione né mostra un messaggio di errore.

A volte è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella in modo programmatico. Nel caso sopra, ad esempio, l'ingresso dovrebbe fallire.

{{% /alert %}} 
## **Introduzione**
Aspose.Cells for Node.js via C++ fornisce il metodo [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) per convalidare i valori delle celle programmaticamente. Se il valore in una cella non soddisfa la regola di validazione dei dati applicata a quella cella, restituisce **false**, altrimenti **true**.

Il seguente esempio di codice illustra come funziona il metodo [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--). Per prima cosa, inserisce il valore 3 in C1. Poiché questo non soddisfa la regola di validazione dei dati, il metodo [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) restituisce **false**. Quindi, inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di validazione dei dati, il metodo [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) restituisce **true**. Allo stesso modo, restituisce **false** per il valore 30.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **Output**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
