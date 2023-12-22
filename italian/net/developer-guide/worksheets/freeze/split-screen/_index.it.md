---
title: Schermo diviso del foglio di lavoro Excel
linktitle: Schermo diviso
type: docs
weight: 190
url: /it/net/how-to-split-screen-of-excel-worksheet
description: In questo articolo imparerai come visualizzare determinate righe e/o colonne in riquadri separati dividendo il foglio di lavoro in due o quattro parti a livello di codice utilizzando la Libreria C# con .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

In questo articolo impareremo come visualizzare determinate righe e/o colonne in riquadri separati dividendo il foglio di lavoro in due o quattro parti.
Quando si lavora con set di dati di grandi dimensioni, è necessario vedere alcune aree dello stesso foglio di lavoro alla volta per confrontare diversi sottoinsiemi di dati.
La funzione schermo diviso può soddisfare le tue esigenze.

{{% /alert %}}

##  **Come dividere lo schermo in Excel**
Per dividere un foglio di lavoro in due o quattro parti, procedere come segue:

1. Seleziona la riga/colonna/cella prima della quale vuoi posizionare la divisione.
2. Nella scheda Visualizza, nel gruppo Windows, fare clic sul pulsante Dividi.

**![Schermo diviso](Split-Screen.png)**

##  **Dividi il foglio di lavoro verticalmente sulle colonne**

Per separare verticalmente due aree del foglio di calcolo, seleziona la colonna a destra della colonna in cui desideri che venga visualizzata la divisione e fai clic sul pulsante Dividi in Excel.

È facile dividere il foglio di lavoro verticalmente sulle colonne a livello di codice con Aspose.Cells per .Net, dobbiamo solo selezionare una cella nella riga superiore come cella attiva, quindi
dividere con[**Foglio di lavoro.Dividi**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) metodo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **Dividi il foglio di lavoro orizzontalmente su righe**
Per separare la finestra di Excel orizzontalmente, seleziona la riga sotto la riga in cui desideri che avvenga la divisione in Excel.

È facile dividere il foglio di lavoro orizzontalmente sulle righe a livello di codice con Aspose.Cells per .Net, dobbiamo solo selezionare una cella nella colonna di sinistra come cella attiva, quindi
dividere con[**Foglio di lavoro.Dividi**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) metodo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **Dividere il foglio di lavoro in quattro parti**
Per visualizzare contemporaneamente quattro diverse sezioni dello stesso foglio di lavoro, dividi lo schermo sia verticalmente che orizzontalmente in Excel.

È facile dividere il foglio di lavoro verticalmente sulle colonne a livello di codice con Aspose.Cells per .Net, dobbiamo solo selezionare una cella non nella prima riga e colonna come cella attiva, quindi
dividere con[**Foglio di lavoro.Dividi**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) metodo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **Come rimuovere la divisione**
Per rimuovere la suddivisione del foglio di lavoro, è sufficiente fare nuovamente clic sul pulsante Dividi.

 Aspose.Cells per .Net fornisce a[**Foglio di lavoro.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) metodo per rimuovere l'impostazione di divisione.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}