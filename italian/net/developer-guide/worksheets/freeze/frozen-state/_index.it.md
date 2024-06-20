---
title: Come controllare lo stato congelato senza Excel.
linktitle: Stato congelato
type: docs
weight: 190
url: /it/net/how-to-check-frozen-state-of-excel-worksheet
description: In questo articolo, imparerai come verificare lo stato congelato del foglio di lavoro di Excel in modo programmatico utilizzando la libreria C# con API .NET.

---

## **Introduzione**

In questo articolo, impareremo come verificare lo stato bloccato del foglio di lavoro di Excel in modo programmato. Possiamo facilmente verificare se il foglio di lavoro è bloccato o diviso in MS Excel. Ma c'è un modo per sapere se è bloccato o diviso con CSharp. Possiamo farlo facilmente con Aspose.Cells for .Net.

## **Le riquadri della finestra sono congelati**
Con Aspose.Cells per .Net, possiamo verificare se la finestra è congelata e quante righe e colonne sono bloccate.

Si prega di utilizzare la proprietà [**Worksheet.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) per verificare lo stato dei riquadri della finestra 
e ottenere righe e colonne bloccate con il metodo [**Worksheet.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/).
1. Costruire il Workbook per aprire il file.
2. Verificare se il foglio di lavoro è congelato.
3. Ottiene le righe e le colonne bloccate

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}
