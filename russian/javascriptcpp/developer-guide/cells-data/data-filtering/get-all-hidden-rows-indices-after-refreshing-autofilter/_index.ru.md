---
title: Получить все скрытые индексы строк после обновления автофильтра 
type: docs  
weight: 320  
url: /ru/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Узнайте, как получать индексы всех скрытых строк после обновления AutoFilter с помощью скрипта Aspose.Cells for Java и API C++.  
keywords: Получить все индексы скрытых строк после обновления AutoFilter через JavaScript и C++, получить все индексы скрытых строк после обновления AutoFilter через JavaScript и C++, извлечь все индексы скрытых строк после обновления AutoFilter через JavaScript и C++  
---

## **Возможные сценарии использования**  

Когда вы применяете автофильтр к ячейкам листа, некоторые строки автоматически скрываются. Но возможно, что некоторые из них были скрыты вручную пользователем Excel и не скрыты автофильтром. Это затрудняет определение, какие строки скрыты автофильтром, а какие — вручную. Скрипт Aspose.Cells for Java через C++ решает эту проблему, используя массив [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-). Этот метод возвращает индексы всех строк, скрытых автофильтром, и не скрытых вручную пользователем Excel.  

## **Получить все скрытые индексы строк после обновления автофильтра**  

Посмотрите следующий пример кода, который загружает [пример файла Excel](64716909.xlsx), содержащий некоторые строки, скрытые вручную пользователем Excel. Код применяет автофильтр и обновляет его с помощью метода [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-), который возвращает индексы всех скрытых строк автофильтром. Затем он выводит индексы скрытых строк на консоль вместе с именами ячеек и их значениями.  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Вывод в консоль**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
