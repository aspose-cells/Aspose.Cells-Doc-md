---
title: Blocca i riquadri del foglio di lavoro di Excel
linktitle: Congelare i riquadri
type: docs
weight: 190
url: /it/net/how-to-freeze-panes-of-excel-worksheet
description: In questo articolo imparerai come bloccare i riquadri dei fogli di lavoro di Excel a livello di codice utilizzando la libreria C# con .NET API.
keywords: Freeze panes, Feeze window.
---
{{% alert color="primary" %}}

In questo articolo impareremo come bloccare i riquadri.
Quando si dispone di un'enorme quantità di dati sotto un'intestazione comune, non è possibile visualizzare l'intestazione quando si scorre il foglio di lavoro. E ogni record contiene molti dati. Puoi bloccare i riquadri in modo da poter vedere quella parte bloccata anche quando il resto dei dati viene fatto scorrere. Puoi vedere facilmente le intestazioni nelle righe superiori o nelle prime colonne. Il blocco e lo sblocco dei riquadri modifica solo la visualizzazione dei dati senza modificare i dati stessi.

{{% /alert %}}

##  **In Excel**

**![Blocca riquadri in Excel](Freeze-panes.png)**


1. Se desideri bloccare i riquadri per bloccare righe e colonne, seleziona prima una cella (come B2)
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Blocca riquadri.
4. Se scorri verso il basso o verso destra, la prima riga e colonna vengono bloccate.

**![Fonzen panges](Frozen-Panes.png)**

Come puoi vedere 1st Row e la colonna A sono Freezed , la seconda riga che mostra è 32 e la seconda colonna visibile è D.

I riquadri di blocco ti consentono di visualizzare i tuoi dati di grandi dimensioni senza tenere traccia dell'etichetta di riga o colonna.




##  **Blocca i riquadri con Aspose.Cells per .Net**
 È semplice bloccare i riquadri con Aspose.Cells per .Net. Si prega di utilizzare il[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)metodo per visualizzare i riquadri allo Cell selezionato.
1. Crea cartella di lavoro per aprire il file o creare un file vuoto.
2. Blocca i riquadri con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

 Allegato[file Excel sorgente di esempio](Freeze.xlsx).
