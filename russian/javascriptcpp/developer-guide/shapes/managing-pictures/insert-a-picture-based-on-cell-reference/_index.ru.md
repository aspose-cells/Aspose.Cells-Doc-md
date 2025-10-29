---
title: Вставить изображение на основе ссылки на ячейку с помощью JavaScript через C++
linktitle: Вставка изображения на основе ссылки на ячейку
type: docs
weight: 150
url: /ru/javascript-cpp/insert-a-picture-based-on-cell-reference/
description: Узнайте, как вставить изображение в рабочий лист на основе ссылки на ячейку с помощью Aspose.Cells for JavaScript через C++. Отобразите данные ячейки в виде изображения.
---

{{% alert color="primary" %}}
Иногда у вас есть пустое изображение, и вам нужно показать данные или содержимое в изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).
{{% /alert %}}

## Вставка изображения на основе ссылки на ячейку

Aspose.Cells for JavaScript через C++ поддерживает отображение содержимого ячейки рабочего листа в виде фигуры изображения. Вы можете связать изображение с ячейкой, содержащей отображаемые данные. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения данных в этой ячейке или диапазоне автоматически отображаются в графическом объекте. Добавьте изображение на рабочий лист, вызвав метод [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection) (инкапсулированный в объект [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). Укажите диапазон ячеек с помощью атрибута [**Picture.formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--) объекта [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture).

### Пример кода

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
