---
title: Pubblico API Modifiche Aspose.Cells 8.4.1
type: docs
weight: 140
url: /it/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.4.0 alla 8.4.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-1/) e[classi rimosse ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-1/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per modificare la connessione al database**
La classe Aspose.Cells.ExternalConnections.ExternalConnection conteneva già il metodo e le proprietà che potevano essere utilizzate per ispezionare i dettagli della connessione al database archiviati in un foglio di calcolo. La maggior parte delle proprietà associate alla classe Aspose.Cells.ExternalConnections.ExternalConnection erano di sola lettura fino al rilascio di Aspose.Cells for .NET 8.4.1. Con questa versione, lo API ha fornito il supporto per manipolare anche le impostazioni di connessione al database.

Il frammento di codice seguente mostra come modificare dinamicamente le impostazioni di connessione al database.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



Di seguito sono riportate alcune delle proprietà più importanti esposte dalla classe {Aspose.Cells.ExternalConnections.ExternalConnection}}.

|**Nome della proprietà**|**Descrizione**|
|:- |:- |
|BackgroundRefresh|Indica se la connessione può essere aggiornata in background (in modo asincrono).<br> true se l'utilizzo preferito della connessione consiste nell'aggiornare in modo asincrono in background;<br>false se l'utilizzo preferito della connessione consiste nell'aggiornare in modo sincrono in primo piano.|
|Descrizione connessione|Specifica la descrizione utente per questa connessione|
|ID connessione|Specifica l'identificatore univoco di questa connessione.|
|Credenziali|Specifica il metodo di autenticazione da utilizzare quando si stabilisce (o si ristabilisce) la connessione.|
|È eliminato|Indica se la connessione alla cartella di lavoro associata è stata eliminata. vero se il<br>la connessione è stata cancellata; altrimenti, falso.|
|È nuovo| True se la connessione non è stata aggiornata per la prima volta; altrimenti, falso. Questo<br>state può verificarsi quando l'utente salva il file prima che una query abbia finito di restituire.|
|KeepAlive|Vero quando l'applicazione del foglio di calcolo deve sforzarsi di mantenere la connessione<br> aprire. Se falso, l'applicazione dovrebbe chiudere la connessione dopo aver recuperato il file<br>informazione.|
|Nome|Specifica il nome della connessione. Ogni connessione deve avere un nome univoco.|
|OdcFile| Specifica il percorso completo del file di connessione esterno da cui proveniva questa connessione<br> creato. Se una connessione non riesce durante un tentativo di aggiornamento dei dati e reconnectionMethod=1,<br> quindi l'applicazione del foglio di calcolo riproverà utilizzando le informazioni dal file di connessione esterno<br>invece dell'oggetto connessione incorporato nella cartella di lavoro.|
|Usa solo il file di connessione| Indica se l'applicazione per fogli di calcolo deve utilizzare sempre e solo il file<br> informazioni sulla connessione nel file di connessione esterno indicato dall'attributo odcFile<br> quando la connessione viene aggiornata. Se falso, l'applicazione del foglio di calcolo<br>deve seguire la procedura indicata dall'attributo reconnectionMethod|
|Parametri|Ottiene ConnectionParameterCollection per una query ODBC o Web.|
|Metodo di riconnessione|Specificare il tipo di metodo di riconnessione|
|RefreshInternal|Specifica il numero di minuti tra gli aggiornamenti automatici della connessione.|
|Aggiorna al caricamento|True se questa connessione deve essere aggiornata all'apertura del file; altrimenti, falso.|
|Salvare i dati|True se i dati esterni recuperati tramite la connessione per popolare una tabella devono essere salvati<br>con la cartella di lavoro; altrimenti, falso.|
|Salva la password|True se la password deve essere salvata come parte della stringa di connessione; altrimenti Falso.|
|File sorgente| Utilizzato quando l'origine dati esterna è basata su file. Quando una connessione a tali dati<br> source non riesce, l'applicazione del foglio di calcolo tenta di connettersi direttamente a questo file. Forse<br>espresso in URI o notazione del percorso file specifica del sistema.|
|SSOID|Identificatore per Single Sign On (SSO) utilizzato per l'autenticazione tra un intermediario<br>server spreadsheetML e l'origine dati esterna.|
|Tipo|Specifica il tipo di origine dati.|

