---
title: Controlla il Numero di Versione
type: docs
weight: 80
url: /it/net/check-version-number/
---

{{% alert color="primary" %}}

Ti chiedi quale versione di Aspose.Cells stai utilizzando? Pubblichiamo regolarmente nuove versioni di Aspose.Cells, per introdurre nuove funzionalità e risolvere problemi. Il numero di versione è composto da numero di versione principale, numero di versione minore, e numero di correzione. Ogni numero deve essere un intero da 0 in su. Il formato è il seguente:

versionePrincipale.versioneMinore.correzione

Quando rilasciamo un nuovo build di Aspose.Cells, aggiorniamo il numero di versione.

Questo articolo spiega come verificare manualmente quale versione di Aspose.Cells è installata sul sistema e utilizzando l'API Aspose.Cells.

{{% /alert %}}

## **Controlla il Numero di Versione Manualmente**

Per scoprire quale versione di Aspose.Cells stai utilizzando manualmente:

1. Fai clic con il pulsante destro del mouse sul file Aspose.Cells.dll e seleziona **Proprietà**.
1. Fai clic sulla scheda Versione (o Dettagli) per verificare il numero di versione.

## **Controlla il Numero di Versione Utilizzando l'API Aspose.Cells**

Per scoprire quale versione di Aspose.Cells stai utilizzando attraverso l'API, utilizza il metodo statico GetVersion della classe [CellsHelper](https://reference.aspose.com/cells/net/aspose.cells/cellshelper) per ottenere il numero di versione di Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
