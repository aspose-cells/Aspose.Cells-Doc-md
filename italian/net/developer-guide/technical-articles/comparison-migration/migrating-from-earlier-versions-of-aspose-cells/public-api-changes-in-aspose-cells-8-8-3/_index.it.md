---
title: Modifiche all'API pubblica in Aspose.Cells 8.8.3
type: docs
weight: 290
url: /it/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.8.2 alla 8.8.3 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per controlli ActiveX**
Aspose.Cells for .NET 8.8.3 ha esposto il metodo AddActiveXControl che permette di aggiungere un controllo ActiveX alla ShapeCollection. Il suddetto metodo richiede 7 parametri per specificare il tipo di controllo, la posizione in cui posizionare il controllo e la dimensione del controllo. Il tipo può essere specificato usando l'enumerazione ControlType con i seguenti valori possibili.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Aggiunta di controlli ActiveX al foglio di lavoro](/cells/it/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Aggiunto metodo LoadOptions.SetPaperSize**
Aspose.Cells for .NET 8.8.3 consente di impostare il formato carta di stampa predefinito dall'impostazione della stampante predefinita mentre si utilizza il metodo LoadOptions.SetPaperSize appena esposto come mostrato di seguito. Si noti che il parametro di input per il suddetto metodo è il valore dell'enumerazione PaperSizeType contenente i formati carta predefiniti.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Carica fogli di calcolo con il formato carta specificato](/cells/it/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Aggiunto il metodo Cell.GetCharacters(flag).**
Le API Aspose.Cells consentono di ottenere gli oggetti caratteri sotto forma di array FontSetting utilizzando il metodo Cell.GetCharacters. Con questa versione, l'API Aspose.Cells for .NET ha esposto una versione di overload di Cell.GetCharacters che potrebbe accettare Boolean come parametro, indicando se lo stile tabella deve essere applicato alla cella se la cella fa parte di un ListObject.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **Aggiunta proprietà OleObject.AutoLoad**
Aspose.Cells for .NET 8.8.3 ha esposto la proprietà OleObject.AutoLoad che permette di aggiornare l'immagine dell'OleObject se i contenuti/dati dell'oggetto sottostante sono stati modificati. La suddetta proprietà, se impostata su true, forza l'applicazione Excel ad aggiornare l'immagine di OleObject quando viene caricato il foglio di calcolo risultante.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Aggiorna automaticamente OleObjects](/cells/it/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **Aggiunta proprietà HTMLLoadOptions.SupportDivTag**
Aspose.Cells for .NET 8.8.3 ha esposto la proprietà HTMLLoadOptions.SupportDivTag che consente di analizzare i tag DIV incorporati nei tag TD durante il caricamento di file/snippet HTML nel modello a oggetti Aspose.Cells. La proprietà di tipo booleano ha il valore predefinito false.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Supporta i tag DIV interni durante il caricamento dell'HTML](/cells/it/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **Aggiunta proprietà HtmlSaveOptions.ExportGridLines**
Aspose.Cells for .NET 8.8.3 ha esposto la proprietà HtmlSaveOptions.ExportGridLines che consente di eseguire il rendering delle linee della griglia durante l'esportazione del foglio di calcolo in formato HTML. La proprietà di tipo booleano ha il valore predefinito false, tuttavia, se impostata su true, l'API esegue il rendering delle linee della griglia per l'intervallo di dati disponibile in formato HTML.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Renderizza le linee della griglia in HTML](/cells/it/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Aggiunta proprietà ListObject.Comment**
Aspose.Cells Le API ora consentono di ottenere e impostare i commenti per un'istanza di ListObject. Per fornire la suddetta funzionalità, le API Aspose.Cells hanno esposto la proprietà ListObject.Comment.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Aggiunta di commenti per ListObjects](/cells/it/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Aggiunta proprietà GridWeb.SessionStorePath**
Aspose.Cells.GridWeb for .NET 8.8.3 ha esposto la proprietà SessionStorePath che consente di ottenere o impostare il percorso dell'archivio di sessione quando Session Mode è ViewState. La suddetta proprietà ottiene o imposta il percorso relativo alla directory di base dell'applicazione Web corrente.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Specificare il percorso per i file di sessione temporanei](/cells/it/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.
## **API rimosse**
### **Metodo Workbook.Decrypt rimosso**
La suddetta proprietà è stata contrassegnata come obsoleta qualche tempo fa. Questa versione lo ha completamente rimosso dall'API pubblica. Si consiglia di impostare la proprietà WorkbookSettings.Password su null per raggiungere lo stesso obiettivo.
