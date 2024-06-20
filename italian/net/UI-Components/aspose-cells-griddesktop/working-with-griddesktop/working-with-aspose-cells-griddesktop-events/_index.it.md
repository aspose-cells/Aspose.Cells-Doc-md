---
title: Lavorare con gli eventi Aspose.Cells.GridDesktop
type: docs
weight: 30
url: /it/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, evento, eventi
description: Questo articolo illustra come utilizzare gli eventi in GridDesktop.
---

{{% alert color="primary" %}} 

Gli eventi vengono utilizzati per inviare notifiche quando avviene una modifica in un controllo o una classe. Aspose.Cells.GridDesktop ha diversi eventi che vengono utilizzati per eseguire compiti specifici quando avvengono determinate modifiche nel controllo. Questo argomento fornisce un'introduzione a tutti gli eventi supportati dal controllo Aspose.Cells.GridDesktop e spiega come gestire tali eventi.

{{% /alert %}} 
## **Introduzione**
Il controllo Aspose.Cells.GridDesktop supporta diversi eventi che forniscono maggiore controllo per eseguire operazioni quando vengono attivati eventi specifici. Di seguito è riportato un elenco completo degli eventi supportati dal controllo Aspose.Cells.GridDesktop.

{{% alert color="primary" %}} 

Questo elenco non include gli eventi ereditati da Aspose.Cells.GridDesktop dalla classe Control.

{{% /alert %}} 

|**Eventi**|**Descrizione**|
| :- | :- |
|BeforeCalculate| Si verifica prima di calcolare la formula nel foglio di lavoro.|
|BeforeLoadFile| Si verifica prima che il foglio di lavoro venga caricato da un file.|
|ColumnHeaderClick|Si verifica quando si fa clic sull'intestazione della colonna.|
|ColumnHeaderDoubleClick|Si verifica quando si fa doppio clic sull'intestazione della colonna.|
|CellDataChanged|Si verifica quando i dati o il valore all'interno di una cella di griglia vengono modificati. Questo evento può essere attivato anche se il valore di una cella viene modificato programmaticamente utilizzando la proprietà Value o il metodo SetCellValue di una GridCell.|
|CellButtonClick|Si verifica quando viene fatto clic sul pulsante della cella.|
|CellCheckedChanged|Si verifica quando la proprietà Checked della casella di controllo della cella viene modificata.|
|CellSelectedIndexChanged|Si verifica quando la proprietà SelectedIndex della casella combinata della cella viene modificata.|
|CellClick|Si verifica quando viene cliccata una cella della griglia.|
|CellDoubleClick|Si verifica quando una cella della griglia viene doppio cliccata.|
|CellKeyPressed|Si verifica quando viene premuto un tasto mentre una cella ha il focus. Se si desidera creare un gestore eventi per l'evento CellKeyPressed, impostare la proprietà Handled dell'argomento CellKeyEventArgs su true per impedire al controllo GridDesktop di gestire l'evento del tasto.|
|AfterInsertColumns|Si verifica quando viene inserita una colonna. È possibile ottenere l'indice della colonna utilizzando la proprietà Indice dell'argomento Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|AfterInsertRows|Si verifica quando viene inserita una riga. È possibile ottenere l'indice della riga utilizzando la proprietà Indice dell'argomento Aspose.Cells.GridDesktop.WorksheetEventArgs.|
|FailLoadFile| Si verifica quando non è possibile caricare il file di lavoro.|
|FinishCalculate|Si verifica dopo il calcolo della formula nel foglio di lavoro.|
|FinishLoadFile|Si verifica quando il file di lavoro viene caricato.|
|FocusedCellChanged|Si verifica ogni volta che il focus di una cella viene modificato.|
|RowHeaderClick|Si verifica quando viene cliccato l'intestazione di riga.|
|RowHeaderDoubleClick|Si verifica quando viene doppio cliccata l'intestazione di riga.|
|RowColumnHiddenChanged|Si verifica quando lo stato nascosto della riga o della colonna viene modificato.|
|SelectedSheetIndexChanged|Si verifica quando un utente seleziona un nuovo foglio di lavoro, cioè quando il foglio selezionato cambia da un foglio di lavoro a un altro. Questo evento può anche essere attivato programmaticamente se la proprietà ActiveSheetIndex del controllo GridDesktop cambia.|
## **Gestione degli eventi della griglia**
Per eseguire una specifica operazione quando viene attivato un determinato evento, creare un gestore eventi. Un gestore eventi esegue un'attività particolare quando viene attivato un evento specifico. Di seguito, viene configurato un gestore eventi per gestire un semplice evento della griglia utilizzando Visual Studio.NET.

**Passaggio 1: Selezione di un Evento di Controllo Aspose.Cells.GridDesktop**

1. In Visual Studio, selezionare il controllo Aspose.Cells.GridDesktop e aprire il relativo dialogo **Proprietà**.
1. Fare clic sulla scheda **Eventi**.
1. Selezionare un evento. (per questo esempio, viene selezionato l'evento **CellClick**).

**Passaggio 2: Creazione di un Gestore Eventi**

1. Fare doppio clic su un evento selezionato nella finestra di dialogo delle **Proprietà**.
1. Quando si fa doppio clic sull'evento, viene creato un gestore degli eventi da Visual Studio.NET. Di seguito è riportato il codice generato dal designer che mostra che un evento è stato creato per il controllo GridControl.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


Ora aggiungere del codice per eseguire l'operazione desiderata all'interno del gestore degli eventi. Per questo esempio, abbiamo aggiunto una riga di codice che visualizza una finestra di dialogo per le notifiche. 
Date un'occhiata al gestore degli eventi che visual Studio ha aggiunto all'evento CellClick del controllo GridDesktop. Avrà un aspetto simile al codice sottostante.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Passaggio 3: Esecuzione dell'Applicazione**

1. Compila ed esegui l'applicazione.
1. Ogni volta che viene cliccata una cella della griglia, compare una finestra di dialogo con il messaggio "Cell is Clicked".
