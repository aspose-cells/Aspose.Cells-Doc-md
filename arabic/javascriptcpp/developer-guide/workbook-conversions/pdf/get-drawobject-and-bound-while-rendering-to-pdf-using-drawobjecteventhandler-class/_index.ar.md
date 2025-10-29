---
title: احصل على DrawObject و Bound أثناء التصيير إلى PDF باستخدام فئة DrawObjectEventHandler مع JavaScript عبر C++
linktitle: الحصول على كائن الرسم وBound أثناء التقديم إلى PDF باستخدام فئة DrawObjectEventHandler
type: docs
weight: 70
url: /ar/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells فصلًا مجردًا [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) يمتلك طريقة [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). يمكن للمستخدم تنفيذ [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) واستخدام طريقة [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) للحصول على [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) وBound أثناء تحويل Excel إلى PDF أو صورة. إليك وصف موجز لمعاملات طريقة [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: يتم تهيئته وإرجاعه عند التحويل.

- x: يسار [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- y: أعلى [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- width: عرض [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- height: ارتفاع [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

 إذا كنت تقوم بتصيير ملف إكسل إلى PDF، يمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) مع الخاصية [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--). بالمثل، إذا كنت تقوم بتصيير ملف إكسل إلى صورة، يمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) مع الخاصية [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--).

## **الحصول على DrawObject والحدود أثناء تقديمها إلى PDF باستخدام فئة DrawObjectEventHandler**

يرجى مراجعة رمز النموذج التالي. يقوم بتحميل [ملف Excel النموذجي](64716821.xlsx) ويحفظه كـ [ملف PDF الناتج](64716822.pdf). أثناء التحويل إلى PDF، يستخدم الخاصية [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) ويقوم بالتقاط [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) و Bound من الخلايا والأشياء الموجودة مثل الصور، إلخ. إذا كان النوع [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) هو Cell، يطبع Bound وقيمة السلسلة النصية. وإذا كان النوع [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) هو Image، يطبع Bound واسم الشكل. يرجى مراجعة مخرجات وحدة التحكم للرمز النموذجي أدناه لمزيد من المساعدة.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Get Draw Object and Bound Using DrawObjectEventHandler</title>
    </head>
    <body>
        <h1>Get Draw Object and Bound Using DrawObjectEventHandler</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, DrawObjectEventHandler, DrawObjectEnum } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        class ClsDrawObjectEventHandler extends DrawObjectEventHandler {
            draw(drawObject, x, y, width, height) {
                console.log("");

                // Print the coordinates and the value of Cell object
                if (drawObject.type === DrawObjectEnum.Cell) {
                    console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Cell Value]: ${drawObject.cell.stringValue}`);
                }

                // Print the coordinates and the shape name of Image object
                if (drawObject.type === DrawObjectEnum.Image) {
                    console.log(`[X]: ${x} [Y]: ${y} [Width]: ${width} [Height]: ${height} [Shape Name]: ${drawObject.shape.name}`);
                }

                console.log("----------------------");
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Pdf save options
            const opts = new PdfSaveOptions();

            // Assign the instance of DrawObjectEventHandler class
            opts.drawObjectEventHandler = new ClsDrawObjectEventHandler();

            // Save to Pdf format with Pdf save options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

## **مخرجات الوحدة**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
