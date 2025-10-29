---
title: Как заблокировать ячейки для их защиты
type: docs
weight: 130
url: /ru/javascript-cpp/how-to-lock-cells-to-protect-them/
description: Эта статья показывает вам пример кода, объясняющий, как заблокировать ячейки для их защиты с помощью скрипта Aspose.Cells for Java на C++.
keywords: JavaScript Заблокировать ячейки для защиты, как заблокировать ячейки с помощью JavaScript, блокировать ячейки для защиты в JavaScript.
---

## **Возможные сценарии использования**
Блокировка ячеек с целью защиты — распространённая практика в программах для работы с таблицами, таких как Microsoft Excel или Google Sheets, по нескольким важным причинам:

1. Предотвращение случайных изменений: блокировка ячеек может предотвратить случайное изменение важной информации или формул пользователями. Особенно это актуально в сложных таблицах, где непреднамеренные изменения могут привести к серьезным ошибкам.

1. Поддержание целостности данных: с помощью блокировки ячеек вы можете обеспечить сохранение критически важных данных в постоянном и точном виде. Это важно для финансовых документов, отчетов и любых других документов, где важна целостность данных.

1. Контролируемый доступ: в совместных средах блокировка ячеек позволяет контролировать, кто может редактировать определенные части таблицы. Например, вы можете разрешить только определенным участникам команды редактировать конкретные ячейки, сохраняя остальную часть листа защищенной.

1. Защита формул: формулы часто важны для вычислений и анализа данных. Блокировка ячеек с формулами гарантирует, что эти формулы не будут случайно изменены или удалены, что может нарушить функциональность всего листа.

1. Обеспечение соблюдения бизнес-правил: в некоторых случаях определенные бизнес-правила или нормативы требуют защиты определенных данных от изменений. Блокировка ячеек помогает соответствовать этим требованиям.

1. Руководство пользователями: блокируя ячейки и предоставляя четкие инструкции о том, какие ячейки можно редактировать, вы можете направлять пользователей, как взаимодействовать с таблицей, уменьшая путаницу и ошибки.

## **Как заблокировать ячейки для защиты в Excel**
Вот как можно заблокировать ячейки в Microsoft Excel:

1. Выберите ячейки для блокировки: выберите ячейки, которые хотите заблокировать. Если вы хотите заблокировать весь лист, можете пропустить этот шаг.
1. Откройте диалоговое окно «Формат ячеек»: щелкните правой кнопкой мыши по выбранным ячейкам и выберите «Формат ячеек», или нажмите Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Заблокируйте ячейки: В диалоговом окне Формат ячеек перейдите на вкладку "Защита". Установите флажок "Заблокировано". Нажмите "ОК".
1. Защитите лист: Перейдите на вкладку "Рецензирование" на ленте. Нажмите "Защитить лист." Установите пароль (по желанию) и выберите разрешения, которые хотите разрешить (например, выбор заблокированных ячеек, форматирование ячеек и т.д.). Нажмите "ОК."
<br>
<img src="2.png" width=60% />

## **Как заблокировать ячейки для защиты с помощью JavaScript**

Aspose.Cells — мощная библиотека для работы с файлами Excel программным способом. Чтобы заблокировать ячейки с помощью скрипта Aspose.Cells for Java на C++, выполните следующие шаги: загрузите [образец файла](sample.xlsx), сначала разблокируйте все ячейки (так как по умолчанию все ячейки заблокированы, но это не применяется до защитных мер, пока рабочий лист не защищен), затем заблокируйте конкретные ячейки, которые нужно защитить, и наконец защитите рабочий лист, чтобы обеспечить блокировку.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Результат вывода**
Этот код гарантирует, что только указанные ячейки (например, A1 и B2) будут заблокированы, а лист защищен для активизации этих настроек. Все остальные ячейки в листе останутся разблокированными и редактируемыми.

<br>
<img src="3.png" width=60% />
