---
title: Начало работы
type: docs
weight: 5
url: /ru/javascript-cpp/getting-started/
keywords: "Excel, браузер, безсерверное, XLS, XLSX, XLSB, CSV, PDF, JPG, PNG, HTML, ODS, XLSM, электронная таблица, Markdown, XPS, DOCX, PPTX, MHTML, SVG, JSON, SQL, XML"
description: "Настройка Aspose.Cells для javascript через C++ и рекомендации по установке."
---

## **Описание продукта**
Aspose.Cells for JavaScript через C++ — это высокопроизводительная, богатая функциями библиотека для работы с и преобразования таблиц, включая форматы Excel (XLS, XLSX, XLSB, XLSM), ODS, CSV и HTML. Она предоставляет обширный набор функций для создания, редактирования, конвертации и отображения таблиц как в браузере, так и в среде Node.js. Полная поддержка всех основных форматов Excel обеспечивает максимальную совместимость и гибкость в различных сценариях использования.
Создана с использованием WebAssembly для обеспечения почти нативной скорости непосредственно в браузере, Aspose.Cells for JavaScript через C++ позволяет быстро и эффективно обрабатывать таблицы без необходимости сервера. Ее небольшой вес делает ее идеальной для безсерверных веб-приложений, требующих расширенной функциональности Excel. Независимо от того, создаете ли вы приборные панели, потоки обработки данных или инструменты генерации документов, Aspose.Cells for JavaScript через C++ предлагает надежное, полное и высокопроизводительное решение. Aspose.Cells for JavaScript через C++ поддерживает браузеры и Node.js, в основном браузеры.

## **Ключевые функции**
1. **Создание и редактирование файлов:** Создавайте новые таблицы или редактируйте существующие с легкостью. Это включает добавление или изменение данных, форматирование ячеек, управление листами и многое другое.
1. **Обработка данных:** Выполняйте сложные манипуляции данными, такие как сортировка, фильтрация и валидация. Библиотека также поддерживает расширенные формулы и функции для анализа данных и вычислений.
1. **Конвертация файлов:** Конвертируйте файлы Excel в различные форматы, такие как PDF, HTML, ODS и форматы изображений, например PNG и JPEG. Эта функция полезна для обмена и распространения данных таблицы в разных форматах.
1. **Диаграммы и графика:** Создавайте и настраивайте широкий спектр диаграмм и графиков для визуального представления данных. Библиотека поддерживает гистограммы, линейные диаграммы, круговые диаграммы и многое другое, с настройками для дизайна и макета.
1. **Отрисовка и печать:** Отображайте листы Excel в виде изображений высокого качества и PDF, обеспечивая точное воспроизведение визуального представления. Библиотека также предлагает опции для печати таблиц с точным контролем над макетом страниц и форматированием.
1. **Расширенная защита и безопасность:** Защищайте таблицы паролями, шифруйте файлы и управляйте правами доступа для обеспечения безопасности и целостности данных.
1. **Производительность и масштабируемость:** Разработана для обработки больших наборов данных и сложных таблиц эффективно, Aspose.Cells for JavaScript через C++ обеспечивает высокую производительность и масштабируемость для корпоративных приложений.


## **Предварительные требования**

