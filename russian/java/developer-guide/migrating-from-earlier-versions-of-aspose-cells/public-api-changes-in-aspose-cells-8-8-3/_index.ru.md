---
title: Изменения в открытом API в Aspose.Cells 8.8.3
type: docs
weight: 300
url: /ru/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.2 на 8.8.3, которые могут быть интересны разработчикам модулей/приложений. Он содержит не только новые и обновленные открытые методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка ActiveX контролов**
Aspose.Cells for Java 8.8.3 предоставил метод addActiveXControl, который позволяет добавлять ActiveX контрол в ShapeCollection. Упомянутый метод требует 7 параметров для указания типа контроля, расположения контроля и размера контроля. Тип можно указать, используя перечисление ControlType со следующими возможными значениями.

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

Для получения дополнительной информации о этой функции, ознакомьтесь с подробной статьей по ссылке [Добавление ActiveX контролов на листе](/cells/ru/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Вот простой сценарий использования.

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
### **Добавлен метод LoadOptions.setPaperSize**
Aspose.Cells for Java 8.8.3 позволяет устанавливать размер бумаги по умолчанию из настроек дефолтного принтера при использовании нового метода LoadOptions.setPaperSize, как показано ниже. Обратите внимание, что входным параметром для указанного метода является значение из перечисления PaperSizeType, содержащее предопределенные размеры бумаги.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье [Загрузка электронных таблиц с указанным форматом печати](/cells/ru/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Добавлен метод Cell.getCharacters(flag)**
API Aspose.Cells позволяет получать объекты символов в виде массива FontSetting с помощью метода Cell.getCharacters. В этом релизе API Aspose.Cells for Java предоставил перегруженную версию метода Cell.getCharacters, которая может принимать в качестве параметра логическое значение, указывающее, должен ли применяться стиль таблицы к ячейке, если ячейка является частью ListObject.

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
### **Ниже представлен простой сценарий использования.**
Aspose.Cells for Java 8.8.3 предоставил свойство OleObject.AutoLoad, которое позволяет обновлять изображение OleObject, если содержимое/данные базового объекта были изменены. Упомянутое свойство, установленное в true, заставляет приложение Excel обновлять изображение OleObject при загрузке результирующей электронной таблицы.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье [Автоматическое обновление OleObjects](/cells/ru/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Вот простой сценарий использования.

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
### **Добавлено свойство HTMLLoadOptions.SupportDivTag**
Aspose.Cells for Java 8.8.3 предоставил свойство HTMLLoadOptions.SupportDivTag, которое позволяет парсить вложенные теги DIV в тегах TD при загрузке HTML-файлов/фрагментов в объектную модель Aspose.Cells. Свойство типа Boolean имеет значение по умолчанию false.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье [Поддержка внутренних тегов DIV при загрузке HTML](/cells/ru/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Вот простой сценарий использования.

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
### **Добавлено свойство HtmlSaveOptions.ExportGridLines**
Aspose.Cells for Java 8.8.3 предоставил свойство HtmlSaveOptions.ExportGridLines, которое позволяет отображать линии сетки при экспорте электронной таблицы в формат HTML. Свойство типа Boolean имеет значение по умолчанию false, однако, установленное в true, API отображает линии сетки для доступного диапазона данных в формате HTML.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье [Отображение линий сетки в HTML](/cells/ru/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Вот простой сценарий использования.

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
### **Добавлено свойство ListObject.Comment**
Теперь API Aspose.Cells позволяет получать и устанавливать комментарии для экземпляра ListObject. Для предоставления упомянутой функции API Aspose.Cells предоставил свойство ListObject.Comment.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье [Добавление комментариев к ListObjects](/cells/ru/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Вот простой сценарий использования.

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
## **Удалены API**
### **Удален метод Workbook.decrypt**
Указанное свойство было помечено как устаревшее некоторое время назад. В этом релизе оно было полностью удалено из общедоступного API. Рекомендуется установить свойство WorkbookSettings.Password в null для достижения того же результата.
{{< app/cells/assistant language="java" >}}
