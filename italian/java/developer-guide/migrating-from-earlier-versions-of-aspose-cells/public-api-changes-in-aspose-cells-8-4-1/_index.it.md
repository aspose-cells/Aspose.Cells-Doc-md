---
title: Modifiche all API pubblica in Aspose.Cells 8.4.1
type: docs
weight: 150
url: /it/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche apportate all'API di Aspose.Cells dalla versione 8.4.0 alla 8.4.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, [classi aggiunte ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-1/) e [classi rimosse ecc.](/cells/it/java/public-api-changes-in-aspose-cells-8-4-1/), ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Meccanismo per modificare la connessione al database**
La classe com.aspose.cells.ExternalConnection conteneva già il metodo e le proprietà che potevano essere utilizzate per ispezionare i dettagli della connessione al database memorizzati in un foglio di calcolo. La maggior parte delle proprietà associate alla classe ExternalConnection erano di sola lettura fino al rilascio di Aspose.Cells for Java 8.4.1. Con questo aggiornamento, l'API ha fornito il supporto per manipolare le impostazioni della connessione al database.

Il seguente frammento di codice mostra come modificare dinamicamente le impostazioni della connessione al database.

**Java**

{{< highlight csharp >}}

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

Ecco alcune delle proprietà più importanti esposte dalla classe {ExternalConnection}.

|**Nome Proprietà** |**Descrizione** |
| :- | :- |
|BackgroundRefresh |Indica se la connessione può essere aggiornata in background (in modo asincrono). <br>true se l'uso preferito della connessione è quello di aggiornare in modo asincrono in background; <br>false se l'uso preferito della connessione è quello di aggiornare in modo sincrono in primo piano.
|ConnectionDescription |Specifica la descrizione dell'utente per questa connessione.
|ConnectionId |Specifica l'identificatore univoco di questa connessione.
|Credentials |Specifica il metodo di autenticazione da utilizzare durante l'instaurazione (o il ripristino) della connessione.
|IsDeleted |Indica se la connessione del workbook associata è stata eliminata. true se la<br>connessione è stata eliminata; altrimenti, false.
|IsNew |True se la connessione non è stata aggiornata per la prima volta; altrimenti, false. Questo <br>stato può verificarsi quando l'utente salva il file prima che una query abbia finito di restituire i dati.
|KeepAlive |True quando l'applicazione del foglio di calcolo dovrebbe fare sforzi per mantenere la connessione <br>aperta. Quando è false, l'applicazione dovrebbe chiudere la connessione dopo aver recuperato le <br>informazioni.
|Name |Specifica il nome della connessione. Ogni connessione deve avere un nome univoco.
|OdcFile |Specifica il percorso completo al file di connessione esterna da cui è stata <br>creata questa connessione. Se una connessione fallisce durante un tentativo di aggiornare i dati e il reconnectionMethod=1, <br>allora l'applicazione del foglio di calcolo tenterà di nuovo utilizzando le informazioni dal file di connessione esterna <br>invece dell'oggetto di connessione incorporato nel workbook.
|OnlyUseConnectionFile |Indica se l'applicazione del foglio di calcolo dovrebbe sempre e solo utilizzare le <br>informazioni di connessione nel file di connessione esterna indicato dall'attributo odcFile <br>quando la connessione viene aggiornata. Se false, allora l'applicazione del foglio di calcolo <br>dovrebbe seguire la procedura indicata dall'attributo reconnectionMethod.
|Parameters |Ottiene ConnectionParameterCollection per una query ODBC o web.
|ReConnectionMethod |Specifica il tipo di reconnectionMethod.
|RefreshInternal|Specifica il numero di minuti tra gli aggiornamenti automatici della connessione.
|RefreshOnLoad |True se questa connessione dovrebbe essere aggiornata all'apertura del file; altrimenti, false.
|SaveData |True se i dati esterni recuperati tramite la connessione per popolare una tabella devono essere salvati<br>con il workbook; altrimenti, false.
|SavePassword |True se la password deve essere salvata come parte della stringa di connessione; altrimenti, Falso.
|SourceFile |Utilizzato quando la sorgente dati esterna è basata su file. Quando una connessione a tale sorgente dati non riesce, l'applicazione foglio di calcolo tenta di connettersi direttamente a questo file. Può essere espressa in URI o notazione del percorso di file specifico del sistema.
|SSOId|Identificatore per Single Sign On (SSO) utilizzato per l'autenticazione tra un server intermedio di spreadsheetML e la sorgente dati esterna.
|Type |Specifica il tipo di sorgente dati.

