---
title: Come impostare l area di stampa
type: docs
weight: 200
url: /it/net/how-to-set-print-area/
description: Questo articolo ti mostra come impostare l area di stampa utilizzando la libreria Aspose.Cells.
keywords: Limita l intervallo di stampa, Imposta l intervallo di stampa, Cancella l intervallo di stampa, Imposta e cancella l intervallo di stampa usando C#, C# Come impostare l area di stampa, Imposta e cancella l area di stampa usando C#, Come cancellare l area di stampa in C#, Come aggiungere l area di stampa usando C#, come rimuovere l area di stampa usando C#, Come impostare l area di stampa in Excel, Come cancellare l area di stampa in Excel.
---

## **Possibili Scenari di Utilizzo**

Impostare un'area di stampa in un documento, come un foglio di calcolo Excel, aiuta a controllare quali contenuti vengono inclusi durante la stampa. Ecco alcuni motivi per impostare un'area di stampa:

1. Concentrarsi su dati specifici: puoi stampare solo le sezioni più rilevanti, evitando contenuti non necessari.
1. Layout migliorato: aiuta a organizzare e adattare i contenuti ordinatamente sulle pagine di stampa, evitando interruzioni o salti di pagina indesiderati.
1. Risparmiare risorse: limitando l'area di stampa, puoi ridurre l'uso di carta e inchiostro.
1. Presentazione professionale: garantisce che vengano stampate solo le versioni rifinite e finali dei dati, importante particolarmente per report o presentazioni.
1. Coerenza: quando si stampa lo stesso documento più volte, avere un'area di stampa impostata garantisce coerenza nell'output.

<br>
Impostare un'area di stampa è particolarmente utile in documenti più grandi dove solo una porzione deve essere condivisa o revisionata in forma stampata.

## **Come impostare l'area di stampa in Excel**

Per impostare un'area di stampa in Excel, segui questi passaggi:

1. Seleziona le celle: clicca e trascina per selezionare l'intervallo di celle che desideri impostare come area di stampa.
1. Apri la scheda Layout di pagina: vai alla scheda "Layout di pagina" nella barra multifunzione nella parte superiore della finestra di Excel.
1. Imposta l'area di stampa: nel gruppo "Imposta pagina", clicca su "Area di stampa". Dal menu a discesa, seleziona "Imposta area di stampa".
<br>
<img src="3.png" width=60% />

1. Aggiungi all'area di stampa: se desideri aggiungere ulteriori celle all'area di stampa esistente, seleziona le celle aggiuntive, vai su "Area di stampa" nella scheda "Layout di pagina" e scegli "Aggiungi all'area di stampa".

<br>
Questa azione definirà le celle selezionate come area di stampa. Quando stamperai il foglio di lavoro, verrà stampata solo questa area definita.

## **Come eliminare l'area di stampa in Excel**

Per eliminare l'area di stampa in Excel, segui questi passaggi:

1. Apri la scheda Layout di Pagina: Clicca sulla scheda "Layout di Pagina" nella barra multifunzione in alto alla finestra di Excel.
1. Elimina l'area di stampa: nel gruppo "Impostazione pagina", clicca su "Area di stampa". Dal menu a tendina, seleziona "Elimina area di stampa".
<br>
<img src="4.png" width=60% />

<br>
Questa azione rimuoverà qualsiasi area di stampa precedentemente impostata, consentendo di stampare l'intero foglio di lavoro.

## **Cosa succede dopo aver eliminato l'area di stampa**

Eliminando l'area di stampa in un'applicazione come Excel usando Aspose.Cells, l'intero foglio di lavoro verrà incluso nella stampa del documento. Se è impostata un'area di stampa, verrà stampato solo l'intervallo di celle specificato. Eliminando l'area di stampa, si garantisce che nessun intervallo specifico sia definito, e il comportamento di stampa predefinito, che include l'intero foglio, verrà applicato.

1. Comportamento di stampa predefinito: l'intero foglio di lavoro sarà considerato per la stampa. Ciò significa che tutte le celle con dati o formattazioni verranno stampate.
1. Nessun limite di area di stampa: i limiti dell'area di stampa precedentemente definiti verranno rimossi. Se c'erano righe e colonne specifiche destinate alla stampa, non saranno più vincolate a quei limiti.
1. Stampa di tutto il contenuto: tutto il contenuto, inclusi intestazioni, piè di pagina e altri dati all'interno del foglio di lavoro, sarà incluso nel lavoro di stampa.

## **Come impostare l'area di stampa utilizzando Aspose.Cells**

Per impostare l'area di stampa in un foglio di lavoro specificato: Innanzitutto, carica il [file di esempio](input.xlsx), e poi devi modificare la proprietà [**Worksheet.PageSetup.PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printarea/) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) per il foglio desiderato. Impostare questa proprietà a una stringa di intervallo definirà l'area di stampa.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-print-area.cs" >}}

Il risultato dell'output:
<br>
<img src="1.png" width=60% />

## **Come eliminare l'area di stampa usando Aspose.Cells**

Per eliminare l'area di stampa in un foglio di lavoro specificato: Innanzitutto, carica il [file di esempio](input.xlsx), e poi devi modificare la proprietà [**Worksheet.PageSetup.PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printarea/) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) per il foglio desiderato. Impostare questa proprietà a una stringa vuota eliminerà l'area di stampa.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-clear-print-area.cs" >}}

Il risultato dell'output:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
