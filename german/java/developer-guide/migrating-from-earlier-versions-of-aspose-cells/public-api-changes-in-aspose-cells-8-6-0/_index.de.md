---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.0
type: docs
weight: 200
url: /de/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.5.2 zu 8.6.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-6-0/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für die Bearbeitung von Metadaten, ohne ein Arbeitsmappenobjekt zu erstellen**
Diese Version von Aspose.Cells for Java API hat zwei neue Klassen verfügbar gemacht, nämlich WorkbookMetadata & MetadataOptions, zusammen mit einem neuen Aufzählungs-MetadataType, der es jetzt ermöglicht, die Dokumenteigenschaften (Metadaten) zu manipulieren, ohne eine Instanz von Workbook zu erstellen. Die WorkbookMetadata-Klasse ist leichtgewichtig und bietet einen sehr einfach zu verwendenden, effizienten Mechanismus[Dokumenteigenschaften lesen, schreiben und aktualisieren, ohne die Gesamtleistung zu beeinträchtigen](/cells/de/java/using-workbookmetadata/). 

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **Eigenschaft HtmlSaveOptions.ExportFrameScriptsAndProperties Hinzugefügt**
Aspose.Cells for Java 8.6.0 hat die HtmlSaveOptions.ExportFrameScriptsAndProperties-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die Erstellung zusätzlicher Skripts zu beeinflussen, während die Tabellenkalkulationen in das HTML-Format konvertiert werden. Mit den Standardeinstellungen exportieren die Aspose.Cells-APIs die Tabelle im HTML-Format, da die Excel-Anwendung den Export durchführt, d. Das resultierende HTML enthält die Frames und bedingten Kommentare, die den Browsertyp erkennen und das Layout entsprechend anpassen. Der Standardwert der Eigenschaft HtmlSaveOptions.ExportFrameScriptsAndProperties ist true, das heißt; der Export erfolgt nach Excel-Standards. Wenn die Eigenschaft auf „false“ gesetzt ist, wird dies bei API nicht der Fall sein[Generieren Sie die Skripte, die sich auf die Frames und bedingten Kommentare beziehen](/cells/de/java/disable-exporting-frame-scripts-and-document-properties/). In diesem Fall kann das resultierende HTML in jedem Browser korrekt angezeigt werden, es kann jedoch nicht mithilfe von Aspose.Cells-APIs zurückimportiert werden.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **Eigenschaft Shape.MarcoName Hinzugefügt**
 Aspose.Cells for Java 8.6.0 hat die Shape.MarcoName-Eigenschaft verfügbar gemacht, die verwendet werden kann[Weisen Sie einem Formularsteuerelement ein VBA-Modul zu](/cells/de/java/assign-macro-code-to-form-control/) eine solche Schaltfläche, um die Interaktion bereitzustellen. Die Eigenschaft ist vom Typ String, daher kann sie den Modulnamen annehmen und dem Steuerelement zuweisen.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create a new Workbook object

Workbook workbook = new Workbook();

//Get the instance of first default worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a new module to the first worksheet

int moduleIdx = workbook.getVbaProject().getModules().add(sheet);

//Get the instance of newly added module

VbaModule module = workbook.getVbaProject().getModules().get(moduleIdx);

//Add module code

module.setCodes("Sub ShowMessage()" + "\r\n" +

        "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

        "End Sub");

//Create a new button to the worksheet and set its various properties

Button button = (Button) sheet.getShapes().addShape(MsoDrawingType.BUTTON, 2, 0, 2, 0, 28, 80);

button.setPlacement(PlacementType.FREE_FLOATING);

button.getFont().setName("Tahoma");

button.getFont().setBold(true);

button.getFont().setColor(Color.getBlue());

button.setText("Aspose");

//Assign the newly added module to the button

button.setMacroName(module.getName() + ".ShowMessage" );

//Save the spreadsheet in XLSM format

workbook.save("output.xlsm");

{{< /highlight >}}
### **Eigenschaft OoxmlSaveOptions.UpdateZoom Hinzugefügt**
Mit der Veröffentlichung von v8.6.0 hat Aspose.Cells for Java API die OoxmlSaveOptions.UpdateZoom-Eigenschaft verfügbar gemacht, die verwendet werden kann, um die PageSetup.Zoom-Eigenschaft zu aktualisieren, wenn PageSetup.FitToPagesWide- und/oder PageSetup.FitToPagesTall-Eigenschaften verwendet wurden, um die Arbeitsblattskalierung zu steuern.
