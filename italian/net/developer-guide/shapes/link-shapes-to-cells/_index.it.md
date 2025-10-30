---
title: Come collegare le forme di Excel alle celle del foglio di lavoro
linktitle: Collega forme di Excel alle celle
type: docs
description: "Come collegare forme di Excel alle celle del foglio di lavoro"
weight: 3300
url: /it/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

A volte è necessario visualizzare il contenuto di una cella di un foglio di lavoro in una forma, casella di testo o elemento di un grafico. A volte, quando si modificano i dati in una cella o in un intervallo di celle, è necessario sincronizzare il contenuto della cella con quello di una forma, casella di testo o elemento di un grafico. Per fare ciò, puoi collegare una forma, una casella di testo o un elemento di un grafico alle celle che contengono i dati che desideri visualizzare.

{{% /alert %}}

## Come collegare forme alle celle in Ms Excel

La figura seguente mostra come impostare una cella collegata a una forma.

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. Seleziona una forma. La barra della formula di solito è vuota.

2. Inserisci la formula della forma, come "=A1"

## Come collegare forme alle celle in Aspose.Cells

Il seguente esempio di codice mostra come usare la libreria Aspose.Cells per impostare un collegamento per una forma o una casella di testo per visualizzare dinamicamente i contenuti di una cella.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## Utilizzo Avanzato

Se si desidera che il testo della forma sia costituito da due o più celle, o se si desidera selezionare il contenuto desiderato in base a una formula, il codice di esempio sopra potrebbe non soddisfare le proprie esigenze. In tal caso, è necessario fare qualcosa di più avanzato. È necessario prima inserire la formula che produce il risultato desiderato in una cella, e poi collegare la forma alla cella contenente la formula.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
