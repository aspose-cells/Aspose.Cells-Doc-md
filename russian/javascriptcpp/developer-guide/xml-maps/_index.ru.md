---
title: Импортировать XML в рабочую книгу Excel с помощью JavaScript через C++
linktitle: Сопоставления XML
type: docs
weight: 210
url: /ru/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Импорт данных из XML файлов в Excel с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет импортировать карту XML внутри книги с помощью метода [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Вы можете импортировать карту XML в Microsoft Excel, следуя следующим шагам:

- Выберите вкладку **Разработчик**
- Нажмите **Импорт** в разделе XML и следуйте необходимым шагам.

Для завершения импорта вам потребуется предоставить свои XML-данные. Вот [пример XML-данных](5115037.txt), который вы можете использовать для тестирования.

{{% /alert %}}

## **Импорт XML-схемы с использованием Microsoft Excel**

На следующем скриншоте показано, как импортировать XML-схему с использованием Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Импортировать XML-карту с помощью Aspose.Cells for JavaScript через C++**

В следующем примере кода показано, как использовать [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Это генерирует [выходной файл Excel](5115036.xlsx), как показано на этом снимке экрана.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Добавление карты XML внутри книги с помощью метода XmlMapCollection.add()](/cells/ru/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Экспорт XML-данных, связанных с XML-схемой, внутри книги](/cells/ru/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Найдите имя корневого элемента XML-карты.](/cells/ru/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [Привязка ячеек к элементам XML-отображения](/cells/ru/javascript-cpp/link-cells-to-xml-map-elements/)
