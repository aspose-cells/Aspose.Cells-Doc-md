---
title: Visual Studio esporta GridView in controllo Excel
type: docs
weight: 10
url: /it/net/visual-studio-export-gridview-to-excel-control/
---
## **introduzione**
 Export GridView To Excel Control è un controllo server ASP.NET che consente di esportare i contenuti di GridView in Microsoft Excel o OpenOffice Spreadsheets utilizzando[Aspose.Cells](https://products.aspose.com/cells/net/) . Aggiunge**esportare in Excel** pulsante sopra il controllo GridView. Facendo clic sul pulsante si esporta dinamicamente il contenuto del controllo GridView in un foglio di calcolo Microsoft Excel o OpenOffice e quindi si scarica automaticamente il file esportato nella posizione del disco selezionata dall'utente in appena un paio di secondi.
### **Caratteristiche del modulo**
Questa versione iniziale del controllo fornisce le seguenti funzionalità:

- Ottieni una copia offline dei tuoi contenuti GridView online preferiti per la modifica, la condivisione e la stampa.
- Ereditato dal controllo ASP.NET GridView predefinito e quindi ha tutte le sue caratteristiche e proprietà.
- Esporta GridView in Xlsx, Xlsb, Xls, Txt, Csv, Ods.
- Funziona con tutte le versioni di .NET a partire da .NET 2.0.
- Possibilità di personalizzare/localizzare il testo del pulsante Esporta.
- Applica l'aspetto del tuo tema sul pulsante Esporta usando css.
- Opzione per aggiungere un'intestazione personalizzata sopra il documento esportato
- Opzione per salvare ogni documento esportato sul server in un percorso su disco configurabile
- Opzione per esportare la pagina corrente o tutte le pagine quando il paging è abilitato

![cose da fare:immagine_alt_testo](visual-studio-export-gridview-to-excel-control_1.png)

Questo controllo consente di esportare GridView nei seguenti diversi formati di file.

1. Esporta GridView in Excel
1. Esporta GridView in Xlsx
1. Esporta GridView in Xlsb
1. Esporta GridView in Xls
1. Esporta GridView in Txt
1. Esporta GridView in CSV
1. Esporta GridView in Ods
## **Requisiti di sistema e piattaforme supportate**
### **Requisiti di sistema**
Esporta GridView in Excel Control per Visual Studio può essere utilizzato su qualsiasi sistema in cui sia installato IIS e .NET Framework 2.0 o versioni successive.
### **Piattaforme supportate**
Esporta GridView in Excel Control per Visual Studio è supportato da tutte le versioni di ASP.NET in esecuzione su .NET Framework 2.0 o versioni successive. È possibile utilizzare una delle seguenti versioni di Visual Studio per utilizzare questo controllo nelle applicazioni ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013
## **Download**
È possibile scaricare Export GridView To Excel Control da uno dei percorsi seguenti

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/Export_GridView_Excel)
## **Installazione**
È molto semplice e facile da installare Export GridView To Excel Control, segui questi semplici passaggi
### **Per Visual Studio 2010, 2012 e 2013**
1. Estrai il file zip scaricato
1. Fare doppio clic sul file VSIX Aspose.Excel.GridViewExport.vsix
1. Apparirà una finestra di dialogo che mostra le versioni di Visual Studio disponibili e supportate installate sul tuo computer
1. Selezionare quelli a cui si desidera aggiungere il controllo Esporta GridView in Excel.
1. Fare clic su Installa

Si otterrà una finestra di dialogo di successo una volta completata l'installazione.

**Nota:** Assicurati di riavviare Visual Studio per rendere effettive le modifiche.
### **Per le edizioni Visual Studio 2005, 2008 ed Express**
Si prega di seguire questi passaggi per integrare Export GridView To Excel Control in Visual Studio per trascinare e rilasciare facilmente proprio come altri controlli ASP.NET

1. Estrai il file zip scaricato
1. Assicurati di eseguire Visual Studio come amministratore

Nel menu Strumenti, fare clic su Scegli elementi della casella degli strumenti.

1.  Fare clic su Sfoglia.
 Viene visualizzata la finestra di dialogo Apri.
1. Passare alla cartella estratta e selezionare Aspose.Excel.GridViewExport.dll
1. Fare clic su OK.

Quando apri un controllo aspx o ascx nella casella degli strumenti sul lato sinistro, vedrai ExportGridViewToWord nella scheda Generale

![cose da fare:immagine_alt_testo](visual-studio-export-gridview-to-excel-control_2.png)
## **Usando**
Una volta installato, è molto facile iniziare a utilizzare questo controllo nelle applicazioni ASP.NET

