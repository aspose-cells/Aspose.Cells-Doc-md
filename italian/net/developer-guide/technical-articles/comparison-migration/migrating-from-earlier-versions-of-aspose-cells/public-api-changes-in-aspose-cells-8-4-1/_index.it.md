---
title: Modifiche all API pubblica in Aspose.Cells 8.4.1
type: docs
weight: 140
url: /it/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.4.0 alla 8.4.1 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-1/) e [classi rimosse ecc.](/cells/it/net/public-api-changes-in-aspose-cells-8-4-1/), ma anche una descrizione di eventuali modifiche nel comportamento di sottofondo in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per modificare la connessione al database**
La classe Aspose.Cells.ExternalConnections.ExternalConnection conteneva già il metodo e le proprietà che potevano essere utilizzate per ispezionare i dettagli della connessione al database memorizzati in un foglio di calcolo. La maggior parte delle proprietà associate alla classe Aspose.Cells.ExternalConnections.ExternalConnection erano di sola lettura fino al rilascio di Aspose.Cells for .NET 8.4.1. Con questo rilascio, l'API ha fornito il supporto per manipolare le impostazioni della connessione al database.

Il seguente frammento di codice mostra come modificare dinamicamente le impostazioni della connessione al database.

**C#**

{{< highlight csharp >}}

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



Ecco alcune delle proprietà più importanti esposte dalla classe Aspose.Cells.ExternalConnections.ExternalConnection.

|**Nome Proprietà**|**Descrizione**|
| :- | :- |
|BackgroundRefresh|Indica se la connessione può essere aggiornata in background (asincronamente). <br>true se l'uso preferito della connessione è aggiornare in modo asincrono in background; <br>false se l'uso preferito della connessione è aggiornare in modo sincrono in foreground.|
|ConnectionDescription|Specifica la descrizione utente per questa connessione|
|ConnectionId|Specifica l'identificatore univoco di questa connessione.|
|Credentials|Specifica il metodo di autenticazione da utilizzare durante l'instaurazione (o il ripristino) della connessione.|
|IsDeleted|Indica se la connessione del foglio di lavoro associata è stata eliminata. true se la connessione è stata eliminata; altrimenti, false.|
|IsNew|True se la connessione non è stata aggiornata per la prima volta; altrimenti, false. Questo <br>stato può verificarsi quando l'utente salva il file prima che una query abbia completato il ritorno.|
|KeepAlive|True quando l'applicazione del foglio di calcolo dovrebbe fare sforzi per mantenere aperta la connessione. Quando è false, l'applicazione dovrebbe chiudere la connessione dopo aver recuperato le informazioni.|
|Name|Specifica il nome della connessione. Ogni connessione deve avere un nome univoco.|
|OdcFile|Specifica il percorso completo del file di connessione esterna da cui è stata creata questa connessione. Se una connessione fallisce durante un tentativo di aggiornare i dati e reconnectionMethod=1, allora l'applicazione del foglio di calcolo proverà di nuovo utilizzando informazioni dal file di connessione esterna anziché l'oggetto connessione incorporato nel foglio di calcolo.|
|OnlyUseConnectionFile|Indica se l'applicazione del foglio di calcolo dovrebbe sempre e solo utilizzare le informazioni di connessione nel file di connessione esterno indicato dall'attributo odcFile quando la connessione viene aggiornata. Se false, allora l'applicazione del foglio di calcolo dovrebbe seguire la procedura indicata dall'attributo reconnectionMethod|
|Parametri|Ottiene ConnectionParameterCollection per una query ODBC o web.|
|reConnectionMethod|Specificare il tipo di reconnectionMethod|
|RefreshInternal| Specifica il numero di minuti tra gli aggiornamenti automatici della connessione.|
|AggiornaAllApertura|True se questa connessione deve essere aggiornata all'apertura del file; altrimenti, false.|
|SalvaDati|True se i dati esterni recuperati tramite la connessione per popolare una tabella devono essere salvati con il foglio di lavoro; altrimenti, false.|
|SalvaPassword|True se la password deve essere salvata come parte della stringa di connessione; altrimenti, False.|
|FileOrigine|Usato quando la fonte dati esterna è basata su file. Quando una connessione a tale origine dati fallisce, l'applicazione del foglio di calcolo tenta di connettersi direttamente a questo file. Può essere espressa in notazione URI o percorso file specifico del sistema.|
|SSOId| Identificatore per Single Sign On (SSO) utilizzato per l'autenticazione tra un server intermedio di spreadsheetML e la fonte dati esterna.|
|Tipo|Specifica il tipo di origine dati.|

