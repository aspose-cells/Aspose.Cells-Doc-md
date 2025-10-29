---
title: Преобразование файла XLSX в формат PDF с помощью JavaScript через C++
linktitle: Преобразовать файл XLSX в формат PDF
type: docs
weight: 30
url: /ru/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: Настоящее руководство объясняет, как преобразовать файл Excel (XLSX) в формат PDF с помощью Script Aspose.Cells for Java через C++. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) представляет документы независимо от используемого программного обеспечения, оборудования и операционной системы для создания этих документов. Файл PDF может быть документами с любой комбинацией текста, графики и изображений в устройство- и разрешение-независимом формате. Файлы PDF часто сжимаются, поэтому они занимают меньше места, чем оригинальный файл.

Иногда необходимо преобразовать файл Microsoft Excel в PDF. Для этого потребуется быстрое, безопасное, точное и надежное решение, позволяющее распространять PDF-документы по всему миру. Есть множество инструментов для преобразования, которые могут выполнить эту задачу. Но важно убедиться, что исходная компоновка Excel сохраняется в итоговом файле PDF. Изображения, графики, фигуры, форматирование данных, шрифты, атрибуты, цвета, настройки страницы, ориентация текста, границы, графики и т. д. должны отображаться точно и последовательно. [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) обеспечивает высокоточное преобразование.

Этот документ предназначен для полного понимания процесса преобразования файла Microsoft Excel (с изображениями, графиками, форматированием и т. д.) в PDF. В нем показано, как создать простое консольное приложение на JavaScript через C++, которое преобразует файл Excel в PDF с помощью API Aspose.Cells. Процесс выполняется с высокой точностью и аккуратностью.

{{% /alert %}}

## **Преобразование Excel в PDF**

Этот пример использует файл Excel (SampleInput.xlsx) в качестве шаблона. Рабочая книга содержит листы с графиками и изображениями. Каждый лист содержит разные типы форматирования с использованием шрифтов, атрибутов, цветов, эффектов затенения и границ. На первом листе есть столбчатая диаграмма, а на последнем — изображение.

### **Файл шаблона Excel**

Шаблонный файл содержит три листа, включающие графики и изображения как медиа. Первый лист содержит графики, а последний — изображение, как показано на скриншотах ниже.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Первый лист **(Прогноз продаж)**|Второй лист **(Отчет о продажах)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Третий лист **(Ввод данных)**|Последний лист **(Изображение)**|

### **Процесс конвертации**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Если в таблице есть формулы, рекомендуется перед преобразованием в PDF вызвать метод [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) для пересчета значений зависимых формул и правильного отображения их в PDF.

{{% /alert %}}

### **Результат**

После выполнения вышеуказанного кода создается PDF-файл в папке Files в вашем каталоге приложения.
Следующие скриншоты показывают страницы PDF. Обратите внимание, что в выходном PDF-файле также сохранены заголовки и нижние колонтитулы.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Первый лист **(Прогноз продаж)**|Второй лист **(Отчет о продажах)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Третий лист **(Ввод данных)**|Последний лист **(Изображение)**|