|**Per .NET Framework 4.0 e versioni successive** |**Per .NET Framework 2.0 e versioni successive** |** |
|:- |:- |:- |
| Per le applicazioni in esecuzione in .NET Framework 4.0 e versioni successive in Visual Studio 2010 e versioni successive, dovresti vedere**ExportGridViewToExcel** controllo dentro**Aspose**Scheda nella barra degli strumenti come mostrato di seguito. Puoi semplicemente trascinare questo controllo sulla tua pagina ASP.NET, sul controllo o sulla pagina master proprio come qualsiasi altro controllo .NET e iniziare.|Per utilizzare questo controllo nelle applicazioni in esecuzione in .NET 2.0 in qualsiasi versione di Visual Studio, assicurati di aver aggiunto ExportGridViewToExcel alla tua casella degli strumenti come da istruzioni su ﻿[8.1.2.1 Download e installazione]() sotto rubrica**Per le edizioni Visual Studio 2005, 2008 ed Express** <br> Tu dovresti vedere**ExportGridViewToExcel** controllo dentro**Generale**Scheda nella barra degli strumenti come mostrato di seguito. Puoi semplicemente trascinare questo controllo sulla tua pagina ASP.NET, sul controllo o sulla pagina master proprio come qualsiasi altro controllo .NET e iniziare.||
|<p>![cose da fare:immagine_alt_testo](picture2.png)</p><p></p>|<p>![cose da fare:immagine_alt_testo](picture3.png)</p><p></p>||
### **Aggiunta manuale del controllo ExportGridViewToExcel**
In caso di problemi con i metodi precedenti che utilizzano Visual Studio Toolbox, è possibile aggiungere manualmente questo controllo all'applicazione ASP.NET in esecuzione su qualsiasi framework .NET superiore a 2.0

1. Se stai utilizzando Visual Studio, assicurati di eseguirlo come amministratore
1.  Aggiungi riferimento a**Aspose.Excel.GridViewExport.dll** disponibile nel pacchetto di download estratto nel progetto ASP.NET o nell'applicazione web. Assicurati che l'applicazione Web/Visual Studio abbia accesso completo a questa cartella, altrimenti potresti ricevere un'eccezione Accesso negato.
1. Aggiungi questa riga all'inizio della pagina, del controllo o di MasterPage

{{< highlight "java" >}}

 <%@ Register assembly="Aspose.Excel.GridViewExport" namespace="Aspose.Excel.GridViewExport" tagprefix="aspose" %>

{{< /highlight >}}

1.  Aggiungere quanto segue in un punto della pagina ASP.NET, del controllo o della pagina master in cui si desidera aggiungere il controllo

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel ID="ExportGridViewToExcel1" runat="server"></aspose:ExportGridViewToExcel>

{{< /highlight >}}
### **Domande frequenti**
Domande e problemi comuni che potresti incontrare durante l'utilizzo di questo controllo

|**#** |**Domanda** |**Risposta** |
|:- |:- |:- |
|1 | Non riesco a vedere il controllo ExportGridViewToExcel in Toolbox|<p>**Visual Studio 2010 e versioni successive** </p><p>1. Assicurarsi di aver installato questo controllo utilizzando il file di estensione VSIX trovato nel pacchetto scaricato. Per verificare vai su Strumenti -> Estensione e aggiornamenti. Sotto Installato dovresti vedere 'Aspose Export Export GridView To Excel Control'. Se non lo vedi, prova a reinstallarlo</p><p> 2. Assicurati che la tua applicazione web sia in esecuzione in .NET framework 4.0 o versioni successive, per versioni precedenti di .NET framework controlla il metodo alternativo sopra.<br>   **Versioni precedenti di Visual Studio**</p><p>3. Assicurati di aver aggiunto manualmente questo controllo al tuo Toolbox come da istruzioni precedenti.</p>|
|2 |Ricevo l'errore "Accesso negato" durante l'esecuzione dell'applicazione|<p>1. Se riscontri questo problema in produzione, assicurati di copiare sia Aspose.Excel.dll che Aspose.Excel.GridViewExport.dll nella cartella bin.</p><p>2. Se utilizzi Visual Studio, assicurati di eseguirlo come amministratore anche se hai già effettuato l'accesso come amministratore.</p>|
### **Aspose .NET Esporta GridView nelle proprietà del controllo Excel**
Le seguenti proprietà sono esposte per configurare e utilizzare le funzioni interessanti fornite da questo controllo

