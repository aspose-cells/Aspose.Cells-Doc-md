---
title: Come creare un grafico di Gantt
linktitle: Come creare un grafico di Gantt
type: docs
weight: 72
url: /it/net/how-to-create-gantt-chart/
description: Come creare un grafico di Gantt in Aspose.Cells.
keywords: creare/inserire un grafico di Gantt Excel Aspose
---
## Che cos'è un grafico di Gantt

Un grafico di Gantt ti aiuta a pianificare le attività del tuo progetto e poi ti aiuta a monitorare il tuo progresso.

## Aggiungere un diagramma di Gantt in Excel

Hai bisogno di mostrare lo stato per un semplice programma di progetto con un diagramma di Gantt? Anche se Excel non ha un tipo di diagramma di Gantt predefinito, è possibile simulare uno personalizzando un grafico a barre in pila per mostrare le date di inizio e fine dei compiti, come mostrato qui:

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## Come creare

- Seleziona i dati che vuoi rappresentare graficamente. Nel nostro esempio, cioè B1:B7, e poi inserisci **Grafico a barre in pila**.

![todo:image_alt_text](1.png)

- Seleziona il grafico, **Seleziona dati** -> **Aggiungi**, imposta il **Nome della serie** e i **Valori della serie** come segue

![todo:image_alt_text](2.png)

- Seleziona il grafico, Modifica le **Etichette asse orizzontale (categoria)**

![todo:image_alt_text](3.png)

- **Formatta l'asse** Y, seleziona **Categorie in ordine inverso**
- Seleziona la **Serie blu** e imposta il **Riempimento → Nessun riempimento**
- **Formatta l'asse** X, imposta il **Minimo e Massimo**(1/5/2019:43470,1/30/2019:43494)

![todo:image_alt_text](4.png)

- **Aggiungi etichette dati** per il grafico
Ora hai ottenuto un diagramma di Gantt.

## Aggiungere un diagramma di Gantt in Aspose.Cells

Il seguente codice di esempio crea un diagramma di Gantt aprendo un [file di esempio](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

Otterrai un file simile a [file di risultato](result.xlsx). Nel file, vedrai quanto segue:

![todo:image_alt_text](5.png)

