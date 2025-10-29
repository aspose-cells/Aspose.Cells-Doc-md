---
title: Используйте пользовательские части XML в Aspose.Cells с JavaScript через C++
linktitle: Использование пользовательских XML частей в Aspose.Cells
type: docs
weight: 390
url: /ru/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: Узнайте, как использовать пользовательские части XML в Aspose.Cells for JavaScript через C++. Интегрируйте внешние XML данные в файлы Excel без проблем.
---

## Использование пользовательских XML-частей в Aspose.Cells

Пользовательские XML-части — это XML-данные, хранящиеся разными приложениями, такими как SharePoint и др., внутри файла Excel. Эти данные используются различными приложениями, которым они необходимы. Microsoft Excel не использует эти данные, поэтому для их добавления отсутствует графический интерфейс. Вы можете просмотреть эти данные, изменив расширение **.xlsx** на **.zip**, а затем открыть его с помощью **WinZip**. Также можно открыть ZIP-файл любым сторонним архиватором Windows, например WinRAR или WinZip. Данные находятся внутри папки **customXml**.

Вы можете добавлять пользовательские части XML с помощью Aspose.Cells for JavaScript через C++ с помощью метода [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/).

Следующий пример кода использует метод [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) и добавляет XML-данные **Book Catalog**, название которых **BookStore**. На следующем изображении показан результат этого кода. Как видно, XML **Book Catalog** добавлен внутри узла **BookStore**, который является именем этого свойства.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Код JavaScript для использования пользовательских частей XML

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## Связанная статья

- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