### **Possibilità di formattare la sottostringa del testo delle etichette dati.**
Aspose.Cells for Java 8.4.1 ha esposto il metodo DataLabels.characters per recuperare un'istanza della classe FontSetting che corrisponde alla sottostringa di un ChartPoints.DataLabels. A sua volta, l'istanza della classe FontSetting può essere utilizzata per formattare la sottostringa dei DataLabels con diverse impostazioni del carattere e del colore.

Il seguente snippet di codice mostra come utilizzare il metodo DataLabels.characters.

**Java**

{{< highlight csharp >}}

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

### **Possibilità di impostare le dimensioni desiderate dell'immagine per l'esportazione di fogli di calcolo e grafici.**
Aspose.Cells for Java 8.4.1 ha esposto il metodo ImageOrPrintOptions.setDesiredSize per impostare le dimensioni dell'immagine risultante durante l'esportazione di fogli e grafici in immagini. Il metodo ImageOrPrintOptions.setDesiredSize accetta due parametri di tipo intero, dove il primo è la larghezza desiderata e il secondo è l'altezza desiderata.

Il frammento di codice seguente mostra come impostare le dimensioni desiderate durante l'esportazione del foglio di lavoro in PNG.

**Java**

{{< highlight csharp >}}

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

### **Rendering dei commenti in formato PDF**
Con il rilascio della v8.4.1, l'API di Aspose.Cells ha fornito la proprietà PageSetup.PrintComments e l'enumerazione PrintCommentsType per facilitare il rendering dei commenti durante la conversione dei fogli di calcolo nel formato PDF. L'enumerazione PrintCommentsType ha le seguenti costanti. 

- PrintCommentsType.PRINT_NO_COMMENTS: i commenti non devono essere resi.
- PrintCommentsType.PRINT_IN_PLACE: i commenti devono essere resi dove sono posizionati.
- PrintCommentsType.PRINT_SHEET_END: i commenti devono essere resi alla fine del foglio di lavoro.

Il seguente codice di esempio dimostra l'uso della proprietà PageSetup.PrintComments per rendere i commenti utilizzando tutti i possibili valori di enumerazione PrintCommentsType.

**Java**

{{< highlight csharp >}}

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

### **Aggiunta della proprietà Workbook.isLicensed**
Aspose.Cells for Java 8.4.1 ha esposto Workbook.isLicensed che potrebbe essere di grande aiuto nel determinare se la licenza è stata caricata correttamente o meno. Se si accede a questa proprietà prima di impostare la licenza, restituirà false e viceversa, tuttavia, la licenza dovrebbe essere valida.

Il seguente codice di esempio dimostra l'uso della proprietà Workbook.isLicensed.

**Java**

{{< highlight csharp >}}

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

### **Aggiunta della proprietà ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for Java 8.4.1 ha esposto la proprietà SVGFitToViewPort per la classe ImageOrPrintOptions che può essere utilizzata per attivare l'attributo viewBox per il formato file SVG durante l'esportazione di fogli e grafici in formato SVG. Il valore predefinito di questa proprietà è falso, quindi l'XML di base per il file SVG generato senza impostare la suddetta proprietà non includerà l'attributo viewBox.

Il seguente codice di esempio mostra l'uso della proprietà ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight csharp >}}

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
## **API deprecate**
### **Metodo Workbook.validateFormula obsolete**
Utilizzare la proprietà Cell.Formula per convalidare la formula.
{{< app/cells/assistant language="java" >}}
