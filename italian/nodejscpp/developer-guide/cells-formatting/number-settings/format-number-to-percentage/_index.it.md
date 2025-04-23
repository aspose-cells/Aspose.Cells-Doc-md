---
title: Come formattare un numero come percentuale
type: docs
weight: 10
url: /it/nodejs-cpp/how-to-format-number-to-percentage/
description: Questo articolo introdurrà come formattare il numero in percentuale usando l API Aspose.Cells for Node.js via C++.
keywords: Convertire un numero in formato percentuale, Trasformare valori numerici in percentuali, Cambiare i numeri per essere visualizzati come percentuali, Formattare numeri come percentuali, Regolare i valori numerici alla rappresentazione percentuale, Format Number to Percentage
---

## **Possibili Scenari di Utilizzo**
Formatta i numeri come percentuali in Excel è una pratica comune per vari motivi, ognuno dei quali migliora la chiarezza, l'accuratezza e l'interpretabilità dei dati. Ecco alcune delle principali ragioni per cui potresti formattare i numeri come percentuali in Excel:

1. **Chiarezza e leggibilità**: Le percentuali sono un formato universalmente compreso che può rendere i dati più facili da leggere e interpretare. Convertendo una frazione o un decimale in percentuale, si rende immediatamente chiaro che si sta parlando di una parte di un tutto, il che può essere più intuitivo per molti utenti.

2. **Coerenza**: Nei report o analisi dei dati che implicano confronti, la formattazione dei numeri in percentuale garantisce coerenza. Ciò è particolarmente importante quando si confrontano rapporti o proporzioni tra diversi set di dati. La coerenza nella presentazione dei dati aiuta a fare confronti e conclusioni più accurati.

3. **Semplificazione**: Le percentuali semplificano informazioni complesse. Ad esempio, dire "50%" è più diretto e più facile da capire per la maggior parte delle persone rispetto a "0,5" o "1/2". Questa semplificazione è fondamentale quando si comunica un dato a un pubblico che potrebbe non avere una formazione tecnica.

4. **Visualizzazione**: Quando si creano grafici o diagrammi, le percentuali possono rendere la visualizzazione dei dati più efficace. Ad esempio, i grafici a torta rappresentano intrinsecamente parti di un tutto e sono più intuitivi quando i dati sono formattati come percentuali.

5. **Analisi e decisioni**: Nel mondo degli affari e della finanza, le percentuali sono spesso utilizzate per rappresentare la crescita, i margini di profitto e altri indicatori chiave di prestazione (KPI). La formattazione di questi numeri come percentuali rende più facile analizzare e prendere decisioni basate su metriche chiare e comprensibili.

6. **Risparmio di spazio**: In alcuni casi, la formattazione dei numeri come percentuali può ottimizzare lo spazio nel documento o nel foglio di calcolo, rendendolo più pulito e organizzato. Questo è particolarmente utile in tabelle o dashboard con spazio limitato.

7. **Uso educativo e didattico**: In contesti educativi, la formattazione dei numeri come percentuali può aiutare gli studenti a comprendere meglio frazioni, rapporti e proporzioni. È un'applicazione pratica dei concetti matematici.

Per formattare un numero come percentuale in Excel, basta selezionare le celle contenenti i dati, quindi scegliere l'opzione di formato "Percentuale", sia dalla scheda Home sulla barra multifunzione, sia cliccando con il tasto destro e scegliendo "Formato celle". Excel mostrerà quindi i numeri come percentuali, moltiplicando i valori decimali originali per 100 e aggiungendo il simbolo percentuale. Questa conversione automatica agevola le ragioni sopra menzionate, rendendo la gestione e la presentazione dei dati sia efficiente che efficace.

## **Come formattare un numero come percentuale in Excel**
Formattare i numeri come percentuali in Excel è un processo semplice che può essere completato in pochi passaggi. Ecco come fare:

### Utilizzo della Barra Multifunzione

1. **Seleziona le celle**: Prima, seleziona la cella o intervallo di celle che desideri formattare come percentuale.
2. **Vai alla barra multifunzione**: Guarda la barra sulla parte superiore di Excel. Troverai una scheda chiamata "Home."
3. **Tasto formato percentuale**: Nella scheda "Home", all’interno del gruppo "Numero", vedrai un pulsante con il simbolo "%". Questo è il pulsante "Formato percentuale."
4. **Applica formato percentuale**: Clicca sul pulsante "%". Excel formatterà automaticamente le celle selezionate come percentuali, moltiplicando il valore della cella per 100 e mostrando il simbolo percentuale. Ad esempio, se digiti "0,1" in una cella e applichi il formato percentuale, visualizzerà "10%."

