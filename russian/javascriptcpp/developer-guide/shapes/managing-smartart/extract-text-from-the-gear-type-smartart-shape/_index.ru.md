---
title: Извлечь текст из формы SmartArt типа Gear с помощью JavaScript через C++
linktitle: Извлечение текста из формы SmartArt типа Gear
type: docs
weight: 500
url: /ru/javascript-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Узнайте, как извлечь текст из формы SmartArt типа Gear с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Aspose.Cells может извлекать текст из формы SmartArt типа Gear. Для этого сначала необходимо преобразовать форму SmartArt в групповую форму, используя свойство [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--). Затем нужно получить массив всех отдельных фигур, составляющих групповую форму, с помощью свойства [**GroupShape.groupedShapes**](https://reference.aspose.com/cells/javascript-cpp/groupshape/#groupedShapes--). В конце можно пройти по всем отдельным фигурам и извлечь их текст с помощью свойства [**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--).

## **Извлечение текста из формы SmartArt с шестеренчатым типом**

В следующем примере кода загружается [образец файла Excel](67338483.xlsx), содержащий умную форму Gear Type Smart Art. Затем извлекается текст из ее индивидуальных форм, как обсуждалось выше. Пожалуйста, ознакомьтесь с выводом консоли в приведенном ниже примере кода в качестве примера.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Gear SmartArt Text Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Get the result of gear type smart art shape in the form of group shape.
            const groupShape = shape.resultOfSmartArt;

            // Get the list of individual shapes consisting of group shape.
            const shapes = groupShape.groupedShapes;

            // Extract the text of gear type shapes and display them.
            const results = [];
            for (let i = 0; i < shapes.count; i++) {
                const s = shapes.get(i);

                if (s.type === AsposeCells.AutoShapeType.Gear9 || s.type === AsposeCells.AutoShapeType.Gear6) {
                    const text = s.text;
                    results.push(text);
                    console.log("Gear Type Shape Text: " + text);
                }
            }

            if (results.length) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Found gear shape texts:</p><ul>' + results.map(t => '<li>' + t + '</li>').join('') + '</ul>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No gear type SmartArt shapes found in the first shape.</p>';
            }
        });
    </script>
</html>
```

## **Вывод в консоль**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
