---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.0
type: docs
weight: 200
url: /de/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.5.2 bis 8.6.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-6-0/), sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Metadatenmanipulation ohne Erstellen eines Workbook-Objekts**
Diese Version der Aspose.Cells for Java-API hat zwei neue Klassen, nämlich WorkbookMetadata & MetadataOptions sowie eine neue Aufzählung MetadataType, die es jetzt ermöglicht, die Dokumenteigenschaften (Metadaten) ohne Erstellen einer Instanz von Workbook zu manipulieren. Die Klasse WorkbookMetadata ist leichtgewichtig und bietet einen sehr einfach zu verwendenden, effizienten Mechanismus zum [Lesen, Schreiben und Aktualisieren von Dokumenteigenschaften, ohne die Gesamtleistung zu beeinträchtigen](/cells/de/java/using-workbookmetadata/). 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **Hinzugefügte HtmlSaveOptions.ExportFrameScriptsAndProperties-Eigenschaft**
Aspose.Cells for Java 8.6.0 hat die Eigenschaft HtmlSaveOptions.ExportFrameScriptsAndProperties freigelegt, die verwendet werden kann, um die Erstellung zusätzlicher Skripte beim Konvertieren der Tabellenkalkulationen in das HTML-Format zu beeinflussen. Mit den Standardeinstellungen exportieren die Aspose.Cells-APIs die Tabellenkalkulation im HTML-Format, wie es die Excel-Anwendung macht, d. h. das resultierende HTML enthält die Frames und bedingten Anmerkungen, die den Browsertyp erkennen und das Layout entsprechend anpassen. Der Standardwert der Eigenschaft HtmlSaveOptions.ExportFrameScriptsAndProperties ist true, das bedeutet, der Export erfolgt gemäß den Excel-Standards. Wenn die Eigenschaft auf false gesetzt wird, generiert die API keine [Skripte im Zusammenhang mit den Frames und bedingten Anmerkungen](/cells/de/java/disable-exporting-frame-scripts-and-document-properties/). In diesem Fall kann das resultierende HTML in jedem Browser korrekt angezeigt werden, jedoch kann es nicht mithilfe der Aspose.Cells-APIs zurückimportiert werden.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **Hinzugefügte Shape.MarcoName-Eigenschaft**
Aspose.Cells for Java 8.6.0 hat die Shape.MarcoName-Eigenschaft freigelegt, die verwendet werden kann, um [einem Formularsteuerelement wie einer Schaltfläche eine VBA-Modul zuzuweisen](/cells/de/java/assign-macro-code-to-form-control/) und so die Interaktion zu ermöglichen. Die Eigenschaft ist vom Typ String und kann daher den Modulnamen akzeptieren und ihn dem Steuerelement zuweisen.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

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
### **Hinzugefügte OoxmlSaveOptions.UpdateZoom-Eigenschaft**
Mit der Veröffentlichung von v8.6.0 hat die Aspose.Cells for Java API die OoxmlSaveOptions.UpdateZoom-Eigenschaft freigelegt, die verwendet werden kann, um die PageSetup.Zoom zu aktualisieren, wenn die PageSetup.FitToPagesWide- und/oder PageSetup.FitToPagesTall-Eigenschaften zur Steuerung der Arbeitsblattskalierung verwendet wurden.
{{< app/cells/assistant language="java" >}}
