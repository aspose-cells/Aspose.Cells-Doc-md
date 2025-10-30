---
title: Obtener DrawObject y Bound al renderizar a PDF usando la clase DrawObjectEventHandler con JavaScript vía C++
linktitle: Obtener DrawObject y Bound al representar a PDF usando la clase DrawObjectEventHandler
type: docs
weight: 70
url: /es/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona una clase abstracta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) que tiene un método [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-). El usuario puede implementar [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) y utilizar el método [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) para obtener el [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) y el Bound mientras renderiza Excel a PDF o Imagen. Aquí hay una breve descripción de los parámetros del método [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) será inicializado y devuelto cuando se renderice.

- x: Izquierda de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- y: Superior de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- ancho: Ancho de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

- altura: Altura de [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject).

 Si está renderizando un archivo Excel a PDF, puede utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) con la propiedad [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--). De manera similar, si está renderizando un archivo Excel a Imagen, puede utilizar la clase [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) con la propiedad [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--).

## **Obtenga DrawObject y Bound al renderizar a PDF utilizando la clase DrawObjectEventHandler**

Por favor, vea el siguiente código de ejemplo. Carga el [archivo Excel de ejemplo](64716821.xlsx) y lo guarda como [PDF de salida](64716822.pdf). Mientras renderiza a PDF, utiliza la propiedad [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) y captura el [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) y Bound de celdas y objetos existentes, por ejemplo, imágenes, etc. Si el tipo [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) es Celda, imprime su Bound y StringValue. Y si el tipo [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) es Imagen, imprime su Bound y Nombre de Forma. Por favor, vea la salida de consola del código de ejemplo a continuación para más ayuda.

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
