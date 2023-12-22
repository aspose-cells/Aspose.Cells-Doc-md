---
title: Sblocca righe o colonne
linktitle: Sblocca i riquadri
type: docs
weight: 190
url: /it/net/unfreeze-rows-or-columns-of-excel-worksheet
description: In questo articolo imparerai come sbloccare righe, colonne o riquadri di fogli di lavoro Excel a livello di codice utilizzando la libreria C# con .NET API.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window.
---
{{% alert color="primary" %}}

In questo articolo impareremo come sbloccare righe, colonne e riquadri.
Se i fogli di lavoro nei file Excel sono bloccati, a volte vogliamo sbloccare il foglio di lavoro o regolare righe, colonne o riquadri bloccati.

{{% /alert %}}

##  **In Excel**

1. Fare clic sulla scheda Visualizza > Blocca riquadri > Sblocca riquadri.

**![sblocca riquadri in Excel](Unfreeze-Panes.png)**




##  **Sblocca righe, colonne o riquadri con Aspose.Cells per .Net**
 È semplice sbloccare i riquadri con Aspose.Cells per .Net. Si prega di utilizzare il[**Foglio di lavoro.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes)metodo per sbloccare i riquadri.

1. Costruisci cartella di lavoro per aprire il file congelato.
2. Sblocca i riquadri con il metodo Worksheet.UnFreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

 Allegato[file Excel di origine del campione](Frozen.xlsx).
