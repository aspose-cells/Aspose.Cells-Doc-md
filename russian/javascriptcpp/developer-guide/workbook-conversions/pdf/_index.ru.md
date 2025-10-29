---
title: PDF с помощью JavaScript через C++
linktitle: Pdf
type: docs
weight: 220
url: /ru/javascript-cpp/convert-excel-to-pdf/
description: Узнайте, как преобразовать рабочую книгу Excel в PDF с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает преобразование книги Excel в PDF. В этом примере мы увидим полное преобразование книги Excel в PDF.
{{% /alert %}}

## **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{% alert color="primary" %}}
Script на Aspose.Cells for JavaScript с помощью C++ напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа в PDF, Aspose.Cells for JavaScript через C++ заполняет поле **PDF Producer** значением, например 'Aspose.Cells v23.2'.

Обратите внимание, что вы можете изменить эту информацию в выходных документах с помощью свойства [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#producer--).
{{% /alert %}}

### **Прямое преобразование**

Script на Aspose.Cells for JavaScript с помощью C++ поддерживает конвертацию из таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel как PDF, используя метод [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Метод [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) возвращает член перечисления [**SaveFormat.Pdf**](https://reference.aspose.com/cells/javascript-cpp/saveformat), который преобразует нативные файлы Excel в формат PDF.

Следуйте нижеприведенным шагам, чтобы непосредственно преобразовать электронные таблицы Excel в формат PDF:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона, или пропустить этот шаг, если создаете книгу из нуля.
1. Выполните любую работу (ввод данных, применение форматирования, задание формул, вставка изображений или других объектов рисования и т. д.) на электронной таблице, используя API Aspose.Cells.
1. После завершения кода таблицы вызовите метод [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) для сохранения таблицы.

Формат файла должен быть PDF, поэтому выберите *Pdf* (предопределенное значение) из перечисления [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) для создания окончательного документа PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiate the Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to PDF completed! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Расширенное преобразование**

Вы также можете использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) для установки различных атрибутов конвертации. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) позволяет контролировать настройки печати, шрифта, безопасности и сжатия для выходного PDF. 

Самым важным свойством является [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--), позволяющий устанавливать уровень соответствия стандартам PDF. В настоящее время можно сохранять в форматах PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u. Обратите внимание, что при формате PDF/A размер выходного файла больше, чем у обычного файла PDF.

#### **Сохранение книги в формате PDF/A**

Ниже приведен фрагмент кода, демонстрирующий использование класса [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) для сохранения файлов Excel в формате PDF/A.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF/A from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;

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
            // Instantiate new workbook
            const workbook = new Workbook();

            // Insert a value into the A1 cell in the first worksheet
            workbook.worksheets.get(0).cells.get(0, 0).value = "Testing PDF/A";

            // Define PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set the compliance type
            pdfSaveOptions.compliance = PdfCompliance.PdfA1b;

            // Save the file to PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF/A File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF/A created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Обратите внимание, что свойство [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) было добавлено с выпуском Aspose.Cells for JavaScript через C++ 5.3.0.
{{% /alert %}}

#### **Установить время создания PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) вы можете получать или устанавливать время создания PDF. В следующем коде демонстрируется использование свойства [**PdfSaveOptions.createdTime**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#createdTime--) для установки времени создания файла PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const options = new PdfSaveOptions();
            options.createdTime = new Date();

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Установите опцию ContentCopyForAccessibility**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) вы можете получать или устанавливать параметр PDF [**PdfSecurityOptions.accessibilityExtractContent**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/#accessibilityExtractContent--) для контроля доступа к содержимому в созданном PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Convert to PDF with Security Options</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Security Options</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOpt = new PdfSaveOptions();

            // Create an instance of PdfSecurityOptions
            const securityOptions = new PdfSecurityOptions();

            // Set AccessibilityExtractContent to false (converted from setAccessibilityExtractContent(false))
            securityOptions.accessibilityExtractContent = false;

            // Set the security option in the PdfSaveOptions (converted from setSecurityOptions)
            pdfSaveOpt.securityOptions = securityOptions;

            // Save the workbook to PDF format while passing the PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOpt);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outFile.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

#### **Экспорт пользовательских свойств в PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) можно экспортировать пользовательские свойства из исходной книги в формат PDF. Перечислитель [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/javascript-cpp/pdfcustompropertiesexport/) предназначен для указания способа экспорта свойств. Эти свойства можно увидеть в Adobe Acrobat Reader, нажав на файл, а затем на опцию свойств, как показано на следующем изображении. Файл шаблона "sourceWithCustProps.xlsx" можно загрузить [здесь](sourceWithCustProps.xlsx) для тестирования, а файл PDF "outSourceWithCustProps" доступен [здесь](outSourceWithCustProps.pdf) для анализа.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Custom Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCustomPropertiesExport } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
            pdfSaveOptions.customPropertiesExport = PdfCustomPropertiesExport.Standard;

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourceWithCustProps.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Атрибуты преобразования**

Мы работаем над улучшением функций преобразования с каждым новым выпуском. Преобразование Excel в PDF от Aspose.Cells все еще имеет несколько ограничений. Карта заполнения не поддерживается при преобразовании в формат PDF. Кроме того, некоторые объекты рисования не поддерживаются хорошо.

В таблице ниже перечислены все функции, которые полностью или частично поддерживаются при экспорте в формат PDF с помощью Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты таблиц, но она идентифицирует те функции, которые не поддерживаются или поддерживаются частично для преобразования в PDF.

|**Элемент документа**|**Атрибут**|**Поддерживается**|**Примечания**|
| :- | :- | :- | :- |
|Выравнивание| |Да| |
|Настройки фона| |Да| |
|Граница|Цвет|Да| |
|Граница|Стиль линии|Да| |
|Граница|Толщина линии|Да| |
|Данные ячейки| |Да| |
|Комментарии| |Да| |
|Условное форматирование| |Да| |
|Свойства документа| |Да| |
|Объекты рисования| |Частично|Тени и трехмерные эффекты для объектов рисования плохо поддерживаются; WordArt и SmartArt поддерживаются частично.|
|Шрифт|Размер|Да| |
|Шрифт|Цвет|Да| |
|Шрифт|Стиль|Да| |
|Шрифт|Подчеркивание|Да| |
|Шрифт|Эффекты|Да| |
|Изображения| |Да| |
|Гиперссылка| |Да| |
|Диаграммы| |Частично|Карта диаграмм не поддерживается.|
|Объединенные ячейки| |Да| |
|Разрыв страницы| |Да| |
|Настройка страницы|Верхний/нижний колонтитул|Да| |
|Настройка страницы|Поля|Да| |
|Настройка страницы|Ориентация страницы|Да| |
|Настройка страницы|Размер страницы|Да| |
|Настройка страницы|Область печати|Да| |
|Настройка страницы|Печатные заголовки|Да| |
|Настройка страницы|Масштабирование|Да| |
|Высота строки/Ширина столбца| |Да| |
|Язык справа налево (RTL)| |Да| |

{{% alert color="primary" %}}
Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.
{{% /alert %}}

## **Продвинутые темы**
- [Добавление закладок PDF с именованными местами назначения](/cells/ru/javascript-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Избегание пустой страницы в выходном PDF, когда нет ничего для печати](/cells/ru/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Изменить шрифт только для определенных символов Unicode при сохранении в формате PDF](/cells/ru/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Преобразовать файл XLSX в формат PDF](/cells/ru/javascript-cpp/convert-xlsx-file-to-pdf-format/)
- [Преобразование файла Excel в формат PDF, совместимый с PDFA-1a](/cells/ru/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразовать файл XLS с изображениями или диаграммами в формат PDF](/cells/ru/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создание PdfBookmarkEntry для листа с диаграммой](/cells/ru/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Заполнить все столбцы листа Excel на одной странице PDF](/cells/ru/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Получить DrawObject и Bound при преобразовании в формат PDF с использованием класса DrawObjectEventHandler](/cells/ru/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Получить предупреждения о замене шрифта при преобразовании файла Excel](/cells/ru/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Игнорировать ошибки при преобразовании Excel в PDF](/cells/ru/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничение количества создаваемых страниц - Преобразование Excel в PDF](/cells/ru/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Печать комментариев при сохранении в формат PDF](/cells/ru/javascript-cpp/print-comments-while-saving-to-pdf/)
- [Рендеринг офисных надстроек при преобразовании Excel в PDF](/cells/ru/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Отображать одну страницу PDF для каждого листа Excel - Преобразование Excel в PDF](/cells/ru/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Отобразите дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells](/cells/ru/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Добавление изображений с изменением размера - Преобразование Excel в PDF](/cells/ru/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Сохранить каждый лист в отдельный файл PDF](/cells/ru/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Сохранить Excel в PDF с обычным или минимальным размером](/cells/ru/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Сохранить указанные листы в формат PDF](/cells/ru/javascript-cpp/save-specified-worksheets-to-pdf/)
- [Защищенные документы в формате PDF](/cells/ru/javascript-cpp/secure-pdf-documents/)
- [Указание способа пересечения строк в выходном PDF и изображении](/cells/ru/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
