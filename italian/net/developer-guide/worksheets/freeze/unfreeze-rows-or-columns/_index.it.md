---
title: Scongelare righe o colonne
linktitle: Scongelare riquadri
type: docs
weight: 190
url: /it/net/unfreeze-rows-or-columns-of-excel-worksheet
description: In questo articolo imparerai come scongelare righe, colonne o riquadri dei fogli di lavoro di Excel in modo programmato utilizzando la libreria C# con API .NET.
keywords: Scongelare riquadri, Scongelare righe, Scongelare colonne, scongelare finestra.
---

## **Introduzione**

In questo articolo, impareremo come Sbloccare Righe, Colonne e Riquadri. Se i fogli di lavoro nei file Excel sono bloccati, a volte vogliamo sbloccare il foglio di lavoro o regolare le righe, le colonne o i riquadri bloccati.


## **In Excel**

1. Fare clic sulla scheda Visualizzazione > Riquadri bloccati > Scongela riquadri.

**![scongelare riquadri in Excel](Scongela-Riquadri.png)**




## **Scongela righe, colonne o riquadri con Aspose.Cells for .Net**
È semplice scongelare riquadri con Aspose.Cells for .Net. Si prega di utilizzare il metodo [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/unfreezepanes) per scongelare i riquadri.

1. Costruisci il workbook per aprire il file bloccato.
2. Scongela i riquadri con il metodo Worksheet.UnFreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Unfreeze-Pane.cs" >}}

Allegato il [file Excel di origine di esempio](Frozen.xlsx).
