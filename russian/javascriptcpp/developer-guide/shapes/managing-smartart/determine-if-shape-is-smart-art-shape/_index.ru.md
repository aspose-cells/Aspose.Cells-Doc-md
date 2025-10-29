---
title: Определить, является ли фигура в Excel Smart Art с помощью JavaScript через C++
linktitle: Определить, является ли форма формой Smart Art
type: docs
weight: 400
url: /ru/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Узнайте, как определить, является ли фигура в Excel Smart Art с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

Smart Art Shapes — это специальные фигуры в Microsoft Excel, позволяющие автоматически создавать сложные диаграммы. Вы можете определить, является ли фигура smart art или обычной, используя свойство [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--).  

## **Определение, является ли форма формой Smart Art**  

Следующий пример кода загружает [пример файла Excel](55541792.xlsx), содержащий фигуру Smart Art, как показано на этом скриншоте. Затем он выводит значение свойства [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) первой фигуры. Пожалуйста, смотрите вывод в консоли ниже.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **Вывод в консоль**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
