---
title: Editor di fogli di calcolo - Componenti
type: docs
weight: 50
url: /it/java/spreadsheet-editor-components/
---
**Sommario**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Foglio di lavoroVisualizza](#SpreadsheetEditor-Components-WorksheetView)
- [Cartella di lavoroService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

HTML5 Spreadsheet Editor è costituito da pochi componenti che si uniscono per creare il sistema completo. Qui descriviamo lo scopo e il ruolo di ciascuno.
### **Index.html**
È una pagina JSF che descrive l'interfaccia utente dell'editor e l'endpoint principale della nostra applicazione. Tutte le interazioni eseguite tra il browser Web e il server vengono eseguite tramite questo endpoint.

Oltre a definire l'interfaccia utente, tutti i servizi di backend sono collegati qui utilizzando le tecnologie JSF. Quando l'utente interagisce con gli eventi dell'interfaccia utente e i dati vengono passati avanti e indietro tra i servizi e l'utente per completare le nostre attività, ad esempio l'esportazione di fogli di calcolo.

Ha due principali aree di interesse.

**Nastro**

L'area della barra degli strumenti a schede in alto si chiama nastro, tecnicamente. Contiene pulsanti, menu a discesa, menu radio, caselle di testo e alcuni campi nascosti che vengono utilizzati per eseguire molte operazioni sul foglio di calcolo. Questi pulsanti quando vengono cliccati inviano comandi al server e aggiornano il foglio di conseguenza.

**Foglio**

Il foglio è le righe e le colonne. Quando si fa clic sulle celle, la barra multifunzione viene aggiornata di conseguenza senza inviare richieste al server poiché tutti i dati necessari alla barra multifunzione sono allegati a ciascuna cella. La barra multifunzione tiene traccia anche della cella, della riga e della colonna selezionate quando l'utente naviga nel foglio.

Ogni cella ha il proprio editor in linea che diventa visibile quando una cella è in modalità di modifica.
### **Foglio di lavoroVisualizza**
È un bean backend JSF con scope view responsabile della gestione dei contenuti dinamici dell'interfaccia utente descritta in index.html. Dispone di gestori di eventi per le richieste Ajax che vengono attivate quando l'utente interagisce con l'interfaccia utente.
### **Cartella di lavoroService**
WorkbookService è un bean backend JSF con ambito di visualizzazione. Funziona come un componente di servizio e carica e scarica il foglio di calcolo con l'aiuto di altri servizi. Ha i seguenti endpoint:

**dentro**

 Il**dentro** è**PostConstruct** metodo che viene eseguito subito dopo che la creazione dell'oggetto è stata completata dall'Application Server Java. Controlla**URL** parametro nella mappa dei parametri della richiesta e carica il foglio di calcolo corrispondente da una determinata posizione, se possibile.

**distruggere**

È responsabile della pulizia di tutte le risorse acquisite quando non sono più necessarie.
### **LoaderService**
Crea istanze di fogli di calcolo e le tiene in memoria finché sono necessarie.
### **CellsService**
 Il**CellsService** gestisce la cache di righe, colonne, celle, la formattazione e la struttura dei fogli di lavoro.
