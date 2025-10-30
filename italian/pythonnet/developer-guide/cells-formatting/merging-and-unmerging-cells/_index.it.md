---
title: Unione e separazione di celle
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo, che supporta l’unione e la divisione di celle. Questo articolo presenterà come unire e dividere celle usando Aspose.Cells for Python via .NET e come personalizzare lo stile della cella unita.
keywords: Aspose.Cells per Python via .NET, libreria NET, foglio di calcolo, unisci celle, dividi celle, impostazioni stile, stili personalizzati
type: docs
weight: 190
url: /it/python-net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells per Python via .NET supporta questa funzionalità e può anche unire le celle in un foglio di lavoro. Puoi anche desunire o dividere le celle unite. Il riferimento di cella di una cella unita è il riferimento alla cella in alto a sinistra nell'intervallo originale.

{{% /alert %}} 
## **Introduzione**
Non si desidera sempre lo stesso numero di celle in ogni riga o colonna. Ad esempio, si potrebbe voler inserire un titolo in una cella che si estende su diverse colonne. Oppure, se si crea una fattura, potrebbe essere necessario meno colonne per il totale. Per rendere una cella da due o più celle, unirle. Microsoft Excel consente agli utenti di selezionare i file e unirli per strutturare il foglio di calcolo nel modo desiderato.

{{% alert color="primary" %}} 

Si noti che quando le celle vengono unite, viene conservato solo il dato nelle celle in alto a sinistra. Se ci sono dati nelle altre celle nell'intervallo, questi dati vengono eliminati.
Anche la formattazione si basa sulla cella di riferimento in modo che quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengano applicate sulla cella unita. Quando la cella viene divisa, le nuove celle mantengono le proprie impostazioni di formato originali.

{{% /alert %}} 
## **Unione di celle in un foglio di lavoro**
### **Unione di celle in Microsoft Excel**
I seguenti passaggi descrivono come unire celle nel foglio di lavoro utilizzando MS Excel.

1. Copiare i dati che si desidera nella cella in alto a sinistra nell'intervallo.
1. Selezionare le celle che si desidera unire.
1. Per unire le celle in una riga o colonna e centrare i contenuti della cella, fare clic sull'icona **Unisci e centrato** sulla barra degli strumenti **Formattazione**.

### **Unione di celle con Aspose.Cells per Python via .NET**
La classe Aspose.Cells.Cells dispone di alcuni metodi utili per il compito. Ad esempio, il metodo Merge() unisce le celle in una singola cella all'interno di un intervallo specificato.

Nell'esempio seguente viene mostrato come unire le celle (C6:E7) in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-MergingCellsInWorksheet.-1.py" >}}

## **Dividere (Separare) celle unite**
### **Utilizzando Microsoft Excel**
I seguenti passaggi descrivono come dividere le celle unite usando Microsoft Excel.

1. Seleziona la cella unita. Quando le celle sono state unite, su **Formato** è selezionata l’opzione **Unisci e centra**.
1. Fai clic su **Unisci e centra** sulla barra degli strumenti **Formattazione**.

### **Usando Aspose.Cells per Python via .NET**
La classe Aspose.Cells.Cells ha un metodo chiamato UnMerge() che divide le celle nel loro stato originale. Il metodo divide le celle utilizzando il riferimento delle celle nell'intervallo di celle unite.

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio utilizza il file creato nel precedente esempio e divide le celle unite.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UnMergingtheMergedCells-1.py" >}}


## **Argomenti avanzati**
- [Rileva le celle unite in un foglio di lavoro](/cells/it/python-net/detect-merged-cells-in-a-worksheet/)

{{< app/cells/assistant language="python-net" >}}
