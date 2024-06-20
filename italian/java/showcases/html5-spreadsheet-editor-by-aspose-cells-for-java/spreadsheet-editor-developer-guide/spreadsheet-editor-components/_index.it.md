---
title: Editor del foglio di calcolo  Componenti
type: docs
weight: 50
url: /it/java/spreadsheet-editor-components/
---

**Tabella dei contenuti**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Vista del foglio di lavoro](#SpreadsheetEditor-Components-WorksheetView)
- [Servizio del foglio di lavoro](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

L'editor del foglio di calcolo HTML5 è composto da alcuni componenti che si uniscono per creare il sistema completo. Qui descriviamo lo scopo e il ruolo di ciascuno.
### **Index.html**
È una pagina JSF che descrive l'interfaccia utente dell'editor e il punto principale della nostra applicazione. Tutte le interazioni che avvengono tra il browser web e il server avvengono attraverso questo punto finale.

Oltre a definire l'interfaccia utente, tutti i servizi di backend sono allegati qui utilizzando le tecnologie JSF. Quando l'utente interagisce con gli eventi dell'interfaccia utente, i dati vengono passati avanti e indietro tra i servizi e l'utente per completare le nostre attività, ad esempio l'esportazione dei fogli di calcolo.

Ha due principali aree di interesse.

**Barra multifunzione**

L'area della barra degli strumenti a schede in alto è chiamata barra multifunzione, tecnicamente. Contiene pulsanti, menu a discesa, menu radio, caselle di testo e alcuni campi nascosti che vengono utilizzati per eseguire molte operazioni sul foglio di calcolo. Questi pulsanti, quando cliccati, inviano comandi al server e aggiornano di conseguenza il foglio.

**Foglio**

Il foglio è costituito da righe e colonne. Quando vengono cliccate le celle, la barra multifunzione viene aggiornata di conseguenza senza inviare richieste al server, poiché tutti i dati necessari alla barra multifunzione sono allegati a ciascuna cella. La barra multifunzione tiene anche traccia delle celle, delle righe e delle colonne selezionate quando l'utente naviga attraverso il foglio.

Ogni cella ha il proprio editor inline che diventa visibile quando una cella è in modalità di modifica.
### **Vista del foglio di lavoro**
È un bean di backend JSF a portata di vista responsabile della gestione dei contenuti dinamici dell'interfaccia utente descritta in index.html. Ha gestori di eventi per le richieste Ajax che vengono attivati quando l'utente interagisce con l'interfaccia utente.
### **Servizio del foglio di lavoro**
Il WorkbookService è un bean di backend JSF a vista. Funziona come un componente di servizio e carica e scarica il foglio di calcolo con l'aiuto di altri servizi. Ha i seguenti punti finali:

**init**

Il **init** è un metodo **PostConstruct** che viene eseguito subito dopo il completamento della creazione dell'oggetto da parte del server dell'applicazione Java. Controlla il parametro **url** nella mappa dei parametri della richiesta e carica il foglio di calcolo corrispondente dalla posizione data, se possibile.

**destroy**

È responsabile della pulizia di tutte le risorse acquisite quando non sono più necessarie.
### **LoaderService**
Crea istanze di fogli di calcolo e le mantiene in memoria finché sono necessarie.
### **CellsService**
Il **CellsService** gestisce la cache di righe, colonne, celle, formattazione e struttura dei fogli di lavoro.
