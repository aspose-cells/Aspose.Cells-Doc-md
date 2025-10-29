---
title: Применить Расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям
type: docs
weight: 280
url: /ru/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Узнайте, как применять расширенный фильтр Microsoft Excel для отображения записей, соответствующих сложным критериям, с помощью скрипта Aspose.Cells for Java и API C++.
keywords: Применение расширенного фильтра на JavaScript через C++, установка расширенного фильтра на JavaScript через C++, добавление расширенного фильтра на JavaScript через C++, создание расширенного фильтра на JavaScript через C++, как добавить расширенный фильтр к диапазону JavaScript через C++
---

## **Возможные сценарии использования**  

Microsoft Excel позволяет применять *Расширенный фильтр* к данным листа для отображения записей, соответствующих сложным критериям. Вы можете применить расширенный фильтр через команду *Данные > Расширенный*, как показано на скриншоте.  

![todo:image_alt_text](1.png)  

Скрипт Aspose.Cells for Java через C++ также позволяет применять расширенный фильтр с помощью метода [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Как и Microsoft Excel, он принимает следующие параметры.  

**isFilter**  

Указывает, фильтровать ли список на месте.  

**listRange**  

Диапазон списка.  

**criteriaRange**  

Диапазон критериев.  

**copyTo**  

Диапазон, куда копируются данные.  

**uniqueRecordOnly**  

Отображение или копирование только уникальных строк.  

## **Применение расширенного фильтра Microsoft Excel для отображения записей, удовлетворяющих сложным критериям**  

Следующий пример кода применяет расширенный фильтр к [пробному Excel-файлу](48496692.xlsx) и создает [выходной Excel-файл](48496691.xlsx). Скриншот показывает оба файла для сравнения. Внутри скриншота видно, что данные были отфильтрованы внутри выходного файла согласно сложным условиям.  

![todo:image_alt_text](2.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
