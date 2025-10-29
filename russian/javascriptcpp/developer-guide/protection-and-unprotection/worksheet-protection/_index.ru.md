---
title: Защитить и снять защиту листа с помощью JavaScript через C++
linktitle: Защитить и снять защиту листа
type: docs
weight: 40
url: /ru/javascript-cpp/protect-and-unprotect-worksheets/
description: Защитить и снять защиту листа в Excel с помощью скрипта Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  
Чтобы предотвратить случайное или умышленное изменение, перемещение или удаление данных на листе, вы можете заблокировать ячейки на листе Excel, а затем защитить лист паролем.  
{{% /alert %}}  

## **Защитить и снять защиту листа в MS Excel**  

**![защита и снятие защиты листа](protect-and-unprotect-worksheet.png)**  

1. Нажмите **Обзор > Защитить лист**.  
1. Введите пароль в **поле Пароль**.  
1. Выберите варианты **разрешить**.  
1. Выберите **OK**, введите пароль для подтверждения, затем снова выберите **OK**.  

## **Защитить лист с помощью скрипта Aspose.Cells for JavaScript через C++**  
Для реализации защиты структуры рабочей книги Excel достаточно следующих простых строк кода.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Снять защиту листа с помощью скрипта Aspose.Cells for JavaScript через C++**  
Снятие защиты листа — это просто с API Aspose.Cells. Если лист защищен паролем, потребуется правильный пароль.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **Продвинутые темы**  
- [Расширенные настройки защиты с момента появления Excel XP](/cells/ru/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [Определение, защищен ли рабочий лист паролем](/cells/ru/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [Защита листов](/cells/ru/javascript-cpp/protecting-worksheets/)  
- [Снятие защиты с листа](/cells/ru/javascript-cpp/unprotect-a-worksheet/)  
- [Проверить Пароль, Используемый для Защиты Листа](/cells/ru/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
