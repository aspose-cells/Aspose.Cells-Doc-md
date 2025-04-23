---
title: Offentliga API ändringar i Aspose.Cells 8.8.3
type: docs
weight: 300
url: /sv/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.8.2 till 8.8.3 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för ActiveX-kontroller**
Aspose.Cells for Java 8.8.3 har exponerat addActiveXControl-metoden som tillåter att lägga till en ActiveX-kontroll till ShapeCollection. Den angivna metoden kräver 7 parametrar för att ange kontrolltypen, platsen för att placera kontrollen och storleken på kontrollen. Typen kan specifieras med användning av ControlType-ramverket med följande möjliga värden.

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Lägga till ActiveX-kontroller till kalkylbladet](/cells/sv/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Lade till LoadOptions.setPaperSize Metoden**
Aspose.Cells for Java 8.8.3 tillåter att ställa in standard utskriftspapperstorleken från standard skrivarens inställning medan man använder den nyligen exponerade LoadOptions.setPaperSize metoden som demonstreras nedan. Observera att inmatningsparametern till den angivna metoden är värdet från PaperSizeType-ramverket som innehåller fördefinierade papperstorlekar.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Ladda kalkylblad med specifierad papperstorlek](/cells/sv/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Lade till Cell.getCharacters(flag) Metoden**
Aspose.Cells API:erna tillåter att få teckenobjekt i form av FontSetting-array genom att använda Cell.getCharacters-metoden. Med denna version har Aspose.Cells for Java API:et exponerat en överbelastad version av Cell.getCharacters som kan acceptera Boolean som parameter, vilket anger om tabellstilen måste tillämpas på cellen om cellen är en del av en ListObject.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **Lade till OleObject.AutoLoad Egenskap**
Aspose.Cells for Java 8.8.3 har exponerat OleObject.AutoLoad egenskapen som tillåter att uppdatera OleObject's bild om innehållet/datamängden av den underliggande objektet har ändrats. Den tidigare nämnda egenskapen när den är satt till true, tvingar Excel-applikationen att uppdatera OleObject's bild när den resulterande kalkylbladet laddas.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Automatiskt Uppdatera OleObjects](/cells/sv/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **Lade till HTMLLoadOptions.SupportDivTag Egenskap**
Aspose.Cells for Java 8.8.3 har exponerat HTMLLoadOptions.SupportDivTag egenskapen som tillåter att tolka DIV-taggar inbäddade i TD-taggar vid inläsning av HTML-filer/snutt i Aspose.Cells objektmodellen. Boolesk typ egenskapen har standardvärdet false.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Stöd för Inre DIV-taggar vid inläsning av HTML](/cells/sv/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Lade till HtmlSaveOptions.ExportGridLines Egenskap**
Aspose.Cells for Java 8.8.3 har exponerat HtmlSaveOptions.ExportGridLines egenskapen som tillåter att rendera rutnätlinjer vid export av kalkylblad till HTML-format. Boolesk typ egenskapen har standardvärdet false, men när den är satt till true, renderar API:et rutnätlinjerna för den tillgängliga datamängden i HTML-format.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Rendera Rutnätlinjer till HTML](/cells/sv/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Lade till ListObject.Comment Egenskap**
Aspose.Cells API:er tillåter nu att hämta och sätta kommentarer för en instans av ListObject. För att tillhandahålla den tidigare nämnda funktionen, har Aspose.Cells API:erna exponerat ListObject.Comment egenskapen.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Lägga till Kommentarer för ListObjects](/cells/sv/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **Borttagen API:er**
### **Tog bort Workbook.decrypt Metod**
Den angivna egenskapen markerades som föråldrad för en tid sedan. Denna version har helt tagit bort den från den offentliga API:et. Det rekommenderas att sätta WorkbookSettings.Password egenskapen till null för att uppnå samma mål.
{{< app/cells/assistant language="java" >}}
