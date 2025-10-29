---
title: 在使用DrawObjectEventHandler类和Node.js通过C++渲染到PDF时，获取DrawObject和边界
linktitle: 在使用DrawObjectEventHandler类呈现到PDF时获取绘图对象和边界
type: docs
weight: 70
url: /zh/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能的使用场景**

Aspose.Cells提供一个抽象类[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)，它具有一个[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)方法。用户可以实现[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)，并利用[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)方法在将Excel渲染为PDF或图像时获取[**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)和边界。以下是[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)方法参数的简要说明。

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)将在渲染时初始化并返回。

- x: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)的左边界。

- y: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)的顶部。

- width: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)的宽度。

- height: [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)的高度。

如果您将Excel文件渲染为PDF，可以使用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)类配合[**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--)。类似地，如果您将Excel文件渲染为图像，则可以使用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler)类配合[**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--)。

## **在使用DrawObjectEventHandler类呈现到PDF时获取DrawObject和边界**

请参阅以下示例代码。它加载了[示例Excel文件](64716821.xlsx)，并将其保存为[输出PDF](64716822.pdf)。在渲染为PDF时，它利用[**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--)属性，捕获现有单元格和对象（如图片等）的[**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)和边界。如果[**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject)类型是单元格，它会打印其边界和字符串值；如果类型是图片，则打印其边界和Shape名称。请查看下面的示例代码的控制台输出获得更多帮助。

## **示例代码**

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

## **控制台输出**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
