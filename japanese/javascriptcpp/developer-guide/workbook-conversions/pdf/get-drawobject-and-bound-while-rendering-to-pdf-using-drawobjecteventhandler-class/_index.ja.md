---
title: JavaScript経由のDrawObjectEventHandlerクラスを使用して、描画時にDrawObjectと境界を取得する方法を学ぶ。
linktitle: DrawObjectEventHandler クラスを使用して PDF にレンダリングする際の DrawObject および Bound を取得
type: docs
weight: 70
url: /ja/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能な使用シナリオ**

Aspose.Cellsは、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler)という抽象クラスを提供し、[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)メソッドを持ちます。ユーザーは[**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler)を実装し、ExcelをPDFまたは画像にレンダリングする際に[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)メソッドを利用して[**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)とBoundを取得できます。以下は[**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-)メソッドのパラメータの概要です。

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)はレンダリング時に初期化され返されます。

- x: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)の左端。

- y: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)の上端。

- width: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)の幅。

- height: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)の高さ。

ExcelファイルをPDFに変換する際には、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler)クラスとその[**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--)プロパティを活用できます。同様に、Excelファイルを画像に変換する場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler)クラスと[**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--)プロパティを活用します。

## **DrawObjectEventHandlerクラスを使用してPDFへのレンダリング中にDrawObjectとバインドを取得**

次のサンプルコードを参照してください。これは、サンプルExcelファイル（[64716821.xlsx]）を読み込み、[出力PDF](64716822.pdf)として保存します。PDFへのレンダリング中に、[**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--)プロパティを利用し、既存のセルや画像などのオブジェクトの[**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)とBoundを取得します。[**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)タイプがCellの場合、BoundとStringValueを出力します。[**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)タイプがImageの場合、BoundとShape Nameを出力します。詳細は以下のサンプルコードのコンソール出力をご参照ください。

## **サンプルコード**

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

## **コンソール出力**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
