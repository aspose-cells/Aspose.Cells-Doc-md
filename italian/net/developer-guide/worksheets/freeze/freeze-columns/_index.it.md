---
title: Blocca le prime colonne del foglio di lavoro Excel
linktitle: Blocca colonne
type: docs
weight: 190
url: /it/net/how-to-freeze-columns-of-excel-worksheet
description: In questo articolo imparerai come bloccare le colonne di sinistra dei fogli di lavoro Excel a livello di codice utilizzando la libreria C# con .NET API.
keywords: Freeze left columns, Feeze first columns, Lock the column(s)
---
{{% alert color="primary" %}}

In questo articolo impareremo come bloccare le colonne di sinistra.
Quando hai un'enorme quantità di dati in una riga, non riesci a vedere le colonne di sinistra quando scorri orizzontalmente il foglio di lavoro. Puoi bloccare e bloccare le prime colonne in modo da poter vedere quella parte congelata anche quando viene fatto scorrere il resto dei dati. Puoi facilmente vedere le intestazioni nelle colonne di sinistra.

{{% /alert %}}

##  **Blocca colonne in Excel**

**![Blocca le colonne di sinistra in Excel](freeze-columns.png)**


1. Se desideri bloccare le colonne di sinistra, seleziona prima la colonna sotto la colonna che deve essere bloccata
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Blocca prima colonna.
4. Se scorri verso il basso, la prima colonna è sempre nella vista di sinistra.

**![Colonna Fonzen](frozen-columns.png)**

Come puoi vedere la prima colonna è bloccata, la prima colonna è sempre bloccata nella parte superiore della vista quando scorri in orizzontale.

Blocca colonne ti consente di visualizzare i tuoi dati lunghi senza tenere traccia della prima colonna.




##  **Blocca colonne con Aspose.Cells per .Net**
È semplice bloccare le prime colonne con Aspose.Cells per .Net.
 Si prega di utilizzare il[**Foglio di lavoro.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/)metodo per tariffare le colonne nella colonna selezionata.
1. Costruisci cartella di lavoro per aprire il file o creare un file vuoto.
2. Blocca la prima colonna con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Column.cs" >}}

 Allegato[file Excel di origine del campione](Freeze.xlsx).