Перед началом убедитесь, что у вас есть:
- Node.js установлен на вашей системе (скачать с https://nodejs.org/)
- Действительный лицензионный файл Aspose (например, Aspose.Total.lic, Aspose.Cells.lic или aspose.cells.js.lic) для полнофункционального использования
- Базовые знания HTML и JavaScript

## **Шаг 1: Установка**

### Установите Aspose.Cells for JavaScript

Создайте новую директорию проекта и установите пакет:

{{< highlight bash >}}
# Create a new project directory
mkdir my-excel-project
cd my-excel-project

# Install Aspose.Cells for JavaScript
npm install aspose.cells.js
{{< /highlight >}}

### Установка HTTP-сервера (обязательный для настройки лицензии)

Установите простой HTTP-сервер глобально:

{{< highlight bash >}}
npm install -g http-server
{{< /highlight >}}

Или используйте встроенный сервер Python (если установлен Python):
{{< highlight bash >}}
# Python 3
python -m http.server

# Python 2
python -m SimpleHTTPServer
{{< /highlight >}}

## **Шаг 2: Настройка лицензии (обязательная для полного функционала)**

### Шифрование вашего файла лицензии

1. **Запустите HTTP-сервер** в каталоге вашего проекта:
   {{< highlight bash >}}
   http-server -p 8080
   {{< /highlight >}}

2. **Откройте инструмент шифрования лицензий** в браузере:
   ```
   http://localhost:8080/node_modules/aspose.cells.js/encrypt_lic.html
   ```

3. **Загрузите файл лицензии**:
   - Нажмите "Выбрать файл" и выберите файл лицензии (например, `Aspose.Total.lic`, `Aspose.Cells.lic` или `aspose.cells.js.lic`)
   - Процесс шифрования завершится автоматически (очень быстро)

4. **Загрузите зашифрованную лицензию**:
   - Нажмите "Скачать обработанный файл" для загрузки `aspose.cells.enc`
   - Сохраните этот файл в директории вашего проекта

### Разместите зашифрованную лицензию

Переместите файл `aspose.cells.enc` в корень вашего проекта или в определенную папку, к которой ваше приложение сможет обращаться.

## **Шаг 3: Примеры использования**

### Использование браузера

Создайте файл `index.html` в каталоге проекта:

{{< highlight html >}}
<!DOCTYPE html>
<html>
<head>
    <title>Aspose.Cells Browser Example</title>
</head>
<body>
    <h1>Excel Processing with Aspose.Cells</h1>
    <button id="createExcel">Create Excel File</button>
    <div id="output"></div>

    <script src="./node_modules/aspose.cells.js/aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FileFormatType, SaveFormat } = AsposeCells;

        // Initialize with license (optional, remove for trial mode)
        AsposeCells.onReady({
            license: "aspose.cells.enc"  // Path to your encrypted license
        }).then(() => {
            console.log("Aspose.Cells is ready!");

            document.getElementById('createExcel').onclick = function() {
                // Create a new workbook
                var workbook = new Workbook(FileFormatType.Xlsx);

                // Get the first worksheet
                var worksheet = workbook.worksheets.get(0);

                // Add some data
                worksheet.cells.get("A1").putValue("Hello World");
                worksheet.cells.get("A2").putValue("Created with Aspose.Cells for JavaScript");
                worksheet.cells.get("B1").putValue(42);

                // Save as Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);

                // Create download link
                const blob = new Blob([outputData]);
                const downloadLink = document.createElement('a');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.textContent = 'Download Excel File';
                downloadLink.download = "my-excel-file.xlsx";
                downloadLink.style.display = 'block';

                const output = document.getElementById('output');
                output.innerHTML = '';
                output.appendChild(downloadLink);
            };
        }).catch(error => {
            console.error("Error initializing Aspose.Cells:", error);
        });
    </script>
</html>
{{< /highlight >}}

**Для запуска примера браузера:**

{{< highlight bash >}}
# Start HTTP server
http-server -p 8080

# Open browser and visit:
# http://localhost:8080
{{< /highlight >}}

### Использование Node.js

Создайте файл `node-example.js`:

{{< highlight javascript >}}
const { AsposeCells, Workbook, SaveFormat, FileFormatType } = require("aspose.cells.js");
const fs = require('fs');

// Initialize Aspose.Cells with license
AsposeCells.onReady({
    license: "aspose.cells.enc",  // Path to your encrypted license
    fontPath: "./fonts/"         // Optional: path to system fonts
}).then(() => {
    console.log("Aspose.Cells initialized successfully!");

    // Create a new workbook
    const workbook = new Workbook(FileFormatType.Xlsx);

    // Get the first worksheet
    const worksheet = workbook.worksheets.get(0);

    // Add data to cells
    worksheet.cells.get("A1").putValue("Product");
    worksheet.cells.get("B1").putValue("Price");
    worksheet.cells.get("A2").putValue("Apple");
    worksheet.cells.get("B2").putValue(1.99);
    worksheet.cells.get("A3").putValue("Orange");
    worksheet.cells.get("B3").putValue(2.49);

    // Save as Excel file
    const excelData = workbook.save(SaveFormat.Xlsx);
    fs.writeFileSync('output.xlsx', Buffer.from(excelData));
    console.log('Excel file saved as output.xlsx');

    // Save as PDF
    const pdfData = workbook.save(SaveFormat.Pdf);
    fs.writeFileSync('output.pdf', Buffer.from(pdfData));
    console.log('PDF file saved as output.pdf');

}).catch(error => {
    console.error("Error:", error);
});
{{< /highlight >}}

**Для запуска примера Node.js:**

{{< highlight bash >}}
node node-example.js
{{< /highlight >}}

## **Общие операции с файлами**

### Чтение существующего файла Excel

{{< highlight javascript >}}
// Browser (using File input)
const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
        const arrayBuffer = e.target.result;
        const workbook = new Workbook(new Uint8Array(arrayBuffer));
        // Process the workbook...
    };
    reader.readAsArrayBuffer(file);
});

// Node.js
const fs = require('fs');
const fileBuffer = fs.readFileSync('input.xlsx');
const workbook = new Workbook(fileBuffer);
{{< /highlight >}}

### Конвертация между форматами

{{< highlight javascript >}}
// Convert Excel to PDF
const pdfData = workbook.save(SaveFormat.Pdf);

// Convert Excel to HTML
const htmlData = workbook.save(SaveFormat.Html);

// Convert Excel to CSV
const csvData = workbook.save(SaveFormat.Csv);

// Convert Excel to JSON
const jsonData = workbook.save(SaveFormat.Json);
{{< /highlight >}}

## **Устранение неполадок**

### Распространенные проблемы и их решения

1. **Ошибка "Модуль не найден"**
   - Убедитесь, что вы запускаете HTTP-сервер из правильного каталога
   - Проверьте, что путь script src указывает на правильное место

2. **Лицензия не работает**
   - Убедитесь, что файл `aspose.cells.enc` находится в правильном месте
   - Проверьте, что зашифрованный файл лицензии был сгенерирован правильно
   - Проверьте, что исходный файл лицензии действителен и не просрочен

3. **Проблемы CORS в браузере**
   - Всегда используйте HTTP-сервер, никогда не открывайте HTML-файлы напрямую
   - Используйте `http-server` или podobные инструменты для локальной разработки

### Получение помощи

Если возникнут проблемы:
- Проверьте [документацию Aspose.Cells](https://docs.aspose.com/cells/javascript-cpp/)
- Посетите [форумы Aspose](https://forum.aspose.com/c/cells/9) для поддержки сообщества
- Свяжитесь с поддержкой Aspose, указав информацию о лицензии

## **Следующие шаги**

- Ознакомьтесь с [справочником API](https://reference.aspose.com/cells/javascript-cpp/) для подробной документации
- Узнайте о расширенных функциях, таких как диаграммы, формулы и форматирование
- Посмотрите больше примеров и руководств в документации
- Рассмотрите возможность интеграции с вашими существующими веб-приложениями или инструментами сборки
