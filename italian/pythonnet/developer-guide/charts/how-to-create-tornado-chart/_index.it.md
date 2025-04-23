---
title: Come creare un grafico a tornado
type: docs
weight: 73
url: /it/python-net/create-tornado-chart/
description: Impara come creare un grafico tornado con l API di Aspose.Cells per Python via .NET.
keywords: Creare un grafico tornado con Python, aggiungere un grafico tornado, inserire un grafico tornado
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
5. fai clic sull'asse y e vai alle opzioni asse. Nelle opzioni asse, seleziona Categorie in ordine inverso.
<br>
<img src="5.png" width=70% />

## **Come aggiungere un grafico tornado in Aspose.Cells per Python Excel Library**
Vedi il seguente esempio di codice. Carica il [file Excel di esempio](sample.xlsx) contenente alcuni dati di esempio. Poi crea il grafico a barre impilate in base ai dati iniziali e imposta le proprietà rilevanti. Infine, salva il workbook in [formato XLSX di output](out.xlsx). La schermata seguente mostra il grafico tornado creato da Aspose.Cells per Python via .NET nel file Excel di output.
<br>
<img src="6.png" width=70% />

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-tornado-chart.py" >}}
