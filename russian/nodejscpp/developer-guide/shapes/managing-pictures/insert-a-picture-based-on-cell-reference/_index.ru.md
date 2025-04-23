---
title: Вставка изображения на основе ссылки на ячейку с помощью Node.js via C++
linktitle: Вставка изображения на основе ссылки на ячейку
type: docs
weight: 150
url: /ru/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Узнайте, как вставить изображение в лист на основе ссылки на ячейку с помощью Aspose.Cells for Node.js via C++. Отобразить данные ячейки на изображении.
---

{{% alert color="primary" %}}
Иногда у вас есть пустое изображение, и вам нужно показать данные или содержимое в изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).
{{% /alert %}}

## Вставка изображения на основе ссылки на ячейку

Aspose.Cells for Node.js via C++ поддерживает отображение содержимого ячейки листа в графической фигуре. Вы можете связать изображение с ячейкой, содержащей данные, которые хотите отображать. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения в данных этой ячейки или диапазона автоматически отображаются на изображении. Добавьте изображение в лист, вызвав метод [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (обернутый в объект [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Укажите диапазон ячеек с помощью атрибута [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) объекта [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).

### Пример кода

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

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
