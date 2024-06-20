---
title: Utilizzo della funzione ICustomFunction
description: Questo articolo descrive come creare una funzione personalizzata in Microsoft Excel utilizzando la funzionalità ICustomFunction nella libreria Aspose.Cells. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per definire e registrare funzioni personalizzate e ottenere i risultati. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, funzioni personalizzate, funzioni personalizzate
type: docs
weight: 30
url: /it/net/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

Questo articolo fornisce una comprensione dettagliata di come utilizzare la funzione ICustomFunction per implementare funzioni personalizzate con le API di Aspose.Cells.

L'interfaccia ICustomFunction consente di aggiungere funzioni di calcolo delle formule personalizzate per estendere il motore di calcolo centrale di Aspose.Cells al fine di soddisfare determinati requisiti. Questa funzione è utile per definire funzioni personalizzate (definite dall'utente) in un file di modello o nel codice, dove la funzione personalizzata può essere implementata e valutata utilizzando le API di Aspose.Cells come qualsiasi altra funzione predefinita di Microsoft Excel.

Si prega di notare che questa interfaccia è stata sostituita da [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) e verrà rimossa in futuro. Alcuni articoli/esempi tecnici sulla nuova API: [qui](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) e [qui](/cells/it/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Creazione e valutazione di una funzione definita dall'utente**
Questo articolo illustra l'implementazione dell'interfaccia ICustomFunction per scrivere una funzione personalizzata e utilizzarla nel foglio di calcolo per ottenere i risultati. Definiremo una funzione personalizzata con il nome **MyFunc** che accetterà 2 parametri con i seguenti dettagli.

- Il primo parametro si riferisce a una singola cella
- Il secondo parametro si riferisce a un intervallo di celle

La funzione personalizzata sommerà tutti i valori dell'intervallo di celle specificato come secondo parametro e dividerà il risultato per il valore nel primo parametro.

Ecco come abbiamo implementato il metodo CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Ecco come utilizzare la funzione appena definita in un foglio di calcolo



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Panoramica**
Le API di Aspose.Cells inseriscono semplicemente l'oggetto ReferredArea nel "paramsList" quando il parametro corrispondente è un riferimento o il suo risultato calcolato è un riferimento. Se è necessario il riferimento stesso, è possibile utilizzare direttamente ReferredArea. Se è necessario ottenere il valore di una singola cella dal riferimento corrispondente alla posizione della formula, è possibile utilizzare il metodo ReferredArea.GetValue(rowOffset, colOffset). Se è necessario un array di valori delle celle per l'intera area, è possibile utilizzare il metodo ReferredArea.GetValues.

Poiché le API di Aspose.Cells restituiscono ReferredArea in "paramsList", la ReferredAreaCollection in "contextObjects" non sarà più necessaria (nelle vecchie versioni non era sempre in grado di dare una mappatura uno a uno ai parametri della funzione personalizzata) pertanto è stata rimossa da "contextObjects".

{{< highlight java >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
