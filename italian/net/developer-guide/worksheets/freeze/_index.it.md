---
title: Blocca i riquadri del foglio di lavoro Excel
linktitle: Blocca i riquadri
type: docs
weight: 190
url: /it/net/how-to-freeze-panes-of-excel-worksheet
description: In questo articolo imparerai come bloccare i riquadri dei fogli di lavoro Excel a livello di codice utilizzando la libreria C# con .NET API.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

In questo articolo impareremo come bloccare i riquadri.
Quando hai un'enorme quantità di dati sotto un'intestazione comune, non riesci a vedere l'intestazione quando scorri verso il basso il foglio di lavoro. E ogni record contiene molti dati. È possibile bloccare i riquadri in modo da poter vedere la parte bloccata anche quando si scorre il resto dei dati. Puoi vedere facilmente le intestazioni nelle righe superiori o nelle prime colonne. Il blocco e lo sblocco dei riquadri modifica solo la visualizzazione dei dati senza modificare i dati stessi.

{{% /alert %}}

##  **In Excel**

**![Blocca riquadri in Excel](Freeze-panes.png)**


1. Se desideri bloccare riquadri, bloccare righe e colonne, seleziona prima una cella (come B2)
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Blocca riquadri.
4. Se scorri verso il basso o verso destra, la prima riga e colonna vengono congelate.

**![Fonzen riquadri](Frozen-Panes.png)**

 Come puoi vedere la prima riga e la colonna A sono congelate, la seconda riga è 32 e la seconda colonna visibile è D.

I riquadri di blocco ti consentono di visualizzare dati di grandi dimensioni senza tenere traccia dell'etichetta di riga o colonna.




##  **Blocca riquadri con Aspose.Cells per .Net**
 È semplice bloccare i riquadri con Aspose.Cells per .Net. Si prega di utilizzare il[**Foglio di lavoro.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)metodo per tariffare i vetri allo Cell selezionato .
1. Costruisci cartella di lavoro per aprire il file o creare un file vuoto.
2. Blocca i riquadri con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Allegato[file Excel di origine del campione](Freeze.xlsx).
