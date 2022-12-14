---
title: Lavorare con Aspose.Cells.GridDesktop Events
type: docs
weight: 30
url: /it/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

Gli eventi vengono utilizzati per inviare notifiche quando si verifica una modifica in un controllo o in una classe. Aspose.Cells.GridDesktop dispone di diversi eventi utilizzati per eseguire attività specifiche quando si verificano determinate modifiche nel controllo. Questo argomento fornisce un'introduzione a tutti gli eventi supportati dal controllo Aspose.Cells.GridDesktop e spiega come gestire tali eventi.

{{% /alert %}} 
## **introduzione**
Il controllo Aspose.Cells.GridDesktop supporta diversi eventi che forniscono un maggiore controllo per l'esecuzione di operazioni quando vengono attivati eventi specifici. Di seguito è riportato un elenco completo degli eventi supportati dal controllo Aspose.Cells.GridDesktop.

{{% alert color="primary" %}} 

Questo elenco non include gli eventi ereditati da Aspose.Cells.GridDesktop dalla classe Control.

{{% /alert %}} 

|**Eventi**|**Descrizione**|
|:- |:- |
|PrimaCalcola|Si verifica prima di calcolare la formula nella cartella di lavoro.|
|Prima di caricare file|Si verifica prima che la cartella di lavoro venga caricata dal file.|
|ColumnHeaderClic|Si verifica quando si fa clic sull'intestazione di colonna.|
|ColumnHeaderDoubleClick|Si verifica quando si fa doppio clic sull'intestazione di colonna.|
|CellDataChanged|Si verifica quando i dati o il valore all'interno di una cella Grid vengono modificati. Questo evento può essere attivato anche se il valore di una cella viene modificato a livello di codice utilizzando la proprietà Value o il metodo SetCellValue di un oggetto GridCell.|
|CellButtonClic|Si verifica quando si fa clic sul pulsante della cella.|
|CellCheckedChanged|Si verifica quando la proprietà Checked della casella di controllo della cella viene modificata.|
|CellSelectedIndexChanged|Si verifica quando la proprietà SelectedIndex della casella combinata della cella viene modificata.|
|CellClic|Si verifica quando si fa clic su una cella della griglia.|
|CellDoubleClick|Si verifica quando si fa doppio clic su una cella della griglia.|
|CellKeyPressed|Si verifica quando viene premuto un tasto mentre una cella ha lo stato attivo. Se si desidera creare un gestore eventi per l'evento CellKeyPressed, impostare la proprietà Handled dell'argomento CellKeyEventArgs su true per impedire al controllo GridDesktop di gestire l'evento chiave.|
|AfterInsertColumns|Si verifica quando viene inserita una colonna. È possibile ottenere l'indice della colonna utilizzando la proprietà Index dell'argomento Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|AfterInsertRows|Si verifica quando viene inserita una riga. È possibile ottenere l'indice di riga utilizzando la proprietà Index dell'argomento Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|Errore di caricamento del file|Si verifica quando non è possibile caricare la cartella di lavoro.|
|FineCalcola|Si verifica dopo aver calcolato la formula nella cartella di lavoro.|
|FineCarica file|Si verifica quando la cartella di lavoro viene caricata.|
|FocusedCellChanged|Si verifica ogni volta che viene modificato lo stato attivo di una cella.|
|RowHeaderClic|Si verifica quando si fa clic sull'intestazione di riga.|
|RowHeaderDoubleClick|Si verifica quando si fa doppio clic sull'intestazione di riga.|
|RowColumnHiddenChanged|Si verifica quando lo stato nascosto della riga o della colonna viene modificato.|
|SelectedSheetIndexChanged|Si verifica quando un utente seleziona un nuovo foglio di lavoro, ovvero quando il foglio selezionato passa da un foglio di lavoro a un altro. Questo evento può essere attivato anche a livello di codice se la proprietà ActiveSheetIndex del controllo GridDesktop cambia.|
## **Gestione degli eventi della griglia**
Per eseguire un'operazione specifica quando viene attivato un evento specifico, creare un gestore eventi. Un gestore di eventi esegue una particolare attività quando viene attivato un determinato evento. Di seguito, un gestore eventi è configurato per gestire un semplice evento Grid usando Visual Studio.NET.

**Passaggio 1: selezione di un evento di Aspose.Cells.GridDesktop Control**

1. In Visual Studio selezionare il controllo Aspose.Cells.GridDesktop e aprirlo**Proprietà**dialogo.
1.  Clicca il**Eventi** scheda.
1.  Seleziona un evento. (per questo esempio, il**CellClic** l'evento è selezionato).

**Passaggio 2: creazione di un gestore di eventi**

1.  Fare doppio clic su un evento selezionato nel file**Proprietà**dialogo.
1. Quando si fa doppio clic sull'evento, Visual Studio.NET crea un gestore eventi. Di seguito è riportato il codice generato dal progettista che mostra che viene creato un evento per il controllo GridControl.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


 Ora aggiungi il codice per eseguire l'operazione desiderata all'interno del gestore eventi. Per questo esempio, abbiamo aggiunto una riga di codice che visualizza una finestra di messaggio per le notifiche.
Dai un'occhiata al gestore eventi che Visual Studio ha aggiunto all'evento CellClick del controllo GridDesktop. Sembrerà qualcosa di simile al codice qui sotto.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Passaggio 3: eseguire l'applicazione**

1. Compilare ed eseguire l'applicazione.
1. Ogni volta che si fa clic su una cella della griglia, viene visualizzata una finestra di messaggio con il messaggio "È stato fatto clic su Cell".
