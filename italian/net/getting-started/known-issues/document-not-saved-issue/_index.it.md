---
title: Documento non salvato Problema
type: docs
weight: 40
url: /it/net/document-not-saved-issue/
---
## **Problema**
Sto riscontrando uno strano problema con un foglio di calcolo che ho creato con il tuo controllo. Si apre e modifica bene in Excel, ma quando provo a eseguire un salvataggio o un salvataggio con nome, ottengo un msgbox "Documento non salvato".
### **Riepilogo del problema**
 Questo è un bug di Excel:

"Documento non salvato" Salvataggio del file creato dal modello

Identificativo articolo : 121942

Ultima revisione : 15 agosto 2005

Revisione : 1.3

Questo articolo è stato precedentemente pubblicato con Q121942
### **Sintomo**
 Quando si tenta di salvare una cartella di lavoro, è possibile che venga visualizzato il seguente messaggio di errore:**"Documento non salvato"**
### **Cause**
Questo problema può verificarsi quando sono vere le seguenti condizioni:

- La cartella di lavoro è stata creata da un modello che conteneva un oggetto incorporato.
- Hai inserito un foglio di lavoro nella tua cartella di lavoro da un modello.
- Il modello contiene un oggetto incorporato.
### **Soluzione**
Per salvare il tuo lavoro, devi prima eliminare gli oggetti incorporati nella tua cartella di lavoro.
