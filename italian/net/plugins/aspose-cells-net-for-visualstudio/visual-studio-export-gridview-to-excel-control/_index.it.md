---
title: Esportazione della griglia di Visual Studio in Excel
type: docs
weight: 10
url: /it/net/visual-studio-export-gridview-to-excel-control/
---

## **Introduzione**
Export GridView To Excel Control è un controllo server ASP.NET che consente di esportare i contenuti della griglia in Microsoft Excel o Fogli di calcolo OpenOffice utilizzando [Aspose.Cells](https://products.aspose.com/cells/net/). Aggiunge il pulsante **Esporta in Excel** in cima al controllo GridView. Facendo clic sul pulsante esporta dinamicamente il contenuto del controllo GridView in un Foglio di calcolo Microsoft Excel o OpenOffice e quindi scarica automaticamente il file esportato nella posizione del disco selezionata dall'utente in un paio di secondi.
### **Caratteristiche del Modulo**
Questo versione iniziale del controllo fornisce le seguenti funzionalità:

- Ottenere una copia offline dei tuoi contenuti preferiti online della griglia per la modifica, la condivisione e la stampa.
- Ereditato dal controllo GridView ASP.NET predefinito e quindi ha tutte le sue funzionalità e proprietà.
- Esporta GridView in Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Funziona con tutte le versioni .NET a partire da .NET 2.0.
- Possibilità di personalizzare/localizzare il testo del pulsante di esportazione.
- Applica l'aspetto del tuo tema al pulsante di esportazione utilizzando css.
- Opzione per aggiungere un'intestazione personalizzata in cima al documento esportato
- Opzione per salvare ciascun documento esportato sul server in un percorso del disco configurabile
- Opzione per esportare la pagina corrente o tutte le pagine quando è abilitato il paging

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_1.png)

Questo controllo ti consente di esportare GridView nei seguenti formati di file diversi.

1. Esporta GridView in Excel
1. Esporta GridView in Xlsx
1. Esporta GridView in Xlsb
1. Esporta GridView in Xls
1. Esporta GridView in Txt
1. Esporta GridView in Csv
1. Esporta GridView in Ods
## **Requisiti di sistema e piattaforme supportate**
### **Requisiti di sistema**
Il controllo Export GridView To Excel per Visual Studio può essere utilizzato su qualsiasi sistema dotato di IIS e .NET framework 2.0 o superiore installato.
### **Piattaforme Supportate**
Il controllo Export GridView To Excel per Visual Studio è supportato da tutte le versioni di ASP.NET in esecuzione su .NET framework 2.0 o superiore. Puoi utilizzare una qualsiasi delle seguenti versioni di Visual Studio per utilizzare questo controllo nelle tue applicazioni ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **Download**
Puoi scaricare il controllo Export GridView To Excel da uno dei seguenti luoghi

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Installazione**
È molto semplice e facile installare il controllo Export GridView To Excel, segui questi semplici passaggi
### **Per Visual Studio 2010, 2012 e 2013**
1. Estrarre il file zip scaricato
1. Fare doppio clic sul file VSIX Aspose.Excel.GridViewExport.vsix
1. Verrà visualizzata una finestra di dialogo che mostra le versioni di Visual Studio disponibili e supportate installate sul tuo computer
1. Seleziona quelle a cui desideri aggiungere il controllo Esporta GridView su Excel.
1. Fai clic su Installa

Riceverai una finestra di dialogo di successo una volta completata l'installazione.

**Nota:** Assicurati di riavviare Visual Studio affinché le modifiche abbiano effetto.
### **Per Visual Studio 2005, 2008 ed edizioni Express**
Segui questi passaggi per integrare il controllo Esporta GridView su Excel in Visual Studio per un semplice trascinamento e rilascio come gli altri controlli ASP.NET

1. Estrarre il file zip scaricato
1. Assicurati di eseguire Visual Studio come amministratore

Nel menu Strumenti, fare clic su Scegli elementi della casella degli strumenti.

1. Fare clic su Sfoglia. 
   Si aprirà la finestra di dialogo Apri.
1. Passa alla cartella estratta e seleziona Aspose.Excel.GridViewExport.dll
1. Fare clic su OK.

