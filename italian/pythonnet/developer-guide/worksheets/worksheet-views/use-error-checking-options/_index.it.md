---
title: Usa le opzioni di controllo degli errori
type: docs
weight: 140
url: /it/python-net/use-error-checking-options/
description: In questo articolo, troverai codice di esempio che utilizza programmaticamente le opzioni di verifica degli errori dei fogli di lavoro Excel, ad esempio numeri memorizzati come testo, usando l API Aspose.Cells per Python via .NET.
keywords: Biblioteca Python Excel, memorizzare numeri come testo in Excel in Python, Come gestire le opzioni di verifica degli errori di Excel in Python.
---

{{% alert color="primary" %}}

Microsoft Excel consente agli utenti di definire opzioni e regole di controllo degli errori. Gli utenti vedono spesso controlli degli errori quando creano formule, in alto a destra di una cella compare un piccolo triangolo quando c'è un problema con una cella. Excel fornisce informazioni che aiutano gli utenti a correggere problemi comuni.

{{% /alert %}}

## **Tipi di errori**

Gli errori che significano che la formula non può restituire un risultato - come dividere un numero per zero - richiedono immediata attenzione e un valore di errore viene visualizzato nella cella. Cliccando sul triangolo verde appare un punto esclamativo, cliccandoci apre un elenco di opzioni.

L'errore può essere risolto utilizzando le opzioni, o essere ignorato. Ignorare un errore significa che quell'errore non apparirà nei successivi controlli degli errori.

Aspose.Cells for Python via .NET fornisce funzioni di controllo degli errori. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/python-net/aspose.cells/errorcheckoption) gestisce diversi tipi di controlli degli errori, ad esempio numeri memorizzati come testo, errori di calcolo delle formule ed errori di validazione. Usa l'enumerazione [**ErrorCheckType**](https://reference.aspose.com/cells/python-net/aspose.cells/errorchecktype) per impostare il controllo degli errori desiderato.

## **Numeri memorizzati come testo**

Occasionalmente, i numeri potrebbero essere formattati e memorizzati nelle celle come testo. Questo può causare problemi con i calcoli o produrre ordini di ordinamento confusi. I numeri formattati come testo sono allineati a sinistra invece che a destra nella cella. Se una formula che dovrebbe eseguire un'operazione matematica sulle celle non restituisce un valore, controllare l'allineamento delle celle a cui si riferisce la formula: alcune o tutte quelle celle potrebbero essere numeri formattati come testo.

È possibile utilizzare le opzioni di controllo degli errori per convertire rapidamente i numeri memorizzati come testo in numeri reali. In Microsoft Excel 2003:

1. Nel menu **Strumenti**, fare clic su **Opzioni**.
1. Seleziona la scheda Controllo errori. l'opzione **Numero memorizzato come testo** è selezionata di default.
1. Disabilitala.

Il seguente esempio di codice mostra come disabilitare l'opzione di controllo degli errori di numeri memorizzati come testo per un foglio di lavoro nel file modello XLS usando le API di Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ErrorCheckingOptions-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