### **Possibilità di formattare la sottostringa del testo di DataLabels**
Aspose.Cells for .NET 8.4.1 ha esposto il metodo DataLabels.Characters per recuperare un'istanza della classe FontSetting che corrisponde alla sottostringa di un ChartPoints.DataLabels. A sua volta, l'istanza della classe FontSetting può essere utilizzata per formattare la sottostringa di DataLabels con diverse impostazioni e colori dei caratteri.

Il frammento di codice seguente mostra come utilizzare il metodo DataLabels.Characters.

**C#**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Possibilità di impostare le dimensioni dell'immagine desiderate per l'esportazione di fogli di calcolo e grafici**
Aspose.Cells for .NET 8.4.1 ha esposto il metodo ImageOrPrintOptions.SetDesiredSize per impostare le dimensioni dell'immagine risultante durante l'esportazione di fogli di calcolo e grafici in immagini. Il metodo ImageOrPrintOptions.SetDesiredSize accetta due parametri di tipo intero, dove il primo è la larghezza desiderata e il secondo l'altezza desiderata.

Il seguente frammento di codice mostra come impostare le dimensioni desiderate durante l'esportazione del foglio di lavoro in PNG.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

La stessa proprietà può essere utilizzata anche per convertire i grafici in immagini.

{{% /alert %}} 


### **Rendering di commenti in PDF**
Con il rilascio di v8.4.1, Aspose.Cells API ha fornito la proprietà PageSetup.PrintComments e l'enumerazione PrintCommentsType per facilitare il rendering dei commenti durante la conversione dei fogli di calcolo in formato PDF. L'enumerazione PrintCommentsType ha le seguenti costanti.

- PrintCommentsType.PrintNoComments: i commenti non devono essere visualizzati.
- PrintCommentsType.PrintInPlace: i commenti devono essere visualizzati nel punto in cui sono inseriti.
- PrintCommentsType.PrintSheetEnd: i commenti devono essere visualizzati alla fine del foglio di lavoro.

Il codice di esempio seguente illustra l'utilizzo della proprietà PageSetup.PrintComments per eseguire il rendering dei commenti utilizzando tutti i possibili valori di enumerazione PrintCommentsType.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **Sposta i fogli di lavoro in Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop fornisce il metodo WorksheetCollection.MoveTo, che può essere utilizzato per spostare un foglio di lavoro nell'indice specificato. Il suddetto metodo prende come parametri gli indici (in base zero) del foglio di lavoro di origine e del foglio di lavoro di destinazione.

Il codice di esempio seguente illustra l'utilizzo della proprietà WorksheetCollection.MoveTo.

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Proprietà Workbook.IsLicensed aggiunta**
Aspose.Cells for .NET 8.4.1 ha esposto Workbook.IsLicensed che potrebbe essere di grande aiuto nel determinare se la licenza è stata caricata correttamente o meno. Se accedi a questa proprietà prima di impostare la licenza, restituirà false e viceversa, tuttavia, la licenza dovrebbe essere valida.

Il codice di esempio seguente illustra l'utilizzo della proprietà Workbook.IsLicensed.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **Aggiunta proprietà ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for .NET 8.4.1 ha esposto la proprietà SVGFitToViewPort per la classe ImageOrPrintOptions che può essere utilizzata per attivare l'attributo viewBox per il formato file SVG durante l'esportazione di fogli di calcolo o grafici in formato SVG. Il valore predefinito di questa proprietà è false pertanto l'XML di base per il file SVG generato senza impostare la suddetta proprietà non includerà l'attributo viewBox.

Il codice di esempio seguente illustra l'utilizzo della proprietà ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **API obsolete**
### **Metodo Workbook.ValidateFormula Obsoleto**
Utilizzare il metodo Cell.Formula per convalidare la formula.
