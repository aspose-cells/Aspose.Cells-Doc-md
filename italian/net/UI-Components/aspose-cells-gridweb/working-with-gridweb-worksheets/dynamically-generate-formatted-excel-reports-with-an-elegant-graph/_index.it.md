---
title: Genera dinamicamente report Excel formattati con un grafico elegante
type: docs
weight: 130
url: /it/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

Questo documento è progettato per fornire le informazioni necessarie su come estrarre i dati da alcune fonti di dati in una splendida griglia come controllo, incollare un grafico al suo interno ed esportare il rapporto con il grafico in MS Excel per effettuare analisi, confronti e stampa.

{{% /alert %}} 
## **Panoramica**
Esistono alcuni scenari Web che richiedono sia Reporting che Presentazioni, una combinazione di parti o oggetti che possono funzionare bene insieme. L'articolo spiega quanto sia facile progettare e generare dinamicamente eleganti report Excel in modo WYSIWYG. Esporta i dati da un file XML (puoi anche utilizzare altre fonti di dati) al controllo Aspose.Cells.GridWeb che ti fornisce l'ambiente reale che ti consente di applicare un formato ricco e accattivante ai dati e calcolare i risultati delle formule come MS Excel. Genera anche un grafico sofisticato basato sui dati di origine del foglio di lavoro utilizzando[Aspose.Cells](https://products.aspose.com/cells/) componente e incolla l'immagine del grafico nel report sulle vendite. Infine, il report excel con il grafico allegato viene salvato su disco utilizzando il componente Aspose.Cells.

Questo articolo include il codice sorgente e il progetto demo completo per tale funzionalità.

Consente agli utenti con una percezione dettagliata su come creare un report aziendale di inserire i dati in un foglio di lavoro della griglia e applicare una formattazione alle celle nelle righe e nelle colonne, incorporare un grafico basato sull'intervallo di dati di origine prima di salvare il rapporto excel sul disco.
## **I componenti Aspose**
 Ne uso tre di[Aspose](http://www.aspose.com/) i componenti di per eseguire l'attività con facilità.[Aspose](http://www.aspose.com/) , The .NET e Java Component Publisher, fornisce una varietà di componenti ricchi di funzionalità.[Aspose](http://www.aspose.com/) fornisce una grande linea di componenti .NET e Java. Scelti da migliaia di clienti in tutto il mondo, i prodotti includono Componenti per formati di file, Prodotti per la creazione di report, Componenti visivi e Componenti di utilità che consentono di aprire, modificare, generare, salvare, unire, convertire ecc. Documenti in vari formati tra cui DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, delimitato da tabulazioni, CSV, PPT, SWF, EMF, WMF, MPX, MPD e altri formati.

Colgo l'occasione per presentarvi tre di questi componenti che sono stati utilizzati in questa ricerca.
## **Aspose.Cells Controlli di rete**
 Aspose.Cells Grid Controls è una soluzione totale per la rete. Aspose.Cells Grid Controls viene fornito con due diversi componenti GUI .NET (Aspose.Cells.GridDesktop e Aspose.Cells.GridWeb): uno per supportare le applicazioni desktop e l'altro per supportare le applicazioni web. Entrambe le versioni sono ugualmente abbinate per rendere l'implementazione in entrambe le piattaforme un gioco da ragazzi. Aspose.Cells.GridWeb offre la possibilità di importare ed esportare in fogli di calcolo Excel. Quindi chiunque abbia familiarità con Excel (anche gli utenti finali) può progettare l'aspetto di una griglia. Aspose.Cells.GridWeb offre anche un API facile da usare e ricco di funzionalità che fornisce agli sviluppatori il controllo completo sull'aspetto, la sensazione e il comportamento della loro griglia. Per saperne di più sul prodotto, le sue caratteristiche e per una guida per i programmatori, consultare il riepilogo dell'elenco delle funzionalità, Aspose.Cells. Documentazione GridWeb e funzionalità online[Demo](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**è un componente di reporting del foglio di calcolo Excel che consente di leggere e scrivere fogli di calcolo Excel senza utilizzare Microsoft Excel da installare sul lato client o server.**Aspose.Cells** è un componente ricco di funzionalità che offre molto di più della semplice esportazione di dati di base. Con**Aspose.Cells** gli sviluppatori possono esportare dati, formattare fogli di calcolo in ogni dettaglio e ad ogni livello, importare immagini, importare grafici, creare grafici, manipolare grafici, eseguire lo streaming di dati Excel, salvare in vari formati tra cui XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) integrato) e molti altri.**Aspose.Cells** offre un facile da usare, ricco di funzionalità**API** per i programmatori. Ha un enorme elenco di funzionalità. Per saperne di più sul prodotto, le sue caratteristiche e per una guida del programmatore, consulta il sommario di**Elenco caratteristiche**, **Aspose.Cells Documentazione** e demo in primo piano online. Potresti[Scarica](https://downloads.aspose.com/cells) la sua versione di valutazione gratuitamente.
## **Progettare l'interfaccia**
Iniziamo a creare una nuova applicazione Web Asp.Net in Visual Studio.Net.

 io**Aggiungi riferimento**ai tre componenti ieAspose.Cells.GridWeb.dll, Aspose.Chart.dll e Aspose.Cells.dll al progetto prima. Metto alcuni controlli sulla pagina e ne imposto le proprietà, ad esempio un elenco a discesa, un pulsante di comando e un'etichetta. poi posto**Aspose.Cells.GridWeb****controllo**(**GrigliaWeb**) ad esso dalla casella degli strumenti, poiché dopo aver aggiunto i riferimenti ai tre componenti, the**GrigliaWeb**il controllo è apparso sulla casella degli strumenti. Gli altri due componenti (**Aspose.Chart**e**Aspose.Cells**) sono solo librerie, vengono solo referenziate al progetto.

Creo anche due cartelle "file" e "immagini", aggiungo rispettivamente "Products.xml" e "chart.gif" a queste cartelle. Il file xml è un file di origine dati da cui verranno estratti i dati per riempire il file**GrigliaWeb**foglio di lavoro. Il file immagine fornirà un'immagine per un pulsante personalizzato posizionato su**GrigliaWeb**controllo.

Ora creo un pulsante di comando personalizzato. Faccio semplicemente clic con il pulsante destro del mouse sul file**GrigliaWeb**control e fare clic sull'opzione "Pulsanti di comando personalizzati...".

Attiverà l'editor del pulsante di comando personalizzato, l'editor ti consente di creare pulsanti di immagine di comando personalizzati con la descrizione del comando allegata. Specifico i valori per alcune proprietà del pulsante, ad esempio Command (Name) ->"btnChart", ImageUrl -> indica il percorso del file immagine ("chart.gif") e ToolTip -> indica il suggerimento.

Quindi, il pulsante di comando personalizzato viene aggiunto come puoi vederlo (cerchiato di colore rosso) nella seguente schermata.

|![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


Infine, ho impostato alcuni attributi Font (in grassetto) per l'etichetta e il pulsante di comando. Regolo anche le dimensioni dei controlli per ottenere l'aspetto finale.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Recupero di dati da un file XML**
Di seguito è riportata la struttura del file XML utilizzata nel progetto.
### **Struttura del file XML**
**XML**

{{< highlight "csharp" >}}

 <?xml version="1.0" standalone="yes"?>

<SalesData>

  <Products>

    <ProductName>Data</ProductName>

    <QuantityPerUnit>Data</QuantityPerUnit>

    <CategoryName>Data</CategoryName>

    <UnitPrice>Data</UnitPrice>

    <Sale>Data</Sale>

  </Products>

 .........

</SalesData>



{{< /highlight >}}

{{< highlight "java" >}}

 private void Page_Load(object sender, System.EventArgs e)

{

if (!IsPostBack)

{

	// Uncomment the code below when you have purchased license

	// for Aspose.Cells.GridWeb, Aspose.Chart and Aspose.Cells. You need

	// to deploy the licenses in the same folder as your executable,

      // alternatively you can add the license files as an embedded

      // resource to your project.

	//

	// Set the license for Aspose.Cells.GridWeb

	// Aspose.Cells.GridWeb.License gridwebLicense = new

	// Aspose.Cells.GridWeb.License();

	// gridwebLicense.SetLicense("Aspose.Grid.lic");

	//

	// // Set the license for Aspose.Chart

	// Aspose.Chart.License chartLicense = new

	// Aspose.Chart.License();

	// chartLicense.SetLicense("Aspose.Chart.lic");

	//

	// // Set the license for Aspose.Cells

	// Aspose.Cells.License cellsLicense = new

	// Aspose.Cells.License();

	// cellsLicense.SetLicense("Aspose.Cells.lic");

	//Create a DataSet object.

	DataSet ds = new DataSet();

	//Get the Virtual Folder Path.

	string path = MapPath(".");

	//Reads XML data from xml file into DataSet object.

	ds.ReadXml(path + "\\file\\Products.xml");

	//Call the custom method to obtain distinct values from

	//CategoryName field and store data into an object array.

	object [] drs = GetDistinctValues(ds.Tables[0],"CategoryName");

	//Fill the drop down list with distinct field items.

	for(int i = 0;i<drs.Length;i++)

	{

		DropDownList1.Items.Add(drs[i].ToString());

	}

}

}

//This method is used to filter distinct values from CategoryName field in the datatable.

private object[]GetDistinctValues(DataTable dtable, string colName)

{

	// Create a Hashtable object.

	Hashtable hTable = new Hashtable();

	// Loop through the datatable rows and add distinct values to

	// Hashtable object minimizing the duplicates in the field.

	foreach (DataRow drow in dtable.Rows)

	if(!hTable.ContainsKey(drow[colName]))

	hTable.Add(drow[colName], string.Empty);

	// Create an object array based on the distinct key values of the Hashtable object.

	object[] objArray = new object[hTable.Keys.Count];

	// Copy the disctinct values to fill the array.

	hTable.Keys.CopyTo(objArray, 0);

	// Return the array object.

	return objArray;

}

{{< /highlight >}}
## **Compilazione del foglio di lavoro del controllo Aspose.Cells.GridWeb con i dati**
Io uso alcuni API del**GrigliaWeb**control per riempire un foglio di lavoro con i dati del file XML di origine. Scrivo il codice nel gestore di eventi click del pulsante di comando (con l'etichetta "Mostra report"). Il rapporto sui dati viene filtrato in base all'elemento selezionato dall'elenco a discesa.



{{< highlight "java" >}}

 //Clears datasheets of the GridWeb control.

GridWeb1.WebWorksheets.Clear();

//Create a DataSet object.

DataSet ds = new DataSet();

//Get the Virtual Folder path.

string path = MapPath(".");

//Reads XML data from xml file into DataSet object.

ds.ReadXml(path + "\\file\\Products.xml");

//Create a DataView based on the datatable.

DataView dv = new DataView(ds.Tables[0]);

//Filter data in the DataView object based on the selected drop down list item.

dv.RowFilter = "CategoryName ='" + DropDownList1.SelectedItem.Text + "'";

//Importing data from the filtered DataView object to create and

//fill "Products" Worksheet start from A4 cell.

GridWeb1.WebWorksheets.ImportDataView(dv, null, null,"Products",3,0);

{{< /highlight >}}
## **Formattazione dei dati nel Cells**
Per distinguere tra diversi tipi di informazioni su un foglio di lavoro, per la visualizzazione ottimale dei dati sul foglio di lavoro e per semplificare la scansione di un foglio di lavoro, si formatta il foglio di lavoro. UN**Formato**rappresenta uno stile ed è definito come un insieme di caratteristiche, come caratteri e dimensioni dei caratteri, formati numerici, bordi delle celle, ombreggiatura delle celle con un colore di sfondo a tinta unita o uno schema di colore specifico, rientro, allineamento e orientamento del testo nelle celle.

Unisco alcune righe di codice in più a quanto sopra. Inserisco il titolo/sottotitolo del rapporto, eseguo un po' di formattazione per il titolo, il sottotitolo e le celle di dettaglio. Applico anche la formattazione del numero ai due campi (imposta il formato del numero di valuta sui campi Prezzo unitario e Vendita) e aggiusto l'altezza/larghezza delle righe e delle colonne utilizzando**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 //Crea la cella del titolo (A1) nel foglio e applica le formattazioni.

//Le righe seguenti inseriscono un valore stringa nella cella, specifica

//dimensione del carattere, specifica le impostazioni di allineamento orizzontale e verticale, imposta

//colori di primo piano e di sfondo e unisci celle (A1:E2).

Foglio WebWorksheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Vendite prodotti per categoria");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sheet.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

sheet.Cells["A1"].Style.ForeColor = Color.Blue;

foglio.Cells.Merge(0, 0, 2, 5);

//Crea la cella del sottotitolo (A3) nel foglio e applica le formattazioni.

//Le righe seguenti inseriscono un valore stringa nella cella, specifica

//dimensione del carattere con attributi, specifica l'allineamento orizzontale e verticale

//impostazioni, imposta i colori di primo piano e di sfondo e unisci le celle

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sheet.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

sheet.Cells["A3"].Style.ForeColor = Color.Yellow;

foglio.Cells.Merge(2, 0, 1, 5);

//Ottiene gli ultimi indici di riga e colonna (che contengono dati).

int totalrow = sheet.Cells.MaxRow +1;

int totalcol = foglio.Cells.MaxColumn;

//Prendi il foglio Cells collezioni

celle WebCells = foglio.Cells;

//Definisci l'oggetto Cell.

cella WebCell;

//Scorri i dati nel foglio e formatta due campi con

//Stile del numero di valuta.

per (int i = 4;i<=totalrow;i++)

{

	//Format the Sale Column.

	cell = cells[i,totalcol];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

	//Format the UnitPrice Column.

	cell = cells[i,totalcol-1];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

}

//Insert the Total row with data, formula and formatting style.

//It will calculate the total Sales of a Category.

cells[totalrow,0].PutValue( DropDownList1.SelectedItem.Text + " Total" );

cells[totalrow,0].Style.Font.Bold = true;

cells[totalrow,totalcol].Formula = "=SUM(E5:E" + totalrow.ToString() + ")";

cells[totalrow,totalcol].Style.Font.Bold = true;

//Specify some Row and Column formattings. It will set row height

//and column width accordingly.

cells.SetRowHeight(2, new Unit("17pt"));

cells.SetColumnWidth(0, new Unit("157pt"));

cells.SetColumnWidth(1, new Unit("106pt"));

cells.SetColumnWidth(2, new Unit("87pt"));

cells.SetColumnWidth(3, new Unit("56pt"));

cells.SetColumnWidth(4, new Unit("50pt"));



{{< /highlight >}}
## **Produzione del report formattato (file .XLS) con Graph utilizzando il componente Aspose.Cells**
Ora scriverò del codice per salvare il rapporto formattato con il grafico su disco. utilizzo**GrigliaWeb** 'S**Salva**pulsante, Il**GrigliaWeb** 'S**SalvaComando**L'evento viene attivato quando fai clic sul pulsante Salva, quindi lo gestirò io. Ecco, io uso**Aspose.Cells**componente per esportare il report formattato in MS Excel, generare il grafico e incorporarlo nel file excel di output. Non ho inserito l'immagine del grafico (creato da**Aspose.Chart**componente) piuttosto creare il grafico simile utilizzando il API di**Aspose.Cells**in modo da poter modificare il grafico in MS Excel per le tue necessità.





{{< highlight "java" >}}

 //This GridWeb control event is fired when you click on the "Save" button

//of the control. After Clicking this button "File Download" dialog is

//displayed and you may open into MS Excel / save the output excel file //with graph to disk.

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

	//Create MemoryStream object.

	System.IO.MemoryStream ms = new System.IO.MemoryStream();

	//Save the GridWeb's Report to the stream.

	this.GridWeb1.WebWorksheets.SaveToExcelFile(ms);

	//Create a new Workbook.

	Workbook workbook = new Workbook();

	//Open the stream into the Workbook.

	workbook.Open(ms);

	//Call the custom method which creates Chart.

	Workbook book = CellsChart(workbook);

	//Save the excel file displaying "File Download" dialog box.

	book.Save(ms, FileFormatType.Default);

	this.Response.ContentType = "application/vnd.ms-excel";

	this.Response.AddHeader("content-disposition", "attachment; filename=Export.xls");

	this.Response.BinaryWrite(ms.ToArray());

}

//This custom method is used to create the Chart based on the data source

//range in the GridWeb control. In this method we will use Aspose.Cells

//APIs to create the graph which will be saved later into the output //excel file.

private Workbook CellsChart(Workbook workbook)

{

	//Get the first Worksheet.

	Aspose.Cells.Worksheet sheet = workbook.Worksheets[0];

	//Get the Cells collection in the sheet.

	Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

	//Get the last row index.

	int maxrow = sheet.Cells.MaxDataRow;

	//Unmerge the cells.

	sheet.Cells.UnMerge(maxrow,0,15,10);

	int chartIndex = 0;

	//Add a new Chart into the sheet's Chart Collection.

chartIndex = sheet.Charts.Add(Aspose.Cells.ChartType.Pie,maxrow,0,maxrow+28,5);

	//Get the Chart object.

	Aspose.Cells.Chart chart = sheet.Charts[chartIndex];

	//Set the Chart Area.

	Aspose.Cells.ChartArea chartarea = chart.ChartArea;

	chartarea.Area.Formatting = FormattingType.Custom;

	chartarea.Border.IsVisible = false;

		chartarea.Area.FillFormat.SetTwoColorGradient(Color.PowderBlue, Color.LightSkyBlue, GradientStyleType.FromCenter,1);

	//Set some properties of Chart Plot Area.

	chart.PlotArea.Area.Formatting = FormattingType.None;

	chart.PlotArea.Border.IsVisible = false;

	//Set properties of Chart Title.

	chart.Title.Text = DropDownList1.SelectedItem.Text + " Sales";

	chart.Title.TextFont.Size = 20;

	//Set properties of NSeries

	int lastdatarow = maxrow-1;

	chart.NSeries.Add("E5:E" + lastdatarow.ToString(), true);

	chart.NSeries.CategoryData = "A5:A" + lastdatarow.ToString();

	//Set the Data Labels in the chart

	Aspose.Cells.DataLabels datalabels;

	for ( int i = 0; i < chart.NSeries.Count ;i ++ )

	{

		datalabels = chart.NSeries[i].DataLabels;

		datalabels.Postion = Aspose.Cells.LabelPositionType.Center;

		datalabels.IsPercentageShown = true;

	}

	//Set the Legend settings.

	Aspose.Cells.Legend legend = chart.Legend;

	legend.Position = Aspose.Cells.LegendPositionType.Bottom;

	legend.Height = 85;

	legend.Width = 330;

	legend.AutoScaleFont = true;

	legend.Border.Color = Color.Blue;

	legend.Area.Formatting = FormattingType.Custom;

	FillFormat fillformat = legend.Area.FillFormat;

	legend.Area.Formatting = FormattingType.None;

	legend.Border.IsVisible = false;

	//Autofit the first column.

	sheet.AutoFitColumn(0);

	//Return the Workbook.

	return workbook;

}



{{< /highlight >}}
## **Esecuzione dell'applicazione**
Ora eseguo l'applicazione. L'elenco a discesa è riempito con le categorie distinte.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Seleziono una categoria in base alla quale voglio mostrare il rapporto sulle vendite e faccio clic sul pulsante "Mostra rapporto".

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Quindi, il rapporto viene mostrato nel file**GrigliaWeb**in base alla categoria selezionata. Il report è formattato per impostazione predefinita in base al codice (scritto in precedenza).

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Se vuoi formattare i dati in alcune celle in modo WYSIWYG, puoi farlo abbastanza facilmente.**Aspose.Cells.GridWeb**mette a disposizione**Formato Cells**editor, seleziona la cella o le celle desiderate e fai clic con il pulsante destro del mouse su di essa, fai clic sull'opzione "Formato Cell…".

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Viene visualizzata la finestra di dialogo Formato Cell.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Specifico alcuni attributi Font e faccio clic su OK.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

E ottieni il risultato.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Oltre alla formattazione delle celle, puoi anche modificare i valori delle celle. Fare doppio clic sulle celle desiderate e modificare il valore.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Per inviare il risultato della modifica e ricalcolare tutta la formula, faccio clic sul relativo pulsante (cerchiato di colore rosso) per aggiornare il rapporto.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Ora creerò il grafico e lo incollerò nel controllo. Faccio clic sul pulsante di comando personalizzato (cerchiato di colore rosso) per creare il grafico a torta basato sull'intervallo di dati.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Infine, esporterò questo rapporto di dati con il grafico in MS Excel. clicco il**Salva**pulsante (cerchiato di colore rosso). Cliccando sul**Salva**verrà visualizzato il pulsante**Download file**dialogo, puoi farlo**Aprire**il report risultante (file excel di output con grafico) in MS Excel o salvarlo sul disco.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Quando faccio clic sul pulsante Apri (finestra di dialogo Download file), il rapporto Excel con il grafico viene esportato in MS Excel. Viene visualizzata la parte superiore del report.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Viene mostrata la parte inferiore del report Excel.

![cose da fare:immagine_alt_testo](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
