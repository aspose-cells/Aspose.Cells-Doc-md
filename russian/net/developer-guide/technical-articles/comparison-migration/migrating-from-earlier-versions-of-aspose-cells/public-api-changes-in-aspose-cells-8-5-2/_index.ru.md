---
title: Общедоступный API Изменения в Aspose.Cells 8.5.2
type: docs
weight: 180
url: /ru/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.5.1 до 8.5.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/net/public-api-changes-in-aspose-cells-8-5-2/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Рендеринг рабочего листа в графическом контексте**
 В этом выпуске Aspose.Cells for .NET API представлены две новые перегрузки метода SheetRender.ToImage, которые теперь позволяют принимать экземпляр класса System.Drawing.Graphics для[визуализировать в графическом контексте](/cells/ru/net/render-worksheet-to-graphic-context/). Сигнатуры недавно добавленных методов следующие.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage (int pageIndex, Graphics g, float x, float y, ширина float, высота float)

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлен метод PivotTable.GetCellByDisplayName**
 Aspose.Cells for .NET 8.5.2 предоставил метод PivotTable.GetCellByDisplayName, который можно использовать для[получить объект Cell по имени PivotField](/cells/ru/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Этот метод может быть полезен в сценариях, когда вы хотите выделить или отформатировать заголовок PivotField.

Ниже приведен простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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


### **Свойство SaveOptions.MergeAreas добавлено**
Aspose.Cells for .NET 8.5.2 предоставил свойство SaveOptions.MergeAreas, которое может принимать значение логического типа. Значение по умолчанию — false, однако, если установлено значение true, Aspose.Cells for .NET API пытается объединить отдельные CellArea перед сохранением файла.

{{% alert color="primary" %}} 

Если в электронной таблице слишком много отдельных ячеек с примененной проверкой, есть вероятность, что результирующая электронная таблица может быть повреждена. Одним из возможных решений является объединение ячеек с идентичными правилами проверки, или теперь вы можете использовать свойство SaveOptions.MergeAreas, чтобы указать API для автоматического объединения ячеек CellAreas перед операцией сохранения.

{{% /alert %}} 
### **Добавлено свойство Shape.Geometry.ShapeAdjustValues**
 В выпуске v8.5.2 Aspose.Cells API предоставил свойство Shape.Geometry.ShapeAdjustValues, которое можно использовать для[вносить изменения в точки регулировки разных форм](/cells/ru/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

В интерфейсе Excel Microsoft точки корректировки отображаются в виде желтых ромбовидных узлов.

{{% /alert %}} 

Например,

1. Прямоугольник со скругленными углами имеет настройку для изменения дуги.
1. Треугольник имеет корректировку для изменения положения точки
1. Трапеция имеет регулировку для изменения ширины верха.
1. Стрелы имеют две регулировки для изменения формы головы и хвоста.

Вот самый простой сценарий использования.

**C#**

{{< highlight "csharp" >}}

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


### **Добавлено поле перечисления ConsolidationFunction.DistinctCount.**
 Aspose.Cells for .NET 8.5.2 предоставил поле ConsolidationFunction.DistinctCount, которое можно использовать для[применить функцию консолидации Distinct Count](/cells/ru/net/consolidation-function/) в поле данных сводной таблицы.

{{% alert color="primary" %}} 

Функция консолидации Distinct Count поддерживается только в версии Microsoft Excel 2013.

{{% /alert %}} 
### **Улучшенная обработка событий для GridDesktop**
В этом выпуске Aspose.Cells.GridDesktop представлены 4 новых события. 2 из этих событий запускаются при различных состояниях загрузки файлов электронных таблиц в GridDesktop, тогда как другие 2 запускаются при вычислении формул.

События перечислены следующим образом.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
