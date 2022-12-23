---
title: Utilizzo della funzione ICustomFunction
type: docs
weight: 30
url: /it/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Questo articolo fornisce informazioni dettagliate su come utilizzare la funzionalità ICustomFunction per implementare funzioni personalizzate con le API Aspose.Cells.

L'interfaccia ICustomFunction consente di aggiungere funzioni di calcolo delle formule personalizzate per estendere il motore di calcolo principale Aspose.Cells al fine di soddisfare determinati requisiti. Questa funzionalità è utile per definire funzioni personalizzate (definite dall'utente) in un file modello o nel codice in cui la funzione personalizzata può essere implementata e valutata utilizzando le API Aspose.Cells come qualsiasi altra funzione Excel Microsoft predefinita.

{{% /alert %}} 
## **Creazione e valutazione di una funzione definita dall'utente**
Questo articolo illustra l'implementazione dell'interfaccia ICustomFunction per scrivere una funzione personalizzata e utilizzarla nel foglio di calcolo per ottenere i risultati. Definiremo una funzione personalizzata per nome**MyFunc** che accetterà 2 parametri con i seguenti dettagli.

- Il primo parametro si riferisce a una singola cella
- Il secondo parametro si riferisce a un intervallo di celle

La funzione personalizzata aggiungerà tutti i valori dall'intervallo di celle specificato come secondo parametro e dividerà il risultato con il valore nel primo parametro.

Ecco come abbiamo implementato il metodo CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Ecco come utilizzare la funzione appena definita in un foglio di calcolo



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Panoramica**
Le API Aspose.Cells inseriscono semplicemente l'oggetto ReferredArea in "paramsList" quando il parametro corrispondente è un riferimento o il risultato calcolato è un riferimento. Se hai bisogno del riferimento stesso, puoi utilizzare direttamente la ReferredArea. Se è necessario ottenere il valore di una singola cella dal riferimento corrispondente alla posizione della formula, è possibile utilizzare il metodo ReferredArea.GetValue(rowOffset, int colOffset). Se hai bisogno di un array di valori di cella per l'intera area, puoi utilizzare il metodo ReferredArea.GetValues.

Siccome le API Aspose.Cells danno la ReferredArea in "paramsList", la ReferredAreaCollection in "contextObjects" non sarà più necessaria (nelle vecchie versioni non era sempre possibile dare una mappa uno-a-uno ai parametri della funzione custom) quindi è è stato rimosso dai "contextObjects".

{{< highlight "java" >}}

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
