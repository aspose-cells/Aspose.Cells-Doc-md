---
title: Usa le opzioni di controllo degli errori
type: docs
weight: 140
url: /it/python-net/use-error-checking-options/
description: In questo articolo, troverai un codice di esempio che utilizzerà in modo programmato le opzioni di controllo degli errori dei fogli di calcolo di Excel, ad es. Numeri memorizzati come Testo utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Python memorizza il numero come testo in excel, Come gestire le opzioni di controllo degli errori in excel in Python.
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di definire opzioni e regole di controllo degli errori. Gli utenti vedono spesso controlli degli errori quando creano formule, in alto a destra di una cella compare un piccolo triangolo quando c'è un problema con una cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.

{{% /alert %}}

## **Tipi di errori**

Gli errori che significano che la formula non può restituire un risultato - come dividere un numero per zero - richiedono immediata attenzione e un valore di errore viene visualizzato nella cella. Cliccando sul triangolo verde appare un punto esclamativo, cliccandoci apre un elenco di opzioni.

L'errore può essere risolto utilizzando le opzioni, o essere ignorato. Ignorare un errore significa che quell'errore non apparirà nei successivi controlli degli errori.

Aspose.Cells per Python via .NET fornisce funzionalità di opzione per il controllo degli errori. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption) gestisce diversi tipi di controlli degli errori, ad esempio, numeri memorizzati come testo, errori di calcolo delle formule e errori di convalida. Utilizzare l'enumerazione [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype) per impostare il controllo degli errori desiderato.

## **Numeri memorizzati come testo**

Occasionalmente, i numeri potrebbero essere formattati e memorizzati nelle celle come testo. Questo può causare problemi con i calcoli o produrre ordini di ordinamento confusi. I numeri formattati come testo sono allineati a sinistra invece che a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controllare l'allineamento delle celle a cui si riferisce la formula: alcune o tutte quelle celle potrebbero essere numeri formattati come testo.

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:

1. Nel menu **Strumenti**, fare clic su **Opzioni**.
1. Seleziona la scheda Controllo errori. L'opzione **Numero memorizzato come testo** è selezionata per impostazione predefinita.
1. Disabilitala.

Il seguente codice di esempio mostra come disabilitare l'opzione di controllo degli errori dei numeri memorizzati come testo per un foglio di lavoro nel file XLS di modello utilizzando le API Aspose.Cells per Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
