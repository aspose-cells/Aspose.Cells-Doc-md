---
title: Изменения в публичном API в Aspose.Cells 8.8.1
type: docs
weight: 280
url: /ru/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.8.0 до 8.8.1, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т.д., но также описание любых изменений в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Фильтрация данных при загрузке**
Aspose.Cells for Java 8.8.1 добавило перечисление LoadDataFilterOptions вместе со свойством LoadOptions.LoadDataFilterOptions, которое можно использовать для указания типа данных, который должен быть загружен при создании рабочей книги из шаблонного файла. Фильтрация загруженных данных может улучшить производительность для особых целей, особенно при использовании LightCells API.

Перечисление LoadDataFilterOptions предоставляет следующие варианты выбора.

1. ALL для загрузки всего из электронной таблицы.
1. NONE для загрузки ничего из электронной таблицы.
1. CELL_BLANK загружает ячейки, значения которых пусты.
1. CELL_BOOL загружает ячейки, значения которых являются логическими.
1. CELL_DATA загружает данные ячеек, включая значения, формулы и форматирование.
1. CELL_ERROR загружает ячейки, значения которых являются ошибками.
1. CELL_NUMERIC загружает ячейки, значения которых являются числовыми (включая даты и время).
1. CELL_STRING загружает ячейки, значения которых являются текстовыми/строковыми.
1. CELL_VALUE загружает только значения ячеек (все типы).
1. CHART загружает только графики.
1. CONDITIONAL_FORMATTING загружает только правила условного форматирования.
1. DATA_VALIDATION загружает только правила проверки данных.
1. DOCUMENT_PROPERTIES загружает только свойства документа.
1. FORMULA загружает формулы, включая определенные имена.
1. MERGED_AREA загружает только объединенные ячейки.
1. PIVOT_TABLE загружает сводные таблицы.
1. SETTINGS загружает только настройки книги и листов.
1. SHAPE загружает только формы.
1. STYLE загружает форматирование ячеек.
1. TABLE загружает таблицы Excel/Объекты списков.

{{% alert color="primary" %}} 

Для получения более подробной информации об этой функции, пожалуйста, ознакомьтесь с подробной статьей по [Фильтрации данных для загрузки](/cells/ru/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Преобразование графика в PDF напрямую**
API Aspose.Cells уже предоставило возможность рендеринга графиков в PDF с помощью метода Chart.toPdf. В этом выпуске API предоставило еще одну версию этого метода, которая может принимать экземпляр OutputStream, позволяя пользователям сохранять PDF-файл графика в экземпляр ByteArrayOutputStream.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **Добавлено свойство WorkbookSettings.PaperSize**
Aspose.Cells for Java 8.8.1 предоставил свойство WorkbookSettings.PaperSize для установки размера бумаги по умолчанию для всей электронной таблицы. Свойство WorkbookSettings.PaperSize принимает значение из перечисления PaperSizeType, которое содержит предопределенные размеры для наиболее часто используемых типов печатной бумаги.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Добавлено свойство Shape.TextBody**
В данной версии Aspose.Cells for Java API было добавлено свойство Shape.TextBody для управления аспектами текста в форме. В следующем фрагменте использовано это свойство для установки эффекта тени текста в текстовом поле.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье по ссылке [Установка тени для текста](/cells/ru/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Добавлен метод Worksheet.calculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for Java 8.8.1 добавил перегрузку метода Worksheet.calculateFormula, которая позволяет вычислить заданную формулу непосредственно с настраиваемыми параметрами.

{{% alert color="primary" %}} 

Дополнительные сведения об этой функции можно найти в подробной статье по ссылке [Прямое вычисление пользовательской функции](/cells/ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Добавлен метод GridCell.createValidation**
Aspose.Cells.GridWeb предоставила возможность напрямую добавлять правило проверки к одной ячейке при использовании метода GridCell.createValidation. Указанный метод требует 2 параметра. Первый из них имеет тип GridValidationType, который определяет тип проверки, в то время как второй параметр (isRequied) имеет тип Boolean.

**Java**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **Добавлен метод GridCell.removeValidation**
Aspose.Cells.GridWeb также предоставила возможность удалять правило проверки данных из GridCell при использовании метода GridCell.removeValidation.
## **Устаревшие API**
### **Устаревшее свойство Shape.TextFrame**
Рекомендуется использовать свойство Shape.TextBody.TextAlignment вместо.
