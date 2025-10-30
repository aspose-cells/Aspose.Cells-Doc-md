---
title: Come creare un grafico a tornado con Golang tramite C++
linktitle: Crea Grafico a Tornado
type: docs
weight: 73
url: /it/go-cpp/create-tornado-chart/
description: Impara come creare un grafico a tornado con API Aspose.Cells for C++.
keywords: C++ crea un grafico a tornado, aggiungi un grafico a tornado, inserisci un grafico a tornado
---

## **Introduzione**
Un grafico a tornado, noto anche come diagramma a tornado o grafico a tornado, è un tipo di visualizzazione dei dati che viene spesso utilizzato per l'analisi di sensibilità in Excel. Ti aiuta a capire l'impatto delle variabili in cambiamento su un particolare risultato o esito.

## **Come creare un grafico a tornado in Excel**
Puoi creare un grafico a tornado in Excel seguendo questi passaggi:
1. Seleziona i dati e vai su Inserisci --> Grafici --> Inserisci grafico a colonne o a barre --> Grafico a barre sovrapposte. Clicca su di esso.
<br>
<img src="1.png" width=70% />
2. Cambia l'asse Y: Fai clic con il pulsante destro sull'asse y. Fai clic su formatta asse. Nelle etichette, fai clic sul menu a discesa della posizione dell'etichetta e seleziona l'elemento Basso.
<br>
<img src="2.png" width=70% />
3. Seleziona una qualsiasi barra e vai al formato. Imposta una larghezza di intervallo appropriata.
<br>
<img src="3.png" width=70% />
4. Rimuoviamo il segno meno (-) dal grafico a tornado. Seleziona l'asse x. Vai al formato. Nelle opzioni asse, fai clic sul numero. Nella categoria, seleziona personalizzato. Nel codice di formato scrivi ###0,###0. Clicca su aggiungi.
<br>
<img src="4.png" width=70% />
5. Clicca sull'asse y e vai alle opzioni dell'asse. Nelle opzioni dell'asse, seleziona le **Categorie in ordine inverso**.
<br>
<img src="5.png" width=70% />

## **Come aggiungere un grafico a tornado in Aspose.Cells**
Si prega di consultare il seguente codice di esempio. Carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati di esempio. Successivamente, crea il grafico a barre sovrapposte basato sui dati iniziali e imposta le proprietà rilevanti. Infine, salva il lavoro in formato XLSX di output. La seguente schermata mostra il grafico a tornado creato da Aspose.Cells nel file Excel di output.
<br>
<img src="6.png" width=70% />

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToCreateTornadoChart.go" >}}
