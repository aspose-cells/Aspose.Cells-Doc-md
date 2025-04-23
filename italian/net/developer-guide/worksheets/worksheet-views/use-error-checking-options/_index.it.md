---
title: Usa le opzioni di controllo degli errori
type: docs
weight: 140
url: /it/net/use-error-checking-options/
description: In questo articolo, troverai del codice di esempio che utilizzerà in modo programmato le opzioni di controllo degli errori delle viste di Excel, ad es. Numeri memorizzati come testo utilizzando API C# o libreria .NET.
keywords: memorizzare numero come testo in excel usando c#, errori di controllo opzioni c# excel
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di definire opzioni e regole di controllo degli errori. Gli utenti vedono spesso controlli degli errori quando creano formule, in alto a destra di una cella compare un piccolo triangolo quando c'è un problema con una cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.

{{% /alert %}}

## **Tipi di errori**

Gli errori che significano che la formula non può restituire un risultato - come dividere un numero per zero - richiedono immediata attenzione e un valore di errore viene visualizzato nella cella. Cliccando sul triangolo verde appare un punto esclamativo, cliccandoci apre un elenco di opzioni.

L'errore può essere risolto utilizzando le opzioni, o essere ignorato. Ignorare un errore significa che quell'errore non apparirà nei successivi controlli degli errori.

Aspose.Cells fornisce funzionalità di opzioni di controllo errori. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) gestisce diversi tipi di controlli degli errori, ad esempio numeri memorizzati come testo, errori di calcolo delle formule e errori di convalida. Utilizza l'enumerazione [**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype) per impostare il controllo degli errori desiderato.

## **Numeri memorizzati come testo**

Occasionalmente, i numeri potrebbero essere formattati e memorizzati nelle celle come testo. Questo può causare problemi con i calcoli o produrre ordini di ordinamento confusi. I numeri formattati come testo sono allineati a sinistra invece che a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controllare l'allineamento delle celle a cui si riferisce la formula: alcune o tutte quelle celle potrebbero essere numeri formattati come testo.

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:

1. Nel menu **Strumenti**, fare clic su **Opzioni**.
1. Seleziona la scheda Controllo errori.
   L'opzione **Numero memorizzato come testo** è selezionata per impostazione predefinita.
1. Disabilitala.

Il seguente codice di esempio mostra come disabilitare l'opzione di controllo degli errori del numero memorizzato come testo per un foglio di lavoro nel file XLS di modello utilizzando le API di Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
