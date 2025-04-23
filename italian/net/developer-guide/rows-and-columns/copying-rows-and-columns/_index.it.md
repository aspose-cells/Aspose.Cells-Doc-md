---
title: Copiatura di righe e colonne
type: docs
weight: 40
url: /it/net/copying-rows-and-columns/
description: Questo articolo mostra come copiare righe e colonne tramite l API Aspose.Cells for .NET.
keywords: C# Come copiare righe e colonne, Copia righe in C#, Copia colonne usando C#, Come incollare righe e colonne usando Aspose.Cells for .NET, Incolla righe e colonne multiple, Come copiare e incollare singola riga o colonna.
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

Aspose.Cells fornisce il metodo [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Questo metodo copia tutti i tipi di dati, incluse formule, valori, commenti, formati delle celle, celle nascoste, immagini e altri oggetti grafici dalla riga di origine alla riga di destinazione.

Il metodo [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) richiede i seguenti parametri:

- l'oggetto [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) di origine,
- l'indice della riga di origine e
- l'indice della riga di destinazione.

Utilizza questo metodo per copiare una riga all'interno di un foglio o in un altro foglio. Il metodo [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) funziona in modo simile a Microsoft Excel. Quindi, ad esempio, non è necessario impostare esplicitamente l'altezza della riga di destinazione, quel valore viene copiato anche.

Nell'esempio seguente viene mostrato come copiare una riga in un foglio di lavoro. Utilizza un file modello di Microsoft Excel e copia la seconda riga (completa di dati, formattazione, commenti, immagini e così via) e la incolla nella dodicesima riga nello stesso foglio di lavoro.

Puoi saltare il passaggio che ottiene l'altezza della riga di origine utilizzando il metodo [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) e poi imposta l'altezza della riga di destinazione utilizzando il metodo [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) poiché il metodo [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) si occupa automaticamente dell'altezza della riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Quando si copiano le righe, è importante notare immagini correlate, grafici o altri oggetti disegnati poiché è lo stesso con Microsoft Excel:

1. Se l'indice della riga di origine è 5, l'immagine, il grafico, ecc., vengono copiati se sono contenuti nelle tre righe (l'indice della riga di inizio è 4 e l'indice della riga di fine è 6).
1. Le immagini, i grafici, ecc., esistenti nella riga di destinazione non verranno rimossi.

{{% /alert %}}

## **Come Copiare Più Righe**

Puoi anche copiare più righe su una nuova destinazione utilizzando il metodo [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) che richiede un parametro aggiuntivo di tipo intero per specificare il numero di righe di origine da copiare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Come Copiare Colonne**

Aspose.Cells fornisce il metodo [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) della classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), questo metodo copia tutti i tipi di dati, inclusi formule - con riferimenti aggiornati - e valori, commenti, formati di celle, celle nascoste, immagini e altri oggetti disegnati dalla colonna di origine alla colonna di destinazione.

Il metodo [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) richiede i seguenti parametri:

- l'oggetto [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) di origine,
- l'indice della colonna di origine e
- l'indice della colonna di destinazione.

Utilizza il metodo [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) per copiare una colonna all'interno di un foglio o in un altro foglio.

Questo esempio copia una colonna da un foglio di lavoro e la incolla in un foglio di lavoro in un altro documento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Come Copiare Più Colonne**

Similmente al metodo [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index), le API di Aspose.Cells forniscono anche il metodo [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) per copiare più colonne di origine in una nuova posizione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Come Incollare Righe e Colonne con Opzioni di Incollaggio**

Aspose.Cells fornisce ora [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) utilizzando le funzioni [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) e [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Consente di impostare l'opzione di incollaggio appropriata simile a Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
