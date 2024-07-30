---
title: Come creare un diagramma di Gantt
linktitle: Come creare un diagramma di Gantt
type: docs
weight: 72
url: /it/net/how-to-create-gantt-chart/
description: Scopri come creare un diagramma di Gantt con l API Aspose.Cells for .NET.
keywords: C# crea un diagramma di Gantt, aggiungi un diagramma di Gantt, inserisci un diagramma di Gantt
---

## **Cos'è un diagramma di Gantt**

Un diagramma di Gantt è un tipo di diagramma a barre che illustra una pianificazione del progetto. Mostra le date di inizio e fine dei vari elementi di un progetto. Ogni attività è rappresentata da una barra, con la sua lunghezza che corrisponde alla sua durata. I diagrammi di Gantt indicano anche le dipendenze tra le attività, consentendo ai project manager di visualizzare la sequenza in cui le attività devono essere completate. Sono ampiamente utilizzati nella gestione dei progetti per pianificare, programmare e monitorare i progetti in modo efficace.

## **Come creare un diagramma di Gantt in Excel**

Puoi creare un diagramma di Gantt in Excel seguendo questi passaggi:
1. Aggiungi dei dati per il diagramma di Gantt. 
<br>
<img src="00.png" width=50% />
1. Seleziona i dati e vai su Inserisci --> Grafici --> Inserisci grafico a colonne o a barre --> Grafico a barre in pila. Nel nostro esempio, sarebbe B1:B7, quindi inserisci il grafico a barre in pila.
<br>
<img src="1.png" width=50% />

1. Seleziona il grafico, ***Seleziona dati*** -> ***Aggiungi***, imposta il ***Nome serie*** e i ***Valori serie*** come segue.
<br>
<img src="2.png" width=50% />

1. Seleziona il grafico, modifica le **Etichette dell'asse orizzontale (Categoria)**.
<br>
<img src="3.png" width=50% />

1. Formatta l'asse Y, seleziona **Categorie in ordine inverso**.
1. Seleziona la **Serie blu** e imposta il **Riempimento->Nessun riempimento**.
1. Formatta l'asse X, imposta il **Minimo e Massimo**(1/5/2019:43470,1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Aggiungi etichette dati** per il grafico, ora otterrai un diagramma di Gantt.
<br>
<img src="0.png" width=50% />


## **Come aggiungere un diagramma di Gantt in Aspose.Cells**
Si prega di vedere il codice campione seguente. Carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati di esempio. Quindi crea il grafico a barre in pila basato sui dati iniziali e imposta le proprietà rilevanti. Infine, salva il workbook in [formato XLSX di output](result.xlsx). La schermata seguente mostra il diagramma di Gantt creato da Aspose.Cells nel file Excel di output.
<br>
<img src="5.png" width=60% />

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

