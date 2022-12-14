---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.0
type: docs
weight: 190
url: /de/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.5.2 zu 8.6.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-6-0/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für die Bearbeitung von Metadaten, ohne ein Arbeitsmappenobjekt zu erstellen**
Diese Version von Aspose.Cells for .NET API hat zwei neue Klassen verfügbar gemacht, nämlich WorkbookMetadata & MetadataOptions, zusammen mit einem neuen Aufzählungs-MetadataType, der jetzt die Bearbeitung der Dokumenteigenschaften (Metadaten) ermöglicht, ohne eine Instanz von Workbook zu erstellen. Die WorkbookMetadata-Klasse ist leichtgewichtig und bietet einen sehr einfach zu verwendenden, effizienten Mechanismus[Dokumenteigenschaften lesen, schreiben und aktualisieren, ohne die Gesamtleistung zu beeinträchtigen](/cells/de/net/using-workbookmetadata/).

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **Eigenschaft HtmlSaveOptions.ExportFrameScriptsAndProperties Hinzugefügt**
Aspose.Cells for .NET 8.6.0 hat die HtmlSaveOptions.ExportFrameScriptsAndProperties-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die Erstellung zusätzlicher Skripts zu beeinflussen, während die Tabellenkalkulationen in das HTML-Format konvertiert werden. Mit den Standardeinstellungen exportieren die Aspose.Cells-APIs die Tabelle im HTML-Format, da die Excel-Anwendung den Export durchführt, d. Das resultierende HTML enthält die Frames und bedingten Kommentare, die den Browsertyp erkennen und das Layout entsprechend anpassen. Der Standardwert der Eigenschaft HtmlSaveOptions.ExportFrameScriptsAndProperties ist true, das heißt; der Export erfolgt nach Excel-Standards. Wenn die Eigenschaft jedoch auf „false“ gesetzt ist, wird dies bei API nicht der Fall sein[Generieren Sie die Skripte für Frames und bedingte Kommentare](/cells/de/net/disable-exporting-frame-scripts-and-document-properties/). In diesem Fall kann das resultierende HTML in jedem Browser korrekt angezeigt werden, es kann jedoch nicht mithilfe von Aspose.Cells-APIs zurückimportiert werden.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **Eigenschaft Shape.MarcoName Hinzugefügt**
 Aspose.Cells for .NET 8.6.0 hat die Shape.MarcoName-Eigenschaft verfügbar gemacht, die verwendet werden kann[Weisen Sie einem Formularsteuerelement ein beliebiges VBA-Modul zu](/cells/de/net/assign-macro-to-form-control/) eine solche Schaltfläche, um die Interaktion bereitzustellen. Die Eigenschaft ist vom Typ String, daher kann sie den Modulnamen annehmen und dem Steuerelement zuweisen.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access first default worksheet

Worksheet sheet = workbook.Worksheets[0];

//Add a module to the worksheet

int moduleIdx = workbook.VbaProject.Modules.Add(sheet);

//Access newly added module from the collection

VbaModule module = workbook.VbaProject.Modules[moduleIdx];

//Add code to the module

module.Codes =

    "Sub ShowMessage()" + "\r\n" +

    "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

    "End Sub";

//Add a Button on the worksheet and set its various properties

Aspose.Cells.Drawing.Button button = sheet.Shapes.AddButton(2, 0, 2, 0, 28, 80);

button.Placement = Aspose.Cells.Drawing.PlacementType.FreeFloating;

button.Font.Name = "Tahoma";

button.Font.IsBold = true;

button.Font.Color = System.Drawing.Color.Blue;

button.Text = "Aspose";

//Assign the VBA module to the button

button.MacroName = sheet.Name + ".ShowMessage";

//Save the result

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Eigenschaft OoxmlSaveOptions.UpdateZoom Hinzugefügt**
Mit der Veröffentlichung von v8.6.0 hat Aspose.Cells for .NET API die OoxmlSaveOptions.UpdateZoom-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die PageSetup.Zoom-Eigenschaft zu aktualisieren, wenn PageSetup.FitToPagesWide- und/oder PageSetup.FitToPagesTall-Eigenschaften verwendet wurden, um die Arbeitsblattskalierung zu steuern.
