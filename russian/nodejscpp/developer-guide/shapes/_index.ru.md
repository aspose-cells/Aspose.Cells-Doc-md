---  
title: Вставка изображений и фигур в файлы Excel с помощью Node.js через C++  
linktitle: Фигуры  
type: docs  
weight: 140  
url: /ru/nodejs-cpp/insert-shapes/  
description: Управление изображениями, объектами OLE и фигурами в файлах Excel с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Иногда необходимо вставить некоторые необходимые фигуры в лист. Вам может понадобиться вставить одну и ту же фигуру в разные места листа. Или вам нужно пакетно вставить фигуры в лист.  
Не волнуйтесь! [Aspose.Cells](https://products.aspose.com/cells/) поддерживает все эти операции.  
{{% /alert %}}  

Фигуры в Excel делятся на следующие основные типы:  
- **Изображения**  
- **OLE-объекты**  
- **Линии**  
- **Прямоугольники**  
- **Базовые формы**  
- **Блочные стрелки**  
- **Уравнения**  
- **Блок-схемы**  
- **Звезды и баннеры**  
- **Выноски**  

Этот руководственный документ выберет одну или две фигуры из каждого типа для создания образцов. Благодаря этим примерам вы научитесь использовать [Aspose.Cells](https://products.aspose.com/cells/) для вставки указанной фигуры в лист.  

## **Добавление изображений в лист Excel с помощью Node.js**  

Добавление изображений в электронную таблицу очень просто. Нужно лишь несколько строк кода:  
 Просто вызовите метод [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) коллекции [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (обёрнутой в объект [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Метод [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-) принимает следующие параметры:  

- **Индекс верхнего левого ряда**, индекс верхнего левого ряда.  
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.  
- **Имя файла изображения**, имя файла изображения с полным путем.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Вставка объектов OLE в лист Excel с помощью Node.js**  

Aspose.Cells поддерживает добавление, извлечение и управление объектами OLE в рабочих листах. Поэтому у Aspose.Cells есть класс [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), который используется для добавления нового OLE-объекта в список коллекции. Другой класс, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), представляет объект OLE. В нем есть важные члены:  

- Свойство [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) задает изображение (иконку) в виде массива байтов. Это изображение отображается для отображения OLE-объекта в листе.  
- Свойство [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) задает данные объекта в виде массива байтов. Эти данные будут отображаться в соответствующей программе при двойном щелчке по иконке OLE-объекта.  

Нижеприведенный пример показывает, как добавить объект(ы) OLE в лист Excel.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Добавление линии в лист Excel с помощью Node.js**  

Форма линии относится к категории **линии**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, куда хотите вставить линию  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите линию из 'Недавно использованные фигуры' или 'Линии'  

![](line.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки линии в таблицу.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Метод возвращает объект [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

Следующий пример показывает, как вставить линию в лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](line2.png)  

## **Вставка стрелки линии в лист Excel с помощью Node.js**  

Форма стрелки линии относится к категории **Линии**. Это особый случай линии.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, в которую хотите вставить стрелку.  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите стрелку линии из 'Недавно использованные фигуры' или 'Линии'  

![](line_arrow1.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки стрелки на лист.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Метод возвращает объект [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape).  
{{% /alert %}}  

Следующий пример показывает, как вставить стрелку линии в лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](line_arrow2.png)  

## **Добавление прямоугольника в лист Excel с помощью Node.js**  

Форма прямоугольника относится к категории **Прямоугольники**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, в которую хотите вставить прямоугольник.  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите прямоугольник из 'Недавно использованные фигуры' или 'Прямоугольники'  

![](rectangle.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки прямоугольника на листе.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Метод возвращает объект [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape).  
{{% /alert %}}  

Следующий пример показывает, как вставить прямоугольник в лист.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](rectangle2.png)  

## **Добавление куба в лист Excel с помощью Node.js**  

Форма куба относится к категории **Основные фигуры**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, в которую хотите вставить куб  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите Куб из раздела **Основные фигуры**  

![](cube.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки куба на листе.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Этот метод возвращает объект [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Следующий пример показывает, как вставить куб в лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](cube2.png)  

## **Вставка выносной стрелки-квадрата в лист Excel с помощью Node.js**  

Форма выносной стрелки-квадрата относится к категории **Блок-стрелки**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, в которую хотите вставить стрелку квадратного выноса  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите квадрокрестовую стрелку вызова из **Блок-стрелки**  

![](callout_quad_arrow.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки стрелки квадратного выноса на лист Excel.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Этот метод возвращает объект [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Пример ниже показывает, как вставить квадрокрестовую стрелку вызова в лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](callout_quad_arrow2.png)  

## **Вставка знака умножения в Excel-таблицу с помощью Node.js**  

Форма знака умножения принадлежит категории **Формулы фигур**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, в которую хотите вставить знак умножения  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите знак умножения из **Формулы фигур**  

![](multiplication_sign.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки знака умножения в листе Excel.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Этот метод возвращает объект [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Пример ниже показывает, как вставить знак умножения в лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](multiplication_sign2.png)  

## **Вставка мультидокумента в Excel-таблицу с помощью Node.js**  

Форма мультидокумента принадлежит категории **Блок-схемы**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, куда вы хотите вставить мультидокумент  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите мультидокумент из **Блок-схемы**  

![](multidocument.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки мультидокумента в листе Excel.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Этот метод возвращает объект [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Пример ниже показывает, как вставить мультидокумент в лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](multidocument2.png)  

## **Вставка пятиконечной звезды в Excel-таблицу с помощью Node.js**  

Форма пятиконечной звезды принадлежит категории **Звёзды и Баннеры**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, в которую хотите вставить пятиконечную звезду  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите пятиконечную звезду из **Звёзды и Баннеры**  

![](star_5_points.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки пятиконечной звезды в лист.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Этот метод возвращает объект [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Пример ниже показывает, как вставить пятиконечную звезду в лист.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](star_5_points2.png)  

## **Вставка облака вызова мысленного пузыря в Excel с помощью Node.js**  

Форма облака мыслительного пузыря принадлежит категории **Вызовы**.  

***В Microsoft Excel (например, 2007 год):***  

- Выберите ячейку, в которую хотите вставить размышляющее облачко  
- Нажмите меню Вставка и выберите Фигуры.  
- Затем выберите облако мысленного пузыря из **Вызовы**  

![](thought_bubble_cloud.png)  

***Используя Aspose.Cells***  

Вы можете использовать следующий метод для вставки облака с мыслями на листе.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Этот метод возвращает объект [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape).  
{{% /alert %}}  

Пример ниже показывает, как вставить облако мысленного пузыря в лист.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Выполните приведенный выше код, и вы получите следующие результаты:  

![](thought_bubble_cloud2.png)  

## **Продвинутые темы**  
- [Изменение значений коррекции формы](/cells/ru/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [Копировать формы между рабочими листами](/cells/ru/nodejs-cpp/copy-shapes-between-worksheets/)  
- [Данные в не-примитивной форме](/cells/ru/nodejs-cpp/data-in-non-primitive-shape/)  
- [Поиск абсолютной позиции формы внутри рабочего листа](/cells/ru/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Получить точки соединения от формы](/cells/ru/nodejs-cpp/get-connection-points-from-shape/)  
- [Управление элементами управлениями](/cells/ru/nodejs-cpp/managing-controls/)  
- [Добавление значков на рабочий лист](/cells/ru/nodejs-cpp/insert-svg-to-excel/)  
- [Управление объектами OLE](/cells/ru/nodejs-cpp/managing-ole-objects/)  
- [Управление изображениями](/cells/ru/nodejs-cpp/managing-pictures/)  
- [Управление умным искусством](/cells/ru/nodejs-cpp/managing-smartart/)  
- [Управление текстовыми полями](/cells/ru/nodejs-cpp/managing-textbox-of-excel/)  
- [Добавление водяного знака WordArt на лист](/cells/ru/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [Обновить значения связанных форм](/cells/ru/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [Отправить форму вперед или назад внутри листа](/cells/ru/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Управление параметрами формы](/cells/ru/nodejs-cpp/managing-shape-options/)  
- [Управление параметрами текста формы](/cells/ru/nodejs-cpp/managing-shape-text-options/)  
- [Веб-расширения - дополнения для Office](/cells/ru/nodejs-cpp/web-extensions-office-add-ins/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
