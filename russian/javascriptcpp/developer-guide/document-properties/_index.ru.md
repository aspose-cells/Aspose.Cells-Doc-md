---
title: Управлять свойствами документа с помощью JavaScript через C++
linktitle: Свойства документа
type: docs
weight: 80
url: /ru/javascript-cpp/managing-document-properties/
description: Узнайте, как управлять свойствами документа через API Aspose.Cells for JavaScript через C++.
keywords: Как управлять свойствами документа в JavaScript через C++, получать или устанавливать свойства документа с помощью JavaScript через C++, добавлять или удалять свойства документа с помощью via JavaScript через C++, вставлять или удалять свойства документа с помощью JavaScript через C++, как получать свойства документа с помощью API Aspose.Cells for JavaScript через C++.
---

## **Введение**

Microsoft Excel предоставляет возможность добавлять свойства к файлам электронных таблиц. Эти свойства документов предоставляют полезную информацию и делятся на 2 категории, как описано ниже.

- Системные (встроенные) свойства: Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (пользовательские) свойства: Пользовательские свойства, определенные конечным пользователем в виде пары имя-значение.

{{% alert color="primary" %}}

Самый важный момент, который нужно знать о встроенных и пользовательских свойствах, заключается в том, что встроенные свойства можно получить доступ, изменить, но не создать или удалить. Однако пользовательские свойства можно создавать и управлять ими.

{{% /alert %}}

## **Как управлять свойствами документа с помощью Microsoft Excel**

Microsoft Excel позволяет управлять свойствами документа Excel в WYSIWYG-режиме. Пожалуйста, выполните следующие шаги, чтобы открыть диалог **Свойства** в Excel 2016.

1. В меню **Файл** выберите **Сведения**.

|**Выбор меню Сведения**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Нажмите на заголовок **Свойства** и выберите "Расширенные свойства".

|**Нажмите на выбор расширенных свойств**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Управляйте свойствами документа файла.

|**Диалоговое окно свойств**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
В диалоговом окне свойств есть различные вкладки, такие как Общее, Резюме, Статистика, Содержание и Пользовательские. Каждая вкладка помогает настраивать различные виды информации, связанные с файлом. Вкладка Пользовательские используется для управления пользовательскими свойствами.

## **Как работать со свойствами документа с помощью Aspose.Cells**

Разработчики могут динамически управлять свойствами документа с помощью API Aspose.Cells. Эта функция помогает разработчикам сохранять полезную информацию вместе с файлом, такую как время получения файла, обработки, отметки времени и т. д.

{{% alert color="primary" %}}

Aspose.Cells for JavaScript через C++ напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа в PDF, Aspose.Cells for JavaScript через C++ заполняет поле **Приложение** значением 'Aspose.Cells' и поле **Производитель PDF** значением, например, 'Aspose.Cells v17.9'.

Обратите внимание, что вы не можете заставить Aspose.Cells for JavaScript через C++ изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

### **Как получить доступ к свойствам документа**

API Aspose.Cells поддерживают оба типа свойств документа: встроенные и пользовательские. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) в Aspose.Cells представляет файл Excel и, как и файл Excel, класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) может содержать несколько листов, каждый из которых представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet), а коллекция листов — классом [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).

Используйте [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) для получения доступа к свойствам файла, как описано ниже.

- Чтобы получить доступ к встроенным свойствам документа, используйте [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--).
- Чтобы получить доступ к настраиваемым свойствам документа, используйте [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--).

Иметь тож экземпляры [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) и [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--) возвращают экземпляр [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/). Эта коллекция содержит [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) объектов, каждый из которых представляет отдельное встроенное или пользовательское свойство документа.

Ответ на вопрос, как получить свойство, зависит от требований приложения: можно использовать индекс или имя свойства из [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/), как показано в примере ниже.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

Класс [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) позволяет получать имя, значение и тип свойства документа:

- Чтобы получить имя свойства, используйте [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--).
- Для получения значения свойства используйте [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) возвращает значение в виде объекта.
- Для получения типа свойства используйте [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). Это возвращает одно из значений перечисления [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/). После определения типа свойства используйте один из методов **DocumentProperty.ToXXX** для получения значения соответствующего типа вместо [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). Методы **DocumentProperty.ToXXX** описаны в таблице ниже.

{{% alert color="primary" %}}

Класс [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) также предоставляет набор методов, возвращающих значения других типов данных.

{{% /alert %}}

|**Имя участника**|**Описание**|**Метод ToXXX**|
| :- | :- | :- |
|Boolean|Тип данных свойства - Логический|ToBool|
|Date|Тип данных свойства - Дата и время. Обратите внимание, что Microsoft Excel сохраняет только <br>часть даты, не сохраняется время в настраиваемом свойстве этого типа|ToDateTime|
|Float|Тип данных свойства - Число двойной точности|ToDouble|
|Number|Тип данных свойства - Int32|ToInt|
|String|Тип данных свойства — string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **Как добавить или удалить пользовательские свойства документа**

Как мы уже описывали ранее в начале этой темы, разработчики не могут добавлять или удалять встроенные свойства, потому что эти свойства определены системой, но возможно добавить или удалить пользовательские свойства, потому что они определены пользователем.

### **Как добавить пользовательские свойства**

API Aspose.Cells предоставили метод [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) для класса [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/) для добавления пользовательских свойств в коллекцию. Метод [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) добавляет свойство в файл Excel и возвращает ссылку на новое свойство документа в виде объекта [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **Как настроить пользовательское свойство 'Ссылка на содержимое'**

Чтобы создать пользовательское свойство, связанное с содержанием выбранного диапазона, вызовите метод [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) и передайте название свойства и источник. Проверить, настроено ли свойство как связанное с содержимым, можно с помощью свойства [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--). Также возможно получить исходный диапазон с помощью свойства [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--) класса [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

Мы используем простой шаблон файла Microsoft Excel в примере. Рабочая книга содержит определенный именованный диапазон с меткой '**MyRange**', который ссылается на значение ячейки.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **Как удалить пользовательские свойства**

Чтобы удалить пользовательские свойства через Aspose.Cells, вызовите метод [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-) и передайте название свойства документа, которое нужно удалить.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
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

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа](/cells/ru/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Указание версии документа Excel с использованием встроенных свойств документа](/cells/ru/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Указание языка файла Excel с использованием встроенных свойств документа](/cells/ru/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
