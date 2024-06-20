---
title: Raggruppamento Dati
type: docs
weight: 10
url: /it/net/grouping-data/
---

In alcuni report Excel potrebbe essere necessario suddividere i dati in gruppi per renderli più facili da leggere e analizzare. Uno dei principali scopi per suddividere i dati in gruppi è eseguire calcoli (eseguire operazioni di riepilogo) su ciascun gruppo di record

I marcatori intelligenti di Aspose.Cells ti permettono di raggruppare i tuoi dati per campo(i) e inserire righe di riepilogo tra i set di dati o gruppi di dati. Ad esempio, se raggruppi i dati per Customer.CustomerID, puoi aggiungere un record di riepilogo ogni volta che cambia il gruppo.

Gli esempi di codice che seguono mostrano come raggruppare i dati in un report Excel utilizzando i marcatori intelligenti.
## **Parametri**
Di seguito sono riportati alcuni dei parametri di smart marker utilizzati per raggruppare i dati.
**group:normal/merge/repeat**

Supportiamo tre tipi di gruppo tra cui puoi scegliere.

- normale - Il valore del campo/i di raggruppamento non viene ripetuto per i record corrispondenti nella colonna; invece viene stampato una volta per ogni gruppo di dati.
- unisci - Lo stesso comportamento del parametro normale, eccetto che unisce le celle nel campo/i di raggruppamento per ogni set di gruppo.
- ripeti - Il valore del campo/i di raggruppamento viene ripetuto per i record corrispondenti.

Se hai più parametri, separali con virgole, ma senza spazi: parametroA, parametroB, parametroC
### **Esempio**
Questo esempio mostra alcuni dei parametri di raggruppamento in azione. Utilizza il database Microsoft Access Northwind.mdb ed estrae i dati dalla tabella chiamata "Dettagli ordine". Creiamo un file designer chiamato SmartMarker_Designer.xls in Microsoft Excel e inseriamo smart marker in varie celle nei fogli di lavoro. I marker vengono elaborati per riempire i fogli di lavoro. I dati sono collocati e organizzati da un campo di raggruppamento.

Il file designer ha due fogli di lavoro. Nel primo mettiamo smart marker con parametri di raggruppamento come mostrato nello screenshot qui sotto. Sono collocati tre smart marker (con parametri di raggruppamento):
&=Order Details.OrderID(group:merge,skip:1),
&=Dettagli dell'ordine.Quantità(subtotale9:Dettagli dell'ordine.IDOrdine), e
&= I dettagli dell' ordine. Prezzo unitario (subtotal9: ID ordine) vanno rispettivamente in A5, B5 e C5.

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Grouping Data OLE DB.xlsx";

//Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=~\\..\\..\\..\\Data\\Northwind.mdb");

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

wd.Workbook = new Workbook(FileName);

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save(FileName);

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
