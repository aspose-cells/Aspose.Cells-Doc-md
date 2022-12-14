---
title: Общедоступный API Изменения в Aspose.Cells 8.8.3
type: docs
weight: 290
url: /ru/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

Этот документ описывает изменения в Aspose.Cells API с версии 8.8.2 до 8.8.3, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка элементов управления ActiveX**
Aspose.Cells for .NET 8.8.3 предоставил метод AddActiveXControl, который позволяет добавить элемент управления ActiveX в ShapeCollection. Вышеупомянутый метод требует 7 параметров для указания типа элемента управления, места для размещения элемента управления и размера элемента управления. Тип можно указать с помощью перечисления ControlType со следующими возможными значениями.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ТипКонтроля.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Добавление элементов управления ActiveX на рабочий лист](/cells/ru/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Добавлен метод LoadOptions.SetPaperSize.**
Aspose.Cells for .NET 8.8.3 позволяет установить размер бумаги для печати по умолчанию из настроек принтера по умолчанию при использовании нового открытого метода LoadOptions.SetPaperSize, как показано ниже. Обратите внимание, что входным параметром вышеупомянутого метода является значение из перечисления PaperSizeType, содержащего предопределенные размеры бумаги.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Загрузка электронных таблиц с указанным размером бумаги](/cells/ru/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Добавлен метод Cell.GetCharacters(flag)**
Aspose.Cells API позволяют получить объекты символов в виде массива FontSetting с помощью метода Cell.GetCharacters. В этом выпуске Aspose.Cells for .NET API представлена перегруженная версия Cell.GetCharacters, которая может принимать логическое значение в качестве параметра, указывающего, должен ли стиль таблицы применяться к ячейке, если ячейка является частью ListObject.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **Добавлено свойство OleObject.AutoLoad**
Aspose.Cells for .NET 8.8.3 предоставляет свойство OleObject.AutoLoad, которое позволяет обновлять изображение OleObject, если содержимое/данные базового объекта были изменены. Вышеупомянутое свойство, если установлено значение true, заставляет приложение Excel обновлять изображение OleObject при загрузке результирующей электронной таблицы.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Автоматически обновлять OleObjects](/cells/ru/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **Добавлено свойство HTMLLoadOptions.SupportDivTag.**
Aspose.Cells for .NET 8.8.3 предоставляет свойство HTMLLoadOptions.SupportDivTag, которое позволяет анализировать теги DIV, встроенные в теги TD, при загрузке файлов/фрагментов HTML в объектной модели Aspose.Cells. Свойство логического типа имеет значение по умолчанию false.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Поддержка внутренних тегов DIV при загрузке HTML](/cells/ru/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **Добавлено свойство HtmlSaveOptions.ExportGridLines.**
Aspose.Cells for .NET 8.8.3 предоставляет свойство HtmlSaveOptions.ExportGridLines, которое позволяет отображать линии сетки при экспорте электронной таблицы в формат HTML. Свойство логического типа по умолчанию имеет значение false, однако, если установлено значение true, API отображает линии сетки для доступного диапазона данных в формате HTML.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Рендеринг линий сетки в HTML](/cells/ru/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Добавлено свойство ListObject.Comment**
Aspose.Cells API теперь позволяют получать и устанавливать комментарии для экземпляра ListObject. Чтобы обеспечить вышеупомянутую функцию, API-интерфейсы Aspose.Cells предоставили свойство ListObject.Comment.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Добавление комментариев для ListObjects](/cells/ru/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Добавлено свойство GridWeb.SessionStorePath.**
Aspose.Cells.GridWeb for .NET 8.8.3 предоставляет свойство SessionStorePath, которое позволяет получить или задать путь к хранилищу сеансов, когда режим сеанса установлен на ViewState. Вышеупомянутое свойство получает или задает относительный путь к текущему базовому каталогу веб-приложения.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Укажите путь для временных файлов сеанса](/cells/ru/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.
## **Удаленные API**
### **Удален метод Workbook.Decrypt**
Некоторое время назад указанное имущество было признано устаревшим. В этом выпуске он полностью удален из общего доступа API. Для достижения той же цели рекомендуется установить для свойства WorkbookSettings.Password значение null.
