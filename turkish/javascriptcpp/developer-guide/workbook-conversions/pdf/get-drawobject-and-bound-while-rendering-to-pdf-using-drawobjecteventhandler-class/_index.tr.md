---
title: DrawObject ve Bound değerlerini almak için DrawObjectEventHandler kullanarak PDF ye dönüştürürken JavaScript ve C++ ile
linktitle: DrawObjectEventHandler sınıfını kullanarak PDF ye render ederken DrawObject ve Bound almak
type: docs
weight: 70
url: /tr/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) adlı soyut bir sınıf sağlar ve bunun içinde [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) yöntemi bulunur. Kullanıcı, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler)yi uygulayabilir ve [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) yöntemini kullanarak Excel'i PDF veya Görüntü’ye dönüştürürken [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) ve Sınır bilgilerini alabilir. İşte [**DrawObjectEventHandler.draw(DrawObject, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler/#draw-drawobject-number-number-number-number-) yönteminin parametrelerinin kısa bir açıklaması.

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject), görünüm sırasında başlatılır ve döndürülür.

- x: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)'ın Solu.

- y: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject)'ın Üstü.

- width: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) genişliği.

- height: [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) yüksekliği.

Excel dosyasını PDF'ye dönüştürürken, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) sınıfını ve [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) özelliğini kullanabilirsiniz. Benzer şekilde, Excel dosyasını Resim'e dönüştürürken [**DrawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/drawobjecteventhandler) sınıfını ve [**ImageOrPrintOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#drawObjectEventHandler--) özelliğini kullanabilirsiniz.

## **DrawObjectEventHandler sınıfını kullanarak PDF'ye dönüştürürken DrawObject ve Sınırlı Alın**

Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, [örnek Excel dosyasını](64716821.xlsx) yükler ve [çıkış PDF'si](64716822.pdf) olarak kaydeder. PDF’ye dönüştürürken, [**PdfSaveOptions.drawObjectEventHandler**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#drawObjectEventHandler--) özelliğini kullanır ve mevcut hücreler ile nesnelerin (örneğin görsellerin) [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) ve sınırlarını yakalar. Eğer [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) tipi Hücre ise, sınırını ve StringValue’sunu yazdırır. Eğer [**DrawObject**](https://reference.aspose.com/cells/javascript-cpp/drawobject) tipi Görüntü ise, sınırını ve Nesne İsmini yazdırır. Daha fazla yardım için aşağıda verilen örnek kodun konsol çıktısına bakabilirsiniz.

## **Örnek Kod**

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

## **Konsol Çıktısı**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