Quando apri un controllo aspx o ascx nella casella degli strumenti a sinistra, vedrai ExportGridViewToWord sotto la scheda Generale

![todo:image_alt_text](visual-studio-export-gridview-to-excel-control_2.png)
## **Utilizzo**
Una volta installato, è molto facile iniziare a utilizzare questo controllo nelle tue applicazioni ASP.NET

|**Per .NET framework 4.0 e successivi**|**Per .NET framework 2.0 e successivi**|
| :- | :- | :- |
|Per le applicazioni in esecuzione in .NET framework 4.0 e successive in Visual Studio 2010 e successive, dovresti vedere il controllo **ExportGridViewToExcel** nella scheda **Aspose** nella barra degli strumenti come mostrato di seguito. Puoi trascinare e rilasciare semplicemente questo controllo sulla tua pagina ASP.NET, controllo o pagina master proprio come qualsiasi altro controllo .NET e iniziare. |Per utilizzare questo controllo nelle applicazioni in esecuzione in .NET 2.0 in qualsiasi versione di Visual Studio, assicurati di aver aggiunto ExportGridViewToExcel alla tua casella degli strumenti come indicato nelle istruzioni su [8.1.2.1 Download e installazione]() nell'ambito **Per Visual Studio 2005, 2008 ed edizioni Express** <br>Dovresti vedere il controllo **ExportGridViewToExcel** nella scheda **Generale** nella barra degli strumenti come mostrato di seguito. Puoi trascinare e rilasciare semplicemente questo controllo sulla tua pagina ASP.NET, controllo o pagina master proprio come qualsiasi altro controllo .NET e iniziare. | |
|<p>![todo:image_alt_text](picture2.png)</p><p></p>|<p>![todo:image_alt_text](picture3.png)</p><p></p>| |
### **Aggiunta manuale del controllo ExportGridViewToExcel**
Se riscontri problemi con i metodi sopra che utilizzano la casella degli strumenti di Visual Studio, puoi aggiungere manualmente questo controllo alla tua applicazione ASP.NET in esecuzione su qualsiasi framework .NET superiore al 2.0

1. Se stai utilizzando Visual Studio, assicurati di eseguirlo come amministratore
1. Aggiungi riferimento a **Aspose.Excel.GridViewExport.dll** disponibile nel pacchetto di download estratto nel tuo progetto ASP.NET o applicazione web. Assicurati che la tua applicazione web/Visual Studio abbia pieno accesso a questa cartella, altrimenti potresti ricevere un'eccezione di accesso negato.
1. Aggiungi questa riga in cima alla pagina, al controllo o alla MasterPage 