|**Nome della proprietà** |**Tipo** |**Esempio/Possibili valori** |**Descrizione** |
|:- |:- |:- |:- |
| ExportButtonText| corda| esportare in Excel| È possibile utilizzare questa proprietà per ignorare il testo predefinito esistente|
| ExportButtonCssClass| corda| btn btn-primario| Classe Css applicata al div esterno del pulsante di esportazione. Per applicare css sul pulsante puoi usare l'input .yourClass|
| Esporta intestazione file| corda|<h4>Rapporto di esempio di esportazione di GridView</h4> | Puoi utilizzare i tag html per aggiungere stile alla tua intestazione|
| ExportOutputFormat|enum| Xlsx, Xlsb, Xls, Txt, Csv, Ods| Formato di output del documento esportato. I formati supportati sono Xlsx, Xlsb, Xls, Txt, Csv, Ods|
| ExportOutputPathSuServer| corda| c:<br> temp| Output locale Percorso del disco sul server in cui viene salvata automaticamente una copia dell'esportazione. L'applicazione deve disporre dell'accesso in scrittura a questo percorso.|
| ExportDataSource| oggetto| allRowsDataTable| Imposta l'oggetto da cui questo controllo di associazione dati recupera l'elenco di elementi di dati. L'oggetto deve contenere tutti i dati che devono essere esportati. Questa proprietà viene utilizzata in aggiunta alla normale proprietà DataSource ed è utile quando il paging personalizzato è abilitato e la pagina corrente recupera solo le righe da visualizzare sullo schermo.|
| LicenseFilePath| corda|| Percorso locale sul server del file di licenza. Ad esempio c:<br> inetpub<br> Aspose.Cells.lic|
Di seguito è riportato un esempio di controllo Export GridView in Excel con tutte le proprietà utilizzate

{{< highlight "java" >}}

 <aspose:ExportGridViewToExcel Width="800px" ID="ExportGridViewToExcel1" ExportButtonText="Export to Excel"

    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExcelOutputFormat="xlsx"

    ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h1>Example Report</h1>"

    OnPageIndexChanging="ExportGridViewToExcel1_PageIndexChanging" PageSize="5" AllowPaging="True"

    LicenseFilePath="c:\inetpub\Aspose.Cells.lic" runat="server" CellPadding="4"

    ForeColor="#333333" GridLines="Both">

</aspose:ExportGridViewToExcel>


{{< /highlight >}}
## **Dimostrazione video**
 si prega di controllare[il video](https://www.youtube.com/watch?v=_fSq_3TP1oM) sotto per vedere il modulo in azione.
## **Supporto, estensione e contributo**
### **Supporto**
Fin dai primi giorni di Aspose, sapevamo che solo dare ai nostri clienti buoni prodotti non sarebbe bastato. Avevamo anche bisogno di fornire un buon servizio. Siamo sviluppatori noi stessi e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Per questo offriamo assistenza gratuita. Chiunque utilizzi il nostro prodotto, sia che lo abbia acquistato o che stia utilizzando una valutazione, merita la nostra piena attenzione e rispetto.

Puoi registrare eventuali problemi o suggerimenti relativi a questo controllo utilizzando una delle seguenti piattaforme

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
### **Estendi e contribuisci**
Aspose .NET Export GridView To Excel Control per Visual Studio è open source e il relativo codice sorgente è disponibile sui principali siti Web di social coding elencati di seguito. Gli sviluppatori sono incoraggiati a scaricare il codice sorgente ed estendere la funzionalità secondo i propri requisiti.
#### **Codice sorgente**
È possibile ottenere il codice sorgente più recente da una delle seguenti posizioni

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins)
#### **Come configurare il codice sorgente**
È necessario che sia installato quanto segue per aprire ed estendere il codice sorgente

- Visual Studio 2010

Segui questi semplici passaggi per iniziare

1. Scarica/clona il codice sorgente.
1.  Apri Visual Studio 2010 e scegli**File** > **Progetto aperto**
1.  Sfoglia fino all'ultimo codice sorgente che hai scaricato e aperto**Aspose.Excel.GridViewExport.sln**
#### **Panoramica del codice sorgente**
Ci sono tre progetti nella soluzione

- Aspose.Excel.GridViewExport - Contiene il pacchetto VSIX e il controllo server for .NET 4.0.
- Aspose.Excel.GridViewExport_PuntoNet_2.0 - Controllo GridView esteso for .NET 2.0
- Aspose.Excel.GridViewExport.Website - Progetto Web per testare il controllo GridView esportabile di Excel
