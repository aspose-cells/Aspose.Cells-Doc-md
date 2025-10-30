---
title: Scongelare righe o colonne
linktitle: Scongelare riquadri
type: docs
weight: 190
url: /it/python-net/unfreeze-rows-or-columns-of-excel-worksheet
description: In questo articolo, imparerai come sbloccare righe, colonne o riquadri di fogli di lavoro Excel programmaticamente usando le API di Aspose.Cells for Python via .NET.
keywords: Libreria Excel Python, Python Sblocca i riquadri, Python Come sbloccare righe, Python Come sbloccare colonne, Python Come sbloccare finestra.
---

## **Introduzione**

In questo articolo, impareremo come Sbloccare Righe, Colonne e Riquadri. Se i fogli di lavoro nei file Excel sono bloccati, a volte vogliamo sbloccare il foglio di lavoro o regolare le righe, le colonne o i riquadri bloccati.


## **Come sbloccare righe o colonne in Excel**

1. Fare clic sulla scheda Visualizzazione > Riquadri bloccati > Scongela riquadri.

**![scongelare riquadri in Excel](Scongela-Riquadri.png)**




## **Come sbloccare righe, colonne o riquadri con Aspose.Cells per Python Libreria Excel**
È semplice sbloccare i riquadri con Aspose.Cells for Python via .NET. Usa il metodo [**Worksheet.un_freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/un_freeze_panes/) per sbloccare i riquadri.

1. Costruisci il workbook per aprire il file bloccato.
2. Scongela i riquadri con il metodo Worksheet.UnFreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Unfreeze-Pane.py" >}}

Allegato il [file Excel di origine di esempio](Frozen.xlsx).
{{< app/cells/assistant language="python-net" >}}
