---
title: Fusione e Separazione Cells
type: docs
weight: 140
url: /it/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

Non vuoi sempre lo stesso numero di celle in ogni riga o colonna. Ad esempio, potresti voler inserire un titolo in una cella che si estende su più colonne. Oppure, se crei una fattura, potresti volere meno colonne per il totale. Per creare una cella da due o più celle, uniscile. Microsoft Excel consente agli utenti di selezionare le celle e unirle per strutturare il foglio di calcolo nel modo desiderato.

**Il risultato dell'unione e quindi della divisione di un intervallo di celle formattate come celle a sinistra in Microsoft Excel** 

![cose da fare:immagine_alt_testo](merging-and-unmerging-cells_1.png)

Aspose.Cells supporta questa funzione e può anche unire celle in un foglio di lavoro. Puoi separare o dividere anche le celle unite. Il riferimento di cella di una cella unita è il riferimento per la cella in alto a sinistra nell'intervallo originariamente selezionato.

Tieni presente che quando le celle vengono unite, vengono conservati solo i dati nella cella in alto a sinistra. Se sono presenti dati nelle altre celle dell'intervallo, tali dati vengono eliminati.

La formattazione, allo stesso modo, si basa sulla cella di riferimento in modo che quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengono applicate alla cella unita. Quando la cella viene divisa, le nuove celle mantengono le impostazioni del formato originale.

{{% /alert %}}

## **Unire Cells in un foglio di lavoro.**

### **Utilizzo di Microsoft Excel**

I seguenti passaggi descrivono come unire le celle nel foglio di lavoro utilizzando Microsoft Excel.

1. Copia i dati desiderati nella cella in alto a sinistra all'interno dell'intervallo.
1. Seleziona le celle che desideri unire.
1.  Per unire le celle in una riga o colonna e centrare il contenuto della cella, fare clic su**Unisci e centra** icona sul**Formattazione** barra degli strumenti.

### **Utilizzando Aspose.Cells**

 Il[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) class ha alcuni metodi utili per l'attività. Ad esempio, il metodo[**unire()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) unisce le celle in una singola cella all'interno di un intervallo di celle specificato.

Il seguente output viene generato dopo l'esecuzione del codice seguente.

**Le celle (C6:E7) sono state unite** 

![cose da fare:immagine_alt_testo](merging-and-unmerging-cells_2.png)

#### **Esempio di codice**

L'esempio seguente mostra come unire le celle (C6:E7) in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Unmerging (Splitting) Unificato Cells**

### **Utilizzo di Microsoft Excel**

I seguenti passaggi descrivono come dividere le celle unite utilizzando Microsoft Excel.

1.  Seleziona la cella unita.
 Quando le celle sono state combinate,**Unisci e centra** è selezionato sul**Formattazione** barra degli strumenti.
1.  Clic**Unisci e centra** sul**Formattazione** barra degli strumenti.

#### **Utilizzando Aspose.Cells**

 Il[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) class ha un metodo chiamato[**separare()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) che divide le cellule nel loro stato originale. Il metodo separa le celle utilizzando il riferimento della cella nell'intervallo di celle unite.

#### **Esempio di codice**

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio usa il file creato nell'esempio precedente e divide le celle unite.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **articoli Correlati**

- [Trovare e dividere le celle unite](/cells/it/java/detect-merged-cells-in-a-worksheet/).
- [Unire e dividere un intervallo di celle utilizzando i metodi Range.merge() e Range.unMerge()](/cells/it/java/merge-or-unmerge-range-of-cells/).

