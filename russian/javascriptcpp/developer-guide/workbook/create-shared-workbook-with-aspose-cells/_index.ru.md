---
title: Создать совместно используемую книгу с помощью Aspose.Cells for JavaScript через C++
linktitle: Создание общей книги с Aspose.Cells
type: docs
weight: 40
url: /ru/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: Узнайте, как создать совместно используемую книгу с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

Microsoft Excel позволяет делиться книгой, как показано на следующем скриншоте. Когда вы делитесь книгой, более одного пользователя могут редактировать книгу в сети. Aspose.Cells for JavaScript через C++ позволяет создать совместную книгу с помощью свойства [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--).   

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Создание общей книги с Aspose.Cells**  

Следующий пример кода создает совместную книгу, устанавливая свойство [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) в значение **true**. Открыв [выходной файл Excel](55541786.xlsx) в Microsoft Excel, вы увидите указание **Shared** рядом с именем файла, как показано на скриншоте.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
