---
title: الحصول على DrawObject و Bound أثناء التحويل إلى PDF باستخدام فصل DrawObjectEventHandler مع Node.js عبر C++
linktitle: الحصول على كائن الرسم وBound أثناء التقديم إلى PDF باستخدام فئة DrawObjectEventHandler
type: docs
weight: 70
url: /ar/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells فصلًا مجردًا [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) يمتلك طريقة [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). يمكن للمستخدم تنفيذ [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) واستخدام طريقة [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) للحصول على [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) وBound أثناء تحويل Excel إلى PDF أو صورة. إليك وصف موجز لمعاملات طريقة [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: يتم تهيئته وإرجاعه عند التحويل.

- x: يسار [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- y: أعلى [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- width: عرض [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

- height: ارتفاع [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject).

إذا كنت تقوم بتحويل ملف Excel إلى PDF، يمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) مع [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--). بالمثل، إذا كنت تقوم بتحويل ملف Excel إلى صورة، يمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/nodejs-cpp/drawobjecteventhandler) مع [**ImageOrPrintOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDrawObjectEventHandler--).

## **الحصول على DrawObject والحدود أثناء تقديمها إلى PDF باستخدام فئة DrawObjectEventHandler**

يرجى مراجعة رمز النموذج التالي. يقوم بتحميل [ملف Excel النموذجي](64716821.xlsx) ويحفظه كـ [ملف PDF الناتج](64716822.pdf). أثناء التحويل إلى PDF، يستخدم الخاصية [**PdfSaveOptions.getDrawObjectEventHandler()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDrawObjectEventHandler--) ويقوم بالتقاط [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) و Bound من الخلايا والأشياء الموجودة مثل الصور، إلخ. إذا كان النوع [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) هو Cell، يطبع Bound وقيمة السلسلة النصية. وإذا كان النوع [**DrawObject**](https://reference.aspose.com/cells/nodejs-cpp/drawobject) هو Image، يطبع Bound واسم الشكل. يرجى مراجعة مخرجات وحدة التحكم للرمز النموذجي أدناه لمزيد من المساعدة.

## **الكود المثالي**

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

## **مخرجات الوحدة**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
