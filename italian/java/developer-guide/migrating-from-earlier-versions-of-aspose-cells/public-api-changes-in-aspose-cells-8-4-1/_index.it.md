---
title: Pubblico API Modifiche Aspose.Cells 8.4.1
type: docs
weight: 150
url: /it/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.4.0 alla 8.4.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati,[classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-1/) e[classi rimosse ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-1/), ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per modificare la connessione al database**
La classe com.aspose.cells.ExternalConnection conteneva già il metodo e le proprietà che potevano essere utilizzate per ispezionare i dettagli della connessione al database archiviati in un foglio di calcolo. La maggior parte delle proprietà associate alla classe ExternalConnection erano di sola lettura fino al rilascio di Aspose.Cells for Java 8.4.1. Con questa versione, lo API ha fornito il supporto per manipolare anche le impostazioni di connessione al database.

Il frammento di codice seguente mostra come modificare dinamicamente le impostazioni di connessione al database.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

Ecco alcune delle proprietà più importanti esposte dalla classe {ExternalConnection}}.

|**Nome della proprietà** |**Descrizione** |
|:- |:- |
| BackgroundRefresh|Indica se la connessione può essere aggiornata in background (in modo asincrono).<br> true se l'utilizzo preferito della connessione consiste nell'aggiornare in modo asincrono in background;<br> false se l'utilizzo preferito della connessione consiste nell'aggiornare in modo sincrono in primo piano.|
| Descrizione connessione| Specifica la descrizione utente per questa connessione|
| ID connessione| Specifica l'identificatore univoco di questa connessione.|
| Credenziali| Specifica il metodo di autenticazione da utilizzare quando si stabilisce (o si ristabilisce) la connessione.|
| È eliminato|Indica se la connessione alla cartella di lavoro associata è stata eliminata. vero se il<br> la connessione è stata cancellata; altrimenti, falso.|
| È nuovo| True se la connessione non è stata aggiornata per la prima volta; altrimenti, falso. Questo<br> state può verificarsi quando l'utente salva il file prima che una query abbia finito di restituire.|
| KeepAlive|Vero quando l'applicazione del foglio di calcolo deve sforzarsi di mantenere la connessione<br> aprire. Se falso, l'applicazione dovrebbe chiudere la connessione dopo aver recuperato il file<br> informazione.|
| Nome| Specifica il nome della connessione. Ogni connessione deve avere un nome univoco.|
| OdcFile| Specifica il percorso completo del file di connessione esterno da cui proveniva questa connessione<br> creato. Se una connessione non riesce durante un tentativo di aggiornamento dei dati e reconnectionMethod=1,<br> quindi l'applicazione del foglio di calcolo riproverà utilizzando le informazioni dal file di connessione esterno<br> invece dell'oggetto connessione incorporato nella cartella di lavoro.|
| Usa solo il file di connessione| Indica se l'applicazione per fogli di calcolo deve utilizzare sempre e solo il file<br> informazioni sulla connessione nel file di connessione esterno indicato dall'attributo odcFile<br> quando la connessione viene aggiornata. Se falso, l'applicazione del foglio di calcolo<br>deve seguire la procedura indicata dall'attributo reconnectionMethod|
| Parametri| Ottiene ConnectionParameterCollection per una query ODBC o Web.|
| Metodo di riconnessione| Specificare il tipo di metodo di riconnessione|
|RefreshInternal| Specifica il numero di minuti tra gli aggiornamenti automatici della connessione.|
| Aggiorna al caricamento| True se questa connessione deve essere aggiornata all'apertura del file; altrimenti, falso.|
| Salvare i dati|True se i dati esterni recuperati tramite la connessione per popolare una tabella devono essere salvati<br> con la cartella di lavoro; altrimenti, falso.|
| Salva la password| True se la password deve essere salvata come parte della stringa di connessione; altrimenti Falso.|
| File sorgente| Utilizzato quando l'origine dati esterna è basata su file. Quando una connessione a tali dati<br> source non riesce, l'applicazione del foglio di calcolo tenta di connettersi direttamente a questo file. Forse<br> espresso in URI o notazione del percorso file specifica del sistema.|
|SSOID|Identificatore per Single Sign On (SSO) utilizzato per l'autenticazione tra un intermediario<br> server spreadsheetML e l'origine dati esterna.|
| Tipo| Specifica il tipo di origine dati.|

