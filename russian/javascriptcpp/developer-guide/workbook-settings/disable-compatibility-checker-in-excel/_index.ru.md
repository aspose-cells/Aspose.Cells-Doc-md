---
title: Отключить проверку совместимости в Excel с помощью JavaScript через C++
linktitle: Отключение проверки совместимости в Excel
type: docs
weight: 170
url: /ru/javascript-cpp/disable-compatibility-checker-in-excel/
description: Узнайте, как отключить проверку совместимости через скрипт Aspose.Cells for JavaScript с помощью API C++.
keywords: JavaScript отключение проверки совместимости, отключить проверку совместимости в Excel через JavaScript с помощью C++, отключить проверку совместимости в рабочей книге.
---

## Отключение проверки совместимости в листах Excel в JavaScript  

{{% alert color="primary" %}}  
Проверка совместимости Microsoft Excel сигнализирует о том, что сохранение файла в более раннем формате файла может вызвать проблемы с функциональностью или потерей достоверности. Проверка совместимости - это функция Microsoft Office Excel 2007 и Microsoft Excel 2010.  

Когда вы сохраняете книгу в предыдущей версии, Excel 97 through Excel 2003, из Excel 2007 или Excel 2010, проверка совместимости сканирует книгу, чтобы увидеть, содержит ли она функции, не поддерживаемые более ранней версией. Чтобы помочь вам с принятием решений о том, как обрабатывать проблемы совместимости, проверка совместимости отображает диалоговые окна с выбором. Ее также можно использовать для создания отчета о любых проблемах в книге или отключения функции.  

Иногда необходимо отключить Проверку Совместимости для конкретной таблицы. С помощью API Aspose.Cells вы можете сделать это программно, чтобы пользователи не расстраивались или не путалися с диалоговым окном проверки совместимости, которое появляется при повторном сохранении файла в Microsoft Excel.  
{{% /alert %}}  

## **Как отключить проверку совместимости с помощью Microsoft Excel**  

Для отключения проверки совместимости в Microsoft Excel (например, Microsoft Excel 2007/2010):  

- (Excel 2007) На кнопке Office нажмите **Подготовка**, затем **Запустить проверку совместимости** и снимите флажок с параметра **Проверять совместимость при сохранении этой книги**.  
- (Excel 2010) На вкладке **Файл** нажмите **Сведения**, затем **Проверить наличие проблем**, нажмите **Проверка совместимости**, и, наконец, снимите флажок с **Проверять совместимость при сохранении этой рабочей книги**.  

## **Как отключить проверку совместимости с помощью Aspose.Cells API**  

Установите свойство [**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--) в значение **ложь**, чтобы отключить Проверку Совместимости Microsoft Excel.  

### **Примеры кода**  

Примеры кода, показывающие, как отключить проверку совместимости с помощью Aspose.Cells for JavaScript через C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
