---
title: Come creare un grafico tornado
type: docs
weight: 73
url: /it/net/create-tornado-chart/
description: Scopri come creare un grafico tornado con Aspose.Cells for .NET API.
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
---
##  **introduzione**
Un grafico tornado, noto anche come diagramma tornado o grafico tornado, è un tipo di visualizzazione dei dati spesso utilizzato per l'analisi di sensibilità in Excel. Ti aiuta a comprendere l'impatto della modifica delle variabili su un particolare risultato o risultato.

##  **Come creare un grafico Tornado in Excel**
È possibile creare un grafico tornado in Excel seguendo questi passaggi:
1. Seleziona i dati e vai a Inserisci --> Grafici --> Inserisci grafico a colonne o a barre --> Grafico a barre in pila. Cliccaci sopra.
<br>
<img src="1.png" width=70% />
2. Modificare l'asse Y: fare clic con il pulsante destro del mouse sull'asse Y. Fare clic sull'asse del formato. Nelle etichette, fai clic sul menu a discesa della posizione dell'etichetta e seleziona Elemento basso.
<br>
<img src="2.png" width=70% />
3. Seleziona una barra qualsiasi e vai alla formattazione. Impostare una larghezza di spazio adeguata.
<br>
<img src="3.png" width=70% />
4. Rimuoviamo il segno meno (-) dal grafico del tornado. Seleziona l'asse x. Vai alla formattazione. Nelle opzioni dell'asse, fare clic sul numero. Nella categoria, seleziona personalizzato. Nel codice formato scrivere ###0,###0. Fare clic su aggiungi.
<br>
<img src="4.png" width=70% />
5. fai clic sull'asse y e vai alle opzioni dell'asse. Nelle opzioni dell'Asse, seleziona Categorie in ordine inverso.
<br>
<img src="5.png" width=70% />

##  **Come aggiungere un grafico Tornado in Aspose.Cells**
 Consultare il seguente codice di esempio. Carica il[file Excel di esempio](sample.xlsx) che contiene alcuni dati di esempio. Quindi crea il grafico a barre in pila in base ai dati iniziali e imposta le proprietà pertinenti. Infine, salva la cartella di lavoro in[formato uscita XLSX](out.xlsx). La schermata seguente mostra il grafico tornado creato da Aspose.Cells nel file Excel di output.
<br>
<img src="6.png" width=70% />

###  **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}