---
title: Unione e separazione di celle
type: docs
weight: 140
url: /it/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

Non sempre si desidera lo stesso numero di celle in ogni riga o colonna. Ad esempio, si potrebbe voler inserire un titolo in una cella che si estende su più colonne. O se si sta creando una fattura, si potrebbero volere meno colonne per il totale. Per fare una cella da due o più celle, uniscile. Microsoft Excel consente agli utenti di selezionare le celle e unirle per strutturare il foglio elettronico come desiderano.

**Il risultato di unire e poi dividere un intervallo di celle formattate come le celle a sinistra in Microsoft Excel** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells supporta questa funzione e può anche unire celle in un foglio di lavoro. È possibile anche dividere le celle unite. Il riferimento della cella unita è il riferimento della cella in alto a sinistra nell'intervallo originariamente selezionato.

Si noti che quando le celle vengono unite, viene conservato solo il dato nella cella in alto a sinistra. Se ci sono dati nelle altre celle nell'intervallo, quei dati vengono eliminati.

Anche la formattazione si basa sulla cella di riferimento in modo che quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengono applicate sulla cella unita. Quando la cella viene divisa, le nuove celle mantengono le loro impostazioni di formato originali.

{{% /alert %}}

## **Unione di celle in un foglio di lavoro.**

### **Utilizzando Microsoft Excel**

I seguenti passaggi descrivono come unire le celle nel foglio di lavoro utilizzando Microsoft Excel.

1. Copiare i dati che si desidera nella cella in alto a sinistra nell'intervallo.
1. Selezionare le celle che si desidera unire.
1. Per unire le celle in una riga o colonna e centrare i contenuti della cella, fare clic sull'icona **Unisci e centrato** sulla barra degli strumenti **Formattazione**.

### **Usare Aspose.Cells**

La classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) dispone di alcuni metodi utili per il compito. Ad esempio, il metodo [**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-) unisce le celle in una singola cella all'interno di un intervallo specificato di celle.

L'output seguente è generato dopo aver eseguito il codice sottostante.

**Le celle (C6:E7) sono state unite** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **Esempio di codice**

Nell'esempio seguente viene mostrato come unire le celle (C6:E7) in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Dividere (Separare) celle unite**

### **Utilizzando Microsoft Excel**

I seguenti passaggi descrivono come dividere le celle unite usando Microsoft Excel.

1. Seleziona la cella unita. 
   Quando le celle sono state unite, **Unisci e centra** è selezionato sulla barra degli strumenti **Formattazione**.
1. Fai clic su **Unisci e centra** sulla barra degli strumenti **Formattazione**.

#### **Usare Aspose.Cells**

La classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) ha un metodo chiamato [**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge-int-int-int-int-) che divide le celle nel loro stato originale. Il metodo divide le celle utilizzando il riferimento della cella nell'intervallo della cella unita.

#### **Esempio di codice**

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio utilizza il file creato nel precedente esempio e divide le celle unite.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Articoli Correlati**

- [Trova e divide le celle unite](/cells/it/java/detect-merged-cells-in-a-worksheet/).
- [Unisci e divide un intervallo di celle utilizzando i metodi Range.merge() e Range.unMerge()](/cells/it/java/merge-or-unmerge-range-of-cells/).

{{< app/cells/assistant language="java" >}}
