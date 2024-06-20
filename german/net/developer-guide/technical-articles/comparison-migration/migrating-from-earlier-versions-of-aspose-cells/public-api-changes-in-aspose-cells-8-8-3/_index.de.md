---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.3
type: docs
weight: 290
url: /de/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.8.2 auf 8.8.3, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von etwaigen Änderungen im Verhalten im Hintergrund von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für ActiveX-Steuerelemente**
Aspose.Cells for .NET 8.8.3 hat die AddActiveXControl Methode freigelegt, die es ermöglicht, ein ActiveX-Steuerelement zur ShapeCollection hinzuzufügen. Die genannte Methode erfordert 7 Parameter, um den Steuerelementtyp, den Platzierungsort des Steuerelements und die Größe des Steuerelements anzugeben. Der Typ kann mithilfe der ControlType-Aufzählung mit den folgenden möglichen Werten spezifiziert werden.

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

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Hinzufügen von ActiveX-Steuerelementen zur Arbeitsmappe](/cells/de/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügter LoadOptions.SetPaperSize-Methode**
Aspose.Cells for .NET 8.8.3 ermöglicht das Festlegen der Standarddruckpapiergröße aus den Einstellungen des Standarddruckers, während die neu freigegebene LoadOptions.SetPaperSize-Methode wie unten dargestellt verwendet wird. Bitte beachten Sie, dass der Eingabeparameter für die genannte Methode der Wert aus dem PaperSizeType-Enum ist, der die vordefinierten Papiergrößen enthält.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel zu [Laden von Arbeitsmappen mit bestimmter Papiergröße](/cells/de/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Hinzugefügte Cell.GetCharacters(flag)-Methode**
Aspose.Cells APIs ermöglichen das Abrufen von Zeichenobjekten in Form eines FontSetting-Arrays mithilfe der Cell.GetCharacters-Methode. Mit diesem Release hat die Aspose.Cells for .NET API eine überladene Version der Cell.GetCharacters freigegeben, die Boolean als Parameter akzeptieren kann, um anzuzeigen, ob der Tabellenstil auf die Zelle angewendet werden soll, wenn die Zelle Teil eines ListObject ist.

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


### **Hinzugefügtes OleObject.AutoLoad Eigenschaft**
Aspose.Cells for .NET 8.8.3 hat die Eigenschaft OleObject.AutoLoad freigelegt, die es ermöglicht, das Bild des OleObjects zu aktualisieren, wenn der Inhalt/Daten des zugrunde liegenden Objekts geändert wurde. Die genannte Eigenschaft zwingt die Excel-Anwendung dazu, das Bild des OleObjects zu aktualisieren, wenn das resultierende Arbeitsblatt geladen wird, wenn sie auf true gesetzt wird.

{{% alert color="primary" %}} 

Für weitere Details zu dieser Funktion lesen Sie bitte den ausführlichen Artikel zu [Automatisches Aktualisieren von OleObjects](/cells/de/net/automatisch-aktualisieren-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügte HTMLLoadOptions.SupportDivTag Eigenschaft**
Aspose.Cells for .NET 8.8.3 hat die Eigenschaft HTMLLoadOptions.SupportDivTag freigelegt, die es ermöglicht, die DIV-Tags, die in TD-Tags eingebettet sind, beim Laden von HTML-Dateien/Schnipseln im Aspose.Cells-Objektmodell zu analysieren. Die boolesche Eigenschaft hat den Standardwert false.

{{% alert color="primary" %}} 

Für weitere Details zu dieser Funktion lesen Sie bitte den ausführlichen Artikel zu [Unterstützung innerer DIV-Tags beim Laden von HTML](/cells/de/net/unterstutzung-des-layouts-von-div-tags-beim-laden-von-html-in-excel-arbeitsmappe/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügte HtmlSaveOptions.ExportGridLines Eigenschaft**
Aspose.Cells for .NET 8.8.3 hat die Eigenschaft HtmlSaveOptions.ExportGridLines freigelegt, die es ermöglicht, die Gitterlinien beim Exportieren des Arbeitsblatts in HTML-Format zu rendern. Die boolesche Eigenschaft hat standardmäßig den Wert false, jedoch rendert die API die Gitterlinien für den verfügbaren Datenbereich im HTML-Format, wenn sie auf true gesetzt wird.

{{% alert color="primary" %}} 

Für weitere Details zu dieser Funktion lesen Sie bitte den ausführlichen Artikel zu [Gitterlinien als HTML rendern](/cells/de/net/exportieren-sie-excel-in-html-mit-gitterlinien/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügte ListObject.Comment Eigenschaft**
Die Aspose.Cells APIs ermöglichen es jetzt, die Kommentare für eine Instanz von ListObject abzurufen und zu setzen. Um diese Funktion zu ermöglichen, haben die Aspose.Cells APIs die Eigenschaft ListObject.Comment freigelegt.

{{% alert color="primary" %}} 

Für weitere Details zu dieser Funktion lesen Sie bitte den detaillierten Artikel zu [Hinzufügen von Kommentaren für ListObjects](/cells/de/net/setzen-des-kommentars-von-tabelle-oder-list-objekt-im-arbeitsblatt/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Die Eigenschaft GridWeb.SessionStorePath wurde hinzugefügt**
Aspose.Cells.GridWeb für .NET 8.8.3 hat die Eigenschaft SessionStorePath freigelegt, die es ermöglicht, den Sitzungsspeicherpfad festzulegen, wenn der Sitzungsmodus ViewState ist. Die genannte Eigenschaft legt den relativen Pfad zum aktuellen Basisverzeichnis der Webanwendung fest.

{{% alert color="primary" %}} 

Für weitere Details zu dieser Funktion lesen Sie bitte den ausführlichen Artikel zu [Festlegen des Pfads für temporäre Sitzungsdateien](/cells/de/net/geben-sie-den-pfad-an-wo-gridweb-temporare-sitzungsdateien-speichert/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.
## **Entfernte APIs**
### **Entfernte Workbook.Decrypt-Methode**
Die genannte Eigenschaft wurde vor einiger Zeit veraltet. In dieser Version wurde sie vollständig aus der öffentlichen API entfernt. Es wird empfohlen, die Eigenschaft WorkbookSettings.Password auf null zu setzen, um dasselbe Ziel zu erreichen.
