---
title: Come formattare un numero in tempo
type: docs
weight: 10
url: /it/nodejs-cpp/how-to-format-number-to-time/
description: Questo articolo introdurrà come formattare un numero in tempo utilizzando l API Aspose.Cells for Node.js via C++.
keywords: Convertire valori numerici in formato temporale, Trasformare cifre in rappresentazioni temporali, Modificare numeri in un formato di tempo leggibile, Formattare dati numerici in notazioni temporali, Adattare input numerici a una struttura temporale, Format Number to Time
---

## **Possibili Scenari di Utilizzo**
Formattare i numeri in tempo in Excel è una pratica comune per diversi motivi, principalmente perché permette agli utenti di rappresentare i dati in modo facile da comprendere e analizzare. Ecco alcuni dei motivi principali per cui potresti voler formattare i numeri in tempo in Excel:

1. **Rappresentazione dei dati**: La formattazione temporale aiuta a rappresentare i numeri in un formato di tempo familiare (ore, minuti, secondi), rendendo più facile l'interpretazione dei dati. Ad esempio, rappresentare "6.5" come "6:30" chiarisce che si riferisce a 6 ore e 30 minuti.

2. **Analisi dei dati**: Quando si tratta di dati basati sul tempo, come durata, ore di lavoro o tempi di evento, formattare i numeri come tempo permette un'analisi più semplice. Consente di calcolare facilmente totali, medie e differenze. Ad esempio, sommare le durate del tempo per un progetto o calcolare il tempo medio trascorso su attività diventa più intuitivo.

3. **Coerenza**: Applicare la formattazione temporale garantisce che tutti i dati relativi al tempo nel tuo documento siano coerenti, cosa fondamentale per presentazione e analisi. La coerenza nella presentazione dei dati aiuta a evitare confusione e rende i tuoi dati professionali.

4. **Compatibilità con le funzioni temporali**: Excel offre un'ampia gamma di funzioni progettate specificamente per lavorare con dati in formato temporale, come `NETWORKDAYS`, `HOUR`, `MINUTE` e `SECOND`. Formattando i tuoi numeri come valori temporali, garantisci compatibilità con queste funzioni, permettendoti di eseguire calcoli e analisi temporali complessi.

5. **Atractivo visivo e chiarezza**: I dati in formato temporale possono essere utilizzati insieme alle funzionalità di formattazione condizionale e grafici di Excel per creare report e dashboard visivamente attraenti e informativi. Ad esempio, puoi evidenziare valori temporali che superano una certa soglia o visualizzare tendenze temporali nel tempo.

6. **Riduzione degli errori**: Formatando i numeri come tempo, puoi ridurre il rischio di interpretare erroneamente i dati. Ad esempio, "7:45" indica chiaramente 7 ore e 45 minuti, mentre "7.75" potrebbe essere interpretato erroneamente come 7 ore e 75 minuti da qualcuno non familiare con il contesto.

7. **Facilità di inserimento**: Quando inserisci dati basati sul tempo, formattare le celle come tempo permette un inserimento più naturale. Gli utenti possono inserire "1:30" invece di calcolare l'equivalente decimale di 1 ora e 30 minuti, che è "1.5".

In sintesi, formattare i numeri in tempo in Excel migliora la rappresentazione, l'analisi e la coerenza dei dati, rendendo più facile agli utenti lavorare con dati temporali. Sfrutta le funzionalità integrate di Excel per i calcoli temporali e migliora l'esperienza complessiva rendendo i dati più accessibili e comprensibili.

## **Come formattare un numero come tempo in Excel**
La formattazione dei numeri come tempo in Excel può essere fatta in diversi modi, a seconda del formato dei dati iniziali e del risultato desiderato. Ecco alcune situazioni comuni e come gestirle:

### Scenario 1: Convertire le ore decimali in formato temporale

