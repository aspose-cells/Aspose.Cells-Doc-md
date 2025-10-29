---
title: Добавление пользовательских свойств внутри панели информации о документе с помощью JavaScript через C++
linktitle: Добавление пользовательских свойств, видимых в панели информации о документе
type: docs
weight: 300
url: /ru/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Узнайте, как добавлять пользовательские свойства в объект рабочей книги с помощью Aspose.Cells for JavaScript через C++. Эти свойства можно просматривать в панели информации о документе.
---

## **Добавление пользовательских свойств, видимых в панели информации о документе**

 Aspose.Cells for JavaScript через C++ можно использовать для добавления пользовательских свойств внутри объекта рабочей книги, которые отображаются внутри панели информации о документе. Вы можете открыть панель информации о документе в Microsoft Excel, используя команды меню: Файл > Информация > Свойства > Показать панель документов.

Пожалуйста, используйте метод [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-) для добавления пользовательского свойства, которое будет отображаться в Панели информации о документе.

Следующий пример кода добавляет два пользовательских свойства. Первое свойство без типа, а второе с типом DateTime. После открытия созданного этим кодом файла Excel вы увидите эти два свойства в Панели информации о документе.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских XML-частей в Aspose.Cells](/cells/ru/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
