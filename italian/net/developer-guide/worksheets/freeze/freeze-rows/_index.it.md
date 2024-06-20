---
title: Congelare la/e riga/e superiore/i del foglio di calcolo di Excel
linktitle: Congelare righe
type: docs
weight: 190
url: /it/net/how-to-freeze-rows-of-excel-worksheet
description: In questo articolo imparerai come congelare le righe superiori dei fogli di lavoro di Excel in modo programmato usando la libreria C# con API .NET.
keywords: Blocca le righe in alto
---

## **Introduzione**

In questo articolo, impareremo come bloccare (freezare) righe in alto. Quando hai una grande quantità di dati sotto un'intestazione comune e non riesci a vedere l'intestazione quando scendi verticalmente, puoi bloccare le righe in alto in modo da poter vedere quella parte fissa anche quando si scorrono il resto dei dati. In questo modo, puoi vedere facilmente le intestazioni nelle righe in alto.

## **Congelare le righe in Excel**

**![Congelare la/e riga/e superiore/i in Excel](Freeze-Rows.png)**


1. Se si desidera congelare la/e riga/e superiore/i, selezionare prima la riga sotto la riga che deve essere congelata
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Congela riga superiore.
4. Se si scorre verso il basso, la prima riga è sempre nella vista superiore.

**![Fila congelata](Frozen-Row.png)**

Come puoi vedere, la prima riga è congelata, la prima riga rimane sempre in cima alla visualizzazione quando scorri verso il basso.

Congelare le righe ti consente di visualizzare i tuoi dati di grandi dimensioni senza dover tenere traccia dell'etichetta della riga.




## **Congelare le righe con Aspose.Cells per .Net**
È semplice congelare la/e riga/e con Aspose.Cells per .Net. 
Si prega di utilizzare il metodo [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) per congelare la/e riga/e alla riga selezionata.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Congelare la prima riga con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Row.cs" >}}

File Excel di esempio allegato(../Freeze.xlsx).
