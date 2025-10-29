---
title: Создания фигур в графиках с Node.js через C++
linktitle: Формы в диаграммах
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для добавления элементов управления и настройки диаграмм в Microsoft Excel. Этот гид демонстрирует, как управлять элементами диаграммы, изменять форматирование и улучшать внешний вид и удобство использования ваших графиков.
keywords: Aspose.Cells for Node.js via C++, Элементы управления графиками, Настройка диаграмм, Microsoft Excel, Элементы графика, Форматирование.
type: docs
weight: 70
url: /ru/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Иногда вам может потребоваться вставить объекты рисования, такие как метки, текстовые поля, изображения и т. д., в график. Aspose.Cells может добавлять элементы управления в график во время выполнения.
{{% /alert %}}

## **Добавление элемента управления метки в график**

Метки предоставляют средство информирования пользователей о содержании электронной таблицы. Aspose.Cells позволяет добавлять и управлять метками даже в диаграммах.

Класс [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) содержит метод с именем [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-), используемый для добавления элемента управления меткой в график. Ниже приведен список параметров, используемых для этого метода:

- **top** – вертикальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота метки в единицах 1/4000 от области графика.
- **width** – ширина метки в единицах 1/4000 от области графика.

Метод возвращает объект [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/). Класс [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) представляет собой метку в графике. Он имеет несколько важных членов:

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (свойство) – указывает строку заголовка метки.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (свойство) – указывает атрибуты цвета заливки.

В следующем примере показано, как добавить метку в график. В примере используется файл дизайнера (**exp_piechart.xls**), в котором есть график. Мы используем этот файл для вставки метки в график. Ниже приведен исходный код для добавления метки в график. При выполнении кода генерируется следующий вывод.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);

// Set the caption of the label.
label.setText("A Label In Chart");

// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Добавление элемента управления текстовым полем в график**

Один из способов выделить важную информацию в отчете – использование текстового поля. Например, введите текст для выделения названия компании или для указания географического региона с наибольшими продажами. Класс [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) предоставляет метод с именем [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), который используется для добавления элемента управления текстовым полем в график. Ниже приведен список параметров, используемых для метода:

- **top** – вертикальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота текстового поля в единицах 1/4000 от области графика.
- **ширина** - ширина текстового блока в единицах 1/4000 от области диаграммы.

Метод возвращает объект [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/). Класс [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) представляет собой текстовый блок на диаграмме.

В следующем примере показано, как добавить текстовое поле на диаграмму. В примере используется предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить текстовое поле на диаграмму для отображения заголовка диаграммы. Ниже приведен исходный код для добавления текстового поля на диаграмму.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);

// Fill the text.
textbox0.setText("Sales By Region");

// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();

// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);

// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);

// Set the font to bold.
textbox0.getFont().setIsBold(true);

// Set the font size.
textbox0.getFont().setSize(14);

// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);

// Get the fill format of the textbox.
const fillformat = textbox0.getFill();

// Get the line format type of the textbox.
const lineformat = textbox0.getLine();

// Set the line weight.
lineformat.setWeight(2);

// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Добавление изображения на диаграмму**

Aspose.Cells позволяет вставлять изображения в диаграмму. Например, добавьте изображение, чтобы подчеркнуть или придать больший смысл диаграмме или ее содержимому, или вставьте файл изображения бренда.

Класс [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) предоставляет метод с именем [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), который используется для добавления объекта изображения на диаграмму. Ниже приведен список параметров, используемых для метода:

- **верх** - вертикальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **слева** - горизонтальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **поток** - объект потока, содержащий данные изображения.
- **масштабШирины** - масштаб ширины изображения, значение в процентах.
- **масштабВысоты** - масштаб высоты изображения, значение в процентах.

Метод возвращает объект [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Класс [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) представляет собой объект изображения на диаграмме.

В следующем примере показано, как добавить изображение на диаграмму. Пример использует предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить изображение на диаграмму. Ниже приведен исходный код для добавления изображения на диаграмму.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));

// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);

// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);

// Get the lineformat type of the picture.
const lineformat = pic0.getLine();          

// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Set the line weight.
lineformat.setWeight(4);    

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Добавление флажка на диаграмму**

Aspose.Cells позволяет вставлять флажки на лист диаграммы, используя перечисление [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/). В следующем примере показано добавление флажка на лист диаграммы.

На следующем изображении показан лист диаграммы с флажком в выходном файле.

![todo:image_alt_text](controls-in-charts_1.jpg)

Ссылка на [выходной файл](101089316.xlsx), сгенерированный следующим фрагментом кода, прикреплена для вашего ознакомления.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);

const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);

// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");

// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```

## **Продвинутые темы**
- [Добавить водяной знак WordArt на диаграмму](/cells/ru/nodejs-cpp/add-wordart-watermark-to-chart/)

{{< app/cells/assistant language="nodejs-cpp" >}}