### **Possibilità di formattare la sottostringa del testo di DataLabels**
Aspose.Cells for Java 8.4.1 ha esposto il metodo DataLabels.characters per recuperare un'istanza della classe FontSetting che corrisponde alla sottostringa di un ChartPoints.DataLabels. A sua volta, l'istanza della classe FontSetting può essere utilizzata per formattare la sottostringa di DataLabels con diverse impostazioni e colori dei caratteri.

Il frammento di codice seguente mostra come utilizzare il metodo DataLabels.characters.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Possibilità di impostare le dimensioni dell'immagine desiderate per l'esportazione di fogli di calcolo e grafici**
Aspose.Cells for Java 8.4.1 ha esposto il metodo ImageOrPrintOptions.setDesiredSize per impostare le dimensioni dell'immagine risultante durante l'esportazione di fogli di calcolo e grafici in immagini. Il metodo ImageOrPrintOptions.setDesiredSize accetta due parametri di tipo intero, dove il primo è la larghezza desiderata e il secondo l'altezza desiderata.

Il seguente frammento di codice mostra come impostare le dimensioni desiderate durante l'esportazione del foglio di lavoro in PNG.

**Java**

{{< highlight "csharp" >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Lo stesso metodo può essere utilizzato anche per convertire i grafici in immagini.

{{% /alert %}} 

### **Rendering di commenti in PDF**
 Con il rilascio di v8.4.1, Aspose.Cells API ha fornito la proprietà PageSetup.PrintComments e l'enumerazione PrintCommentsType per facilitare il rendering dei commenti durante la conversione dei fogli di calcolo in formato PDF. L'enumerazione PrintCommentsType ha le seguenti costanti.

- PrintCommentsType.PRINT_NO_COMMENTI: I commenti non devono essere resi.
- PrintCommentsType.PRINT_IN_LUOGO: i commenti devono essere resi dove sono inseriti.
- PrintCommentsType.PRINT_FOGLIO_FINE: i commenti devono essere resi alla fine del foglio di lavoro.

Il codice di esempio seguente illustra l'utilizzo della proprietà PageSetup.PrintComments per eseguire il rendering dei commenti utilizzando tutti i possibili valori di enumerazione PrintCommentsType.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **Aggiunta proprietà Workbook.isLicensed**
Aspose.Cells for Java 8.4.1 ha esposto Workbook.isLicensed che potrebbe essere di grande aiuto nel determinare se la licenza è stata caricata correttamente o meno. Se accedi a questa proprietà prima di impostare la licenza, restituirà false e viceversa, tuttavia, la licenza dovrebbe essere valida.

Il codice di esempio seguente illustra l'utilizzo della proprietà Workbook.isLicensed.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **Aggiunta proprietà ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for Java 8.4.1 ha esposto la proprietà SVGFitToViewPort per la classe ImageOrPrintOptions che può essere utilizzata per attivare l'attributo viewBox per il formato file SVG durante l'esportazione di fogli di calcolo o grafici in formato SVG. Il valore predefinito di questa proprietà è false pertanto l'XML di base per il file SVG generato senza impostare la suddetta proprietà non includerà l'attributo viewBox.

Il codice di esempio seguente illustra l'utilizzo della proprietà ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **API obsolete**
### **Metodo Workbook.validateFormula Obsoleto**
Utilizzare la proprietà Cell.Formula per convalidare la formula.
