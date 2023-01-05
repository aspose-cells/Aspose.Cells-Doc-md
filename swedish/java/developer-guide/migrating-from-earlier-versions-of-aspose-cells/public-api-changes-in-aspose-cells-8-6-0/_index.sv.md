---
title: Offentlig API Ändringar i Aspose.Cells 8.6.0
type: docs
weight: 200
url: /sv/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.5.2 till 8.6.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-6-0/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för metadatamanipulation utan att skapa ett objekt i arbetsboken**
Den här utgåvan av Aspose.Cells for Java API har exponerat två nya klasser, nämligen WorkbookMetadata & MetadataOptions tillsammans med en ny uppräkning MetadataType som nu gör det möjligt att manipulera dokumentegenskaperna (metadata) utan att skapa en instans av Workbook. WorkbookMetadata-klassen är lätt och ger en mycket lättanvänd, effektiv mekanism till[läs, skriv och uppdatera dokumentegenskaper utan att påverka den övergripande prestandan](/cells/sv/java/using-workbookmetadata/). 

Följande är det enkla användningsscenariot.

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
### **Egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties har lagts till**
Aspose.Cells for Java 8.6.0 har avslöjat egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties som kan användas för att påverka skapandet av ytterligare skript samtidigt som kalkylbladen konverteras till formatet HTML. Med standardinställningar exporterar API:erna Aspose.Cells kalkylarket i formatet HTML eftersom Excel-programmet gör exporten, det vill säga; den resulterande HTML innehåller ramar och villkorliga kommentarer, som upptäcker webbläsartypen och anpassar layouten därefter. Standardvärdet för egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties är sant, det betyder; Exporten sker enligt Excel-standarder. Om egenskapen är inställd på false kommer API inte att göra det[generera skript relaterade till ramarna och villkorliga kommentarer](/cells/sv/java/disable-exporting-frame-scripts-and-document-properties/). I det här fallet kan den resulterande HTML ses korrekt i vilken webbläsare som helst, men den kan inte importeras tillbaka med Aspose.Cells API:er.

Följande är det enkla användningsscenariot.

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
### **Egenskap Shape.MarcoName tillagd**
Aspose.Cells for Java 8.6.0 har exponerat egenskapen Shape.MarcoName som kan användas för att[tilldela en VBA-modul till en formulärkontroll](/cells/sv/java/assign-macro-code-to-form-control/) en sådan knapp för att tillhandahålla interaktionen. Egenskapen är av typen string, därför kan den acceptera modulnamnet och tilldelar det till kontrollen.

Följande är det enkla användningsscenariot.

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
### **Egenskapen OoxmlSaveOptions.UpdateZoom har lagts till**
Med utgåvan av v8.6.0 har Aspose.Cells for Java API avslöjat egenskapen OoxmlSaveOptions.UpdateZoom som kan användas för att uppdatera PageSetup.Zoom om PageSetup.FitToPagesWide och/eller PageSetupTalling har använts för att kontrollera Worksheets.Fit.
