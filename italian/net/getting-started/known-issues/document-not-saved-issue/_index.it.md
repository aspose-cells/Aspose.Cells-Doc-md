---
title: Problema di salvataggio del documento non salvato
type: docs
weight: 40
url: /it/net/document-not-saved-issue/
---

## **Problema**
Sto avendo un problema strano con un foglio di calcolo che ho creato con il tuo controllo. Si apre e si modifica bene in Excel, ma quando cerco di eseguire un Salvataggio o un Salva come, ottengo un messaggio "Documento non salvato".
### **Riepilogo della problematica**
Si tratta di un bug di Excel: 

"Documento non salvato" Salvare File Creato da Modello

ID Articolo: 121942

Ultima revisione: 15 agosto 2005

Revisione: 1.3

Questo articolo è stato precedentemente pubblicato con il codice Q121942
### **Sintomo**
Quando si tenta di salvare un foglio di lavoro, potresti ricevere il seguente messaggio di errore: **"Documento non salvato"**
### **Cause**
Questo problema potrebbe verificarsi quando sono verificate le seguenti condizioni:

- Il foglio di lavoro è stato creato da un modello che conteneva un oggetto incorporato.
- Hai inserito un foglio di lavoro nel tuo foglio di lavoro da un modello.
- Il modello contiene un oggetto incorporato.
### **Soluzione**
Per salvare il tuo lavoro, devi prima eliminare gli oggetti incorporati nel tuo foglio di lavoro.
