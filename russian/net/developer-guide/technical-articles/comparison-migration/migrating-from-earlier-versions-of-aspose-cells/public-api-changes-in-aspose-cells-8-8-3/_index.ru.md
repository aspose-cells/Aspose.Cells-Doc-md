---
title: Изменения в открытом API в Aspose.Cells 8.8.3
type: docs
weight: 290
url: /ru/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.2 на 8.8.3, которые могут быть интересны разработчикам модулей/приложений. Он содержит не только новые и обновленные открытые методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка ActiveX контролов**
Aspose.Cells for .NET 8.8.3 добавил метод AddActiveXControl, который позволяет добавить элемент ActiveX в ShapeCollection. Упомянутый метод требует 7 параметров для указания типа элемента управления, местоположения для его размещения и размера элемента управления. Тип можно указать с использованием перечисления ControlType со следующими возможными значениями.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, прочитайте подробную статью о [Добавлении элементов ActiveX в лист Excel](/cells/ru/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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


### **Добавлен метод LoadOptions.SetPaperSize**
Aspose.Cells for .NET 8.8.3 позволяет установить размер бумаги по умолчанию из настроек стандартного принтера при использовании вновь открытого метода LoadOptions.SetPaperSize, как показано ниже. Пожалуйста, обратите внимание, что входным параметром к вышеупомянутому методу является значение из перечисления PaperSizeType, содержащее предопределенные размеры бумаги.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, прочтите подробную статью о [Загрузке таблиц со специфическим размером бумаги](/cells/ru/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Добавлен метод Cell.GetCharacters(flag)**
API Aspose.Cells позволяет получить объекты символов в виде массива FontSetting с помощью метода Cell.GetCharacters. С этим выпуском Aspose.Cells for .NET API предоставил перегруженную версию Cell.GetCharacters, которая может принимать параметр Boolean, указывающий, должен ли применяться стиль таблицы к ячейке, если ячейка является частью ListObject.

**C#**

{{< highlight csharp >}}

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


### **Ниже представлен простой сценарий использования.**
Aspose.Cells for .NET 8.8.3 предоставил свойство OleObject.AutoLoad, которое позволяет обновить изображение OleObject, если содержимое/данные внутреннего объекта были изменены. Упомянутое свойство, когда установлено в true, заставляет приложение Excel обновить изображение OleObject при загрузке результирующей таблицы.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, прочтите подробную статью о [Автоматическом обновлении OleObjects](/cells/ru/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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


### **Добавлено свойство HTMLLoadOptions.SupportDivTag**
Aspose.Cells for .NET 8.8.3 предоставил свойство HTMLLoadOptions.SupportDivTag, которое позволяет преобразовывать DIV-теги, вложенные в TD-теги при загрузке HTML-файлов/фрагментов в объектную модель Aspose.Cells. Свойство типа Boolean имеет значение по умолчанию false.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, прочтите подробную статью о [Поддержке внутренних тегов DIV при загрузке HTML](/cells/ru/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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


### **Добавлено свойство HtmlSaveOptions.ExportGridLines**
Aspose.Cells for .NET 8.8.3 предоставил свойство HtmlSaveOptions.ExportGridLines, которое позволяет отображать линии сетки при экспорте таблицы в формат HTML. Свойство типа Boolean имеет значение по умолчанию false, однако, установив его в true, API отображает линии сетки для доступного диапазона данных в формате HTML.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, прочтите подробную статью о [Отображении линий сетки в формате HTML](/cells/ru/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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
Теперь API Aspose.Cells позволяет получать и устанавливать комментарии для экземпляра ListObject. Для предоставления упомянутой функции API Aspose.Cells предоставил свойство ListObject.Comment.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, пожалуйста, прочтите подробную статью на тему [Добавление комментариев для ListObjects](/cells/ru/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

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


### **Добавлено свойство GridWeb.SessionStorePath**
Aspose.Cells.GridWeb для .NET 8.8.3 представил свойство SessionStorePath, которое позволяет получить или установить путь хранения сеанса при режиме сеанса ViewState. Упомянутое свойство получает или устанавливает относительный путь к текущему каталогу базового веб-приложения.

{{% alert color="primary" %}} 

Для получения дополнительной информации об этой функции, пожалуйста, ознакомьтесь с подробной статьей о [Указании пути для временных файлов сеанса](/cells/ru/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Вот простой сценарий использования.
## **Удалены API**
### **Удален метод Workbook.Decrypt**
Указанное свойство было помечено как устаревшее некоторое время назад. В этом релизе оно было полностью удалено из общедоступного API. Рекомендуется установить свойство WorkbookSettings.Password в null для достижения того же результата.
