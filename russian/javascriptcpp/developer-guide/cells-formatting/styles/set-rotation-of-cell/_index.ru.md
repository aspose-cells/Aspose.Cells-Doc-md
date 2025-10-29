---
title: Как повернуть текст ячейки
linktitle: Как повернуть текст ячейки  
type: docs  
weight: 80  
url: /ru/javascript-cpp/how-to-rotate-text-of-cell/  
description: Научитесь программно поворачивать текст ячейки с помощью Aspose.Cells for JavaScript через C++.  
keywords: JavaScript через C++ — поворот текста ячейки, программное поворачивание текста в ячейке рабочей книги, установка угла поворота ячейки программно, как повернуть текст ячейки в Excel с помощью JavaScript  
---

## **Поворот текста ячейки в Aspose.Cells for JavaScript через C++**

Aspose.Cells — мощный компонент JavaScript, позволяющий разработчикам работать с файлами Excel программно. Одна из функций Aspose.Cells — возможность поворота ячеек, что позволяет настраивать ориентацию текста и улучшать визуальное восприятие данных. В этом документе мы рассмотрим, как поворачивать ячейки с помощью Aspose.Cells.

## **Как вращать текст ячейки в Excel**
Для вращения ячейки в Excel вы можете использовать следующие шаги:
1. Откройте Excel и выберите ячейку или диапазон ячеек, которые вы хотите повернуть.
1. Щелкните правой кнопкой мыши на выбранной ячейке(ях) и выберите "Формат ячеек" в контекстном меню. В качестве альтернативы вы можете перейти на вкладку "Главная" в ленте Excel, нажать на выпадающий список "Формат" в группе "Ячейки" и выбрать "Формат ячеек".
1. В диалоговом окне "Формат ячеек" перейдите на вкладку "Выравнивание".
1. В разделе "Ориентация" вы увидите варианты вращения текста. Вы можете непосредственно ввести желаемый угол поворота в градусах в поле "Градусы". Положительные значения вращают текст против часовой стрелки, а отрицательные - по часовой.
<br>
![todo:image_alt_text](alignment.png)
1. После выбора желаемого угла поворота нажмите "OK", чтобы применить изменения. Выбранные ячейки теперь будут повернуты в соответствии с выбранным углом поворота или ориентацией.

## **Как вращать текст ячейки с использованием API Aspose.Cells**

Свойство [**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) упрощает вращение ячеек. Чтобы вращать ячейки в Aspose.Cells, вам нужно выполнить следующие шаги:
1. Загрузите книгу Excel  
<br>
Сначала вам нужно загрузить книгу Excel с помощью Aspose.Cells. Вы можете использовать класс Workbook для открытия существующего файла Excel или создания нового. 

1. Получите доступ к листу  
<br>
После загрузки книги вам нужно получить доступ к листу, на котором вы хотите повернуть ячейки. Вы можете получить доступ к листу по его индексу или имени. 

1. Поверните текст ячейки  
<br>
Теперь, когда у вас есть доступ к листу, вы можете повернуть ячейки, модифицируя объект Style нужных ячеек. Объект Style позволяет устанавливать различные варианты форматирования, включая вращение. 

1. Сохраните книгу  
<br>
После вращения ячеек вы можете сохранить измененную книгу обратно в файл или поток, используя метод Save.

## **Пример кода на JavaScript**

Пожалуйста, смотрите следующий код, он создает объект книги и устанавливает разные углы вращения для нескольких ячеек. Скриншот показывает результат после выполнения примера кода.
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
