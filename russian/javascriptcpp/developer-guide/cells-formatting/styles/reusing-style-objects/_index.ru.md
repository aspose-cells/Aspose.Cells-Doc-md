---
title: Повторное использование объектов стиля
linktitle: Повторное использование объектов стиля
description: В Aspose.Cells for JavaScript через C++, создавая и используя повторно используемые объекты стилей, вы можете упростить управление стилями и повысить эффективность кода. Наше руководство поможет вам использовать преимущества повторно используемых объектов стилей и реализовать их в вашем приложении.
keywords: Aspose.Cells for JavaScript через C++, повторное использование объектов стилей, управление стилями, эффективность кода, повторно используемые стили, разработка приложений, API документация, пример кода, загрузка, поддержка.
type: docs
weight: 3000
url: /ru/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
Повторное использование объектов стиля может сэкономить память и ускорить работу программы.  
{{% /alert %}}  

Чтобы применить форматирование к большому диапазону ячеек на листе:

1. Создайте объект стиля.
1. Укажите атрибуты.
1. Примените стиль к ячейкам в диапазоне.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
Поскольку подход [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) использует намного меньше памяти и является более эффективным, устаревшее свойство Cell.style, которое занимало много лишней памяти, было удалено с выпуском Aspose.Cells 7.1.0.  
{{% /alert %}}
