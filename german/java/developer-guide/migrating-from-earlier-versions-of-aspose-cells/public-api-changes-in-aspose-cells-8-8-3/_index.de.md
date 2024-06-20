---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.3
type: docs
weight: 300
url: /de/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.8.2 auf 8.8.3, die für Modul-/Anwendungs-Entwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung von etwaigen Änderungen im Verhalten im Hintergrund von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für ActiveX-Steuerelemente**
Aspose.Cells for Java 8.8.3 hat die Methode addActiveXControl freigelegt, mit der ein ActiveX-Steuerelement zur ShapeCollection hinzugefügt werden kann. Die oben genannte Methode erfordert 7 Parameter, um den Steuerelementtyp, den Ort zur Platzierung des Steuerelements und die Größe des Steuerelements anzugeben. Der Typ kann mithilfe der Aufzählung ControlType mit folgenden möglichen Werten angegeben werden.

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

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über [Hinzufügen von ActiveX-Steuerelementen zur Arbeitsmappe](/cells/de/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügter LoadOptions.setPaperSize Methode**
Aspose.Cells for Java 8.8.3 ermöglicht die Festlegung der standardmäßigen Druckpapiergröße aus den Einstellungen des Standarddruckers unter Verwendung der neu freigegebenen LoadOptions.setPaperSize-Methode, wie unten gezeigt. Bitte beachten Sie, dass der Eingabeparameter für die oben genannte Methode der Wert aus dem PaperSizeType-Enumerations enthält, der die vordefinierten Papiergrößen enthält.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den detaillierten Artikel zu [Tabellenkalkulationen mit bestimmter Papiergröße laden](/cells/de/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Hinzugefügte Cell.getCharacters(flag) Methode**
Aspose.Cells APIs bieten die Möglichkeit, die Zeichenobjekte in Form eines FontSetting-Arrays mithilfe der Cell.getCharacters-Methode zu erhalten. Mit diesem Release hat das Aspose.Cells for Java API eine überladene Version des Cell.getCharacters freigegeben, die einen Boolean als Parameter akzeptieren kann, der angibt, ob der Tabellenstil auf die Zelle angewendet werden muss, wenn die Zelle Teil eines ListObject ist.

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
### **Hinzugefügtes OleObject.AutoLoad Eigenschaft**
Aspose.Cells for Java 8.8.3 hat die OleObject.AutoLoad-Eigenschaft freigegeben, die es ermöglicht, das Bild des OleObjects zu aktualisieren, wenn sich der Inhalt/Daten des zugrunde liegenden Objekts geändert hat. Wenn die oben genannte Eigenschaft auf true gesetzt wird, zwingt dies die Excel-Anwendung, das Bild des OleObjects zu aktualisieren, wenn die resultierende Tabellenkalkulation geladen wird.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den detaillierten Artikel zu [OleObjects automatisch aktualisieren](/cells/de/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügte HTMLLoadOptions.SupportDivTag Eigenschaft**
Aspose.Cells for Java 8.8.3 hat die HTMLLoadOptions.SupportDivTag-Eigenschaft freigegeben, die das Parsen von DIV-Tags ermöglicht, die in TD-Tags eingebettet sind, während HTML-Dateien/Schnipsel im Aspose.Cells-Objektmodell geladen werden. Die Boolean-Typ-Eigenschaft hat den Standardwert false.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den detaillierten Artikel zu [Unterstützung innerer DIV-Tags beim Laden von HTML](/cells/de/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügte HtmlSaveOptions.ExportGridLines Eigenschaft**
Aspose.Cells for Java 8.8.3 hat die HtmlSaveOptions.ExportGridLines-Eigenschaft freigegeben, die es ermöglicht, die Grid-Linien beim Exportieren von Tabellenkalkulationen in das HTML-Format zu rendern. Die Boolean-Typ-Eigenschaft hat den Standardwert false, jedoch werden bei Einstellung auf true die Grid-Linien für den verfügbaren Datenbereich im HTML-Format gerendert.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den detaillierten Artikel zu [Grid-Linien in HTML rendern](/cells/de/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügte ListObject.Comment Eigenschaft**
Die Aspose.Cells APIs ermöglichen es jetzt, die Kommentare für eine Instanz von ListObject abzurufen und zu setzen. Um diese Funktion zu ermöglichen, haben die Aspose.Cells APIs die Eigenschaft ListObject.Comment freigelegt.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den detaillierten Artikel zu [Hinzufügen von Kommentaren für ListObjects](/cells/de/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
## **Entfernte APIs**
### **Entfernte Workbook.decrypt Methode**
Die genannte Eigenschaft wurde vor einiger Zeit veraltet. In dieser Version wurde sie vollständig aus der öffentlichen API entfernt. Es wird empfohlen, die Eigenschaft WorkbookSettings.Password auf null zu setzen, um dasselbe Ziel zu erreichen.
