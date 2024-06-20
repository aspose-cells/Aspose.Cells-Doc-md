---
title: Изменения в публичном API в Aspose.Cells 8.8.1
type: docs
weight: 270
url: /ru/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.0 до 8.8.1, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т.д., но также описание любых изменений в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Фильтрация данных при загрузке**
Aspose.Cells for .NET 8.8.1 предоставил перечисление LoadDataFilterOptions вместе с свойством LoadOptions.LoadDataFilterOptions, которое можно использовать для указания типа данных, которые должны быть загружены при построении рабочей книги из файла шаблона. Фильтрация загруженных данных может улучшить производительность для особых целей, особенно при использовании LightCells APIs.

Перечисление LoadDataFilterOptions предоставляет следующие варианты выбора.

1. All для загрузки всего из электронной таблицы.
1. None для загрузки ничего из электронной таблицы.
1. CellBlank для загрузки ячеек, значение которых пусто.
1. CellBool для загрузки ячеек, значение которых представляет булев тип.
1. CellData загружает данные ячеек, включая значения, формулы и форматирование.
1. CellError загружает ячейки со значением ошибки.
1. CellNumeric загружает ячейки со значениями числового типа (включая дату и время).
1. CellString загружает ячейки со значениями текста/строки.
1. CellValue загружает только значения ячеек (все типы).
1. Chart загружает только диаграммы.
1. ConditionalFormatting загружает только правила условного форматирования.
1. DataValidation загружает только правила проверки данных.
1. DocumentProperties загружает только свойства документа.
1. Formula загружает формулы, включая определенные имена.
1. MergedArea загружает только объединенные ячейки.
1. PivotTable загружает сводные таблицы.
1. Settings загружает только настройки книги и листа.
1. Shape загружает только формы.
1. Style загружает форматирование ячеек.
1. Table загружает таблицы Excel/Объекты списка.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, ознакомьтесь со статьей [Фильтрация загружаемых данных](/cells/ru/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Преобразование графика в PDF напрямую**
API Aspose.Cells уже предоставило возможность отображать диаграммы в PDF с помощью метода Chart.ToPdf. В этом релизе API предоставлен еще один перегруженный вариант указанного метода, который может принимать экземпляр Stream, что позволяет пользователям сохранять PDF диаграммы в экземпляре MemoryStream.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **Добавлено свойство WorkbookSettings.PaperSize**
Aspose.Cells for .NET 8.8.1 добавил свойство WorkbookSettings.PaperSize для установки размера бумаги по умолчанию для всего электронного таблицы. Свойство WorkbookSettings.PaperSize принимает значение из перечисления PaperSizeType, которое содержит предопределенные размеры для наиболее часто используемых типов печатной бумаги.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Добавлено свойство Shape.TextBody**
В этом релизе Aspose.Cells for .NET API было добавлено свойство Shape.TextBody для управления аспектами текста в фигурах. Приведенный ниже отрывок использует данное свойство для установки эффекта тени текста в TextBox.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции ознакомьтесь с подробной статьей по ссылке [Установка эффекта тени для текста](/cells/ru/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Добавлен метод Worksheet.CalculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for .NET 8.8.1 добавил еще одну перегрузку метода CalculateFormula, которая обеспечивает возможность вычисления заданной формулы непосредственно с настраиваемыми параметрами.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции ознакомьтесь с подробной статьей по ссылке [Прямой расчет пользовательской функции](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Добавлен метод GridCell.CreateValidation**
Aspose.Cells.GridWeb предоставляет возможность добавления правила проверки данных для одной ячейки непосредственно с использованием метода GridCell.CreateValidation. Данный метод требует 2 параметра. Первый из них имеет тип GridValidationType, который определяет тип проверки, в то время как второй параметр (isRequied) имеет тип Boolean.



**C#**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **Добавлен метод GridCell.RemoveValidation**
Aspose.Cells.GridWeb также предоставляет возможность удаления правила проверки данных из GridCell с использованием метода GridCell.RemoveValidation.
## **Устаревшие API**
### **Устаревшее свойство Shape.TextFrame**
Рекомендуется использовать свойство Shape.TextBody.TextAlignment вместо.
