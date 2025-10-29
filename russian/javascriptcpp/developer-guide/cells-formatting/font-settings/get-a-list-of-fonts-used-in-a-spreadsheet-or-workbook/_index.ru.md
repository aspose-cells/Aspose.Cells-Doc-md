---
title: Получение списка используемых шрифтов в электронной таблице или книге
linktitle: Получение списка используемых шрифтов в электронной таблице или книге
description: Узнайте, как получать список используемых шрифтов в таблице или рабочей книге с помощью Script Aspose.Cells for Java через C++. Эта статья покажет, как извлекать информацию о шрифтах из документа.
keywords: Aspose.Cells, JavaScript через C++, таблица, рабочая книга, шрифт, список
type: docs
weight: 20
url: /ru/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Возможные сценарии использования**

Часто необходимо знать, какие шрифты используются в вашей книге для целей рендеринга. При преобразовании книги в PDF или изображение, Aspose.Cells требует, чтобы все необходимые шрифты были установлены на вашей системе или находились в вашем **каталоге шрифтов**. Если Aspose.Cells не может найти необходимый шрифт, он пытается заменить его на другой подходящий шрифт, который присутствует на вашей системе или в вашем каталоге шрифтов и может заменить ваш фактический шрифт. Это приводит не только к нежелательному рендерингу PDF или изображений, но и занимает время на поиск подходящих шрифтов.

Чтобы работать с такими случаями, вам нужно знать, какие шрифты используются в вашей книге, затем либо установить эти шрифты на вашей системе в случае Windows, либо поместить их в каталог шрифтов в случае Windows или Linux.

Script Aspose.Cells for Java через C++ предоставляет метод [**Workbook.fonts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fonts--), который возвращает список всех используемых шрифтов в вашей рабочей книге или таблице.

## **Получение списка используемых шрифтов в электронной таблице или книге**

Приведенный ниже образец кода загружает исходный файл Excel и извлекает список шрифтов, используемых в нем. В нем есть один фиктивный рабочий лист, в котором для иллюстрационных целей добавлены некоторые фиктивные шрифты. Когда код выводит все шрифты в рабочей книге, он также выводит эти фиктивные шрифты. Ниже показан снимок экрана [образца файла Excel](25395211.xlsx) и то, как отображаются фиктивные шрифты.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Get Fonts Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Get Fonts from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Fonts</button>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the fonts inside the workbook (converted from getFonts())
            const fonts = workbook.fonts;

            // Print all the fonts into the result div
            if (!fonts || fonts.length === 0) {
                document.getElementById('result').innerHTML = '<p>No fonts found in the workbook.</p>';
                return;
            }

            let html = '<h2>Fonts in Workbook</h2><ul>';
            for (let i = 0; i < fonts.length; i++) {
                html += `<li>${fonts[i].toString()}</li>`;
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```


## **Вывод в консоль**



{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
