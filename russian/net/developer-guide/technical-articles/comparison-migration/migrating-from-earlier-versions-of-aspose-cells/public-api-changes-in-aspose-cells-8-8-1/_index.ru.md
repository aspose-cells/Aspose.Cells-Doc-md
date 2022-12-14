---
title: Общедоступный API Изменения в Aspose.Cells 8.8.1
type: docs
weight: 270
url: /ru/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.8.0 до 8.8.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Отфильтровать данные для загрузки**
Aspose.Cells for .NET 8.8.1 предоставляет перечисление LoadDataFilterOptions вместе со свойством LoadOptions.LoadDataFilterOptions, которое можно использовать для указания типа данных, которые должны быть загружены при создании книги из файла шаблона. Фильтрация загружаемых данных может повысить производительность для специальных целей, особенно при использовании API LightCells.

Перечисление LoadDataFilterOptions предоставляет следующие варианты выбора.

1. All для загрузки всего из электронной таблицы.
1. Нет, чтобы ничего не загружать из электронной таблицы.
1. CellBlank загружает ячейки, значения которых пусты.
1. CellBool загружает ячейки, значения которых являются логическими.
1. CellData загружает данные ячеек, включая значения, формулы и форматирование.
1. CellError загружает ячейки, значения которых ошибочны.
1. CellNumeric загружает ячейки, значения которых являются числовыми (включая дату и время).
1. CellString загружает ячейки, значениями которых являются текст/строка.
1. CellValue загружает только значения ячеек (всех типов).
1. Chart загружает только графики.
1. ConditionalFormatting загружает только правила условного форматирования.
1. DataValidation загружает только правила проверки данных.
1. DocumentProperties загружает только свойства документа.
1. Формула загружает формулы, включая определенные имена.
1. MergedArea загружает только объединенные ячейки.
1. PivotTable загружает сводные таблицы.
1. Настройки загружают только настройки рабочей книги и рабочего листа.
1. Форма загружает только фигуры.
1. Стиль загружает форматирование ячеек.
1. Таблица загружает таблицы Excel/объекты списка.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Фильтровать данные для загрузки](/cells/ru/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Прямое преобразование диаграммы в PDF**
Aspose.Cells API-интерфейсы уже предоставляют возможность рендеринга диаграмм в PDF при использовании метода Chart.ToPdf. В этом выпуске API представлена еще одна перегруженная версия указанного метода, которая может принимать экземпляр Stream, позволяя пользователям сохранять PDF-файл диаграммы в экземпляре MemoryStream.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлено свойство WorkbookSettings.PaperSize.**
Aspose.Cells for .NET 8.8.1 предоставил свойство WorkbookSettings.PaperSize, чтобы установить размер бумаги для печати по умолчанию для всей электронной таблицы. Свойство WorkbookSettings.PaperSize принимает значение из перечисления PaperSizeType, которое содержит предопределенные размеры для наиболее широко используемых типов бумаги для печати.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Добавлено свойство Shape.TextBody**
В этом выпуске Aspose.Cells for .NET API объект Shape.TextBody используется для управления аспектами текста в фигурах. В следующем фрагменте указанное свойство используется для установки эффекта тени текста в TextBox.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Настройка эффекта тени для текста](/cells/ru/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 //Создаем экземпляр Workbook

var book = новая рабочая книга();

//Доступ к первому рабочему листу рабочей книги

лист var = book.Worksheets[0];

// Добавляем TextBox в ShapeCollection

var textBox = лист.Фигуры.Добавитьтекстовое поле(2, 0, 2, 0, 100, 400);

//Устанавливаем текст TextBox

textBox.Text = "Этот текст имеет следующие настройки.\n\nТекстовые эффекты > Тень > Смещение нижнего края";

//Устанавливаем эффект тени для текста

 для (целое я = 0; я< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Добавлен метод Worksheet.CalculateFormula(строковая формула, параметры CalculationOptions)**
Aspose.Cells for .NET 8.8.1 предоставляет другую перегрузку для метода CalculateFormula, который обеспечивает возможность прямого вычисления заданной формулы с пользовательскими параметрами.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Прямой расчет пользовательской функции](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Добавлен метод GridCell.CreateValidation.**
Aspose.Cells.GridWeb предоставляет возможность напрямую добавлять правило проверки в одну ячейку при использовании метода GridCell.CreateValidation. Указанный метод требует 2 параметра. Первый параметр имеет тип GridValidationType, который определяет тип проверки, тогда как второй параметр (isRequied) имеет тип Boolean.



**C#**

{{< highlight "csharp" >}}

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


### **Добавлен метод GridCell.RemoveValidation.**
Aspose.Cells.GridWeb также предоставляет возможность удалить правило проверки данных из GridCell при использовании метода GridCell.RemoveValidation.
## **Устаревшие API**
### **Устаревшее свойство Shape.TextFrame**
Вместо этого рекомендуется использовать свойство Shape.TextBody.TextAlignment.
