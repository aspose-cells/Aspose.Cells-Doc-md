---
title: Offentlig API Ändringar i Aspose.Cells 8.8.3
type: docs
weight: 300
url: /sv/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.8.2 till 8.8.3 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för ActiveX-kontroller**
Aspose.Cells for Java 8.8.3 har avslöjat metoden addActiveXControl som gör det möjligt att lägga till en ActiveX-kontroll till ShapeCollection. Den ovannämnda metoden kräver 7 parametrar för att specificera kontrolltyp, plats för att placera kontroll och storlek på kontroll. Typen kan specificeras med hjälp av ControlType-uppräkningen med följande möjliga värden.

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
1. ControlType.OKÄNDA

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Lägga till ActiveX-kontroller i arbetsbladet](/cells/sv/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
### **Lade till LoadOptions.setPaperSize Method**
Aspose.Cells for Java 8.8.3 gör det möjligt att ställa in standardstorleken för utskriftspapper från standardskrivarens inställning medan du använder den nyligen exponerade metoden LoadOptions.setPaperSize som visas nedan. Observera att indataparametern för ovannämnda metod är värdet från uppräkningen PaperSizeType som innehåller de fördefinierade pappersstorlekarna.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ladda kalkylblad med specificerad pappersstorlek](/cells/sv/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Lade till metoden Cell.getCharacters(flagga).**
Aspose.Cells API:er gör det möjligt att hämta teckenobjekten i form av FontSetting-arrayen genom att använda metoden Cell.getCharacters. Med den här versionen har Aspose.Cells for Java API avslöjat en överbelastad version av Cell.getCharacters som kan acceptera Boolean som parameter, vilket indikerar om tabellstilen måste tillämpas på cellen om cellen är en del av ett ListObject.

**Java**

{{< highlight "csharp" >}}

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

FontSetting[]characters = cell.getCharacters(true);

{{< /highlight >}}
### **Lade till egenskapen OleObject.AutoLoad**
Aspose.Cells for Java 8.8.3 har exponerat egenskapen OleObject.AutoLoad som gör det möjligt att uppdatera OleObjects bild om innehållet/data för det underliggande objektet har ändrats. Den tidigare nämnda egenskapen när den är satt till true tvingar Excel-applikationen att uppdatera OleObjects bild när det resulterande kalkylbladet laddas.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Uppdatera OleObjects automatiskt](/cells/sv/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
### **Tillagd HTMLLoadOptions.SupportDivTag-egenskap**
Aspose.Cells for Java 8.8.3 har avslöjat egenskapen HTMLLoadOptions.SupportDivTag som gör det möjligt att analysera DIV-taggar inbäddade i TD-taggar medan HTML-filer/snippet laddas i Aspose.Cells-objektmodellen. Boolesk typegenskap har standardvärdet false.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Stöd inre DIV-taggar under laddning HTML](/cells/sv/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
### **Tillagd HtmlSaveOptions.ExportGridLines Property**
Aspose.Cells for Java 8.8.3 har exponerat egenskapen HtmlSaveOptions.ExportGridLines som gör det möjligt att rendera rutnätslinjerna medan kalkylblad exporteras till formatet HTML. Egenskapen av typen Boolean har standardvärdet false, men när den är inställd på true, återger API rutnätslinjerna för det tillgängliga dataintervallet i formatet HTML.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Gör rutnätslinjer till HTML](/cells/sv/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Tillagd ListObject.Comment-egenskap**
Aspose.Cells API:er tillåter nu att hämta och ställa in kommentarerna för en instans av ListObject. För att tillhandahålla den ovannämnda funktionen har API:erna Aspose.Cells exponerat egenskapen ListObject.Comment.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Lägga till kommentarer för ListObjects](/cells/sv/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
## **Borttagna API:er**
### **Tog bort Workbook.decrypt-metoden**
Nämnda egendom märktes föråldrad för en tid sedan. Den här versionen har helt tagit bort den från den offentliga API. Det rekommenderas att ställa in WorkbookSettings.Password-egenskapen på null för att uppnå samma mål.
