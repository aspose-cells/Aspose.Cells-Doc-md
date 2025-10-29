---
title: Установка режима вычисления формул книги с помощью JavaScript через C++
linktitle: Установка режима расчета формул в книге Excel
description: В этой статье рассказывается, как установить режим вычисления формул книги в Microsoft Excel с помощью Aspose.Cells for JavaScript через C++. Загрузите существующий файл Excel или создайте новый, используйте свойство, предоставленное Aspose.Cells, чтобы установить режим вычислений формул, и получите результат. В конце сохраните измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, рабочая книга, режим вычисления формулы, настройки, JavaScript через C++
type: docs
weight: 110
url: /ru/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
В Microsoft Excel вы можете установить режим вычисления формул, то есть способ, которым происходит вычисление формул. Существуют три возможных значения:  

- Автоматический - пересчитывать при изменении чего-либо и каждый раз при открытии книги.  
- Автоматический, за исключением таблиц данных - пересчитывать при изменении чего-либо, но исключая таблицы данных.  
- Ручной - пересчитывать только при явном запросе пользователя нажатием F9 или CTRL+ALT+F9, или при сохранении книги.  
{{% /alert %}}  

Для установки режима вычисления формул в Microsoft Excel:  

1. Выберите **Формулы**, а затем **Параметры расчета**.  
1. Выберите один из вариантов.  

Aspose.Cells for JavaScript через C++ также позволяет установить **Режим вычисления формулы** с помощью свойства режима [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--). Вы можете присвоить ему перечисление [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype), которое имеет один из следующих значений:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
