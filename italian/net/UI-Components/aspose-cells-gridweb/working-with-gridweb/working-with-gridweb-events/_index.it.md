---
title: Lavorare con gli eventi di GridWeb
type: docs
weight: 70
url: /it/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb, eventi, evento
description: Questo articolo introduce come lavorare con tipi di eventi in GridWeb.
---

{{% alert color="primary" %}} 

Tutti i programmatori devono essere familiari con gli eventi e il loro scopo. Gli eventi vengono utilizzati per inviare notifiche di modifiche che possono verificarsi in un controllo o classe. Aspose.Cells.GridWeb ha diversi eventi che possono essere utilizzati per eseguire compiti specifici quando determinate modifiche avvengono nel controllo.

Questo argomento fornisce un'introduzione a tutti gli eventi supportati dal controllo Aspose.Cells.GridWeb insieme ad alcuni dettagli su come gestire questi eventi.

{{% /alert %}} 
## **Lavorare con gli eventi di Grid**
### **Introduzione agli eventi della griglia**
Il controllo Aspose.Cells.GridWeb supporta diversi eventi che forniscono maggior controllo per eseguire operazioni quando vengono attivati eventi specifici nel controllo. Di seguito è possibile trovare un elenco completo degli eventi supportati dal controllo Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Questa lista non include eventi ereditati da Aspose.Cells.GridWeb dalla classe Control.

{{% /alert %}} 

|**Eventi** |**Descrizione** |
| :- | :- |
|CellCommand | Si verifica quando viene fatto clic sull'iperlink di un comando di una cella. Quando questo evento viene attivato, il suo parametro e.Argument fornisce il nome del comando. |
|CellDoubleClick | Si verifica quando la cella viene doppio cliccata. |
|CellError | Si verifica quando il valore di input di una cella contiene un errore. |
|ColumnDeleted | Si verifica quando un utente elimina una colonna da un foglio di lavoro utilizzando il menu lato client. |
|ColumnDeleting |Si verifica quando un utente sta cercando di eliminare una colonna da un foglio di lavoro utilizzando il menu sul lato client. |
|ColumnDoubleClick |Si verifica quando l'intestazione della colonna viene cliccata due volte. |
|ColumnInserted |Si verifica quando un utente inserisce una colonna nel foglio di lavoro utilizzando il menu sul lato client. |
|CustomCommand |Si verifica quando un utente fa clic su un pulsante di comando personalizzato. |
|LoadCustomData |Si verifica quando la proprietà EnableSession del controllo è impostata su false e deve caricare i dati del foglio di lavoro. È possibile gestire questo evento in modalità senza sessione per caricare i dati del foglio di lavoro da un file o da un database. |
|PageIndexChanged |Si verifica quando l'indice della pagina del foglio del controllo viene modificato. |
|RowDeleted |Si verifica quando un utente elimina una riga dal foglio di lavoro utilizzando il menu sul lato client. |
|RowDeleting |Si verifica quando un utente sta cercando di eliminare una riga da un foglio di lavoro utilizzando il menu sul lato client. |
|RowDoubleClick |Si verifica quando l'intestazione della riga viene cliccata due volte. |
|RowInserted |Si verifica quando un utente inserisce una riga nel foglio di lavoro utilizzando il menu sul lato client. |
|SaveCommand |Si verifica quando il pulsante **Salva** viene cliccato. |
|SheetDataUpdated |Si verifica quando il controllo ha caricato i dati inviati e aggiornato i dati del foglio di lavoro. |
|SheetTabClick |Si verifica quando viene cliccata una scheda del foglio. |
|SubmitCommand |Si verifica quando viene cliccato il pulsante **Invia**. |
|UndoCommand |Si verifica quando viene cliccato il pulsante **Annulla**. |
|AjaxCallFinished |Si verifica quando l'aggiornamento AJAX del controllo è completato. (l'EnableAJAX deve essere impostato su true). |
|CellModifiedOnAjax |Si verifica quando la cella viene modificata nella chiamata AJAX. |
|OnAfterColumnFilter |Si verifica dopo che il filtro è stato applicato su una colonna. |
|OnBeforeColumnFilter |Si verifica prima che il filtro venga applicato su una colonna. |
## **Gestione degli eventi della griglia**
Per eseguire una specifica operazione al verificarsi di un evento specifico, è necessario creare un gestore di eventi. Un gestore di eventi esegue il compito desiderato quando si verifica un determinato evento. I passaggi illustrati di seguito mostrano come gestire un semplice evento della griglia utilizzando Visual Studio.
### **Passo 1: Selezione di un Evento del Controllo Aspose.Cells.GridWeb**
1. Seleziona il controllo Aspose.Cells.GridWeb e apri il suo dialogo Proprietà sul lato destro.
1. Clicca sul pulsante **Scheda Eventi**.
1. Seleziona un evento.
   Per questo esempio, è stato selezionato l'evento SaveCommand.
### **Passo 2: Creazione di un Gestore di Eventi**
1. Fai doppio clic su un evento nel dialogo Proprietà. 

   **Doppio clic su un evento selezionato** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




Quando l'evento viene doppio cliccato, un gestore di eventi viene creato automaticamente da Visual Studio. 

**Un gestore di eventi creato da Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Aggiungi del codice per eseguire qualche azione all'interno del gestore di eventi.

Qui è stata aggiunta una singola riga di codice che salva il contenuto della griglia in un file Excel quando viene cliccato il pulsante **Salva**.

Per ottenere più informazioni, sposta il cursore sopra per vedere del codice e scoprirai che Visual Studio è abbastanza intelligente da aggiungere un gestore di eventi all'evento SaveCommand di GridWeb.
### **Passo 3: Esecuzione dell'Applicazione**
1. Compila ed esegui l'applicazione.
1. Clicca su **Salva**.

Il contenuto della griglia viene salvato in un file Excel. 

**Applicazione in modalità di esecuzione** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