### **Possibilità di formattare la sottostringa del testo delle etichette dati.**
Aspose.Cells for .NET 8.4.1 ha esposto il metodo DataLabels.Characters per recuperare un'istanza della classe FontSetting che corrisponde alla sottostringa delle DataLabels di un ChartPoints.DataLabels. A sua volta, l'istanza della classe FontSetting può essere utilizzata per formattare la sottostringa delle DataLabels con diverse impostazioni del carattere e del colore.

Il frammento di codice seguente mostra come utilizzare il metodo DataLabels.Characters.

**C#**

{{< highlight csharp >}}

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


### **Possibilità di impostare le dimensioni desiderate dell'immagine per l'esportazione di fogli di calcolo e grafici.**
Aspose.Cells for .NET 8.4.1 ha esposto il metodo ImageOrPrintOptions.SetDesiredSize per impostare le dimensioni dell'immagine risultante durante l'esportazione di fogli di calcolo e grafici in immagini. Il metodo ImageOrPrintOptions.SetDesiredSize accetta due parametri di tipo intero, dove il primo è la larghezza desiderata e il secondo è l'altezza desiderata.

Il frammento di codice seguente mostra come impostare le dimensioni desiderate durante l'esportazione del foglio di lavoro in PNG.

**C#**

{{< highlight csharp >}}

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


### **Rendering dei commenti in formato PDF**
Con il rilascio della v8.4.1, l'API di Aspose.Cells ha fornito la proprietà PageSetup.PrintComments e l'enumerazione PrintCommentsType per facilitare il rendering dei commenti durante la conversione dei fogli di calcolo nel formato PDF. L'enumerazione PrintCommentsType ha le seguenti costanti.

- PrintCommentsType.PrintNoComments: I commenti non devono essere resi.
- PrintCommentsType.PrintInPlace: I commenti devono essere resi sul posto.
- PrintCommentsType.PrintSheetEnd: I commenti devono essere resi alla fine del foglio di lavoro.

Il seguente codice di esempio dimostra l'uso della proprietà PageSetup.PrintComments per rendere i commenti utilizzando tutti i possibili valori di enumerazione PrintCommentsType.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells.GridDesktop fornisce il metodo WorksheetCollection.MoveTo, che può essere utilizzato per spostare un foglio di lavoro all'indice specificato. Il suddetto metodo prende gli indici (con base zero) del foglio di lavoro di origine e del foglio di lavoro di destinazione come parametri.

Il seguente codice di esempio mostra l'uso della proprietà WorksheetCollection.MoveTo.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Aggiunta della proprietà Workbook.IsLicensed**
Aspose.Cells for .NET 8.4.1 ha esposto Workbook.IsLicensed che potrebbe essere di grande aiuto nel determinare se la licenza è stata caricata con successo o meno. Se si accede a questa proprietà prima di impostare la licenza, restituirà falso e viceversa, tuttavia, la licenza dovrebbe essere valida.

Il seguente codice di esempio mostra l'uso della proprietà Workbook.IsLicensed.

**C#**

{{< highlight csharp >}}

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


### **Aggiunta della proprietà ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for .NET 8.4.1 ha esposto la proprietà SVGFitToViewPort per la classe ImageOrPrintOptions che può essere utilizzata per attivare l'attributo viewBox per il formato file SVG durante l'esportazione di fogli di calcolo o grafici nel formato SVG. Il valore predefinito di questa proprietà è falso pertanto il XML di base per il file SVG generato senza impostare la suddetta proprietà non includerà l'attributo viewBox.

Il seguente codice di esempio mostra l'uso della proprietà ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight csharp >}}

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
### **Workbook.ValidateFormula Method obsoleto**
Usa il metodo Cell.Formula per convalidare la formula.
{{< app/cells/assistant language="csharp" >}}
