---
title: Общедоступный API Изменения в Aspose.Cells 8.8.1
type: docs
weight: 280
url: /ru/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.8.0 до 8.8.1, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Отфильтровать данные для загрузки**
Aspose.Cells for Java 8.8.1 предоставляет перечисление LoadDataFilterOptions вместе со свойством LoadOptions.LoadDataFilterOptions, которое можно использовать для указания типа данных, которые должны быть загружены при создании книги из файла шаблона. Фильтрация загружаемых данных может повысить производительность для специальных целей, особенно при использовании API LightCells.

Перечисление LoadDataFilterOptions предоставляет следующие варианты выбора.

1. ALL, чтобы загрузить все из электронной таблицы.
1. NONE, чтобы ничего не загружать из электронной таблицы.
1. CELL_BLANK загружает ячейки, значения которых пусты.
1. CELL_BOOL загружает ячейки, значения которых являются логическими.
1. CELL_DATA загружает данные ячеек, включая значения, формулы и форматирование.
1. CELL_ERROR загружает ячейки, значения которых ошибочны.
1. CELL_NUMERIC загружает ячейки, значения которых являются числовыми (включая дату и время).
1. CELL_STRING загружает ячейки, значениями которых являются текст/строка.
1. CELL_VALUE загружает только значения ячеек (всех типов).
1. CHART загружает только графики.
1. CONDITIONAL_FORMATTING загружает только правила условного форматирования.
1. DATA_VALIDATION загружает только правила проверки данных.
1. DOCUMENT_PROPERTIES загружает только свойства документа.
1. FORMULA загружает формулы, включая определенные имена.
1. MERGED_AREA загружает только объединенные ячейки.
1. PIVOT_TABLE загружает сводные таблицы.
1. SETTINGS загружает только настройки рабочей книги и рабочего листа.
1. SHAPE загружает только фигуры.
1. СТИЛЬ загружает форматирование ячеек.
1. TABLE загружает таблицы Excel/объекты списка.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Фильтровать данные для загрузки](/cells/ru/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Прямое преобразование диаграммы в PDF**
API-интерфейсы Aspose.Cells уже предоставили возможность отображать диаграммы на PDF при использовании метода Chart.toPdf. В этом выпуске API представлена другая перегруженная версия указанного метода, которая может принимать экземпляр OutputStream, позволяя пользователям сохранять PDF диаграммы в экземпляре ByteArrayOutputStream.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

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
### **Добавлено свойство WorkbookSettings.PaperSize.**
Aspose.Cells for Java 8.8.1 предоставил свойство WorkbookSettings.PaperSize, чтобы установить размер бумаги для печати по умолчанию для всей электронной таблицы. Свойство WorkbookSettings.PaperSize принимает значение из перечисления PaperSizeType, которое содержит предопределенные размеры для наиболее широко используемых типов бумаги для печати.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Добавлено свойство Shape.TextBody**
В этом выпуске Aspose.Cells for Java API объект Shape.TextBody используется для управления аспектами текста в фигурах. В следующем фрагменте указанное свойство используется для установки эффекта тени текста в TextBox.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Настройка эффекта тени для текста](/cells/ru/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Создаем экземпляр Workbook

Книга рабочей книги = новая рабочая книга();

//Доступ к первому рабочему листу рабочей книги

Рабочий лист = book.getWorksheets().get(0);

// Добавляем TextBox в ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = лист.getTextBoxes().get(index);

//Устанавливаем текст TextBox

textBox.setText("Этот текст имеет следующие настройки.\n\nТекстовые эффекты > Тень > Смещение снизу");

//Устанавливаем эффект тени для текста

 для (целое я = 0; я< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Добавлен метод Worksheet.calculateFormula(строковая формула, параметры CalculationOptions)**
Aspose.Cells for Java 8.8.1 представила еще одну перегрузку для метода Worksheet.calculateFormula, который позволяет вычислять заданную формулу напрямую с пользовательскими параметрами.

{{% alert color="primary" %}} 

 Дополнительные сведения об этой функции см. в подробной статье о[Прямой расчет пользовательской функции](/cells/ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Добавлен метод GridCell.createValidation.**
Aspose.Cells.GridWeb предоставляет возможность напрямую добавлять правило проверки в одну ячейку при использовании метода GridCell.createValidation. Указанный метод требует 2 параметра. Первый параметр имеет тип GridValidationType, который определяет тип проверки, тогда как второй параметр (isRequied) имеет тип Boolean.

**Java**

{{< highlight "csharp" >}}

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
### **Добавлен метод GridCell.removeValidation.**
Aspose.Cells.GridWeb также предоставляет возможность удалить правило проверки данных из GridCell при использовании метода GridCell.removeValidation.
## **Устаревшие API**
### **Устаревшее свойство Shape.TextFrame**
Вместо этого рекомендуется использовать свойство Shape.TextBody.TextAlignment.
