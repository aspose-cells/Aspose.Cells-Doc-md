---
title: Come creare un diagramma di Gantt
linktitle: Come creare un diagramma di Gantt
type: docs
weight: 72
url: /it/net/how-to-create-gantt-chart/
description: Come creare un diagramma di Gantt in Aspose.Cells.
keywords: create/insert Gantt Chart Excel Aspose
---
##  Cos'è il diagramma di Gantt

Un diagramma di Gantt ti aiuta a pianificare le attività del tuo progetto e quindi a monitorare i tuoi progressi.

##  Aggiungi il diagramma di Gantt in Excel

Hai bisogno di mostrare lo stato di una semplice pianificazione del progetto con un diagramma di Gantt? Sebbene Excel non disponga di un tipo di diagramma di Gantt predefinito, puoi simularne uno personalizzando un grafico a barre in pila per mostrare le date di inizio e fine delle attività, in questo modo:

![cose da fare:immagine_alt_testo](00.png)

![cose da fare:immagine_alt_testo](0.png)

##  Come creare

-  Seleziona i dati che desideri rappresentare nel grafico. Nel nostro esempio, è B1:B7, quindi Inserisci**Barra impilata** grafico.

![cose da fare:immagine_alt_testo](1.png)

- Seleziona il grafico,**Seleziona dati**->**Aggiungi**, imposta il **nome della serie** E**Valori di serie** come segue

![cose da fare:immagine_alt_testo](2.png)

-  Seleziona il grafico, Modifica il**Etichette dell'asse orizzontale (categoria).**

![cose da fare:immagine_alt_testo](3.png)

- **Formato Asse** l'asse Y, seleziona**Categorie in ordine inverso**
-  Seleziona il**Serie Blu** e impostare il**Riempi->NO Riempi**
- **Formato Asse** l'asse X, imposta il *minimo e il massimo**(5/1/2019:43470,30/1/2019:43494)

![cose da fare:immagine_alt_testo](4.png)

- **Aggiungi file dati** per il grafico
Ora ottieni un diagramma di Gantt.

## Aggiungi il diagramma di Gantt in Aspose.Cells

 Il codice di esempio seguente crea un diagramma di Gantt aprendo a[file di esempio](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

 Otterrai un file simile a[file dei risultati](result.xlsx).Nel file vedrai quanto segue:

![cose da fare:immagine_alt_testo](5.png)

