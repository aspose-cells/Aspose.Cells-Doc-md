---
title: Blocca le righe superiori del foglio di lavoro Excel
linktitle: Blocca righe
type: docs
weight: 190
url: /it/net/how-to-freeze-rows-of-excel-worksheet
description: In questo articolo imparerai come bloccare le righe superiori dei fogli di lavoro Excel a livello di codice utilizzando la libreria C# con .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

In questo articolo impareremo come bloccare le righe superiori.
Quando hai un'enorme quantità di dati sotto un'intestazione comune, non riesci a vedere l'intestazione quando scorri verso il basso il foglio di lavoro. Puoi bloccare le righe superiori in modo da poter vedere la parte bloccata anche quando viene fatto scorrere il resto dei dati. Puoi facilmente vedere le intestazioni nelle righe superiori.

{{% /alert %}}

##  **Blocca righe in Excel**

**![Blocca le righe superiori in Excel](Freeze-Rows.png)**


1. Se desideri congelare le righe superiori, seleziona prima la riga sotto quella che deve essere congelata
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Blocca riga superiore.
4. Se scorri verso il basso, la prima riga è sempre nella vista dall'alto.

**![Fila Fonzen](Frozen-Row.png)**

Come puoi vedere la prima riga è bloccata, la prima riga rimane sempre nella parte superiore della visualizzazione quando scorri verso il basso.

Blocca righe ti consente di visualizzare dati di grandi dimensioni senza tenere traccia dell'etichetta della riga.




##  **Blocca righe con Aspose.Cells per .Net**
 È semplice bloccare le righe con Aspose.Cells per .Net.
 Si prega di utilizzare il[**Foglio di lavoro.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)metodo per fissare le righe nella riga selezionata.
1. Costruisci cartella di lavoro per aprire il file o creare un file vuoto.
2. Blocca la prima riga con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

 Allegato[file Excel di origine del campione](../Freeze.xlsx).
