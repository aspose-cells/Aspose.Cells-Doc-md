---
title: Copiatura di righe e colonne
type: docs
weight: 40
url: /it/python-net/copying-rows-and-columns/
description: Questo articolo mostra come copiare righe e colonne tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Come copiare righe e colonne in Python, Copiare righe in Python, Copiare colonne usando Python, Come incollare righe e colonne usando Aspose.Cells per Python via .NET, Come incollare righe e colonne multiple in Python, Come copiare e incollare singola riga o colonna in Python.
---

## **Introduzione**

A volte è necessario copiare righe e colonne in un foglio di lavoro senza copiare l'intero foglio di lavoro. Con Aspose.Cells, è possibile copiare righe e colonne all'interno o tra i fogli di lavoro.
Quando viene copiata una riga (o colonna), vengono copiati anche i dati contenuti al suo interno, inclusi formule - con riferimenti aggiornati - e valori, commenti, formattazione, celle nascoste, immagini e altri oggetti grafici.

## **Come copiare righe e colonne con Microsoft Excel**

1. Seleziona la riga o la colonna che desideri copiare.
1. Per copiare righe o colonne, fai clic su **Copia** sulla barra degli strumenti **Standard**, oppure premi **CTRL**+**C**.
1. Seleziona una riga o una colonna sotto o alla destra di dove desideri copiare la tua selezione.
1. Quando stai copiando righe o colonne, fai clic su **Celle Copiate** nel menu **Inserisci**.

{{% alert color="primary" %}}

Se fai clic su **Incolla** sulla barra degli strumenti **Standard** o premi **CTRL**+**V** anziché fare clic su un comando nel menu **Inserisci**, i contenuti delle celle di destinazione vengono sostituiti.

{{% /alert %}}

## **Come incollare righe e colonne utilizzando le opzioni di incolla con Microsoft Excel**

1. Seleziona le celle che contengono i dati o altri attributi che desideri copiare.
1. Nella scheda Home, fai clic su **Copia**.
1. Fai clic sulla prima cella nell'area in cui desideri **incollare** quello che hai copiato.
1. Nella scheda Home, fai clic sulla freccia accanto a **Incolla**, quindi seleziona **Incolla speciale**.
1. Seleziona le **opzioni** desiderate.

## **Come copiare righe e colonne usando Aspose.Cells for .NET**

## **Come copiare singole righe**

Aspose.Cells fornisce il metodo [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) della classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Questo metodo copia tutti i tipi di dati, incluse formule, valori, commenti, formati delle celle, celle nascoste, immagini e altri oggetti grafici dalla riga di origine alla riga di destinazione.

Il metodo [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) richiede i seguenti parametri:

- l'oggetto [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) di origine,
- l'indice della riga di origine, e
- l'indice della riga di destinazione.

Utilizza questo metodo per copiare una riga all'interno di un foglio o in un altro foglio. Il metodo [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) funziona in modo simile a Microsoft Excel. Quindi, ad esempio, non è necessario impostare esplicitamente l'altezza della riga di destinazione, quel valore viene copiato anche.

Nell'esempio seguente viene mostrato come copiare una riga in un foglio di lavoro. Utilizza un file modello di Microsoft Excel e copia la seconda riga (completa di dati, formattazione, commenti, immagini e così via) e la incolla nella dodicesima riga nello stesso foglio di lavoro.

Puoi saltare il passaggio che ottiene l'altezza della riga di origine utilizzando il metodo [**Cells.get_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/get_row_height/#int) e poi imposta l'altezza della riga di destinazione utilizzando il metodo [**Cells.set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) poiché il metodo [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) si occupa automaticamente dell'altezza della riga.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingRows-1.py" >}}

{{% alert color="primary" %}}

Quando si copiano le righe, è importante notare immagini correlate, grafici o altri oggetti disegnati poiché è lo stesso con Microsoft Excel:

1. Se l'indice della riga di origine è 5, l'immagine, il grafico, ecc., vengono copiati se sono contenuti nelle tre righe (l'indice della riga di inizio è 4 e l'indice della riga di fine è 6).
1. Le immagini, i grafici, ecc., esistenti nella riga di destinazione non verranno rimossi.

{{% /alert %}}

## **Come Copiare Più Righe**

Puoi anche copiare più righe su una nuova destinazione utilizzando il metodo [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int) che richiede un parametro aggiuntivo di tipo intero per specificare il numero di righe di origine da copiare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleRows-1.py" >}}


## **Come Copiare Colonne**

Aspose.Cells fornisce il metodo [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) della classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), questo metodo copia tutti i tipi di dati, inclusi formule - con riferimenti aggiornati - e valori, commenti, formati di celle, celle nascoste, immagini e altri oggetti disegnati dalla colonna di origine alla colonna di destinazione.

Il metodo [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) richiede i seguenti parametri:

- l'oggetto [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) di origine,
- l'indice della colonna di origine e
- l'indice della colonna di destinazione.

Utilizza il metodo [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) per copiare una colonna all'interno di un foglio o in un altro foglio.

Questo esempio copia una colonna da un foglio di lavoro e la incolla in un foglio di lavoro in un altro documento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingColumns-1.py" >}}

## **Come Copiare Più Colonne**

Similmente al metodo [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int), le API di Aspose.Cells forniscono anche il metodo [**Cells.copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/) per copiare più colonne di origine in una nuova posizione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleColumns-1.py" >}}


## **Come Incollare Righe e Colonne con Opzioni di Incollaggio**

Aspose.Cells fornisce ora [**PasteOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions) utilizzando le funzioni [**copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int-aspose.cells.CopyOptions-aspose.cells.PasteOptions) e [**copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/#aspose.cells.Cells-int-int-int-aspose.cells.PasteOptions). Consente di impostare l'opzione di incollaggio appropriata simile a Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.py" >}}

