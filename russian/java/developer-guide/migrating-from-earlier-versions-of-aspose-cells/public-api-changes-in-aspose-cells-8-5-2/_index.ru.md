---
title: Изменения в публичном API в Aspose.Cells 8.5.2
type: docs
weight: 190
url: /ru/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

В данном документе описаны изменения в API Aspose.Cells с версии 8.5.1 по 8.5.2, которые могут быть интересны для разработчиков модулей/приложений. Здесь не только описаны новые и обновленные открытые методы, [добавленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-5-2/), но также описываются любые изменения в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Отобразить Рабочий лист на графический контекст**
В этом выпуске API Aspose.Cells for Java появилась еще одна перегрузка метода SheetRender.toImage, которая теперь позволяет принимать экземпляр класса Graphics2D для [визуализации листа в графическом контексте](/cells/ru/java/render-worksheet-to-graphic-context/). Сигнатура нового метода выглядит следующим образом.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.5.2 добавлен метод PivotTable.getCellByDisplayName, который можно использовать для [получения объекта ячейки по имени поля сводной таблицы](/cells/ru/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Этот метод может быть полезен, если требуется выделить или форматировать заголовок поля сводной таблицы.

Вот простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
### **Добавлено свойство SaveOptions.MergeAreas**
Aspose.Cells for Java 8.5.2 добавлено свойство SaveOptions.MergeAreas, которое может принимать значение типа Boolean. Значение по умолчанию — false; однако, если установить его в true, API Aspose.Cells for Java будет пытаться объединить индивидуальные CellArea перед сохранением файла.

{{% alert color="primary" %}} 

Если электронная таблица содержит слишком много индивидуальных ячеек с примененной проверкой или может быть повреждена. Одно из возможных решений — объединить ячейки с идентичными условиями проверки или теперь можно использовать свойство SaveOptions.MergeAreas для указания API автоматически объединять CellArea перед операцией сохранения.

{{% /alert %}} 
### **Добавлено свойство Geometry.ShapeAdjustValues**
С выпуском v8.5.2 API Aspose.Cells теперь содержит метод Geometry.getShapeAdjustValues, который можно использовать для [доступа и внесения изменений в точки коррекции различных форм](/cells/ru/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

В пользовательском интерфейсе Microsoft Excel точки коррекции отображаются в виде желтых алмазных узлов.

{{% /alert %}} 

Например, 

1. У закругленного прямоугольника есть точка коррекции для изменения дуги
1. У треугольника есть точка коррекции для изменения положения точки
1. Трапеция имеет настройку для изменения ширины верхней части
1. Стрелки имеют две настройки для изменения формы головы и хвоста

Вот самый простой сценарий использования.

**Java**

{{< highlight csharp >}}

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
### **Добавлено перечисление Field ConsolidationFunction.DISTINCT_COUNT**
Aspose.Cells for Java 8.5.2 выставил поле ConsolidationFunction.DISTINCT_COUNT, которое может использоваться для применения функции сведения уникальных значений к DataField PivotTable.

{{% alert color="primary" %}} 

Функция сведения уникальных значений поддерживается только в Microsoft Excel 2013.

{{% /alert %}}
