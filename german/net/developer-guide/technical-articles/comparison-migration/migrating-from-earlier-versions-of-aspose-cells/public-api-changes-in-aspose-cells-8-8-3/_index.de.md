---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.3
type: docs
weight: 290
url: /de/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.8.2 zu 8.8.3, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für ActiveX-Steuerelemente**
Aspose.Cells for .NET 8.8.3 hat die AddActiveXControl-Methode verfügbar gemacht, die das Hinzufügen eines ActiveX-Steuerelements zur ShapeCollection ermöglicht. Die oben erwähnte Methode erfordert 7 Parameter, um den Steuerelementtyp, den Ort zum Platzieren des Steuerelements und die Größe des Steuerelements anzugeben. Der Typ kann mithilfe der ControlType-Enumeration mit den folgenden möglichen Werten angegeben werden.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.Befehlsschaltfläche
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unbekannt

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Hinzufügen von ActiveX-Steuerelementen zum Arbeitsblatt](/cells/de/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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


### **LoadOptions.SetPaperSize-Methode hinzugefügt**
Aspose.Cells for .NET 8.8.3 ermöglicht das Festlegen der Standarddruckpapiergröße aus der Standarddruckereinstellung, während die neu bereitgestellte LoadOptions.SetPaperSize-Methode wie unten gezeigt verwendet wird. Bitte beachten Sie, dass der Eingabeparameter für die oben genannte Methode der Wert aus der PaperSizeType-Enumeration ist, die die vordefinierten Papierformate enthält.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Tabellenkalkulationen mit angegebenem Papierformat laden](/cells/de/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Methode Cell.GetCharacters(flag) hinzugefügt**
Aspose.Cells-APIs ermöglichen das Abrufen der Zeichenobjekte in Form eines FontSetting-Arrays mithilfe der Methode Cell.GetCharacters. Mit dieser Version hat Aspose.Cells for .NET API eine überladene Version von Cell.GetCharacters verfügbar gemacht, die Boolean als Parameter akzeptieren könnte und angibt, ob der Tabellenstil auf die Zelle angewendet werden muss, wenn die Zelle Teil eines ListObject ist.

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


### **OleObject.AutoLoad-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.8.3 hat die OleObject.AutoLoad-Eigenschaft verfügbar gemacht, mit der das Bild des OleObject aktualisiert werden kann, wenn der Inhalt/die Daten des zugrunde liegenden Objekts geändert wurden. Wenn die oben genannte Eigenschaft auf „true“ gesetzt ist, zwingt sie die Excel-Anwendung, das Bild des OleObjects zu aktualisieren, wenn das resultierende Arbeitsblatt geladen wird.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[OleObjects automatisch aktualisieren](/cells/de/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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


### **HTMLLoadOptions.SupportDivTag-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.8.3 hat die HTMLLoadOptions.SupportDivTag-Eigenschaft verfügbar gemacht, die es ermöglicht, die in TD-Tags eingebetteten DIV-Tags zu analysieren, während HTML-Dateien/Snippets im Aspose.Cells-Objektmodell geladen werden. Die Eigenschaft vom Typ Boolean hat den Standardwert false.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Unterstützung innerer DIV-Tags beim Laden von HTML](/cells/de/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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


### **HtmlSaveOptions.ExportGridLines-Eigenschaft hinzugefügt**
Aspose.Cells for .NET 8.8.3 hat die HtmlSaveOptions.ExportGridLines-Eigenschaft verfügbar gemacht, die es ermöglicht, die Rasterlinien zu rendern, während die Tabelle in das HTML-Format exportiert wird. Die Eigenschaft vom Typ Boolean hat den Standardwert „false“. Wenn sie jedoch auf „true“ gesetzt ist, rendert API die Rasterlinien für den verfügbaren Datenbereich im HTML-Format.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Rasterlinien in HTML rendern](/cells/de/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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


### **ListObject.Comment-Eigenschaft hinzugefügt**
Aspose.Cells APIs ermöglichen jetzt das Abrufen und Festlegen der Kommentare für eine Instanz von ListObject. Um die oben genannte Funktion bereitzustellen, haben die Aspose.Cells-APIs die ListObject.Comment-Eigenschaft verfügbar gemacht.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Hinzufügen von Kommentaren für ListObjects](/cells/de/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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


### **GridWeb.SessionStorePath-Eigenschaft hinzugefügt**
Aspose.Cells.GridWeb for .NET 8.8.3 hat die SessionStorePath-Eigenschaft verfügbar gemacht, die es ermöglicht, den Sitzungsspeicherpfad abzurufen oder festzulegen, wenn der Sitzungsmodus ViewState ist. Die oben genannte Eigenschaft ruft den relativen Pfad zum Basisverzeichnis der aktuellen Webanwendung ab oder legt ihn fest.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Geben Sie den Pfad für temporäre Sitzungsdateien an](/cells/de/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.
## **Entfernte APIs**
### **Workbook.Decrypt-Methode entfernt**
Die besagte Eigenschaft wurde vor einiger Zeit als veraltet markiert. Diese Version hat es vollständig aus der Öffentlichkeit API entfernt. Es wird empfohlen, die WorkbookSettings.Password-Eigenschaft auf null zu setzen, um dasselbe Ziel zu erreichen.
