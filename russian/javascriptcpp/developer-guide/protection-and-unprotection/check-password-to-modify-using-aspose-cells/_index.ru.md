---
title: Проверьте пароль для редактирования с помощью Aspose.Cells for JavaScript на C++
linktitle: Проверка пароля для изменений
type: docs
weight: 2400
url: /ru/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Узнайте, как проверять соответствие пароля для редактирования с помощью Aspose.Cells for JavaScript на C++.
---

{{% alert color="primary" %}}  
 Иногда необходимо программно проверить, совпадает ли данный пароль с «Паролем для внесения изменений». Aspose.Cells предоставляет метод `WorkbookSettings.writeProtection.validatePassword()`, который можно использовать для проверки правильности введенного пароля.  
{{% /alert %}}  

## **Проверка пароля на доступ на изменение в Microsoft Excel**  

Вы можете указать **Пароль на открытие** и **Пароль на доступ на изменение** при создании ваших книг в Microsoft Excel. Пожалуйста, посмотрите этот скриншот, который показывает интерфейс, предоставляемый Microsoft Excel для указания этих паролей.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Проверьте пароль для изменения с помощью Aspose.Cells for JavaScript через C++**  

 Следующий код загружает файл [исходного Excel](5112232.xlsx). В нем установлен пароль для открытия 1234 и пароль для внесения изменений 5678. Код сначала проверяет, правильен ли пароль для изменений 567, и возвращает false, затем проверяет, правильен ли пароль 5678, и возвращает true.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Write Protection Passwords</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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

            // Specify password to open inside the load options
            const opts = new LoadOptions();
            opts.password = "1234";

            // Open the source Excel file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Check if 567 is Password to modify
            let ret = workbook.settings.writeProtection.validatePassword("567");
            let outputHtml = `<p>Is 567 correct Password to modify: ${ret}</p>`;

            // Check if 5678 is Password to modify
            ret = workbook.settings.writeProtection.validatePassword("5678");
            outputHtml += `<p>Is 5678 correct Password to modify: ${ret}</p>`;

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```  

### **Вывод в консоль**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
