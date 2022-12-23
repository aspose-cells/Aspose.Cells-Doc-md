---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.3
type: docs
weight: 300
url: /de/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.8.2 zu 8.8.3, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für ActiveX-Steuerelemente**
Aspose.Cells for Java 8.8.3 hat die addActiveXControl-Methode verfügbar gemacht, die das Hinzufügen eines ActiveX-Steuerelements zur ShapeCollection ermöglicht. Die oben erwähnte Methode erfordert 7 Parameter, um den Steuerelementtyp, den Ort zum Platzieren des Steuerelements und die Größe des Steuerelements anzugeben. Der Typ kann mithilfe der ControlType-Enumeration mit den folgenden möglichen Werten angegeben werden.

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
1. ControlType.UNBEKANNT

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Hinzufügen von ActiveX-Steuerelementen zum Arbeitsblatt](/cells/de/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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
### **LoadOptions.setPaperSize-Methode hinzugefügt**
Aspose.Cells for Java 8.8.3 ermöglicht das Festlegen der Standarddruckpapiergröße aus der Standarddruckereinstellung, während die neu bereitgestellte LoadOptions.setPaperSize-Methode wie unten gezeigt verwendet wird. Bitte beachten Sie, dass der Eingabeparameter für die oben genannte Methode der Wert aus der PaperSizeType-Enumeration ist, die die vordefinierten Papierformate enthält.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Tabellenkalkulationen mit angegebenem Papierformat laden](/cells/de/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Methode Cell.getCharacters(flag) hinzugefügt**
Aspose.Cells-APIs ermöglichen das Abrufen der Zeichenobjekte in Form eines FontSetting-Arrays mithilfe der Methode Cell.getCharacters. Mit dieser Version hat Aspose.Cells for Java API eine überladene Version von Cell.getCharacters verfügbar gemacht, die Boolean als Parameter akzeptieren könnte und angibt, ob der Tabellenstil auf die Zelle angewendet werden muss, wenn die Zelle Teil eines ListObject ist.

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
### **OleObject.AutoLoad-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.8.3 hat die OleObject.AutoLoad-Eigenschaft verfügbar gemacht, mit der das Bild des OleObject aktualisiert werden kann, wenn der Inhalt/die Daten des zugrunde liegenden Objekts geändert wurden. Wenn die oben genannte Eigenschaft auf „true“ gesetzt ist, zwingt sie die Excel-Anwendung, das Bild des OleObjects zu aktualisieren, wenn das resultierende Arbeitsblatt geladen wird.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[OleObjects automatisch aktualisieren](/cells/de/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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
### **HTMLLoadOptions.SupportDivTag-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.8.3 hat die HTMLLoadOptions.SupportDivTag-Eigenschaft verfügbar gemacht, die es ermöglicht, die in TD-Tags eingebetteten DIV-Tags zu analysieren, während HTML-Dateien/Schnipsel in das Aspose.Cells-Objektmodell geladen werden. Die Eigenschaft vom Typ Boolean hat den Standardwert false.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Unterstützung innerer DIV-Tags beim Laden von HTML](/cells/de/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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
### **HtmlSaveOptions.ExportGridLines-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.8.3 hat die HtmlSaveOptions.ExportGridLines-Eigenschaft verfügbar gemacht, die es ermöglicht, die Rasterlinien beim Exportieren der Tabelle in das HTML-Format zu rendern. Die Eigenschaft vom Typ Boolean hat den Standardwert „false“. Wenn sie jedoch auf „true“ gesetzt ist, rendert API die Rasterlinien für den verfügbaren Datenbereich im Format HTML.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Gitterlinien auf HTML rendern](/cells/de/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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
### **ListObject.Comment-Eigenschaft hinzugefügt**
Aspose.Cells APIs ermöglichen jetzt das Abrufen und Festlegen der Kommentare für eine Instanz von ListObject. Um die oben genannte Funktion bereitzustellen, haben die Aspose.Cells-APIs die ListObject.Comment-Eigenschaft verfügbar gemacht.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Hinzufügen von Kommentaren für ListObjects](/cells/de/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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
## **Entfernte APIs**
### **Workbook.decrypt-Methode entfernt**
Die besagte Eigenschaft wurde vor einiger Zeit als veraltet markiert. Diese Version hat es vollständig aus der Öffentlichkeit API entfernt. Es wird empfohlen, die WorkbookSettings.Password-Eigenschaft auf null zu setzen, um dasselbe Ziel zu erreichen.