Se hai un numero che rappresenta ore in forma decimale (ad esempio, 1.5 per un'ora e trenta minuti) e vuoi convertirlo in formato temporale:

1. **Inserisci le ore decimali** in una cella (ad esempio, `1.5`).
2. **Fai clic destro** sulla cella e seleziona **Formato Celle**.
3. Nella finestra di dialogo **Formatta celle**, vai alla scheda **Numero**.
4. Seleziona **Ora** dall'elenco delle categorie.
5. Scegli un formato orario che si adatti alle tue esigenze e clicca **OK**.

Per le ore decimali, Excel tratta il valore come una frazione di una giornata di 24 ore. Quindi, `1.5` sarà formattato come `36:00` (36 ore) se scegli un formato che include ore oltre le 24.

### Scenario 2: Convertire testo o numeri in tempo

Se hai un tempo rappresentato come testo o numero senza decimali (ad esempio, `130` per 1:30 o `1530` per 15:30), devi prima convertirlo in un numero seriale di tempo che Excel può riconoscere prima di applicare il formato temporale.

1. **Supponendo che il tuo tempo sia in cella A1** e sia nel formato `hhmm` (ad esempio, `1530`), puoi usare la seguente formula per convertirlo in tempo:
   ```excel
   =TIME(LEFT(A1,LEN(A1)-2), RIGHT(A1,2), 0)
   ```
   Per i formati senza zeri iniziali (ad esempio, `130` per 1:30), potresti aver bisogno di una formula leggermente adattata per gestire le variazioni in lunghezza:
   ```excel
   =TIME(VALUE(LEFT(A1, LEN(A1)-2)), VALUE(RIGHT(A1,2)), 0)
   ```
2. Dopo aver applicato la formula, **clicca con il tasto destro** sulla cella con il risultato della formula, seleziona **Formato celle**, vai alla scheda **Numero**, seleziona **Ora**, scegli il formato desiderato e clicca su **OK**.

### Scenario 3: Convertire un Numero di Secondi in Formato Ora

Se hai un numero che rappresenta i secondi e vuoi convertirlo in un formato orario:

1. **Inserisci i tuoi secondi** in una cella (ad esempio, `3661` per un'ora, un minuto e un secondo).
2. Usa la formula `=A1/86400` per convertire i secondi nel numero seriale di Excel (dato che ci sono 86.400 secondi in un giorno). Sostituisci `A1` con la cella contenente i tuoi secondi.
3. **Clicca con il tasto destro** sulla cella con la formula, seleziona **Formato celle**, vai alla scheda **Numero**, seleziona **Ora**, scegli il formato desiderato e clicca su **OK**.

### Suggerimenti aggiuntivi

- Excel memorizza date e ore come numeri seriali. Per le date, conta i giorni a partire dal 1° gennaio 1900. Per le ore, la parte decimale del numero rappresenta l'ora del giorno.
- Puoi personalizzare i formati delle ore scegliendo **Personalizzato** nella finestra di dialogo **Formato celle** e inserendo il tuo codice di formato (ad esempio, `hh:mm:ss AM/PM`).
- Assicurati sempre che i tuoi dati siano coerenti per evitare risultati imprevisti nell'applicazione di formule o formati.

Seguendo questi passaggi e adattando in base ai tuoi dati e necessità specifiche, puoi formattare efficacemente i numeri come orario in Excel.

## **Come formattare un numero in tempo in Aspose.Cells for Node.js via C++**
La formattazione dei numeri in tempo in Aspose.Cells for Node.js via C++ è un processo semplice che prevede l'applicazione di un formato numerico personalizzato a una cella o a un intervallo di celle. Aspose.Cells è una libreria potente che ti consente di lavorare con i file Excel in applicazioni Node.js senza dover installare Microsoft Excel. Ecco come puoi formattare i numeri in tempo:

### Passo 1: Installa Aspose.Cells

Innanzitutto, assicurati di avere Aspose.Cells for Node.js via C++ nel tuo progetto. Puoi ottenerlo dal sito Aspose.

### Passo 2: Crea un nuovo workbook o apri uno esistente

Puoi creare un nuovo workbook o aprire uno esistente.

### Passo 3: Accedi al foglio di lavoro

Devi accedere al foglio di lavoro in cui desideri formattare i numeri come orario. Se lavori con un nuovo workbook, sarà probabilmente il primo foglio.

### Passo 4: Applica il formato orario a una cella

Per formattare un numero come orario, utilizzerai l'oggetto `Style` associato a una cella. Puoi specificare il formato orario usando stringhe di formato numerico personalizzate. Ecco un esempio di formattazione di una cella per mostrare l'ora nel formato di ore e minuti.

### Passo 5: Salva il workbook

Dopo aver applicato i formati desiderati, non dimenticare di salvare il tuo workbook.

### Formati orari personalizzati

Puoi usare diversi formati personalizzati a seconda delle tue esigenze. Ecco alcuni esempi:

- `"HH:MM"`: Ore e minuti
- `"HH:MM:SS"`: Ore, minuti e secondi
- `"HH:MM AM/PM"`: Ore e minuti con AM o PM

### Codice di esempio

Ecco un esempio di codice che dimostra questi passaggi:
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToTime.js" >}}

### Conclusione

La formattazione dei numeri in tempo in Aspose.Cells for Node.js via C++ comporta la impostazione di un formato numerico personalizzato per le celle dove vuoi visualizzare il tempo. Seguendo i passaggi sopra indicati, puoi facilmente applicare formati di tempo alle celle dei tuoi file Excel usando Aspose.Cells. Ricorda, la chiave è usare la stringa di formato personalizzato corretta che corrisponda al tuo formato di tempo desiderato.

{{< app/cells/assistant language="nodejs-cpp" >}}
