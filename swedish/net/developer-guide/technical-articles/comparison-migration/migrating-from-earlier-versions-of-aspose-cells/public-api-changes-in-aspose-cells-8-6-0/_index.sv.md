---
title: Offentlig API Ändringar i Aspose.Cells 8.6.0
type: docs
weight: 190
url: /sv/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.5.2 till 8.6.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-6-0/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för metadatamanipulation utan att skapa ett objekt i arbetsboken**
Den här utgåvan av Aspose.Cells for .NET API har exponerat två nya klasser, nämligen WorkbookMetadata & MetadataOptions tillsammans med en ny uppräkning MetadataType som nu tillåter manipulering av dokumentegenskaperna (metadata) utan att skapa en instans av Workbook. WorkbookMetadata-klassen är lätt och ger en mycket lättanvänd, effektiv mekanism till[läs, skriv och uppdatera dokumentegenskaper utan att påverka den övergripande prestandan](/cells/sv/net/using-workbookmetadata/).

Följande är det enkla användningsscenariot.

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


### **Egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties har lagts till**
Aspose.Cells for .NET 8.6.0 har exponerat egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties som kan användas för att påverka skapandet av ytterligare skript samtidigt som kalkylbladen konverteras till HTML-format. Med standardinställningar exporterar API:erna Aspose.Cells kalkylarket i HTML-format som Excel-applikationen gör exporten, det vill säga; den resulterande HTML-koden innehåller ramar och villkorliga kommentarer, som upptäcker webbläsartypen och anpassar layouten därefter. Standardvärdet för egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties är sant, det betyder; Exporten sker enligt Excel-standarder. Men om egenskapen är inställd på false kommer API inte att göra det[generera skript relaterade till ramar och villkorliga kommentarer](/cells/sv/net/disable-exporting-frame-scripts-and-document-properties/). I det här fallet kan den resulterande HTML-koden ses korrekt i vilken webbläsare som helst, men den kan inte importeras tillbaka med Aspose.Cells API:er.

Följande är det enkla användningsscenariot.

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


### **Egenskap Shape.MarcoName tillagd**
 Aspose.Cells for .NET 8.6.0 har exponerat egenskapen Shape.MarcoName som kan användas för att[tilldela valfri VBA-modul till en formulärkontroll](/cells/sv/net/assign-macro-to-form-control/) en sådan knapp för att tillhandahålla interaktionen. Egenskapen är av typen string, därför kan den acceptera modulnamnet och tilldelar det till kontrollen.

Följande är det enkla användningsscenariot.

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


### **Egenskapen OoxmlSaveOptions.UpdateZoom har lagts till**
Med utgåvan av v8.6.0 har Aspose.Cells for .NET API avslöjat egenskapen OoxmlSaveOptions.UpdateZoom som kan användas för att uppdatera PageSetup.Zoom om PageSetup.FitToPagesWide och/eller PageSetupTalling har använts för att kontrollera Worksheets.Fit.
