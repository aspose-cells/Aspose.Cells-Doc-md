---
title: Общедоступный API Изменения в Aspose.Cells 8.8.3
type: docs
weight: 300
url: /ru/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.8.2 до 8.8.3, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка элементов управления ActiveX**
Aspose.Cells for Java 8.8.3 предоставил метод addActiveXControl, который позволяет добавить элемент управления ActiveX в ShapeCollection. Вышеупомянутый метод требует 7 параметров для указания типа элемента управления, места для размещения элемента управления и размера элемента управления. Тип можно указать с помощью перечисления ControlType со следующими возможными значениями.

1. Тип управления.CHECK_BOX
1. Тип управления.COMBO_BOX
1. Тип управления.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. Тип управления.LIST_BOX
1. Тип управления.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. Тип управления.SPIN_BUTTON
1. Тип управления.TEXT_BOX
1. Тип управления.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Добавление элементов управления ActiveX на рабочий лист](/cells/ru/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

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
### **Добавлен метод LoadOptions.setPaperSize.**
Aspose.Cells for Java 8.8.3 позволяет установить размер бумаги для печати по умолчанию из настроек принтера по умолчанию при использовании нового открытого метода LoadOptions.setPaperSize, как показано ниже. Обратите внимание, что входным параметром вышеупомянутого метода является значение из перечисления PaperSizeType, содержащего предопределенные размеры бумаги.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Загрузка электронных таблиц с указанным размером бумаги](/cells/ru/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Добавлен метод Cell.getCharacters(flag)**
Aspose.Cells API позволяют получить объекты символов в виде массива FontSetting с помощью метода Cell.getCharacters. В этом выпуске Aspose.Cells for Java API представлена перегруженная версия Cell.getCharacters, которая может принимать логическое значение в качестве параметра, указывающего, должен ли стиль таблицы применяться к ячейке, если ячейка является частью ListObject.

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
### **Добавлено свойство OleObject.AutoLoad**
Aspose.Cells for Java 8.8.3 предоставляет свойство OleObject.AutoLoad, которое позволяет обновлять изображение OleObject, если содержимое/данные базового объекта были изменены. Вышеупомянутое свойство, если установлено значение true, заставляет приложение Excel обновлять изображение OleObject при загрузке результирующей электронной таблицы.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Автоматически обновлять OleObjects](/cells/ru/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

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
### **Добавлено свойство HTMLLoadOptions.SupportDivTag.**
Aspose.Cells for Java 8.8.3 предоставляет свойство HTMLLoadOptions.SupportDivTag, которое позволяет анализировать теги DIV, встроенные в теги TD, при загрузке файлов/фрагментов HTML в объектной модели Aspose.Cells. Свойство логического типа имеет значение по умолчанию false.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Поддержка внутренних тегов DIV при загрузке HTML](/cells/ru/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

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
### **Добавлено свойство HtmlSaveOptions.ExportGridLines.**
Aspose.Cells for Java 8.8.3 предоставляет свойство HtmlSaveOptions.ExportGridLines, которое позволяет отображать линии сетки при экспорте электронной таблицы в формат HTML. Свойство логического типа по умолчанию имеет значение false, однако, если установлено значение true, API отображает линии сетки для доступного диапазона данных в формате HTML.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Рендеринг линий сетки в HTML](/cells/ru/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

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
### **Добавлено свойство ListObject.Comment**
Aspose.Cells API теперь позволяют получать и устанавливать комментарии для экземпляра ListObject. Чтобы обеспечить вышеупомянутую функцию, API-интерфейсы Aspose.Cells предоставили свойство ListObject.Comment.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Добавление комментариев для ListObjects](/cells/ru/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

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
## **Удаленные API**
### **Удален метод Workbook.decrypt**
Некоторое время назад указанное имущество было признано устаревшим. В этом выпуске он полностью удален из общего доступа API. Для достижения той же цели рекомендуется установить для свойства WorkbookSettings.Password значение null.
