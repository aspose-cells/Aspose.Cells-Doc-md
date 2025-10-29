---
title: Управление VBA кодами книги Excel с поддержкой макросов
linktitle: Проект макросов
type: docs
weight: 200
url: /ru/javascript-cpp/manage-vba-project/
description: Добавить модуль VBA и изменить VBA или макрос с помощью Aspose.Cells for JavaScript через C++.
---

## **Добавить модуль VBA в JavaScript через C++**
{{% alert color="primary" %}}

Aspose.Cells позволяет добавлять новый модуль VBA и код макроса с помощью Aspose.Cells for JavaScript через C++. Пожалуйста, используйте метод [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) для добавления нового модуля VBA внутри рабочей книги.

{{% /alert %}}

Следующий пример создает новую книгу и добавляет новый модуль VBA и макрос-код, сохраняет результат в формате XLSM. После открытия файла XLSM в Microsoft Excel и выбора меню **Разработчик > Visual Basic**, вы увидите модуль с именем "TestModule" и внутри его — следующий макрос-код.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Изменить VBA или макросы в JavaScript через C++**

{{% alert color="primary" %}} 

Вы можете изменять код VBA или макросов с помощью Aspose.Cells for JavaScript через C++. Aspose.Cells добавил следующие модули и классы для чтения и изменения проекта VBA в файле Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Эта статья покажет вам, как изменить код VBA или макроса в исходном файле Excel с помощью Aspose.Cells.

{{% /alert %}} 

Следующий пример загружает исходный файл Excel, в котором содержится следующий VBA или макрос-код

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

После выполнения приведенного выше образца кода Aspose.Cells код VBA или макрос будет изменен таким образом.

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Вы можете загрузить [исходный файл Excel](5112508.xlsm) и [файл Excel для вывода](5112511.xlsm) по указанным ссылкам.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Добавить ссылку на библиотеку в проект VBA в книге](/cells/ru/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Назначить макрос элементу управления формы](/cells/ru/javascript-cpp/assign-macro-to-form-control/)
- [Проверить, действителен ли цифровая подпись кода VBA](/cells/ru/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Проверить, подписан ли код VBA](/cells/ru/javascript-cpp/check-if-vba-code-is-signed/)
- [Проверить, подписан ли проект VBA в книге Excel](/cells/ru/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Проверить, защищен ли и заблокирован для просмотра проект VBA](/cells/ru/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Копирование макроса VBA UserForm DesignerStorage из шаблона в целевую книгу](/cells/ru/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Цифрово подписать проект кода VBA c сертификатом](/cells/ru/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Экспортировать сертификат VBA в файл или поток](/cells/ru/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Фильтрация проекта VBA при загрузке книги](/cells/ru/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [Узнать, защищен ли проект VBA](/cells/ru/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Защитить паролем проект VBA книги Excel](/cells/ru/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
