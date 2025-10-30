---
title: JavaScript kullanarak Hücre Referansına Dayalı Resim Ekleme C++ ile
linktitle: Hücre Referansına Dayalı Bir Resim Eklemek
type: docs
weight: 150
url: /tr/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: Aspose.Cells for JavaScript kullanarak bir hücre referansına göre çalışma sayfasına nasıl resim ekleneceğini öğrenin. Hücre verisini gösteren resmi göster.
---

{{% alert color="primary" %}}
Bazen boş bir resminiz vardır ve resimde verileri veya içeriği bir hücre referansı belirleyerek göstermek istersiniz. Aspose.Cells bu özelliği destekler (Microsoft Excel 2010).
{{% /alert %}}

## Hücre Referansına Dayalı Bir Resim Eklemek

 Aspose.Cells for JavaScript C++ ile çalışma sayfası hücre içeriğini bir görsel şekli olarak gösterme desteği sağlar. Resmi, görüntülemek istediğiniz veriyi içeren hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlandığından, bu hücredeki veya hücre aralığındaki veriye yaptığınız değişiklikler otomatik olarak grafik nesnesinde görünür. Çalışma sayfasına resim eklemek için [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) koleksiyonunun [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) yöntemini çağırın ([**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) nesnesinde kapsüllenmiş). Hücre aralığını [**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) özelliğiyle belirtin.

### Kod Örneği

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Referenced Picture Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet's cells collection
            const cells = workbook.worksheets.get(0).cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get the conditional icon's image data
            const imagedata = AsposeCells.ConditionalFormattingIcon.iconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
            // Create a stream based on the image data
            const stream = Uint8Array.from(imagedata);

            // Add a blank picture to the D1 cell
            const pic = workbook.worksheets.get(0).shapes.addPicture(0, 3, stream, 10, 10);
            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";
            // Update the shapes selected value in the worksheet
            workbook.worksheets.get(0).shapes.updateSelectedValue();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'referencedpicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
