---
title: Как вставить изображение в ячейку
type: docs
weight: 130
url: /ru/javascript-cpp/how-to-insert-picture-in-cell/
description: Узнайте, как вставить изображение в ячейку с помощью Aspose.Cells for JavaScript через C++.
keywords: Как вставить изображение в ячейку, вставить изображение над ячейками, поместить изображение в ячейку, поместить изображение над ячейками, как разместить изображение в ячейке, как разместить изображение над ячейками, переключение между изображением в ячейке и изображением над ячейками, переключение между помещением в ячейку и помещением над ячейками.
---

## **Возможные сценарии использования**
Изображение придает яркость вашему листу и обеспечивает визуальное представление содержимого. Они также делают более простым понимание данных и появление идей. Хотя вы могли использовать изображения в Excel в течение многих лет, недавно excel включил функцию, позволяющую изображениям становиться фактическими значениями ячейки. Даже если макет рисунка изменен, он все равно будет привязан к данным. Вы можете использовать его в таблицах, сортировке, фильтрации, включении в формулы и т. Д.!

## **Как вставить изображение в ячейку с помощью Excel**
 Как вставить изображение в ячейку в Excel, выполните следующие действия:

1. Перейдите на вкладку Вставка и нажмите на опцию изображения.
2. Выберите **Разместить в ячейке**. Выберите один из следующих источников из выпадающего меню Вставить изображение из (**Это устройство**, **Готовые изображения** и **Изображения из Интернета**). Это устройство для вставки изображения с вашего устройства. Готовые изображения для вставки изображения из готовых изображений. Изображения из Интернета для вставки изображения из Интернета.
<br>
<img src="1.png" width=60% />
3. Выберите изображение и вставьте его в ячейку.
<br>
<img src="8.png" width=60% />

## **Как вставить изображение над ячейками с помощью Excel**
О том, как вставить изображение над ячейками в Excel, следуйте этим шагам:

1. Перейдите на вкладку Вставка и нажмите на опцию изображения.
2. Выберите **Разместить над ячейками**. Выберите один из следующих источников из раскрывающегося меню Вставить изображение: (**Это устройство**, **Готовые изображения** и **Изображения из Интернета**). Это устройство для вставки изображения с вашего устройства. Готовые изображения для вставки изображения из готовых изображений. Изображения из Интернета для вставки изображения из Интернета.
<br>
<img src="2.png" width=60% />
3. Выберите изображение и вставьте его над ячейками.
<br>
<img src="3.png" width=60% />

## **Как переключиться от изображения в ячейке к изображению над ячейками с помощью Excel**
Вы можете легко переключиться от **Изображение в ячейке** к **Изображение над ячейками**. Пожалуйста, следуйте этим шагам:
1. Нажмите правой кнопкой мыши на ячейке и выберите **Изображение в ячейке** > **Разместить над ячейками**. 
<br>
<img src="4.png" width=60% />
2. Результат после переключения следующий:
<br>
<img src="5.png" width=60% />

## **Как переключиться от изображения над ячейками к изображению в ячейке с помощью Excel**
Вы можете легко переключиться от **Изображение над ячейками** к **Изображение в ячейке**. Пожалуйста, следуйте этим шагам:
1. Нажмите правой кнопкой мыши на изображение и выберите **Разместить в ячейке**. 
<br>
<img src="6.png" width=60% />
2. Результат после переключения следующий:
<br>
<img src="7.png" width=60% />

## **Как вставить изображение в ячейку с помощью Aspose.Cells for JavaScript через C++**
Вставьте изображение в ячейку с помощью Aspose.Cells. Пожалуйста, ознакомьтесь со следующим примером кода. После выполнения образца кода изображение будет вставлено в ячейку.
1. Создать объект Workbook. 
2. Получить ячейку, в которую хотите вставить изображение.
3. Установить свойство Cell.EmbeddedImage. 
4. Наконец, сохраните книгу в формате [output XLSX](out.xlsx). 

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
