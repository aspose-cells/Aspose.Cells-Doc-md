---
title: Как установить свойство AutoRecover рабочей книги с помощью JavaScript через C++
linktitle: Как установить свойство AutoRecover в Рабочей книге
type: docs
weight: 220
url: /ru/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: Узнайте, как установить свойство AutoRecover рабочей книги с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  
Вы можете использовать Aspose.Cells для установки свойства AutoRecover книги. Значение по умолчанию этого свойства — **true**. При установке его в **false** в книге Excel отключается автоматическое восстановление (Авохранение).  

Aspose.Cells предоставляет свойство [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) для включения или отключения этой опции.  
{{% /alert %}}  

Следующий код объясняет, как использовать свойство [**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--) книги. Сначала он считывает значение по умолчанию, которое равно **true**, затем устанавливает его в **false** и сохраняет книгу. После этого он снова читает книгу и получает значение этого свойства, которое в настоящее время равно **false**.  

## JavaScript код для установки свойства AutoRecover рабочей книги  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoRecover</title>
    </head>
    <body>
        <h1>AutoRecover Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // Create workbook object
            const workbook = new Workbook();

            // Read AutoRecover property
            const autoRecoverBefore = workbook.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover before: ${autoRecoverBefore}</p>`;

            // Set AutoRecover property to false
            workbook.settings.autoRecover = false;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output_out.xlsx';

            // Read the saved workbook again from the saved data
            const workbook2 = new Workbook(new Uint8Array(outputData));

            // Read AutoRecover property
            const autoRecoverAfter = workbook2.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover after reload: ${autoRecoverAfter}</p>`;
        });
    </script>
</html>
```  

## **Вывод**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
