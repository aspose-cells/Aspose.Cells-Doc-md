---
title: Verificare che il valore della cella soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Scopri come verificare che il valore della cella soddisfi le regole di convalida dei dati tramite l API Aspose.Cells for .NET.
keywords: Ottieni il valore di convalida della cella, Ottieni il valore di convalida della cella, Verifica se un valore soddisfa le regole di convalida dei dati applicate alla cella
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di convalida dei dati alle celle. Ad esempio, una convalida decimale specifica che possono essere inseriti solo numeri compresi tra 10 e 20. Se un utente inserisce un numero diverso, Microsoft Excel visualizza un messaggio di errore e chiede loro di inserire un numero nell'intervallo corretto. Se si copia e incolla un numero, ad esempio 3, nella cella, Excel non esegue un controllo di convalida o mostra un messaggio di errore.

A volte è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella in modo programmatico. Nel caso sopra, ad esempio, l'ingresso dovrebbe fallire.

{{% /alert %}} 
## **Introduzione**
Aspose.Cells fornisce il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) per convalidare i valori delle celle in modo programmatico. Se il valore in una cella non soddisfa la regola di convalida dei dati applicata a quella cella, restituisce **Falso**, altrimenti **Vero**.

Il seguente codice di esempio illustra il funzionamento del metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue). Prima, inserisce il valore 3 in C1. Poiché ciò non soddisfa la regola di convalida dei dati, il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) restituisce **Falso**. Poi, inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di convalida dei dati, il metodo [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) restituisce **Vero**. Allo stesso modo, restituisce **Falso** per il valore 30.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Output**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
