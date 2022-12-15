---
title: Fusione e Separazione Cells
type: docs
weight: 190
url: /it/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells supporta questa funzione e può anche unire celle in un foglio di lavoro. Puoi separare o dividere anche le celle unite. Il riferimento di cella di una cella unita è il riferimento per la cella in alto a sinistra nell'intervallo selezionato originale.

{{% /alert %}} 
## **introduzione**
Non vuoi sempre lo stesso numero di celle in ogni riga o colonna. Ad esempio, potresti voler inserire un titolo in una cella che si estende su più colonne. Oppure, se crei una fattura, potresti volere meno colonne per il totale. Per creare una cella da due o più celle, uniscile. Microsoft Excel consente agli utenti di selezionare i file e unirli per strutturare il foglio di calcolo nel modo desiderato.

{{% alert color="primary" %}} 

Si noti che quando le celle vengono unite, vengono conservati solo i dati nelle celle in alto a sinistra. Se sono presenti dati nelle altre celle dell'intervallo, questi dati vengono eliminati.
La formattazione, allo stesso modo, si basa sulla cella di riferimento in modo che quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengono applicate alla cella unita. Quando la cella viene divisa, le nuove celle mantengono le impostazioni del formato originale.

{{% /alert %}} 
## **Unire Cells in un foglio di lavoro**
### **Unire Cells in Microsoft Excel**
I seguenti passaggi descrivono come unire le celle nel foglio di lavoro utilizzando MS Excel.

1. Copia i dati desiderati nella cella in alto a sinistra all'interno dell'intervallo.
1. Seleziona le celle che desideri unire.
1.  Per unire le celle in una riga o colonna e centrare il contenuto della cella, fare clic su**Unisci e centra** icona sul**Formattazione** barra degli strumenti.
### **Unire Cells con Aspose.Cells**
La classe Aspose.Cells.Cells ha alcuni metodi utili per il compito. Ad esempio, il metodo Merge() unisce le celle in una singola cella all'interno di un intervallo specificato.

L'esempio seguente mostra come unire le celle (C6:E7) in un foglio di lavoro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Unmerging (Splitting) Unificato Cells**
### **Utilizzo di Microsoft Excel**
I seguenti passaggi descrivono come dividere le celle unite utilizzando Microsoft Excel.

1. Seleziona la cella unita.
 Quando le celle sono state combinate,**Unisci e centra** è selezionato sul**Formattazione** barra degli strumenti.
1.  Clic**Unisci e centra** sul**Formattazione** barra degli strumenti.
### **Utilizzando Aspose.Cells**
La classe Aspose.Cells.Cells ha un metodo chiamato UnMerge() che suddivide le celle nel loro stato originale. Il metodo separa le celle utilizzando il riferimento della cella nell'intervallo di celle unite.

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio usa il file creato nell'esempio precedente e divide le celle unite.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Argomenti avanzati**
- [Rileva Cells unito in un foglio di lavoro](/cells/it/net/detect-merged-cells-in-a-worksheet/)
