---
title: Изменения в публичном API в Aspose.Cells 8.5.2
type: docs
weight: 180
url: /ru/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

В этом документе описаны изменения в общем API Aspose.Cells с версии 8.5.1 до 8.5.2, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-5-2/), но также описание любых изменений в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Отобразить Рабочий лист на графический контекст**
Этот релиз API Aspose.Cells for .NET предоставил две новые перегрузки метода SheetRender.ToImage, которые теперь позволяют принять экземпляр класса System.Drawing.Graphics для [отрисовки в контексте графики](/cells/ru/net/render-worksheet-to-graphic-context/). Сигнатуры добавленных методов следующие.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **Добавлен метод PivotTable.GetCellByDisplayName.**
Aspose.Cells for .NET 8.5.2 вывел метод PivotTable.GetCellByDisplayName, который можно использовать для [получения объекта Cell по имени поля отчетной таблицы](/cells/ru/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Этот метод может быть полезен в сценариях, где требуется выделить или форматировать заголовок поля отчетной таблицы.

Вот простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Добавлено свойство SaveOptions.MergeAreas**
Aspose.Cells for .NET 8.5.2 вывел свойство SaveOptions.MergeAreas, которое принимает значение типа Boolean. Значение по умолчанию - false, однако, если установлено в true, API Aspose.Cells for .NET пытается объединить отдельные CellArea перед сохранением файла.

{{% alert color="primary" %}} 

Если электронная таблица содержит слишком много индивидуальных ячеек с примененной проверкой или может быть повреждена. Одно из возможных решений — объединить ячейки с идентичными условиями проверки или теперь можно использовать свойство SaveOptions.MergeAreas для указания API автоматически объединять CellArea перед операцией сохранения.

{{% /alert %}} 
### **Добавлено свойство Shape.Geometry.ShapeAdjustValues.**
С выпуском v8.5.2 API Aspose.Cells предоставил свойство Shape.Geometry.ShapeAdjustValues, которое можно использовать для [внесения изменений в точки коррекции различных форм](/cells/ru/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

В интерфейсе Microsoft Excel точки коррекции отображаются как желтые ромбовидные узлы.

{{% /alert %}} 

Например,

1. У закругленного прямоугольника есть точка коррекции для изменения дуги
1. У треугольника есть точка коррекции для изменения положения точки
1. Трапеция имеет настройку для изменения ширины верхней части
1. Стрелки имеют две настройки для изменения формы головы и хвоста

Вот самый простой сценарий использования.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **Добавлено перечисление Field ConsolidationFunction.DistinctCount.**
Aspose.Cells for .NET 8.5.2 предоставил поле ConsolidationFunction.DistinctCount, которое можно использовать для [применения функции консолидации Distinct Count](/cells/ru/net/consolidation-function/) к DataField отчетной таблицы.

{{% alert color="primary" %}} 

Функция сведения уникальных значений поддерживается только в Microsoft Excel 2013.

{{% /alert %}} 
### **Улучшен обработчик событий для GridDesktop.**
В этом выпуске Aspose.Cells.GridDesktop предоставил 4 новых события. 2 из них срабатывают в различных состояниях загрузки электронных таблиц в GridDesktop, в то время как другие 2 срабатывают при вычислении формул.

События перечислены ниже.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
{{< app/cells/assistant language="csharp" >}}
