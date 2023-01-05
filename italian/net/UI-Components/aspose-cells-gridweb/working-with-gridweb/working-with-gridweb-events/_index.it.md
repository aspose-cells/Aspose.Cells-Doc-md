---
title: Utilizzo degli eventi GridWeb
type: docs
weight: 70
url: /it/net/working-with-gridweb-events/
---
{{% alert color="primary" %}} 

Tutti i programmatori devono avere familiarità con gli eventi e il loro scopo. Gli eventi vengono utilizzati per inviare notifiche di modifiche che possono verificarsi in un controllo o in una classe. Aspose.Cells.GridWeb ha diversi eventi che possono essere utilizzati per eseguire attività specifiche quando si verificano determinate modifiche nel controllo.

Questo argomento fornisce un'introduzione a tutti gli eventi supportati dal controllo Aspose.Cells.GridWeb insieme ad alcuni dettagli su come gestire questi eventi.

{{% /alert %}} 
## **Lavorare con gli eventi della griglia**
### **Introduzione agli eventi di griglia**
Aspose.Cells. Il controllo GridWeb supporta diversi eventi che forniscono un maggiore controllo per l'esecuzione di operazioni quando vengono attivati eventi specifici nel controllo. Di seguito è riportato un elenco completo degli eventi supportati dal controllo Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Questo elenco non include gli eventi ereditati da Aspose.Cells.GridWeb dalla classe Control.

{{% /alert %}} 

|**Eventi** |**Descrizione** |
|:- |:- |
| CellCommand| Si verifica quando si fa clic sul collegamento ipertestuale del comando di una cella. Quando questo evento viene attivato, il suo parametro e.Argument fornisce il nome del comando.|
| CellDoubleClick| Si verifica quando si fa doppio clic sulla cella.|
| CellError| Si verifica quando il valore di input di una cella presenta un errore.|
| Colonna eliminata|Si verifica quando un utente elimina una colonna da un foglio di lavoro utilizzando il menu lato client.|
| Eliminazione colonna| Si verifica quando un utente tenta di eliminare una colonna da un foglio di lavoro utilizzando il menu lato client.|
| ColonnaDoubleClick| Si verifica quando si fa doppio clic sull'intestazione di colonna.|
| ColonnaInserito| Si verifica quando un utente inserisce una colonna nel foglio di lavoro utilizzando il menu lato client.|
| Comando personalizzato| Si verifica quando un utente fa clic su un pulsante di comando personalizzato.|
| Carica dati personalizzati| Si verifica quando la proprietà EnableSession del controllo è impostata su false e deve caricare i dati del foglio di lavoro. È possibile gestire questo evento in modalità senza sessione per caricare i dati del foglio di lavoro da un file o da un database.|
| PageIndexModificato| Si verifica quando l'indice della pagina del foglio del controllo viene modificato.|
| Riga eliminata| Si verifica quando un utente elimina una riga da un foglio di lavoro utilizzando il menu lato client.|
| RowDeleting| Si verifica quando un utente tenta di eliminare una riga da un foglio di lavoro utilizzando il menu lato client.|
| RigaDoppio clic|Si verifica quando si fa doppio clic sull'intestazione di riga.|
| RigaInserita| Si verifica quando un utente inserisce una riga nel foglio di lavoro utilizzando il menu lato client.|
| SalvaComando| Si verifica quando il**Salva** si fa clic sul pulsante.|
| SheetDataAggiornato| Si verifica quando il controllo ha caricato i dati registrati e aggiornato i dati del foglio di lavoro.|
| FoglioSchedaClic| Si verifica quando si fa clic su una scheda del foglio.|
| InviaComando| Si verifica quando il**Invia** si fa clic sul pulsante.|
| AnnullaComando| Si verifica quando il**Annullare** si fa clic sul pulsante.|
| Ajax CallFinished| Viene eseguito al termine dell'aggiornamento AJAX del controllo. (EnableAJAX deve essere impostato su true).|
| CellModifiedOnAjax| Si attiva quando la cella viene modificata nella chiamata AJAX.|
| OnAfterColumnFilter| Viene eseguito dopo che il filtro è stato applicato a una colonna.|
| OnBeforeColumnFilter| Viene eseguito prima che il filtro venga applicato a una colonna.|
## **Gestione degli eventi della griglia**
Per eseguire un'operazione specifica sull'attivazione di un evento specifico, dobbiamo creare un gestore di eventi. Un gestore di eventi esegue l'attività desiderata quando viene attivato un determinato evento. I passaggi illustrati di seguito mostrano come gestire un semplice evento di griglia usando Visual Studio.
### **Passaggio 1: selezione di un evento di Aspose.Cells.GridWeb Control**
1. Selezionare il controllo Aspose.Cells.GridWeb e aprire la relativa finestra di dialogo Proprietà sul lato destro.
1.  Clicca il**Scheda Eventi** pulsante.
1. Seleziona un evento.
 Per questo esempio, viene selezionato l'evento SaveCommand.
### **Passaggio 2: creazione di un gestore di eventi**
1.  Fare doppio clic su un evento nella finestra di dialogo Proprietà.

   **Fare doppio clic su un evento selezionato** 

![cose da fare:immagine_alt_testo](working-with-gridweb-events_1.png)




 Quando si fa doppio clic sull'evento, Visual Studio crea automaticamente un gestore eventi.

**Un gestore eventi creato da Visual Studio** 

![cose da fare:immagine_alt_testo](working-with-gridweb-events_2.png)




1. Aggiungi codice per eseguire alcune azioni all'interno del gestore eventi.

 Qui, una singola riga di codice che salva il contenuto della griglia in un file Excel quando il file**Salva** il pulsante viene cliccato è stato aggiunto.

Per ottenere maggiori informazioni, sposta il cursore sopra per vedere del codice, quindi scoprirai che Visual Studio è abbastanza intelligente da aggiungere un gestore di eventi all'evento SaveCommand di GridWeb.
### **Passaggio 3: eseguire l'applicazione**
1. Compilare ed eseguire l'applicazione.
1.  Clic**Salva**.

 Il contenuto della griglia viene salvato in un file Excel.

**Applicazione in modalità di esecuzione** 

![cose da fare:immagine_alt_testo](working-with-gridweb-events_3.png)
