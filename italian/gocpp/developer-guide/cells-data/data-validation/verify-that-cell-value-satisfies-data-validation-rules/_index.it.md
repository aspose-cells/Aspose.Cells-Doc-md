---
title: Verificare che il valore della cella soddisfi le regole di validazione dei dati con Golang tramite C++
linktitle: Verificare che il valore della cella soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Scopri come verificare se il valore della cella soddisfa le regole di validazione dei dati tramite l API Aspose.Cells for C++.
keywords: Ottieni il valore di convalida della cella, Ottieni il valore di convalida della cella, Verifica se un valore soddisfa le regole di convalida dei dati applicate alla cella
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di validazione dei dati alle celle. Ad esempio, una validazione decimale specifica che possono essere inseriti solo numeri tra 10 e 20. Se l'utente inserisce un numero diverso, Excel mostra un messaggio di errore e invita a inserire un numero nel range corretto. Se si copia e incolla un numero, per esempio 3, nella cella, Excel non esegue un controllo di validazione né mostra un messaggio di errore.

A volte è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella in modo programmatico. Nel caso sopra, ad esempio, l'ingresso dovrebbe fallire.

{{% /alert %}} 

## **Introduzione**
Aspose.Cells fornisce il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) per convalidare i valori delle celle programmaticamente. Se il valore in una cella non soddisfa la regola di validazione dei dati applicata a quella cella, restituisce **False**, altrimenti **True**.

Il seguente esempio di codice illustra come funziona il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/). Prima, inserisce il valore 3 in C1. Poiché ciò non soddisfa la regola di validazione dei dati, il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) restituisce **False**. Poi, inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di validazione dei dati, il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) restituisce **True**. In modo simile, restituisce **False** per il valore 30.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **Output**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
