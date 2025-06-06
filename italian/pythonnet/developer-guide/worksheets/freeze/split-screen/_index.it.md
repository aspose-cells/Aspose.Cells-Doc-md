---
title: Schermata divisa del foglio di lavoro di Excel
linktitle: Schermata divisa
type: docs
weight: 190
url: /it/python-net/how-to-split-screen-of-excel-worksheet
description: In questo articolo imparerai come visualizzare determinate righe e/o colonne in riquadri separati dividendo il foglio di lavoro in due o quattro parti programmaticamente utilizzando le API di Aspose.Cells for Python via .NET.
keywords: Libreria Excel Python, Python Blocca le prime righe, Python Blocca prima riga, Python Dividi il foglio di lavoro verticalmente in colonne, Python Dividi il foglio di lavoro orizzontalmente in righe, Python Dividi il foglio di lavoro in quattro parti Python Come rimuovere la divisione.
---

## **Introduzione**

In questo articolo, impareremo come visualizzare determinate righe e/o colonne in riquadri separati suddividendo il foglio di lavoro in due o quattro parti. Quando si lavora con grandi set di dati, è necessario vedere diverse aree dello stesso foglio di lavoro contemporaneamente per confrontare differenti sottoinsiemi di dati. La funzione di suddivisione dello schermo può soddisfare le tue esigenze.

## **Come dividere lo schermo in Excel**
Per suddividere un foglio di lavoro in due o quattro parti, procedi come segue:

1. Seleziona la riga/colonna/cella prima della quale desideri posizionare la suddivisione.
2. Sulla scheda Visualizza, nel gruppo Finestre, fai clic sul pulsante Suddivisione.

**![Schermata divisa](Split-Screen.png)**

## **Come dividere il foglio di lavoro verticalmente in colonne**

Per separare due aree del foglio di calcolo verticalmente, seleziona la colonna a destra della colonna in cui desideri che appaia la suddivisione e fai clic sul pulsante Suddivisione in Excel.

È facile dividere verticalmente il foglio di lavoro in colonne programmaticamente con Aspose.Cells for Python via .NET, basta selezionare una cella nella riga superiore come cella attiva, poi
diviso con il metodo [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **Come dividere orizzontalmente il foglio di lavoro in righe**
Per separare la finestra di Excel orizzontalmente, seleziona la riga sotto la riga in cui desideri che avvenga la suddivisione in Excel.

È facile dividere orizzontalmente il foglio di lavoro in righe programmaticamente con Aspose.Cells for Python via .NET, basta selezionare una cella nella colonna a sinistra come cella attiva, poi
diviso con il metodo [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **Come dividere il foglio di lavoro in quattro parti**
Per visualizzare contemporaneamente quattro diverse sezioni dello stesso foglio di lavoro, dividi lo schermo sia verticalmente che orizzontalmente in Excel.

È facile dividere verticalmente il foglio di lavoro in colonne programmaticamente con Aspose.Cells for Python via .NET, basta selezionare una cella che non sia nella prima riga e colonna come cella attiva, poi
diviso con il metodo [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Come rimuovere la divisione**
Per rimuovere la divisione del foglio di lavoro, basta fare clic sul pulsante Dividi di nuovo.

Aspose.Cells for Python via .NET fornisce un metodo [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) per rimuovere la configurazione di divisione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
