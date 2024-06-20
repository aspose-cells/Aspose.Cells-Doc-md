---
title: Ricerca e sostituzione in GridWeb
type: docs
weight: 90
url: /it/net/aspose-cells-gridweb/search-and-replace-in-gridweb/
keywords: GridWeb, ricerca, sostituzione
description: Questo articolo introduce come effettuare ricerca e sostituzione in GridWeb.
---

{{% alert color="primary" %}} 

Uno dei modi più veloci per apportare modifiche ripetitive in un ampio foglio di calcolo è utilizzare la funzione di ricerca e sostituzione. La ricerca ti permette di individuare una stringa di testo o dati e la sostituzione la sostituisce con un nuovo valore. Aspose.Cells.GridWeb fornisce questa funzionalità. Consente di cercare e sostituire con una specifica stringa di testo o valore nel lato client della scheda attraverso una semplice finestra di dialogo. Consente anche di cercare dati parziali.

{{% /alert %}} 
## **Lavorare con Ricerca/Sostituzione**
### **La finestra di dialogo Ricerca/Sostituzione**
Ci sono due modi per aprire la finestra di dialogo Ricerca/Sostituzione:

1. Quando il controllo è attivo, premere **CTRL+F** per aprire la finestra di dialogo, o premere il tasto **CTRL+R** per aprire la finestra di dialogo con il pulsante **Sostituisci** abilitato.
1. Spostare il cursore nell'area della cella nella scheda, quindi fare clic con il pulsante destro del mouse. Selezionare **Ricerca** o **Sostituisci** dal menu. 

   **Selezione di Ricerca** 

![todo:image_alt_text](search-and-replace-in-gridweb_1.png)




Viene visualizzata una finestra di dialogo di stile. 

**La finestra di dialogo Ricerca/Sostituzione** 

![todo:image_alt_text](search-and-replace-in-gridweb_2.png)
### **Usando Trova**
Per cercare:

1. Apri la finestra Trova/Sostituisci.
1. Digita la stringa che vuoi cercare nel campo **Cerca**.
1. Fai clic su **Trova Avanti** per cercare.

La prossima cella che corrisponde alla tua condizione di ricerca viene evidenziata.

{{% alert color="primary" %}} 

Se il criterio di ricerca non viene trovato, viene visualizzata una finestra di dialogo per informarti.

{{% /alert %}} 
### **Opzioni di Ricerca**
Ci sono alcune opzioni di ricerca che puoi personalizzare nella finestra di dialogo. La tabella sottostante le elenca.

|**No.** |**Nome dell'Opzione** |**Descrizione** |
| :- | :- | :- |
|1 |Corrispondenza maiuscole/minuscole |Indica se utilizzare il maiuscolo/minuscolo nella ricerca. |
|2 |Corrispondenza parola intera |Indica se corrispondere alla parola intera nella ricerca. |
|3 |Ricerca in su |Indica se la ricerca verrà effettuata dall'alto verso il basso. |
|4 |Espressione regolare |Quando selezionato, il controllo tratterà la stringa nel campo di testo Trova come espressione regolare nel processo di ricerca. |
|5 |Trova in Formule/Valori |Quando vengono selezionate le Formule, il controllo corrisponderà alla formula o al valore non formattato delle celle se la formula o il valore non formattato è presente. Quando vengono selezionati i Valori, il controllo corrisponderà solo al valore visualizzato delle celle. |
### **Usando Sostituisci**
Per sostituire testo o valori:

1. Apri la finestra di dialogo Trova/Sostituisci premendo **CTRL+F**, o seleziona fare clic con il pulsante destro del mouse su una cella e poi seleziona **Trova** prima di fare clic su **Sostituisci**.
1. Digita la stringa di sostituzione nel campo **Sostituisci con**.
1. Fai clic su **Sostituisci**.

Per sostituire il testo:

1. Apri la finestra di dialogo.
1. Inserisci il testo da cercare nel campo **Trova cosa**, e il testo con cui sostituirlo nel campo **Sostituisci con**.
1. Sostituisci una singola occorrenza facendo clic su **Trova successivo** seguito da **Sostituisci**.
1. Se sei sicuro del contenuto del foglio di lavoro, fai clic su **Sostituisci tutto**.

{{% alert color="primary" %}} 

Se il foglio di lavoro non è in modalità di modifica, il pulsante **Sostituisci** non viene visualizzato.

{{% /alert %}}
