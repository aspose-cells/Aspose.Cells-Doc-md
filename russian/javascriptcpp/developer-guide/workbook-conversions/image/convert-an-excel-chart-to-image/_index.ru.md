---
title: Конвертация диаграммы Excel в изображение с помощью JavaScript через C++
linktitle: Конвертировать диаграмму Excel в изображение
type: docs
weight: 20
url: /ru/javascript-cpp/convert-an-excel-chart-to-image/
description: Узнайте, как конвертировать диаграммы Excel в изображения с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  

Диаграммы наглядны и облегчают пользователю видеть сравнения, паттерны и тенденции в данных. Например, вместо анализа колонок чисел в таблице, диаграмма сразу показывает, уменьшаются ли продажи или растут, или сравнивает фактические продажи с плановыми. Людям часто приходится представлять статистическую и графическую информацию в легко понимаемой и легко поддерживаемой форме. Изображение помогает.  

Иногда в приложениях или веб-страницах требуются графики. Или может понадобиться для документа Word, файла PDF, презентации PowerPoint или другого приложения. В каждом случае вы хотите преобразовать график в изображение, чтобы использовать его в другом месте.  

{{% /alert %}}  

## **Конвертация диаграмм в изображения**  

В приведенных здесь примерах преобразуются круговая диаграмма и столбчатая диаграмма в изображения.  

### **Конвертация круговой диаграммы в файл изображения**  

Сначала создайте круговую диаграмму в Microsoft Excel, а затем преобразуйте ее в файл изображения с помощью Aspose.Cells for JavaScript через C++. Этот пример создает изображение EMF на основе круговой диаграммы в шаблонном файле Microsoft Excel.  

|**Результат: изображение круговой диаграммы**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Создайте круговую диаграмму в Microsoft Excel:  
   1. Откройте новую книгу в Microsoft Excel.  
   1. Введите некоторые данные в лист.  
   1. Создайте круговую диаграмму на основе данных.  
   1. Сохраните файл.  

|**Исходный файл.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Скачайте и установите Aspose.Cells:  
   1. [Скачать Aspose.Cells for JavaScript через C++](https://downloads.aspose.com/cells/javascript-cpp).  
   1. Установите его на вашем компьютере для разработки.  

Все компоненты [Aspose](http://www.aspose.com/) работают в режиме оценки при первой установке. Режим оценки не имеет временных ограничений и вставляет в выходные документы только водяной знак.  

1. Создайте проект:  
   1. Запустите предпочитаемую IDE.  
   1. Создайте новое консольное приложение. В этом примере используется приложение JavaScript, но его можно создать с помощью любой среды выполнения JavaScript.  
   1. Добавьте ссылку. Этот проект использует Aspose.Cells, поэтому добавьте ссылку на Aspose.Cells for JavaScript через C++.  
   1. Напишите код, который находит и конвертирует диаграмму. Приведен ниже код, используемый компонентом для выполнения задачи. Используется очень немного строк кода.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
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

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

### **Конвертация столбчатой диаграммы в файл изображения**  

Сначала создайте столбцовую диаграмму в Microsoft Excel и преобразуйте ее в файл изображения, как указано выше. После выполнения этого кода создается JPEG-файл на основе столбчатой диаграммы из шаблона файла Excel.  

|**Выходной файл: изображение столбчатой диаграммы.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Создайте столбчатую диаграмму в Microsoft Excel:  
   1. Откройте новую книгу в Microsoft Excel.  
   1. Введите некоторые данные в лист.  
   1. Создайте столбчатую диаграмму на основе данных.  
   1. Сохраните файл.  

|**Входной файл.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. Создайте проект с ссылками, как описано выше.  
1. Динамически преобразуйте диаграмму в изображение. Ниже приведен используемый компонентом код для выполнения этой задачи. Код аналогичен предыдущему:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
