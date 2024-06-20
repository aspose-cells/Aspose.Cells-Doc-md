---
title: Generare dinamicamente report Excel formattati con un grafico elegante
type: docs
weight: 130
url: /it/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb,generare report,report
description: Questo articolo introduce come generare report in GridWeb.
---

{{% alert color="primary" %}} 

Questo documento è progettato per fornire le informazioni necessarie su come possiamo estrarre dati da una fonte di dati per un controllo di tipo grid splendido, incollare un grafico e esportare il report con il grafico in MS Excel per effettuare analisi, confronti e stampe.

{{% /alert %}} 
## **Panoramica**
Ci sono determinati scenari web che richiedono sia Reporting che Presentations, una combinazione di parti o oggetti che possono funzionare bene insieme. L'articolo spiega quanto sia facile progettare e generare dinamicamente report Excel eleganti in modo WYSIWYG. Esporta dati da un file XML (È anche possibile utilizzare altre fonti di dati) al controllo Aspose.Cells.GridWeb che fornisce l'ambiente reale che consente di applicare un formato ricco e accattivante ai dati e calcolare risultati delle formule come MS Excel. Genera anche un grafico sofisticato basato sui dati di origine del foglio di lavoro utilizzando il componente [Aspose.Cells](https://products.aspose.com/cells/) e incolla l'immagine del grafico nel Sales Report. Infine, il report Excel con il grafico allegato viene salvato su disco utilizzando il componente Aspose.Cells.

Questo articolo include il codice sorgente e un progetto demo completamente attrezzato per tale funzionalità.

Consente agli utenti di avere una percezione dettagliata su come creare un report aziendale per inserire dati in un foglio del controllo e applicare alcune formattazioni alle celle nelle righe e colonne, incorpora un grafico basato sull'intervallo di dati di origine prima di salvare il report Excel su disco.
## **I componenti Aspose**
Utilizzo tre dei componenti di [Aspose](http://www.aspose.com/) per eseguire il compito con facilità. [Aspose](http://www.aspose.com/), il Publishere di componenti .NET e Java, fornisce una varietà di componenti ricchi di funzionalità. [Aspose](http://www.aspose.com/) fornisce una grande serie di componenti .NET e Java. Affidati da migliaia di clienti in tutto il mondo, i prodotti includono componenti di formato file, prodotti di reportistica, componenti visivi e componenti di utilità che consentono di aprire, modificare, generare, salvare, unire, convertire etc. documenti in vari formati inclusi DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, Delimitato da tabulazione, CSV, PPT, SWF, EMF,WMF, MPX, MPD e altri formati.

Approfitto di questa opportunità per presentarti tre di questi componenti che sono stati utilizzati in questa ricerca.
## **Controlli Griglia Aspose.Cells**
I controlli griglia Aspose.Cells sono una soluzione completa per le griglie. I controlli griglia Aspose.Cells vengono forniti con due diversi componenti GUI .NET (Aspose.Cells.GridDesktop e Aspose.Cells.GridWeb): uno per supportare le applicazioni desktop e l'altro per supportare le applicazioni web. Entrambe le versioni sono parimenti abbinate al fine di rendere l'implementazione in entrambe le piattaforme un gioco da ragazzi. Aspose.Cells.GridWeb fornisce la possibilità di importare e esportare i fogli di calcolo di Excel. Quindi chiunque sia familiare con Excel (anche gli utenti finali) può progettare l'aspetto di una griglia. Aspose.Cells.GridWeb offre anche un'API facile da usare e ricca di funzionalità che fornisce ai programmatori il controllo completo sull'aspetto, sull'aspetto e sul comportamento della propria griglia. Per saperne di più sul prodotto, sulle sue funzionalità e per una guida per programmatori, controllare il riepilogo delle funzionalità, la documentazione di Aspose.Cells.GridWeb e i [Demo](https://aspose.github.io/) online.
## **Aspose.Cells**
**Aspose.Cells** è un componente di reporting di fogli di calcolo Excel che ti consente di leggere e scrivere fogli di calcolo Excel senza utilizzare Microsoft Excel installato sul lato client o server. **Aspose.Cells** è un componente ricco di funzionalità che offre molto più dell'esportazione di base dei dati. Con **Aspose.Cells** gli sviluppatori possono esportare dati, formattare fogli di calcolo in ogni dettaglio e livello, importare immagini, importare grafici, creare grafici, manipolare grafici, trasmettere dati Excel, salvare in vari formati tra cui XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML (integrato con [Aspose.Pdf] (https://products.aspose.com/pdf/) e molti altri. **Aspose.Cells** offre un'**API** facile da usare e ricca di funzionalità per i programmatori. Ha un lungo elenco di funzionalità. Per saperne di più sul prodotto, sulle sue caratteristiche e per una guida per programmatori, controlla il riepilogo dell'elenco delle caratteristiche, la documentazione di **Aspose.Cells** e le Demo online. Puoi [scaricare] (https://downloads.aspose.com/cells) la sua versione di valutazione gratuitamente.
## **Progettare l'Interfaccia**
Iniziamo creando una nuova applicazione web Asp.Net in Visual Studio.Net.

**Aggiungo un riferimento** ai tre componenti ossia Aspose.Cells.GridWeb.dll, Aspose.Chart.dll e Aspose.Cells.dll al progetto per primo. Posiziono alcuni controlli sulla pagina e imposto le loro proprietà, ossia una lista a discesa, un pulsante di comando e un'etichetta. Poi inserisco il controllo **Aspose.Cells.GridWeb** dal toolbox, poiché dopo aver aggiunto i riferimenti ai tre componenti, il controllo **GridWeb** appare nel toolbox. Gli altri due componenti (**Aspose.Chart** e **Aspose.Cells**) sono solo librerie, vengono solo referenziati nel progetto.

Creo anche due cartelle "file" e "images", aggiungo "Products.xml" e "chart.gif" a queste cartelle rispettivamente. Il file xml è un file di origine dati da cui verranno estratti i dati per riempire il foglio di lavoro **GridWeb**. Il file immagine fornirà un'immagine per un pulsante personalizzato posto sul controllo **GridWeb**.

Creo ora un pulsante di comando personalizzato. Semplicemente faccio clic destro sul controllo **GridWeb** e seleziono l'opzione "Pulsanti di Comando Personalizzati...".

Ciò attiverà l'editor dei Pulsanti di Comando Personalizzati, l'editor consente di creare pulsanti immagine di comando personalizzati con suggerimento del tool. Specifico i valori per alcune proprietà del pulsante ad esempio, Comando (Nome) -> "btnChart", UrlImmagine -> dare il percorso del file immagine ("chart.gif") e Suggerimento -> dare il suggerimento del tool.

Così, il pulsante di comando personalizzato è aggiunto come puoi vedere (circondato dal colore rosso) nella seguente schermata.​​

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


Infine, imposto alcuni attributi del Font (grassetto) per l'etichetta e il pulsante di comando. Regolo anche le dimensioni dei controlli per ottenere l'aspetto finale.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Recupero dei Dati da un File XML**
Di seguito la struttura del file XML utilizzata nel progetto.
### **Struttura del File XML**
**XML**

{{< highlight csharp >}}

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

{{< highlight java >}}

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

private object[] GetDistinctValues(DataTable dtable, string colName)

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
## **Riempimento del Foglio di Lavoro del controllo Aspose.Cells.GridWeb con i Dati**
Utilizzo alcune API del controllo **GridWeb** per riempire un foglio di lavoro con dati provenienti dal file XML di origine. Scrivo del codice nell'evento di clic del pulsante di comando (etichettato "Mostra Report"). Il report dati viene filtrato in base all'elemento selezionato dalla lista a discesa.



{{< highlight java >}}

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
## **Formattazione dei Dati nelle Celle**
Per distinguere tra diversi tipi di informazioni in un foglio di lavoro, per la visualizzazione ottimale dei dati sul tuo foglio di lavoro e per rendere più facile la scansione di un foglio di lavoro, si formatta il foglio di lavoro. Un **Formato** rappresenta uno stile ed è definito come un insieme di caratteristiche, come caratteri e dimensioni dei caratteri, formati numerici, bordi delle celle, sfondo delle celle con colore di sfondo solido o un modello di colore specifico, rientro, allineamento e orientamento del testo nelle celle.

Aggiungo ulteriori righe di codice a quanto sopra. Inserisco il titolo / sottotitolo del report, faccio qualche formattazione ai titoli, sottotitoli e celle di dettaglio. Applico anche il formato numerico ai due campi (imposto il formato numerico della valuta ai campi PrezzoUnitario e Vendita) e regolo l'altezza/larghezza delle righe e delle colonne utilizzando l'API di **Aspose.Cells.GridWeb**.



{{< highlight java >}}

 //Create the title cell (A1) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size, specify horizontal and vertical align settings, set

//foreground and background colors and merge cells (A1:E2).

WebWorksheet sheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Product Sales By Category");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sheet.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

sheet.Cells["A1"].Style.ForeColor = Color.Blue;

sheet.Cells.Merge(0, 0, 2, 5);

//Create the subtitle cell (A3) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size with attributes, specify horizontal and vertical align

//settings, set foreground and background colors and merge cells

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sheet.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

sheet.Cells["A3"].Style.ForeColor = Color.Yellow;

sheet.Cells.Merge(2, 0, 1, 5);

//Obtain the last row and column (which contain data) indexes.

int totalrow = sheet.Cells.MaxRow +1;

int totalcol = sheet.Cells.MaxColumn;

//Get the sheet Cells collections

WebCells cells = sheet.Cells;

//Define the Cell object.

WebCell cell;

//Loop through the data in the sheet and format two fields with

//Currency number style.

for (int i = 4;i<=totalrow;i++)

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
## **Produzione del Report Formattato (.XLS File) con Grafico utilizzando il componente Aspose.Cells**
Ora, scriverò del codice per salvare il report formattato con grafico su disco. Utilizzo il pulsante **Salva** di **GridWeb**, l'evento **SaveCommand** di **GridWeb** viene attivato quando si fa clic sul pulsante Salva, quindi, lo gestirò. Qui, utilizzo il componente **Aspose.Cells** per esportare il report formattato in MS Excel, generare il grafico e incorporarlo nel file excel di output. Non ho inserito l'immagine del grafico (creata dal componente **Aspose.Chart**) ma ho creato un grafico simile utilizzando l'API di **Aspose.Cells**, in modo che tu possa modificare il grafico in MS Excel a seconda delle tue esigenze.





{{< highlight java >}}

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
## **Eseguire l'applicazione**
Ora, eseguo l'applicazione. L'elenco a discesa è riempito con le categorie distinte.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Seleziono una categoria per la quale desidero mostrare il report delle vendite e clicco sul pulsante "Mostra report".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Quindi, il report viene mostrato nella **GridWeb** in base alla categoria selezionata. Il report è formattato per impostazione predefinita in base al codice (scritto in precedenza).

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Se desideri formattare i dati in alcuni dei singoli in modo WYSIWYG, puoi farlo facilmente. **Aspose.Cells.GridWeb** fornisce un editor di **Format Cells**, seleziona la cellula (o le celle) desiderata(e) e fai clic con il pulsante destro del mouse, quindi seleziona l'opzione "Format Cell…".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Viene visualizzata la finestra di dialogo Formato cella.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Specifico alcuni attributi del carattere e faccio clic su OK.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

E ottengo il risultato.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Oltre alla formattazione delle celle, puoi anche modificare i valori delle celle. Fai doppio clic sulla cella (o le celle) desiderata(e) e modifica il valore.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Per inviare il risultato della modifica e ricalcolare tutte le formule, faccio clic sul pulsante correlato (cerchiato in rosso) per aggiornare il report.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Ora creerò il grafico e lo incollo nel controllo. Faccio clic sul pulsante di comando personalizzato (cerchiato in rosso) per creare il grafico a torta in base all'intervallo di dati.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Infine, esporterò questo report dei dati con il grafico su MS Excel. Faccio clic sul pulsante **Salva** (cerchiato in rosso). Facendo clic sul pulsante **Salva** verrà visualizzata la finestra di dialogo **Download file**, puoi sia **Aprire** il report risultante (file excel di output con grafico) in MS Excel che salvarlo su disco.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Quando faccio clic sul pulsante Apri (finestra di dialogo Download file), il report excel con il grafico viene esportato in MS Excel. Viene mostrata la parte superiore del report.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Viene mostrata la parte inferiore del report excel.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
