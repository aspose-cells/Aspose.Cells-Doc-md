---
title: Ändringar i offentlig API i Aspose.Cells 8.6.0
type: docs
weight: 200
url: /sv/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.5.2 till 8.6.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-6-0/), utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för metadatahantering utan att skapa en arbetsboksobjekt**
Denna version av Aspose.Cells for Java API har exponerat två nya klasser, nämligen WorkbookMetadata & MetadataOptions tillsammans med en ny uppräkning MetadataType som nu tillåter att hantera dokumentegenskaper (metadata) utan att skapa en instans av Arbetsbok. WorkbookMetadata-klassen är lätt och ger en mycket enkel och effektiv mekanism att [läsa, skriva & uppdatera dokumentegenskaper utan att påverka den övergripande prestandan](/cells/sv/java/using-workbookmetadata/). 

Följande är det enkla användningscenariot.

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
### **Tillagt HtmlSaveOptions.ExportFrameScriptsAndProperties Egenskap**
Aspose.Cells for Java 8.6.0 har exponerat egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties som kan användas för att påverka skapandet av ytterligare skript vid konvertering av kalkylblad till HTML-format. Med standardinställningarna exporterar Aspose.Cells API:erna kalkylbladet i HTML-format som Excel-applikationen gör exporten, det vill säga; det resulterande HTML-innehåller ramverk och villkorliga kommentarer som upptäcker webbläsartypen & justerar layouten därefter. Standardvärdet för HtmlSaveOptions.ExportFrameScriptsAndProperties-egenskapen är true, vilket innebär att exporten sker enligt Excel-standarder. Om egenskapen är inställd på false kommer API:et inte att [generera skript relaterade till ramverk och villkorliga kommentarer](/cells/sv/java/disable-exporting-frame-scripts-and-document-properties/). I detta fall kan det resulterande HTML ses korrekt i vilken webbläsare som helst, men det kan inte importeras tillbaka med Aspose.Cells API:erna.

Följande är det enkla användningscenariot.

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
### **Tillagd Shape.MarcoName Egenskap**
Aspose.Cells for Java 8.6.0 har exponerat egenskapen Shape.MarcoName som kan användas för att [tilldela en VBA-modul till en formulärkontroll](/cells/sv/java/assign-macro-code-to-form-control/) som en knapp för att tillhandahålla interaktionen. Egenskapen är av typen sträng och kan därför acceptera modulnamnet och tilldela det till kontrollen.

Följande är det enkla användningscenariot.

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
### **Tillagd OoxmlSaveOptions.UpdateZoom Egenskap**
Med släppet av v8.6.0 har Aspose.Cells for Java API:et exponerat egenskapen OoxmlSaveOptions.UpdateZoom som kan användas för att uppdatera PageSetup.Zoom om PageSetup.FitToPagesWide och/eller PageSetup.FitToPagesTall-egenskaperna har använts för att styra arbetsbladsskalningen.
