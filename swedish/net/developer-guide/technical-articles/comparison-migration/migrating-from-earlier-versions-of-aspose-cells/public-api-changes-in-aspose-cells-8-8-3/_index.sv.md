---
title: Offentliga API-ändringar i Aspose.Cells 8.8.3
type: docs
weight: 290
url: /sv/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.8.2 till 8.8.3 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för ActiveX-kontroller**
Aspose.Cells för .NET 8.8.3 har avslöjat metoden AddActiveXControl som gör det möjligt att lägga till en ActiveX-kontroll till ShapeCollection. Den ovannämnda metoden kräver 7 parametrar för att specificera kontrolltyp, plats för att placera kontroll och storlek på kontroll. Typen kan specificeras med hjälp av ControlType-uppräkningen med följande möjliga värden.

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
1. ControlType.Okänd

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Lägga till ActiveX-kontroller i arbetsbladet](/cells/sv/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

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


### **Lade till LoadOptions.SetPaperSize Method**
Aspose.Cells för .NET 8.8.3 gör det möjligt att ställa in standardstorleken för utskriftspapper från standardskrivarens inställning medan du använder den nyligen exponerade metoden LoadOptions.SetPaperSize som visas nedan. Observera att indataparametern för ovannämnda metod är värdet från uppräkningen PaperSizeType som innehåller de fördefinierade pappersstorlekarna.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ladda kalkylblad med specificerad pappersstorlek](/cells/sv/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Lade till Cell.GetCharacters(flagga) Method**
Aspose.Cells API:er gör det möjligt att hämta teckenobjekten i form av FontSetting-arrayen genom att använda metoden Cell.GetCharacters. Med den här versionen har Aspose.Cells för .NET API avslöjat en överbelastad version av Cell.GetCharacters som kan acceptera Boolean som parameter, vilket indikerar om tabellstilen måste tillämpas på cellen om cellen är en del av ett ListObject.

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


### **Lade till egenskapen OleObject.AutoLoad**
Aspose.Cells för .NET 8.8.3 har exponerat egenskapen OleObject.AutoLoad som gör det möjligt att uppdatera OleObjects bild om innehållet/data för det underliggande objektet har ändrats. Den tidigare nämnda egenskapen när den är satt till true tvingar Excel-applikationen att uppdatera OleObjects bild när det resulterande kalkylbladet laddas.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Uppdatera OleObjects automatiskt](/cells/sv/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

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


### **Tillagd HTMLLoadOptions.SupportDivTag-egenskap**
Aspose.Cells för .NET 8.8.3 har avslöjat egenskapen HTMLLoadOptions.SupportDivTag som gör det möjligt att analysera DIV-taggar inbäddade i TD-taggar medan HTML-filer/snippet laddas i objektmodellen Aspose.Cells. Boolesk typegenskap har standardvärdet false.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Stöd inre DIV-taggar när du laddar HTML](/cells/sv/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

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


### **Tillagd HtmlSaveOptions.ExportGridLines Property**
Aspose.Cells för .NET 8.8.3 har exponerat egenskapen HtmlSaveOptions.ExportGridLines som gör det möjligt att rendera rutnätslinjerna samtidigt som kalkylblad exporteras till HTML-format. Egenskapen boolesk typ har standardvärdet false, men när den är satt till true, återger API:et rutnätslinjerna för det tillgängliga dataintervallet i HTML-format.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Gör rutnätslinjer till HTML](/cells/sv/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

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


### **Tillagd ListObject.Comment-egenskap**
Aspose.Cells API:er tillåter nu att hämta och ställa in kommentarerna för en instans av ListObject. För att tillhandahålla den ovannämnda funktionen har API:erna Aspose.Cells exponerat egenskapen ListObject.Comment.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Lägga till kommentarer för ListObjects](/cells/sv/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

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


### **Lade till GridWeb.SessionStorePath-egenskap**
Aspose.Cells.GridWeb för .NET 8.8.3 har exponerat SessionStorePath-egenskapen som gör det möjligt att hämta eller ställa in sessionslagringssökvägen när Session Mode är ViewState. Den ovannämnda egenskapen hämtar eller ställer in den relativa sökvägen till den aktuella webbapplikationens Baskatalog.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ange sökväg för tillfälliga sessionsfiler](/cells/sv/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.
## **Borttagna API:er**
### **Borttagen Workbook.Decrypt Method**
Nämnda egendom märktes föråldrad för en tid sedan. Den här versionen har helt tagit bort den från det offentliga API:et. Det rekommenderas att ställa in WorkbookSettings.Password-egenskapen till null för att uppnå samma mål.
