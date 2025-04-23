---
title: Come aggiungere la formattazione condizionale del testo
description: Come usare la libreria Aspose.Cells in C# per applicare la formattazione condizionale del testo. Regolando questi criteri, hai più controllo sull aspetto e l aspetto delle celle.
keywords: Aspose.Cells, Formattazione condizionale del testo, C#, Condizionale, Formattazione
type: docs
weight: 70
url: /it/net/how-to-add-text-conditional-formatting/
---

## **Possibili Scenari di Utilizzo**
Usare la formattazione condizionale basata su testo nei fogli di calcolo è utile per evidenziare le celle che soddisfano criteri testuali specifici. Questo può migliorare l'analisi dei dati e rendere più facile trovare informazioni chiave in un grande set di dati. Ecco alcune ragioni per usare la formattazione condizionale del testo:

1. Evidenziare testo specifico: Puoi applicare formattazione basata su parole, frasi o caratteri specifici. Per esempio, potresti voler evidenziare tutte le celle che contengono la parola "Urgente" o "Completato" per differenziare facilmente i compiti in un progetto.
1. Identificare schemi o tendenze: Se lavori con categorie o stati (come "Alto", "Medio", "Basso"), la formattazione condizionale del testo può distinguere visivamente tra di loro, facilitando il monitoraggio dei progressi o la prioritizzazione dei compiti.
1. Avvisi di errore o inserimento dati: La formattazione del testo può segnalare inserimenti incoerenti o errati, come parole mal scritte, testo incompleto o valori incorretti. Questo è particolarmente utile in set di dati con molto input testuale.
1. Maggiore leggibilità: Codificare a colori il testo o cambiarne lo stile (grassetto, corsivo, ecc.) aiuta a far risaltare le informazioni importanti, migliorando la leggibilità complessiva del foglio.
1. Feedback dinamico: Puoi impostare regole che regolano automaticamente la formattazione quando il testo corrisponde a determinate condizioni. Ciò significa che non devi aggiornare manualmente la formattazione man mano che i dati cambiano.

In sostanza, la formattazione condizionale del testo ti aiuta a individuare rapidamente informazioni rilevanti, errori e tendenze, rendendola uno strumento potente per gestire e interpretare dati testuali.

## **Come aggiungere la formattazione condizionale del testo usando Excel**
Per aggiungere una formattazione condizionale basata su testo in Excel, segui questi passaggi:

1. Seleziona l’intervallo di celle: Evidenzia le celle su cui vuoi applicare la formattazione condizionale.
1. Apri il menu di formattazione condizionale: Vai alla scheda Home nella barra di Excel. Clicca su Formattazione condizionale nel gruppo "Stili".
1. Scegli “Nuova regola”: Dal menu a discesa, seleziona Nuova regola.
1. Seleziona “Formatta solo le celle che contengono”: Nella finestra di dialogo Nuova regola di formattazione, scegli Formatta solo le celle che contengono sotto la sezione "Seleziona un tipo di regola".
1. Imposta i criteri della regola: Nella sezione "Formatta celle con", scegli Testo specifico dal menu a discesa. Seleziona contiene, inizia con o termina con, a seconda della condizione che vuoi applicare. Inserisci il testo che desideri formattare (ad esempio, una parola specifica come "Urgente" o "Completato").
1. Scegli la formattazione: Clicca sul pulsante Formatta. Nella finestra di dialogo Formato celle, puoi selezionare il colore carattere, il colore riempimento o altre opzioni di formattazione preferite.
1. Applica la regola: Una volta impostato il formato desiderato, clicca su OK per applicare la regola. Clicca nuovamente OK nella finestra di dialogo della Nuova regola di formattazione per chiuderla.
1. Visualizza i risultati: Le celle contenenti il testo specificato avranno ora la formattazione applicata, facilitando l’individuazione delle informazioni rilevanti.


## **Come aggiungere la formattazione condizionale del testo usando Aspose.Cells for .NET**

Aspose.Cells supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sulle celle durante l'esecuzione. Questo esempio dimostra esercizi avanzati di formattazione condizionale includendo BeginsWith, ContainsBlank, ContainsText e altri.

### **Formatta la cella quando il valore inizia con il testo specificato**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **Formatta la cella quando il valore contiene uno spazio vuoto**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **Formatta la cella quando il valore contiene errori**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **Formatta la cella quando il valore contiene testo specificato**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **Formatta cella quando il valore contiene valori duplicati**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **Formatta cella quando il valore termina con testo specificato**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **Formatta cella quando il valore non contiene vuoto**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **Formatta cella quando il valore non contiene errori**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **Formatta cella quando il valore non contiene testo specificato**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **Formatta cella quando il valore contiene valori unici**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