### Utilizzo della finestra di dialogo "Formato celle"

1. **Seleziona le celle**: Evidenzia le celle che desideri formattare.
2. **Apri la finestra "Formato celle"**: Fai clic con il pulsante destro su una delle celle evidenziate e scegli "Formato celle" dal menu contestuale. In alternativa, premi `Ctrl + 1` sulla tastiera per aprire la finestra di dialogo "Formato celle."
3. **Seleziona Percentuale**: Nella finestra "Formato celle", clicca sulla scheda "Numero" se non è già selezionata. Quindi, nella lista a sinistra, clicca su "Percentuale."
4. **Regola le decimali**: Puoi impostare il numero di decimali da visualizzare. Ad esempio, se desideri mostrare due decimali, inserisci "2" nella casella "Decimali".
5. **Applica**: Clicca su "OK" per applicare il formato percentuale. Le celle selezionate mostreranno ora i valori come percentuali.

### Utilizzo di una formula

Se inserisci una formula o vuoi convertire un numero esistente in una percentuale all’interno di una formula, puoi semplicemente moltiplicare il numero per 100 e aggiungere il simbolo di percentuale al formato.

Ad esempio, se hai un valore nella cella A1 e vuoi visualizzarlo come percentuale in B1, puoi usare la seguente formula in B1:

```excel
=A1*100 & "%"
```

Tuttavia, nota che questo metodo tratta il risultato come testo piuttosto che come un valore numerico formattato come percentuale, il che potrebbe influire sui calcoli successivi.

### Scorciatoia da tastiera

Per un cambiamento rapido di formato senza usare il mouse:
- Seleziona le celle che desideri formattare.
- Premi `Ctrl + Shift + %`. Questo applicherà il formato percentuale alle celle selezionate.

Ricorda che, quando formatti un numero come percentuale, Excel moltiplica sostanzialmente il valore della cella per 100. Quindi, se inserisci dati che vuoi visualizzare come percentuale, dovresti inserirli come decimale (ad esempio, inserisci "0,1" per il 10%).

## **Come formattare il numero in percentuale in Aspose.Cells for Node.js via C++**
Formattare i numeri in percentuale in Aspose.Cells for Node.js via C++ è un processo semplice. Aspose.Cells è una libreria potente che permette di creare, manipolare e convertire file Excel in applicazioni Node.js senza aver bisogno di Microsoft Excel installato sul sistema. Ecco come puoi formattare numeri in percentuale usando Aspose.Cells for Node.js via C++:

### Passo 1: Installare Aspose.Cells for Node.js via C++

Innanzitutto, assicurati di avere Aspose.Cells for Node.js via C++ nel tuo progetto. Puoi ottenerlo dal sito Aspose.

### Passo 2: Crea un nuovo workbook o apri uno esistente

Puoi creare un nuovo workbook o aprire uno esistente. 


### Passo 3: Accedi al foglio di lavoro

Devi accedere al foglio di lavoro dove vuoi formattare i numeri come percentuali. Se stai lavorando con un nuovo libro di lavoro, probabilmente lavorerai con il primo foglio.

### Passo 4: Applica la formattazione percentuale

Per formattare una cella o un intervallo di celle per visualizzare i numeri come percentuali, sarà necessario impostare il formato numerico dello stile della cella o dell'intervallo su un formato percentuale. Per un intervallo di celle, è possibile ciclare attraverso l'intervallo e applicare lo stile a ogni cella individualmente.

### Passo 5: Salva il workbook

Infine, salva il libro di lavoro in un file o in un flusso.

### Codice di esempio

Ecco un esempio di codice che dimostra questi passaggi:
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToPercentage.js" >}}

### Conclusione

Seguendo questi passaggi, puoi facilmente formattare i numeri in percentuale in Aspose.Cells for Node.js via C++. Aspose.Cells offre una vasta gamma di funzionalità per manipolare i file Excel, inclusa la formattazione delle celle, il lavoro con formule e molto altro, rendendola uno strumento potente per gli sviluppatori Node.js che lavorano con i dati Excel.

