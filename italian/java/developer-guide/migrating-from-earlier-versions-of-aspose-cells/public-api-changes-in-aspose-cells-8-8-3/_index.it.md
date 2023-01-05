---
title: Pubblico API Modifiche Aspose.Cells 8.8.3
type: docs
weight: 300
url: /it/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.8.2 alla 8.8.3 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per controlli ActiveX**
Aspose.Cells for Java 8.8.3 ha esposto il metodo addActiveXControl che permette di aggiungere un controllo ActiveX alla ShapeCollection. Il suddetto metodo richiede 7 parametri per specificare il tipo di controllo, la posizione in cui posizionare il controllo e la dimensione del controllo. Il tipo può essere specificato usando l'enumerazione ControlType con i seguenti valori possibili.

1. TipoControllo.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. TipoControllo.ETICHETTA
1. TipoControllo.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. TipoControllo.SPIN_BUTTON
1. TipoControllo.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Aggiunta di controlli ActiveX al foglio di lavoro](/cells/it/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
### **Aggiunto il metodo LoadOptions.setPaperSize**
Aspose.Cells for Java 8.8.3 consente di impostare il formato carta di stampa predefinito dall'impostazione della stampante predefinita mentre si utilizza il metodo LoadOptions.setPaperSize appena esposto come mostrato di seguito. Si noti che il parametro di input per il suddetto metodo è il valore dell'enumerazione PaperSizeType contenente i formati carta predefiniti.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Carica fogli di calcolo con il formato carta specificato](/cells/it/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Aggiunto il metodo Cell.getCharacters(flag).**
Le API Aspose.Cells consentono di ottenere gli oggetti caratteri sotto forma di array FontSetting utilizzando il metodo Cell.getCharacters. Con questa versione, Aspose.Cells for Java API ha esposto una versione sovraccaricata di Cell.getCharacters che potrebbe accettare Boolean come parametro, indicando se lo stile tabella deve essere applicato alla cella se la cella fa parte di un ListObject.

**Java**

{{< highlight "csharp" >}}

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

FontSetting[]characters = cell.getCharacters(true);

{{< /highlight >}}
### **Aggiunta proprietà OleObject.AutoLoad**
Aspose.Cells for Java 8.8.3 ha esposto la proprietà OleObject.AutoLoad che permette di aggiornare l'immagine dell'OleObject se i contenuti/dati dell'oggetto sottostante sono stati modificati. La suddetta proprietà, se impostata su true, forza l'applicazione Excel ad aggiornare l'immagine di OleObject quando viene caricato il foglio di calcolo risultante.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Aggiorna automaticamente OleObjects](/cells/it/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
### **Aggiunta proprietà HTMLLoadOptions.SupportDivTag**
Aspose.Cells for Java 8.8.3 ha esposto la proprietà HTMLLoadOptions.SupportDivTag che consente di analizzare i tag DIV incorporati nei tag TD durante il caricamento di file/snippet HTML nel modello a oggetti Aspose.Cells. La proprietà di tipo booleano ha il valore predefinito false.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Supporta i tag DIV interni durante il caricamento di HTML](/cells/it/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
### **Aggiunta proprietà HtmlSaveOptions.ExportGridLines**
Aspose.Cells for Java 8.8.3 ha esposto la proprietà HtmlSaveOptions.ExportGridLines che consente di eseguire il rendering delle linee della griglia durante l'esportazione del foglio di calcolo nel formato HTML. La proprietà di tipo booleano ha il valore predefinito false, tuttavia, se impostata su true, API esegue il rendering delle linee della griglia per l'intervallo di dati disponibile nel formato HTML.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Renderizza le linee della griglia a HTML](/cells/it/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Aggiunta proprietà ListObject.Comment**
Aspose.Cells Le API ora consentono di ottenere e impostare i commenti per un'istanza di ListObject. Per fornire la suddetta funzionalità, le API Aspose.Cells hanno esposto la proprietà ListObject.Comment.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Aggiunta di commenti per ListObjects](/cells/it/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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
### **Metodo Workbook.decrypt rimosso**
La suddetta proprietà è stata contrassegnata come obsoleta qualche tempo fa. Questa versione lo ha completamente rimosso dal pubblico API. Si consiglia di impostare la proprietà WorkbookSettings.Password su null per raggiungere lo stesso obiettivo.
