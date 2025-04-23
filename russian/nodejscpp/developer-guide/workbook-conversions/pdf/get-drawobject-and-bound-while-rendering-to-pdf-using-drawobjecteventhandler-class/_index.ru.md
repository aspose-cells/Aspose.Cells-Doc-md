---
title: Получить DrawObject и Bound при отображении в PDF с помощью класса DrawObjectEventHandler с Node.js через C++
linktitle: Получить объект DrawObject и Bound при рендеринге в PDF с использованием класса DrawObjectEventHandler
type: docs
weight: 70
url: /ru/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет абстрактный класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler), который имеет метод [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). Пользователь может реализовать [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) и использовать метод [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-), чтобы получить [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) и Bound при рендеринге Excel в PDF или изображение. Вот краткое описание параметров метода [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) будет инициализирован и возвращен при рендеринге.

- x: Левая граница [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y: Верхняя граница [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- ширина: Ширина [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- высота: Высота [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

Если вы рендерите файл Excel в PDF, то вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) с [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--). Аналогично, если вы рендерите файл Excel в изображение, вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) с [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--).

## **Получить DrawObject и Bound при преобразовании в формат PDF с использованием класса DrawObjectEventHandler**

Пожалуйста, просмотрите следующий пример кода. Он загружает [образец файла Excel](64716821.xlsx) и сохраняет его как [выводной PDF](64716822.pdf). При рендеринге в PDF он использует свойство [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) и захватывает [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) и Bound существующих ячеек и объектов, например, изображений и т.д. Если тип [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) — Cell, он выводит его Bound и StringValue. А если тип [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) — Image, он выводит его Bound и название формы. Пожалуйста, посмотрите вывод консоли приведенного ниже примера кода для получения дополнительной информации.

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");

class ClsDrawObjectEventHandler extends AsposeCells.DrawObjectEventHandler {
draw(drawObject, x, y, width, height) {
console.log("");

// Print the coordinates and the value of Cell object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Cell) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.getCell().getStringValue()}`);
}

// Print the coordinates and the shape name of Image object
if (drawObject.getType() === AsposeCells.DrawObjectEnum.Image) {
console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Shape Name]: ${drawObject.getShape().getName()}`);
}

console.log("----------------------");
}
}

async function run() {
// Load sample Excel file
const workbook = new AsposeCells.Workbook("sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");

// Specify Pdf save options
const opts = new AsposeCells.PdfSaveOptions();

// Assign the instance of DrawObjectEventHandler class
opts.setDrawObjectEventHandler(new ClsDrawObjectEventHandler());

// Save to Pdf format with Pdf save options
await workbook.saveAsync("outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

run();
```

## **Вывод в консоль**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
