---
title: Come controllare lo stato congelato senza Excel.
linktitle: Stato congelato
type: docs
weight: 190
url: /it/net/how-to-check-frozen-state-of-excel-worksheet
description: In questo articolo imparerai come controllare lo stato congelato del foglio di lavoro Excel a livello di codice utilizzando la libreria C# con .NET API.
---
{{% alert color="primary" %}}

In questo articolo impareremo come controllare lo stato congelato del foglio di lavoro Excel a livello di codice.
Possiamo semplicemente scoprire se il foglio di lavoro è congelato o diviso in MS Excel. Ma c'è un modo per scoprire se è congelato o diviso con CSharp.
Possiamo farlo semplicemente con Aspose.Cells per .Net.
{{% /alert %}}

##  **I vetri delle finestre sono congelati**
Con Aspose.Cells per .Net possiamo verificare se la finestra è bloccata e quante righe e colonne sono bloccate.

 Si prega di utilizzare il[**Foglio di lavoro.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) proprietà per verificare lo stato dei vetri delle finestre
 e ottiene righe e colonne bloccate con[**Foglio di lavoro.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)metodo.
1. Costruisci cartella di lavoro per aprire il file.
2. Controlla se il foglio di lavoro è bloccato.
3. Ottiene la riga e le colonne bloccate

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}