---
title: Ändringar i offentlig API i Aspose.Cells 8.6.0
type: docs
weight: 190
url: /sv/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.5.2 till 8.6.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade allmänna metoder, [tillagda klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-6-0/), utan också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för metadatahantering utan att skapa en arbetsboksobjekt**
Denna version av Aspose.Cells for .NET API har exponerat två nya klasser, nämligen WorkbookMetadata & MetadataOptions tillsammans med en ny uppräkning MetadataType som nu tillåter manipulation av dokumentegenskaper (Metadata) utan att skapa en instans av Arbetsbok. WorkbookMetadata-klassen är lättviktig och tillhandahåller en mycket enkel, effektiv mekanism att [läsa, skriva och uppdatera dokumentegenskaper utan att påverka den övergripande prestandan](/cells/sv/net/using-workbookmetadata/).

Följande är det enkla användningscenariot.

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


### **Tillagt HtmlSaveOptions.ExportFrameScriptsAndProperties Egenskap**
Aspose.Cells for .NET 8.6.0 har exponerat egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties som kan användas för att påverka skapandet av extra skript vid konvertering av kalkylblad till HTML-format. Med standardinställningarna exporterar Aspose.Cells API kalkylbladet i HTML-format som Excel-applikationen gör exporten, det vill säga; det resulterande HTML-innehåller ramar och villkorliga kommentarer, som upptäcker webbläsartypen och justerar layouten därefter. Standardvärdet för egenskapen HtmlSaveOptions.ExportFrameScriptsAndProperties är sant, vilket betyder att exporten görs enligt Excel-standarder. Men om egenskapen är inställd på falskt, kommer inte API:et att [generera skript relaterade till ramar och villkorliga kommentarer](/cells/sv/net/disable-exporting-frame-scripts-and-document-properties/). I detta fall kan det resulterande HTML visas korrekt i valfri webbläsare, men det kan inte importeras tillbaka med Aspose.Cells API.

Följande är det enkla användningscenariot.

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


### **Tillagd Shape.MarcoName Egenskap**
Aspose.Cells for .NET 8.6.0 har exponerat egenskapen Shape.MarcoName som kan användas för att [tilldela vilket VBA-modul som helst till en formulärkontroll](/cells/sv/net/assign-macro-to-form-control/) såsom en knapp för att ge interaktion. Egenskapen är av typ sträng och kan därför acceptera modulnamnet och tilldelar det till kontrollen.

Följande är det enkla användningscenariot.

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


### **Tillagd OoxmlSaveOptions.UpdateZoom Egenskap**
Med utgivningen av v8.6.0 har Aspose.Cells for .NET API exponerat egenskapen OoxmlSaveOptions.UpdateZoom som kan användas för att uppdatera PageSetup.Zoom om PageSetup.FitToPagesWide- och/eller PageSetup.FitToPagesTall-egenskaperna har använts för att kontrollera kalkylbladets skalning.
