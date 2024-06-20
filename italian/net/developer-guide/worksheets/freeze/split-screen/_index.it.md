---
title: Schermata divisa del foglio di lavoro di Excel
linktitle: Schermata divisa
type: docs
weight: 190
url: /it/net/how-to-split-screen-of-excel-worksheet
description: In questo articolo imparerai come visualizzare determinate righe e/o colonne in riquadri separati suddividendo il foglio di lavoro in due o quattro parti programmabilmente utilizzando la libreria C# con API .NET.
keywords: Blocca le righe in alto
---

## **Introduzione**

In questo articolo, impareremo come visualizzare determinate righe e/o colonne in riquadri separati suddividendo il foglio di lavoro in due o quattro parti. Quando si lavora con grandi set di dati, è necessario vedere diverse aree dello stesso foglio di lavoro contemporaneamente per confrontare differenti sottoinsiemi di dati. La funzione di suddivisione dello schermo può soddisfare le tue esigenze.

## **Come dividere lo schermo in Excel**
Per suddividere un foglio di lavoro in due o quattro parti, procedi come segue:

1. Seleziona la riga/colonna/cella prima della quale desideri posizionare la suddivisione.
2. Sulla scheda Visualizza, nel gruppo Finestre, fai clic sul pulsante Suddivisione.

**![Schermata divisa](Split-Screen.png)**

## **Suddividi il foglio di lavoro verticalmente sulle colonne**

Per separare due aree del foglio di calcolo verticalmente, seleziona la colonna a destra della colonna in cui desideri che appaia la suddivisione e fai clic sul pulsante Suddivisione in Excel.

È facile suddividere il foglio di lavoro verticalmente sulle colonne in modo programmabile con Aspose.Cells per .Net, è sufficiente selezionare una cella nella riga superiore come cella attiva, quindi
diviso con il metodo [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **Suddividi il foglio di lavoro orizzontalmente sulle righe**
Per separare la finestra di Excel orizzontalmente, seleziona la riga sotto la riga in cui desideri che avvenga la suddivisione in Excel.

È facile suddividere il foglio di lavoro orizzontalmente sulle righe in modo programmabile con Aspose.Cells per .Net, è sufficiente selezionare una cella nella colonna di sinistra come cella attiva, quindi
diviso con il metodo [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **Dividi il foglio di lavoro in quattro parti.**
Per visualizzare contemporaneamente quattro diverse sezioni dello stesso foglio di lavoro, dividi lo schermo sia verticalmente che orizzontalmente in Excel.

È facile dividere il foglio di lavoro verticalmente sulle colonne in modo programmato con Aspose.Cells for .Net, dobbiamo solo selezionare una cella non nella prima riga e colonna come cella attiva, poi
diviso con il metodo [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **Come rimuovere la divisione**
Per rimuovere la divisione del foglio di lavoro, basta fare clic sul pulsante Dividi di nuovo.

Aspose.Cells for .Net fornisce un metodo [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) per rimuovere l'impostazione di divisione.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
