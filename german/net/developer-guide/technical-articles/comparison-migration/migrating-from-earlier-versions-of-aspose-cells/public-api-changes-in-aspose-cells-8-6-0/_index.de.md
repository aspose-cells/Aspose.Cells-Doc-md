---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.0
type: docs
weight: 190
url: /de/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.5.2 auf 8.6.0, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es beinhaltet nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-6-0/), sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Metadatenmanipulation ohne Erstellen eines Workbook-Objekts**
Diese Version von Aspose.Cells for .NET API hat zwei neue Klassen namens WorkbookMetadata & MetadataOptions sowie eine neue Enumeration MetadataType freigegeben, die es jetzt ermöglicht, die Dokumenteigenschaften (Metadaten) ohne Erstellen einer Instanz von Workbook zu manipulieren. Die WorkbookMetadata-Klasse ist leichtgewichtig und bietet einen sehr benutzerfreundlichen, effizienten Mechanismus zum [Lesen, Schreiben und Aktualisieren von Dokumenteigenschaften, ohne die Gesamtleistung zu beeinträchtigen](/cells/de/net/using-workbookmetadata/).

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **Hinzugefügte HtmlSaveOptions.ExportFrameScriptsAndProperties-Eigenschaft**
Aspose.Cells for .NET 8.6.0 hat die HtmlSaveOptions.ExportFrameScriptsAndProperties-Eigenschaft freigegeben, die verwendet werden kann, um die Erstellung zusätzlicher Skripte beim Konvertieren der Tabellenkalkulationen in das HTML-Format zu beeinflussen. Mit den Standardeinstellungen exportieren die Aspose.Cells APIs die Tabelle im HTML-Format, wie es auch die Excel-Anwendung tut, d. h. das resultierende HTML enthält die Frames und bedingten Kommentare, die den Browsertyp erkennen und das Layout entsprechend anpassen. Der Standardwert der HtmlSaveOptions.ExportFrameScriptsAndProperties-Eigenschaft ist true, das bedeutet, dass der Export gemäß den Excel-Standards erfolgt. Wenn jedoch die Eigenschaft auf false gesetzt wird, generiert die API die Skripte im Zusammenhang mit den Frames und bedingten Kommentaren nicht [(/cells/de/net/disable-exporting-frame-scripts-and-document-properties/)]. In diesem Fall kann das resultierende HTML in jedem Browser korrekt angezeigt werden, es kann jedoch nicht mithilfe von Aspose.Cells APIs importiert werden.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **Hinzugefügte Shape.MarcoName-Eigenschaft**
Aspose.Cells for .NET 8.6.0 hat die Shape.MarcoName-Eigenschaft freigegeben, die verwendet werden kann, um [jedes VBA-Modul einem Steuerelement](/cells/de/net/assign-macro-to-form-control/) wie z. B. einer Schaltfläche zuzuweisen, um die Interaktion zu ermöglichen. Die Eigenschaft ist vom Typ String und kann daher den Modulnamen akzeptieren und ihn dem Steuerelement zuweisen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

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


### **Hinzugefügte OoxmlSaveOptions.UpdateZoom-Eigenschaft**
Mit der Veröffentlichung von v8.6.0 hat die Aspose.Cells for .NET-API die OoxmlSaveOptions.UpdateZoom-Eigenschaft freigegeben, die verwendet werden kann, um die PageSetup.Zoom zu aktualisieren, wenn die PageSetup.FitToPagesWide- und/oder PageSetup.FitToPagesTall-Eigenschaften zur Steuerung der Arbeitsblattskalierung verwendet wurden.
{{< app/cells/assistant language="csharp" >}}
