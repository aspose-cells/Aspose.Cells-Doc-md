---
title: Modifiche all API pubblica in Aspose.Cells 8.8.3
type: docs
weight: 300
url: /it/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.8.2 alla 8.8.3 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per i Controlli ActiveX**
Aspose.Cells for Java 8.8.3 ha esposto il metodo addActiveXControl che permette di aggiungere un controllo ActiveX alla ShapeCollection. Il suddetto metodo richiede 7 parametri per specificare il tipo di controllo, la posizione in cui posizionare il controllo e le dimensioni del controllo. Il tipo può essere specificato utilizzando l'enumerazione ControlType con i seguenti possibili valori.

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Aggiunta di controlli ActiveX al foglio di lavoro](/cells/it/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Aggiunto metodo LoadOptions.setPaperSize**
Aspose.Cells for Java 8.8.3 consente di impostare la dimensione predefinita della carta da stampa dalle impostazioni predefinite della stampante durante l'utilizzo del nuovo metodo esposto LoadOptions.setPaperSize come dimostrato di seguito. Si prega di notare che il parametro di input al suddetto metodo è il valore dall'enumerazione PaperSizeType contenente le dimensioni della carta predefinite.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Caricare fogli di calcolo con dimensioni carta specificate](/cells/it/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Aggiunto metodo Cell.getCharacters(flag)**
Le API di Aspose.Cells permettono di ottenere gli oggetti caratteri sotto forma di array di FontSetting utilizzando il metodo Cell.getCharacters. Con questa versione, la API Aspose.Cells for Java ha esposto una versione sovraccaricata del Cell.getCharacters che potrebbe accettare Boolean come parametro, indicando se lo stile tabella deve essere applicato alla cella se la cella fa parte di un ListObject.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **Aggiunta la Proprietà OleObject.AutoLoad**
Aspose.Cells for Java 8.8.3 ha esposto la proprietà OleObject.AutoLoad che consente di aggiornare l'immagine dell'OleObject se i contenuti/dati dell'oggetto sottostante sono stati modificati. La suddetta proprietà, quando impostata su true, obbliga l'applicazione Excel ad aggiornare l'immagine dell'OleObject al caricamento del foglio di calcolo risultante.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Aggiornare automaticamente gli OleObjects](/cells/it/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **Aggiunta la Proprietà HTMLLoadOptions.SupportDivTag**
Aspose.Cells for Java 8.8.3 ha esposto la proprietà HTMLLoadOptions.SupportDivTag che consente di analizzare i tag DIV incorporati nei tag TD durante il caricamento di file/estratti HTML nell'oggetto modello Aspose.Cells. La proprietà di tipo Boolean ha il valore predefinito di false.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Supporto ai tag DIV interni durante il caricamento di HTML](/cells/it/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Aggiunta la Proprietà HtmlSaveOptions.ExportGridLines**
Aspose.Cells for Java 8.8.3 ha esposto la proprietà HtmlSaveOptions.ExportGridLines che consente di visualizzare le linee della griglia durante l'esportazione del foglio di calcolo in formato HTML. La proprietà di tipo Boolean ha il valore predefinito di false, tuttavia, quando impostata su true, la API visualizza le linee della griglia per l'intervallo dati disponibile nel formato HTML.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Rendere le linee della griglia in HTML](/cells/it/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Aggiunta la Proprietà ListObject.Comment**
Le API di Aspose.Cells ora consentono di ottenere e impostare i commenti per un'istanza di ListObject. Per fornire la suddetta funzionalità, le API di Aspose.Cells hanno esposto la proprietà ListObject.Comment.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Aggiunta di commenti per ListObjects](/cells/it/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **API rimosse**
### **Rimosso il metodo Workbook.decrypt**
La suddetta proprietà è stata contrassegnata come obsoleta qualche tempo fa. Questa versione l'ha completamente rimossa dall'API pubblica. Si consiglia di impostare la proprietà WorkbookSettings.Password su null per raggiungere lo stesso obiettivo.
{{< app/cells/assistant language="java" >}}