{{< highlight java >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1. Aggiungi il seguente in un punto della tua pagina ASP.NET, controllo o masterpage dove vuoi che venga aggiunto il controllo 

{{< highlight java >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **Domande frequenti**
Domande comuni e problemi che potresti incontrare durante l'uso di questo controllo

|**#** |**Domanda** |**Risposta** |
| :- | :- | :- |
|1 |Non riesco a vedere il controllo ExportGridViewToExcel in Toolbox |<p>**Visual Studio 2010 e successive** </p><p>1. Assicurati di aver installato questo controllo utilizzando il file di estensione VSIX trovato nel pacchetto scaricato. Per verificare vai su Strumenti -> Estensioni e Aggiornamenti. Nelle installate dovresti vedere 'Aspose Export Export GridView To Excel Control'. Se non lo vedi, prova a reinstallarlo</p><p>2. Assicurati che la tua applicazione web stia eseguendo in framework .NET 4.0 o superiore, per versioni inferiori del framework .NET, controlla il metodo alternativo sopra. <br>   **Versioni più vecchie di Visual Studio**</p><p>3. Assicurati di aver aggiunto manualmente questo controllo al tuo Toolbox come da istruzioni sopra.</p>|
|2 |Sto ricevendo un errore 'Accesso negato' durante l'esecuzione dell'applicazione |<p>1. Se stai riscontrando questo problema in produzione, assicurati di copiare sia Aspose.Excel.dll che Aspose.Excel.GridViewExport.dll nella tua cartella bin.</p><p>2. Se stai utilizzando Visual Studio, assicurati di eseguirlo come amministratore anche se sei già loggato come amministratore.</p>|
### **Proprietà del controllo di esportazione di GridView To Excel Aspose .NET**
Le seguenti proprietà sono esposte per configurare e utilizzare le fantastiche funzionalità fornite da questo controllo

|**Nome della proprietà** |**Tipo** |**Esempio/Valori possibili** |**Descrizione** |
| :- | :- | :- | :- |
|ExportButtonText |string |Esporta in Excel |Puoi utilizzare questa proprietà per sovrascrivere il testo predefinito esistente |
|ExportButtonCssClass |string |btn btn-primary |Classe CSS che viene applicata all'esterno del pulsante di esportazione. Per applicare CSS al pulsante puoi usare .tuaClasse input |
|ExportFileHeading |string |<h4>Esempio di report di esportazione del GridView</h4> |Puoi utilizzare tag html per aggiungere stile al tuo titolo |
|ExportOutputFormat |enumerazione |Xlsx, Xlsb, Xls, Txt, Csv, Ods |Formato di output del documento esportato. I formati supportati sono Xlsx, Xlsb, Xls, Txt, Csv, Ods |
|ExportOutputPathOnServer |string |c: <br>temp |Percorso del disco di output locale sul server dove viene salvata automaticamente una copia dell'esportazione. L'applicazione deve avere accesso in scrittura a questo percorso. |
|ExportDataSource |oggetto |allRowsDataTable |Imposta l'oggetto da cui questo controllo di associazione dati recupera la lista di elementi dati. L'oggetto deve avere tutti i dati che devono essere esportati. Questa proprietà è utilizzata oltre alla normale proprietà DataSource ed è utile quando la paginazione personalizzata è abilitata e la pagina corrente recupera solo le righe da visualizzare sullo schermo. |
|LicenseFilePath |string | |Percorso locale sul server del file di licenza. Ad esempio c: <br>inetpub <br>Aspose.Cells.lic |
Di seguito è mostrato un esempio di controllo di esportazione di GridView in Excel con tutte le proprietà utilizzate

{{< highlight java >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Demo video**
Si prega di controllare [il video](https://www.youtube.com/watch?v=_fSq_3TP1oM) qui sotto per vedere il modulo in azione.
## **Supporto, Estendi e Contribuisci**
### **Supporto**
Fin dai primi giorni di Aspose, sapevamo che fornire ai nostri clienti solo buoni prodotti non sarebbe stato sufficiente. Dovevamo anche offrire un buon servizio. Siamo anche sviluppatori e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Ecco perché offriamo un supporto gratuito. Chiunque utilizzi il nostro prodotto, che li abbia acquistati o li stia usando in valutazione, merita la nostra piena attenzione e rispetto.

È possibile registrare eventuali problemi o suggerimenti relativi a questo controllo utilizzando una delle seguenti piattaforme

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Estensione e Contribuzione**
Aspose .NET Export GridView To Excel Control per Visual Studio è open source e il suo codice sorgente è disponibile sui principali siti di codifica sociale elencati di seguito. Gli sviluppatori sono incoraggiati a scaricare il codice sorgente ed estendere la funzionalità secondo le proprie esigenze.
#### **Codice Sorgente**
Puoi ottenere l'ultimo codice sorgente da uno dei seguenti siti

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Come configurare il codice sorgente**
Devi avere quanto segue installato per aprire ed estendere il codice sorgente

- Visual Studio 2010

Seguire questi semplici passaggi per iniziare

1. Scarica/Clona il codice sorgente.
1. Apri Visual Studio 2010 e scegli **File** > **Apri Progetto**
1. Navigare all'ultimo codice sorgente scaricato e aprire **Aspose.Excel.GridViewExport.sln**
#### **Panoramica del codice sorgente**
Ci sono tre progetti nella soluzione

- Aspose.Excel.GridViewExport - Contiene il pacchetto VSIX e il controllo server per .NET 4.0.
- Aspose.Excel.GridViewExport_DotNet_2.0 - Controllo GridView esteso per .NET 2.0
- Aspose.Excel.GridViewExport.Website - Progetto Web per testare il controllo GridView esportabile in Excel
