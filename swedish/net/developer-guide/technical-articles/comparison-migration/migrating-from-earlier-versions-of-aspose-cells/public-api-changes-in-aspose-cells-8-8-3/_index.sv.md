---
title: Offentliga API ändringar i Aspose.Cells 8.8.3
type: docs
weight: 290
url: /sv/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.8.2 till 8.8.3 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för ActiveX-kontroller**
Aspose.Cells for .NET 8.8.3 har exponerat AddActiveXControl metoden som möjliggör att lägga till en ActiveX-kontroll till ShapeCollection. Nämnda metod kräver 7 parametrar för att ange kontrolltypen, platsen för att placera kontrollen och storleken på kontrollen. Typen kan specificeras med hjälp av ControlType-omfattningen med följande möjliga värden.

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

För mer information om denna funktion, vänligen se den detaljerade artikeln om [Lägga till ActiveX-kontroller till Kalkylbladet](/cells/sv/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Tillagt LoadOptions.SetPaperSize Metod**
Aspose.Cells for .NET 8.8.3 tillåter att ställa in standard utskriftspapperstorlek från standard skrivarens inställning genom att använda den nyexponerade LoadOptions.SetPaperSize metoden som visas nedan. Observera, den inmatningsparameter för nämnda metod är värdet från PaperSizeType-omfattningen som innehåller fördefinierade pappersstorlekar.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen se den detaljerade artikeln om [Ladda Kalkylblad med Specifik Pappersstorlek](/cells/sv/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Lagt till Cell.GetCharacters(flag) Metod**
Aspose.Cells API:er tillåter att få teckenobjekt i form av FontSetting-array genom att använda Cell.GetCharacters-metoden. Med den här versionen har Aspose.Cells for .NET API:et utsatt en överbelastad version av Cell.GetCharacters som kunde acceptera en boolean som parameter och ange om tabellformatet ska tillämpas på cellen om cellen är en del av en ListObject.

**C#**

{{< highlight csharp >}}

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


### **Lade till OleObject.AutoLoad Egenskap**
Aspose.Cells for .NET 8.8.3 har utsatt OleObject.AutoLoad-egenskapen som tillåter att uppdatera OleObject:s bild om innehållet/datat i det underliggande objektet har ändrats. När nämnda egenskap är inställd som sann, tvingar programmet Excelfilen att uppdatera OleObject:s bild när den resulterande kalkylbladet laddas.

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska den detaljerade artikeln om [Automatisk uppdatering av OleObjects](/cells/sv/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Lade till HTMLLoadOptions.SupportDivTag Egenskap**
Aspose.Cells for .NET 8.8.3 har utsatt HTMLLoadOptions.SupportDivTag-egenskapen vilken tillåter att tolka DIV-taggar som är inbäddade i TD-taggar vid inläsning av HTML-filer/snuttar i Aspose.Cells-objektmodellen. Egenskapen av typen boolean har standardvärdet falskt.

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska den detaljerade artikeln om [Stöd för inre DIV-taggar vid inläsning av HTML](/cells/sv/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Lade till HtmlSaveOptions.ExportGridLines Egenskap**
Aspose.Cells for .NET 8.8.3 har utsatt HtmlSaveOptions.ExportGridLines-egenskapen vilken tillåter att rendera rutnätet vid exportering av kalkylblad till HTML-format. Egenskapen av typen boolean har standardvärdet falskt, men när den är inställd som sann, renderar API:et rutnätet för den tillgängliga dataserien i HTML-format.

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska den detaljerade artikeln om [Rendera rutnät till HTML](/cells/sv/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Lade till ListObject.Comment Egenskap**
Aspose.Cells API:er tillåter nu att hämta och sätta kommentarer för en instans av ListObject. För att tillhandahålla den tidigare nämnda funktionen, har Aspose.Cells API:erna exponerat ListObject.Comment egenskapen.

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska den detaljerade artikeln om [Lägga till kommentarer för ListObjects](/cells/sv/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Följande är ett enkelt användningsscenario.**
Aspose.Cells.GridWeb för .NET 8.8.3 har utsatt SessionStorePath-egenskapen vilken tillåter att få eller ställa in sessionens lagringsväg när Sessionsläge är ViewState. Nämnt egenskap får eller ställer in den relativa sökvägen till den aktuella webbapplikationens basmapp.

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska den detaljerade artikeln om [Ange väg för tillfälliga sessionfilen](/cells/sv/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Följande är det enkla användningscenariot.
## **Borttagen API:er**
### **Tog bort Workbook.Decrypt-metoden**
Den angivna egenskapen markerades som föråldrad för en tid sedan. Denna version har helt tagit bort den från den offentliga API:et. Det rekommenderas att sätta WorkbookSettings.Password egenskapen till null för att uppnå samma mål.
{{< app/cells/assistant language="csharp" >}}
