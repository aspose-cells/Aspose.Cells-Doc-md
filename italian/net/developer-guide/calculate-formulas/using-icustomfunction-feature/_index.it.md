---
title: Utilizzo della funzionalità ICustomFunction
description: Questo articolo descrive come creare una funzione personalizzata in Excel Microsoft utilizzando la funzionalità ICustomFunction nella libreria Aspose.Cells. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo utilizzare i metodi forniti da Aspose.Cells per definire e registrare funzioni personalizzate e ottenere i risultati. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /it/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Questo articolo fornisce informazioni dettagliate su come utilizzare la funzionalità ICustomFunction per implementare funzioni personalizzate con le API Aspose.Cells.

L'interfaccia ICustomFunction consente di aggiungere funzioni di calcolo della formula personalizzata per estendere il motore di calcolo principale di Aspose.Cells al fine di soddisfare determinati requisiti. Questa funzionalità è utile per definire funzioni personalizzate (definite dall'utente) in un file modello o nel codice in cui la funzione personalizzata può essere implementata e valutata utilizzando le API Aspose.Cells come qualsiasi altra funzione Excel Microsoft predefinita.

 Tieni presente che questa interfaccia è stata sostituita da[Motore di calcolo astratto](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) verranno rimossi in futuro. Alcuni articoli/esempi tecnici sul nuovo API:[Qui](/cells/it/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) E[Qui](/cells/it/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **Creazione e valutazione di una funzione definita dall'utente**
 Questo articolo illustra l'implementazione dell'interfaccia ICustomFunction per scrivere una funzione personalizzata e utilizzarla nel foglio di calcolo per ottenere i risultati. Definiremo una funzione personalizzata per nome**MyFunc** che accetterà 2 parametri con i seguenti dettagli.

- Il 1° parametro si riferisce a una singola cella
- Il 2° parametro si riferisce a un intervallo di celle

La funzione personalizzata aggiungerà tutti i valori dall'intervallo di celle specificato come 2° parametro e dividerà il risultato con il valore nel 1° parametro.

Ecco come abbiamo implementato il metodo CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Ecco come utilizzare la funzione appena definita in un foglio di calcolo



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **Panoramica**
Le API Aspose.Cells inseriscono semplicemente l'oggetto ReferredArea in "paramsList" quando il parametro corrispondente è un riferimento o il suo risultato calcolato è un riferimento. Se hai bisogno del riferimento stesso, puoi utilizzare direttamente ReferredArea. Se è necessario ottenere il valore di una singola cella dal riferimento corrispondente alla posizione della formula, è possibile utilizzare il metodo ReferredArea.GetValue(rowOffset, int colOffset). Se hai bisogno di un array di valori di cella per l'intera area, puoi utilizzare il metodo ReferredArea.GetValues.

Poiché le API Aspose.Cells forniscono la ReferredArea in "paramsList", la ReferredAreaCollection in "contextObjects" non sarà più necessaria (nelle vecchie versioni non era sempre in grado di fornire una mappa uno a uno ai parametri della funzione personalizzata) quindi è stato rimosso da "contextObjects".

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
