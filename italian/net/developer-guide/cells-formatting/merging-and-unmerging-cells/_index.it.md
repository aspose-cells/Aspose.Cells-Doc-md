---
title: Unire e separare Cells
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo, che supporta l'unione e la separazione delle celle. Questo articolo introdurrà come unire e separare le celle utilizzando la libreria Aspose.Cells e come personalizzare lo stile delle celle unite.
keywords: Aspose.Cells, NET library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /it/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells supporta questa funzionalità e può anche unire le celle in un foglio di lavoro. Puoi anche dividere o dividere le celle unite. Il riferimento di cella di una cella unita è il riferimento per la cella in alto a sinistra nell'intervallo selezionato originale.

{{% /alert %}} 
##  **introduzione**
Non vuoi sempre lo stesso numero di celle in ogni riga o colonna. Ad esempio, potresti voler inserire un titolo in una cella che si estende su più colonne. Oppure, se crei una fattura, potresti volere meno colonne per il totale. Per creare una cella da due o più celle, uniscile. Microsoft Excel consente agli utenti di selezionare file e unirli per strutturare il foglio di calcolo nel modo desiderato.

{{% alert color="primary" %}} 

Tieni presente che quando le celle vengono unite, vengono conservati solo i dati nelle celle in alto a sinistra. Se sono presenti dati nelle altre celle dell'intervallo, questi dati vengono eliminati.
Allo stesso modo, la formattazione è basata sulla cella di riferimento in modo che quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengono applicate alla cella unita. Quando la cella viene divisa, le nuove celle mantengono le impostazioni di formato originali.

{{% /alert %}} 
##  **Unire Cells in un foglio di lavoro**
###  **Unione di Cells in Microsoft Excel**
I seguenti passaggi descrivono come unire le celle nel foglio di lavoro utilizzando MS Excel.

1. Copia i dati desiderati nella cella più in alto a sinistra all'interno dell'intervallo.
1. Seleziona le celle che desideri unire.
1.  Per unire le celle in una riga o colonna e centrare il contenuto della cella, fare clic su**Unisci e centra** icona sul**Formattazione** barra degli strumenti.
###  **Unendo Cells con Aspose.Cells**
La classe Aspose.Cells.Cells dispone di alcuni metodi utili per l'attività. Ad esempio, il metodo Merge() unisce le celle in un'unica cella all'interno di un intervallo specificato.

L'esempio seguente mostra come unire le celle (C6:E7) in un foglio di lavoro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
##  **Separazione (divisione) Unito Cells**
###  **Utilizzando Microsoft Excel**
I passaggi seguenti descrivono come dividere le celle unite utilizzando Microsoft Excel.

1. Seleziona la cella unita.
 Quando le celle sono state combinate,**Unisci e centra** è selezionato su**Formattazione** barra degli strumenti.
1.  Clic**Unisci e centra** sul**Formattazione** barra degli strumenti.
###  **Utilizzando Aspose.Cells**
La classe Aspose.Cells.Cells ha un metodo chiamato UnMerge() che divide le celle nel loro stato originale. Il metodo separa le celle utilizzando il riferimento della cella nell'intervallo di celle unito.

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio utilizza il file creato nell'esempio precedente e divide le celle unite.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


##  **Argomenti avanzati**
- [Rileva unito Cells in un foglio di lavoro](/cells/it/net/detect-merged-cells-in-a-worksheet/)
