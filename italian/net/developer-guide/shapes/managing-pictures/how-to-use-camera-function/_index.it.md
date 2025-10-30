---
title: Come Aggiungere una Fotocamera per Range
type: docs
weight: 10
url: /it/net/how-to-add-camera-for-range/
description: Questo articolo introdurrà come aggiungere una fotocamera per il contenuto del range API Aspose.Cells for .NET.
keywords: Come Usare la Funzione Fotocamera, Come aggiungere una Fotocamera per il contenuto del range, Come usare lo strumento Fotocamera, Funzione Fotocamera in Excel, Come usare la funzione Fotocamera in Aspose.Cells for .NET
---

## **Possibili Scenari di Utilizzo**
Lo strumento Fotocamera in Excel è una funzionalità nascosta ma potente che permette di creare uno snapshot dal vivo e collegato di qualsiasi intervallo di celle. Ecco perché e quando potresti usarlo.

Cosa fa lo Strumento Fotocamera:
1. Cattura una "immagine" di un intervallo di celle selezionato.
2. L"immagine" è un collegamento live — se le celle di origine cambiano, l'immagine si aggiorna automaticamente.
3. Puoi spostare o ridimensionare l’immagine ovunque nel foglio o anche in un altro foglio.


## **Come Usare la Funzione Fotocamera in Excel**
Ecco una guida passo-passo per usare lo Strumento Fotocamera in Excel — un modo potente per creare immagini live e dinamiche di intervalli di celle.

### Abilitare lo Strumento Fotocamera

Lo strumento Fotocamera è nascosto di default. Ecco come aggiungerlo:

1. Clicca sulla freccia rivolta verso il basso sulla Barra di accesso rapido (angolo superiore-sinistro di Excel).
2. Seleziona Altri comandi....
3. Nella finestra di dialogo: Dal menu a tendina "Scegli comandi da", seleziona Comandi non presenti nella barra multifunzione. Scorri verso il basso e seleziona Fotocamera. Clicca su Aggiungi >> per aggiungerlo alla barra degli strumenti.
4. Clicca su OK. Ora vedrai una piccola icona di fotocamera nella barra degli strumenti.

### Usare lo Strumento Fotocamera
1. Seleziona l’intervallo di celle che vuoi catturare (ad esempio A1:C5).
2. Clicca sull’icona Fotocamera sulla Barra di accesso rapido.
3. Il cursore cambierà in una croce.
4. Clicca in qualsiasi punto del foglio di lavoro dove desideri posizionare l'immagine. Viene inserita un'immagine dal vivo dell'intervallo selezionato.

### Collegamento Dinamico
L'immagine è collegata alle celle originali. Se i valori o la formattazione nell'intervallo di origine cambiano, l'immagine si aggiorna automaticamente.


## **Come Aggiungere la Telecamera per Intervallo in Aspose.Cells for .NET**
Aspose.Cells supporta la visualizzazione del contenuto di una cella o intervallo in una forma immagine. Puoi collegare l'immagine alla cella o intervallo che contiene i dati che vuoi visualizzare. Poiché la cella o l'intervallo sono collegati all'oggetto grafico, le modifiche ai dati si riflettono automaticamente sull'oggetto grafico. 

Ecco un esempio di base di come usare la funzione Telecamera usando [file di esempio](camera.xlsx) in Aspose.Cells for .NET:

1. Carica il file di esempio utilizzando la classe [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook).
1. Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) della collezione [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). 
1. Specifica l'intervallo di celle utilizzando l'attributo [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) dell'oggetto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).
1. Aggiorna il valore della forma selezionata nel foglio.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **Risultato dell'Output**
Lo screenshot seguente mostra la telecamera dell'intervallo(A1:E12) creata da Aspose.Cells for .NET nel file Excel di output.
<br>
Prima di aggiungere i dati:
<br>
<img src="1.png" width=70% />
<br>
Dopo aver aggiunto i dati:
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
