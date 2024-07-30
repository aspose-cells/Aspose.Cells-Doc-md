---
title: Scongelare righe o colonne
linktitle: Scongelare riquadri
type: docs
weight: 190
url: /it/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: In questo articolo, imparerai come scongelare righe, colonne o riquadri dei fogli di calcolo di Excel in modo programmato utilizzando le API di Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Scongelare riquadri di Python, Come scongelare righe di Python, come scongelare colonne di Python, come scongelare finestra.
---

## **Introduzione**

In questo articolo, impareremo come Sbloccare Righe, Colonne e Riquadri. Se i fogli di lavoro nei file Excel sono bloccati, a volte vogliamo sbloccare il foglio di lavoro o regolare le righe, le colonne o i riquadri bloccati.


## **Come scongelare righe o colonne in Excel**

1. Fare clic sulla scheda Visualizzazione > Riquadri bloccati > Scongela riquadri.

**![scongelare riquadri in Excel](Scongela-Riquadri.png)**




## **Come scongelare righe, colonne o riquadri con Aspose.Cells per la libreria Excel di Python**
Semplice scongelare i riquadri con Aspose.Cells per Python via .NET. Si prega di utilizzare il metodo [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) per scongelare i riquadri.

1. Costruisci il workbook per aprire il file bloccato.
2. Scongela i riquadri con il metodo Worksheet.UnFreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Allegato il [file Excel di origine di esempio](Frozen.xlsx).
