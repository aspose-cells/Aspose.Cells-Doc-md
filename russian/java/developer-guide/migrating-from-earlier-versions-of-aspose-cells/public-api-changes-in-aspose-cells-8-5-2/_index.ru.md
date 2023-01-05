---
title: Общедоступный API Изменения в Aspose.Cells 8.5.2
type: docs
weight: 190
url: /ru/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 В этом документе описаны изменения в Aspose.Cells API с версии 8.5.1 до 8.5.2, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-5-2/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Рендеринг рабочего листа в графическом контексте**
В этом выпуске Aspose.Cells for Java API представлена другая перегрузка метода SheetRender.toImage, которая теперь позволяет принимать экземпляр класса Graphics2D для[визуализировать рабочий лист в графическом контексте](/cells/ru/java/render-worksheet-to-graphic-context/). Сигнатуры вновь добавленного метода следующие.

- SheetRender.toImage(int pageIndex, графика Graphics2D)

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **Добавлен метод PivotTable.getCellByDisplayName**
 Aspose.Cells for Java 8.5.2 предоставил метод PivotTable.getCellByDisplayName, который можно использовать для[получить объект Cell по имени PivotField](/cells/ru/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Этот метод может быть полезен в сценариях, когда вы хотите выделить или отформатировать заголовок PivotField.

Ниже приведен простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Свойство SaveOptions.MergeAreas добавлено**
Aspose.Cells for Java 8.5.2 предоставил свойство SaveOptions.MergeAreas, которое может принимать значение логического типа. Значение по умолчанию — false, однако, если установлено значение true, Aspose.Cells for Java API пытается объединить отдельные CellArea перед сохранением файла.

{{% alert color="primary" %}} 

Если в электронной таблице слишком много отдельных ячеек с примененной проверкой, есть вероятность, что результирующая электронная таблица может быть повреждена. Одним из возможных решений является объединение ячеек с идентичными правилами проверки, или теперь вы можете использовать свойство SaveOptions.MergeAreas, чтобы указать API для автоматического объединения ячеек CellAreas перед операцией сохранения.

{{% /alert %}} 
### **Добавлено свойство Geometry.ShapeAdjustValues**
 С выпуском v8.5.2 Aspose.Cells API предоставил метод Geometry.getShapeAdjustValues, который можно использовать для[доступ и внесение изменений в точки регулировки различных форм](/cells/ru/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

В интерфейсе Excel Microsoft точки регулировки отображаются в виде желтых ромбовидных узлов.

{{% /alert %}} 

 Например,

1. Прямоугольник со скругленными углами имеет настройку для изменения дуги.
1. Треугольник имеет корректировку для изменения положения точки
1. Трапеция имеет регулировку для изменения ширины верха.
1. Стрелы имеют две регулировки для изменения формы головы и хвоста.

Вот самый простой сценарий использования.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Добавлено поле перечисления ConsolidationFunction.DISTINCT_COUNT**
Aspose.Cells for Java 8.5.2 предоставило поле ConsolidationFunction.DISTINCT_COUNT, которое можно использовать для применения консолидированной функции Distinct Count к DataField сводной таблицы.

{{% alert color="primary" %}} 

Функция консолидации Distinct Count поддерживается только в версии Microsoft Excel 2013.

{{% /alert %}}
