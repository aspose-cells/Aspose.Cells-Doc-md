---
title: Используйте параметры проверки ошибок с помощью JavaScript через C++
linktitle: Использование опций проверки ошибок
type: docs
weight: 140
url: /ru/javascript-cpp/use-error-checking-options/
description: Узнайте, как программно использовать параметры проверки ошибок в листах Excel с помощью Aspose.Cells for JavaScript через C++.
keywords: сохраняйте номер как текст в Excel с помощью JavaScript через C++, параметры проверки ошибок в Excel с помощью JavaScript через C++
---

{{% alert color="primary" %}}  
Microsoft Excel позволяет пользователям определять параметры и правила проверки ошибок. Пользователи часто видят проверки ошибок при создании формул – небольшой треугольник в верхнем правом углу ячейки подствечивает, если в ячейке есть проблема. Excel предоставляет информацию, которая помогает пользователям исправить распространенные проблемы.  
{{% /alert %}}  

## **Типы ошибок**  

Ошибки, означающие, что формула не может вернуть результат — такие как деление числа на ноль — требуют немедленного внимания, и в ячейке отображается значение ошибки. Нажатие на зеленый треугольник показывает знак восклицания; при нажатии открывается список опций.  

Эту ошибку можно устранить с помощью опций или игнорировать. Игнорирование ошибки означает, что эта ошибка не будет отображаться при дальнейших проверках ошибок.  

Aspose.Cells предоставляет функции проверки ошибок. Класс [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) управляет различными видами проверки ошибок, например, числа, сохраненные как текст, ошибки при вычислении формул и ошибки валидации. Используйте перечисление [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) для установки желаемой проверки ошибок.  

## **Числа, сохраненные как текст**  

Иногда числа могут быть отформатированы и сохранены в ячейках как текст. Это может вызвать проблемы с вычислениями или привести к непонятным порядкам сортировки. Числа, отформатированные как текст, выровнены влево, а не вправо, в ячейке. Если формула, которая должна выполнить математическую операцию с ячейками, не возвращает значение, следует проверить выравнивание в ячейках, на которые ссылается формула - некоторые или все эти ячейки могут быть числами, отформатированными как текст.  

Вы можете использовать опции проверки ошибок, чтобы быстро преобразовать числа, сохраненные как текст, в реальные числа. В Microsoft Excel 2003:  

1. На меню **Инструменты** щелкните **Параметры**.  
1. Выберите вкладку Проверка ошибок.  
   Опция **Число сохранено как текст** установлена по умолчанию.  
1. Отключить ее.  

Приведенный ниже образец кода показывает, как отключить опцию проверки ошибок чисел, сохраненных как текст, для листа в файле-шаблоне XLS, используя API Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
