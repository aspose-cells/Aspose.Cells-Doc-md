---
title: Raggruppamento dati in Aspose.Cells
type: docs
weight: 10
url: /it/net/grouping-data-in-aspose-cells/
---
In alcuni report di Excel potrebbe essere necessario suddividere i dati in gruppi per facilitarne la lettura e l'analisi. Uno degli scopi principali per suddividere i dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ogni gruppo di record.

I marcatori intelligenti Aspose.Cells consentono di raggruppare i dati per campo/i e posizionare righe di riepilogo tra set di dati o gruppi di dati. Ad esempio, se si raggruppano i dati per Customers.CustomerID, è possibile aggiungere un record di riepilogo ogni volta che il gruppo cambia.

frammenti di codice di esempio che seguono mostrano come raggruppare i dati in un report di Excel utilizzando marcatori intelligenti.
## **Parametri**
Di seguito sono riportati alcuni dei parametri degli indicatori intelligenti utilizzati per raggruppare i dati.
**gruppo:normale/unisci/ripeti**

Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- normale - Il valore del gruppo per campo/i non viene ripetuto per i record corrispondenti nella colonna; vengono invece stampati una volta per gruppo di dati.
- merge - Lo stesso comportamento del parametro normale, tranne per il fatto che unisce le celle nel campo/i raggruppa per ogni gruppo.
- ripetizione - Il valore del gruppo per campo/i viene ripetuto per i record corrispondenti.

Se hai più parametri, separali con una virgola, ma senza spazio: parametroA,parametroB,parametroC
### **Esempio**
Questo esempio mostra alcuni dei parametri di raggruppamento in azione. Utilizza il database Northwind.mdb Microsoft Access ed estrae i dati dalla tabella denominata "Dettagli ordine". Creiamo un file designer chiamato SmartMarker_Designer.xls in Microsoft Excel e inseriamo marcatori intelligenti in varie celle nei fogli di lavoro. I marcatori vengono elaborati per riempire i fogli di lavoro. I dati vengono inseriti e organizzati da un campo di gruppo.

Il file designer ha due fogli di lavoro. Nel primo inseriamo marcatori intelligenti con parametri di raggruppamento come mostrato nello screenshot qui sotto. Vengono posizionati tre marcatori intelligenti (con parametri di raggruppamento):
&=Dettagli ordine.ID ordine(gruppo:unione,salta:1),
&=Dettagli ordine.Quantità(subtotale9:Dettagli ordine.ID ordine) e
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) vanno rispettivamente in A5, B5 e C5.

{{< highlight "csharp" >}}

 //Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=Northwind.mdb");

//Open the connection object.

con.Open();

//Create a command object and specify the SQL query.

OleDbCommand cmd = new OleDbCommand("Select * from [Order Details]", con);

//Create a data adapter object.

OleDbDataAdapter da = new OleDbDataAdapter();

//Specify the command.

da.SelectCommand = cmd;

//Create a dataset object.

DataSet ds = new DataSet();

//Fill the dataset with the table records.

da.Fill(ds, "Order Details");

//Create a datatable with respect to dataset table.

DataTable dt = ds.Tables["Order Details"];

//Create WorkbookDesigner object.

WorkbookDesigner wd = new WorkbookDesigner();

//Open the template file (which contains smart markers).

wd.Workbook = new Workbook("SmartMarkerDesigner.xls");

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save("outSmartMarker_Designer.xls");

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
