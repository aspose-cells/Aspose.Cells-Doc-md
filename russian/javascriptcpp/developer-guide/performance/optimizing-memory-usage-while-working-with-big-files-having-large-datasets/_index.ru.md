---
title: Оптимизация использования памяти при работе с большими файлами с большими наборами данных
type: docs
weight: 110
url: /ru/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

При создании книги с большими наборами данных или чтении большого файла Microsoft Excel общий объем оперативной памяти, которую займет процесс, всегда вызывает беспокойство. Существуют меры, которые можно адаптировать для справления с этим вызовом. Aspose.Cells предоставляет некоторые соответствующие варианты и вызовы API для снижения, уменьшения и оптимизации использования памяти. Кроме того, это может помочь процессу работать более эффективно и быстрее.

Используйте опцию [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/), чтобы оптимизировать использование памяти для данных ячеек и уменьшить общую стоимость памяти. При создании большого набора данных для ячеек это может сэкономить определенное количество памяти по сравнению с использованием параметров по умолчанию [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).

{{% /alert %}}

## **Оптимизация памяти**

Следующий пример показывает, как оптимизировать использование памяти при работе с большими данными в Aspose.Cells for JavaScript через C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Предостережение**

По умолчанию, опция [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) применяется ко всем версиям. В некоторых случаях, таких как создание книги с большим набором данных для ячеек, параметр [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) может оптимизировать использование памяти и снизить стоимость памяти для приложения. Однако в некоторых специальных случаях это может снизить производительность, таких как следующие.

1. **Доступ к ячейкам в произвольном порядке и повторно**: Самая эффективная последовательность доступа к коллекции ячеек - путем перебора ячеек по одной строке, а затем строка за строкой. Особенно, если вы получаете доступ к строкам/ячейкам с помощью перечислителя, полученного из [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) и [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), производительность будет максимальной с [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
1. **Вставка и удаление ячеек и строк**: Обратите внимание, что если выполняется много операций вставки/удаления для ячеек/строк, производительность в режиме [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) будет значительно снижена по сравнению с режимом [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
1. **Работа с различными типами ячеек**: Если большинство ячеек содержат строковые значения или формулы, стоимость памяти будет такой же, как в режиме [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/), но если есть много пустых ячеек, или значения ячеек являются числовыми, логическими и т.д., опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) обеспечит лучшую производительность.
