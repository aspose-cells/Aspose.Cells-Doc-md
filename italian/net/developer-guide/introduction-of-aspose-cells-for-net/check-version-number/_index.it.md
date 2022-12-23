---
title: Controlla il numero di versione
type: docs
weight: 80
url: /it/net/check-version-number/
---
{{% alert color="primary" %}}

Ti chiedi quale versione di Aspose.Cells stai usando? Pubblichiamo regolarmente nuove versioni di Aspose.Cells, sia per introdurre nuove funzionalità che per risolvere problemi. Il numero di versione è costituito dal numero di versione principale, dal numero di versione secondaria e dal numero di versione dell'aggiornamento rapido. Ogni numero deve essere un numero intero da 0 in su. Il formato è il seguente:

major.minor.hotfix

Quando rilasciamo una nuova build di Aspose.Cells, aggiorniamo il numero di versione.

Questo articolo spiega come verificare manualmente quale versione di Aspose.Cells è installata sul sistema e utilizzando Aspose.Cells API.

{{% /alert %}}

## **Controlla il numero di versione manualmente**

Per scoprire quale versione di Aspose.Cells stai utilizzando manualmente:

1.  Fare clic con il pulsante destro del mouse sul file Aspose.Cells.dll e selezionare**Proprietà**.
1. Fare clic sulla scheda Versione (o Dettagli) per verificare il numero di versione.

## **Controllare il numero di versione utilizzando Aspose.Cells API**

 Per scoprire quale versione di Aspose.Cells stai usando attraverso lo API, usa il[CellsHelper](https://reference.aspose.com/cells/net/aspose.cells/cellshelper) class GetVersion metodo statico per ottenere il numero di versione di Aspose.Cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}
