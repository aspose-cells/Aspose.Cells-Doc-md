---
title: Come verificare lo stato di blocco senza Excel.
linktitle: Stato congelato
type: docs
weight: 190
url: /it/python-net/how-to-check-frozen-state-of-excel-worksheet
description: In questo articolo, imparerai come verificare lo stato di blocco del foglio di lavoro Excel programmaticamente usando Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Python Come verificare lo stato di blocco senza Excel, Verifica dello stato di blocco senza Excel in Python.
---

## **Introduzione**

In questo articolo, impareremo come verificare lo stato di blocco di un foglio di lavoro Excel programmaticamente. Possiamo semplicemente scoprire se il foglio di lavoro è bloccato o diviso in MS Excel. Ma esiste un modo per scoprire se è bloccato o diviso con CSharp. Possiamo farlo facilmente con Aspose.Cells for Python via .NET.

## **Come verificare lo stato di blocco**
Con Aspose.Cells for Python via .NET, possiamo verificare se la finestra è bloccata e quanthe righe e colonne sono di blocco.

Si prega di utilizzare la proprietà [**Worksheet.pane_state**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/pane_state/) per verificare lo stato dei riquadri della finestra 
e ottenere righe e colonne bloccate con il metodo [**Worksheet.get_freezed_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/get_freezed_panes/#any-any-any-any).
1. Costruire il Workbook per aprire il file.
2. Verificare se il foglio di lavoro è congelato.
3. Ottiene le righe e le colonne bloccate

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Is-Worksheet-Frozen.py" >}}
