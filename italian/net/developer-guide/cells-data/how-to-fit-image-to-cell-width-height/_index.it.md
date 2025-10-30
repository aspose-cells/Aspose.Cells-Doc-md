---
title: Come adattare l immagine alla larghezza e all altezza della cella
type: docs
weight: 130
url: /it/net/how-to-fit-image-to-cell-width-height/
description: Impara come adattare l immagine alla larghezza della cella con Aspose.Cells.
keywords: Come adattare l immagine alla larghezza della cella, Come adattare l immagine alla larghezza della cella, Come adattare l immagine alla larghezza e all altezza della cella, Come adattare l immagine all altezza della cella.
---


## **Perché adattare l'immagine alla larghezza e all'altezza della cella**
Adattare un'immagine alla larghezza e all'altezza specifica di una cella non riguarda solo l'estetica. È fondamentalmente una questione di precisione, automazione e organizzazione dei dati.

1. Per presentazione professionale e leggibilità: Quando si crea una dashboard, spesso sono necessari icone, bandiere o immagini di prodotto per allinearsi perfettamente con i punti dati. Un'immagine disallineata sembra approssimativa e poco professionale.Se si progetta un modello per altri da utilizzare (ad esempio, un catalogo prodotti, una directory dei dipendenti), si desidera che le immagini si adattino automaticamente agli spazi designati, garantendo coerenza ogni volta che si utilizza il modello. Le immagini che traboccano le celle possono causare interruzioni di pagina inaspettate e problemi di formattazione durante la stampa. Un'immagine adattata si comporta in modo prevedibile sulla pagina stampata.

2. Per organizzazione e struttura dei dati: Questo è il motivo funzionale più cruciale. Excel è una griglia per dati. Quando un'immagine viene "posizionata" sulla griglia invece di "adattarsi" a una cella, crea problemi. Problemi con le immagini libere: non si Muovono con le Celle: Se si ordina, filtra o si inseriscono/eliminano righe, l'immagine rimane nella sua posizione assoluta sul foglio, disconnettendosi totalmente dai dati che dovrebbe rappresentare. Non si Ridimensionano con le Celle: Se si modifica l'altezza della riga o la larghezza della colonna, un'immagine flottante rimane della stessa dimensione, rompendo il layout. Vantaggio di adattare a una cella: La cella diventa il "contenitore" dell'immagine: Quando un'immagine viene adattata a una cella, la sua posizione e dimensione sono definite dalle coordinate della griglia della cella. Se si sposta i dati (ad esempio, si ordina una tabella), l'immagine si sposta con la riga corrispondente. Crea una vera coppia immagine-dato: Questo consente di trattare l'immagine come attributo visivo dei dati in quella riga, fondamentale per l'automazione.

3. Per automazione e funzionalità avanzate: È qui che l'adattamento delle immagini alle celle diventa un superpotere. Collegare le immagini dinamicamente: È possibile usare una formula per prelevare il percorso di un'immagine da una cella e poi usare una macro (VBA) per dimensionare automaticamente e inserire l'immagine in una cella adiacente. Questa è la modalità per creare un catalogo prodotti dinamico, dove modificando un ID prodotto si aggiornano automaticamente nome, prezzo e immagine.Integrazione con database: Quando si esportano dati o si collega Excel a un database, avere immagini contenute all'interno di celle specifiche rende l'intero set di dati, inclusi i visuali, più strutturato e portatile.

## **Come adattare l'immagine alla larghezza e altezza della cella in Excel**
Puoi adattare l'immagine alla larghezza e altezza della cella in Excel utilizzando due metodi.

### **Adatta immagine alla larghezza e altezza della cella usando "Posiziona nella cella"**
Su come inserire un'immagine in una cella in Excel, segui questi passaggi:

1. Vai alla scheda Inserisci e fai clic sull'opzione Immagini.
2. Seleziona **Posiziona in cella**. Seleziona una delle seguenti fonti dal menu a discesa Inserisci immagine da (**Questo dispositivo**, **Immagini stock** e **Immagini online**). Questo dispositivo per inserire immagini dal tuo dispositivo. Immagini stock per inserire immagini da immagini di archivio. Immagini online per inserire immagini dal web.
<br>
<img src="1.png" width=60% />
3. Seleziona l'immagine e inseriscila in una cella.
<br>
<img src="8.png" width=60% />

### **Adatta immagine alla larghezza e altezza della cella usando "Posiziona sopra le celle"**
Per inserire un'immagine sopra le celle in Excel, seguire questi passaggi:

1. Vai alla scheda Inserisci e fai clic sull'opzione Immagini.
2. Seleziona **Posiziona sopra le celle**. Scegli una delle seguenti fonti dal menu a discesa Inserisci immagine da (**Questo dispositivo**, **Immagini in stock** e **Immagini online**). Questo dispositivo per inserire un'immagine dal tuo dispositivo. Immagini in stock per inserire un'immagine dalle immagini in stock. Immagini online per inserire un'immagine dal web.
<br>
<img src="2.png" width=60% />
3. Seleziona l'immagine e inseriscila sopra le celle.
<br>
<img src="3.png" width=60% />
4. Regolare manualmente la larghezza e altezza dell'immagine per adattarla alle dimensioni delle celle.
<br>
<img src="6.png" width=60% />

## **Come adattare l'immagine alla larghezza e altezza della cella usando Aspose.Cells**
A causa delle variazioni nella larghezza e altezza di righe e colonne a seconda della lingua e del rapporto di visualizzazione, regolare le dimensioni di un'immagine può portare a lievi differenze, e talvolta potrebbe non essere completamente coerente con larghezza e altezza delle celle. Puoi adattare l'immagine alla larghezza e altezza della cella in Aspose.Cells utilizzando i seguenti due metodi.

### **Come adattare l'immagine alla larghezza e altezza della cella usando "Posiziona nella cella"**
Inserire un'immagine nella cella utilizzando Aspose.Cells. Si prega di vedere il seguente codice di esempio. Dopo aver eseguito il codice di esempio, verrà inserita un'immagine in una cella.
1. Istanziare un oggetto Workbook. 
2. Ottenere la cella in cui si desidera inserire l'immagine.
3. Impostare la proprietà Cell.EmbeddedImage. 
4. Infine, salvare il libro di lavoro nel formato [output XLSX](out.xlsx). 

### **Codice di esempio per "Posiziona nella cella"**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-in-cell.cs" >}}
{{< app/cells/assistant language="csharp" >}}

### **Come adattare l'immagine alla larghezza e altezza della cella usando "Posiziona sopra le celle"**
Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:
Basta chiamare il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) della collezione [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (racchiuso nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Quindi regolare la larghezza e l'altezza dell'immagine in base alle dimensioni delle celle. Infine, salvare il file in formato [output XLSX](out_net.xlsx). Il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) richiede i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome del file immagine**, il nome del file immagine, completo di percorso.


### **Codice di esempio per "Posiziona sopra le celle"**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-over-cells-fit-cell-width-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
