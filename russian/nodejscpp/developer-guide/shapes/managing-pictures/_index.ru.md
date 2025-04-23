---  
title: Управление изображениями с помощью Node.js через C++  
linktitle: Управление изображениями  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/managing-pictures/  
description: Узнайте, как добавлять и позиционировать изображения в таблицах с помощью Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells позволяет разработчикам добавлять изображения в электронные таблицы во время выполнения. Более подробно об этом будет рассказано в следующих разделах.

В этой статье объясняется, как добавлять изображения и как вставлять изображение, показывающее содержимое определённых ячеек.

## **Добавление изображений**

Добавление изображений в электронную таблицу очень просто. Нужно лишь несколько строк кода:  
 Просто вызовите метод [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) коллекции [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (обёрнутой в объект [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Метод [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) принимает следующие параметры:

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

## **Позиционирование изображений**

Существует два возможных способа контроля позиционирования изображений с помощью Aspose.Cells:

- Пропорциональное позиционирование: определение положения пропорционально высоте и ширине строки.
- Абсолютное позиционирование: задайте точное расположение на странице, например, 40 пикселей слева и 20 пикселей ниже края ячейки.

### **Пропорциональное позиционирование**

Разработчики могут позиционировать изображения пропорционально высоте строки и ширине столбца, используя свойства [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) и [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) объекта [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Объект [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) может быть получен из коллекции [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) по индексу изображения. Этот пример размещает изображение в ячейке F6.

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
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Абсолютное позиционирование**

Разработчики также могут абсолютно позиционировать изображения, используя свойства [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) и [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) объекта [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Этот пример размещает изображение в ячейке F6, на 60 пикселей слева и 10 пикселей сверху относительно ячейки.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Вставка изображения на основе ссылки на ячейку**

Aspose.Cells позволяет отображать содержимое ячейки листа в виде изображения. Можно связать изображение с ячейкой, содержащей данные, которые нужно отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, внесенные в данные в этой ячейке или диапазоне ячеек, автоматически отобразятся в графическом объекте.

Добавьте изображение на лист, вызвав метод [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (обёрнутой в объект [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Укажите диапазон ячеек с помощью атрибута [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) объекта [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Продвинутые темы**
- [Добавление набора условных значков с текстом ячейки](/cells/ru/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Вставить привязанное изображение из веб-адреса](/cells/ru/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Вставить изображение на основе ссылки на ячейку](/cells/ru/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Загрузка веб-изображения из URL в лист Excel](/cells/ru/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

