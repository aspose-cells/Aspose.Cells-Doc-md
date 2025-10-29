---
title: Получите объекты DrawObject и Bound при рендеринге в PDF с помощью класса DrawObjectEventHandler с JavaScript через C++
linktitle: Получить объект DrawObject и Bound при рендеринге в PDF с использованием класса DrawObjectEventHandler
type: docs
weight: 70
url: /ru/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет абстрактный класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler), который имеет метод [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). Пользователь может реализовать [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) и использовать метод [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-), чтобы получить [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) и Bound при рендеринге Excel в PDF или изображение. Вот краткое описание параметров метода [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) будет инициализирован и возвращен при рендеринге.

- x: Левая граница [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- y: Верхняя граница [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- ширина: Ширина [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- высота: Высота [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

 Если вы рендерите файл Excel в PDF, вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) с свойством [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--). Аналогично, если вы рендерите файл Excel в изображение, вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) с свойством [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--).

## **Получить DrawObject и Bound при преобразовании в формат PDF с использованием класса DrawObjectEventHandler**

Пожалуйста, просмотрите следующий пример кода. Он загружает [образец файла Excel](64716821.xlsx) и сохраняет его как [выводной PDF](64716822.pdf). При рендеринге в PDF он использует свойство [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) и захватывает [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) и Bound существующих ячеек и объектов, например, изображений и т.д. Если тип [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) — Cell, он выводит его Bound и StringValue. А если тип [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) — Image, он выводит его Bound и название формы. Пожалуйста, посмотрите вывод консоли приведенного ниже примера кода для получения дополнительной информации.

## **Образец кода**

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

## **Вывод в консоль**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
