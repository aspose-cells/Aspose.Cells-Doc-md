---
title: Как установить названия печати с помощью JavaScript через C++
linktitle: Как установить заголовки печати
type: docs
weight: 200
url: /ru/javascript-cpp/how-to-set-print-titles/
description: Эта статья показывает, как установить названия печати с помощью библиотеки Aspose.Cells для JavaScript через C++.
keywords: Повторная печать строк и столбцов, как установить названия печати, устанавливать и очищать названия печати с помощью JavaScript, как очистить названия печати в JavaScript, как добавлять названия печати с помощью JavaScript, как удалять названия печати с помощью JavaScript, как установить названия печати в Excel, как очистить названия печати в Excel.  
---

## **Возможные сценарии использования**  

Установка заголовков печати в Excel обеспечивает повторение определенных строк или столбцов на каждой странице печати, что особенно полезно для больших таблиц, занимающих несколько страниц. Вот причины, почему стоит устанавливать заголовки печати:  

1. Повышенная читаемость: Заголовки печати помогают читателям понять данные, оставляя заголовки видимыми на всех страницах, облегчая интерпретацию информации без необходимости возвращения к первой странице.  

1. Профессиональный внешний вид: Постоянное отображение заголовков или меток на каждой странице создает более аккуратный и профессиональный вид печатных документов.  

1. Улучшенная навигация: для документов с обширными данными повторение заголовков на каждой странице позволяет быстрее находить нужную информацию и сокращает необходимость перелистывать страницы.  

1. Меньше ошибок: при наличии заголовков на каждой странице снижается риск неправильного восприятия или ошибок при вводе данных, так как пользователи легко могут понять контекст данных.  

1. Последовательность: обеспечение постоянного отображения важной информации, такой как заголовки столбцов или метки строк, поддерживает последовательность и ясность во всем документе.  

## **Как установить заголовки печати в Excel**  

Чтобы установить заголовки печати в Excel, выполните следующие шаги:  

1. Откройте вкладку Макет страницы: нажмите на вкладку "Макет страницы" в ленте в верхней части окна Excel.  
1. Получить доступ к заголовкам печати: в группе "Настройка страницы" нажмите "Заголовки печати".  
1. Установите строки для повторения: В диалоговом окне "Параметры страницы" перейдите на вкладку "Лист". В разделе "Заголовки печати" укажите строки для повторения в верхней части, щелкнув по полю рядом с "Строки для повторения вверху" и выбрав нужные строки.  
1. Установите столбцы для повторения (если необходимо): Аналогичным образом вы можете указать столбцы для повторения слева, щелкнув по полю рядом с "Столбцы для повторения слева" и выбрав нужные столбцы.  
<br>  
<img src="3.png" width=60% />  

1. Подтвердить и распечатать: нажмите "ОК", чтобы применить настройки. При печати листа, указанные строки или столбцы будут отображаться на каждой странице.  

## **Как удалить заголовки печати в Excel**  

Чтобы удалить заголовки печати в Excel, нужно удалить строки или столбцы, установленные для повторения на каждой странице. Вот как это сделать:  

1. Откройте вкладку Макет страницы: нажмите на вкладку "Макет страницы" в ленте в верхней части окна Excel.  
1. Получить доступ к заголовкам печати: в группе "Настройка страницы" нажмите "Заголовки печати".  
1. Удалить заголовки печати: в диалоговом окне "Настройка страницы" перейдите на вкладку "Лист". Очистите текстовые поля "Строки для повторения сверху" и "Столбцы для повторения слева", удаляя любой содержимое внутри них.  
<br>  
<img src="4.png" width=60% />  

1. Подтвердить и закрыть: нажмите "ОК" для применения изменений.  

## **Как установить названия печати с помощью Aspose.Cells for JavaScript через C++**  

Чтобы установить заголовки печати в указанном листе: сначала загрузите [образец файла](input.xlsx), затем необходимо изменить свойства [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) и [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) объекта [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) для нужного листа. Установка этих свойств в строку диапазона установит заголовки печати.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
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

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Результат вывода:  
<br>  
<img src="1.png" width=60% />  

## **Как очистить названия печати с помощью Aspose.Cells for JavaScript через C++**  

Чтобы удалить заголовки печати в указанном листе: сначала загрузите [образец файла](input.xlsx), затем необходимо изменить свойства [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) и [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) объекта [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) для нужного листа. Установка этих свойств в пустую строку очистит заголовки печати.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
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

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

Результат вывода:  
<br>  
<img src="2.png" width=60% />
